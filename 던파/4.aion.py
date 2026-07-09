import logging
import pyautogui
import robot
import time
import action
import action2
from unit import Unit
from unit import select
import unit
import os
import json
from datetime import datetime
import mailSender
import random
import imageFinder
import keyboard2
import sys
import threading

import tkinter as tk
from tkinter import ttk, messagebox

import cv2
import numpy as np

from tobe import *

select('보리뚜')

os.system('rm -rf imagesLog/*')

# ==========================================================================
# 공유 상태 / 동기화
# ==========================================================================

# 키 풀: 8방향이 모두 한 번씩 실행되도록 보장
# 단일 키: 4방향(동서남북), 튜플: 4방향(대각선)
DIRECTION_POOL = ['a', 'd', 's', 'w', ('w', 'd'), ('w', 'a'), ('s', 'd'), ('s', 'a')]
key_pool = []
key_pool_lock = threading.Lock()

pyautogui_lock = threading.Lock()

PRESET_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'aion_presets.json')
UI_CFG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ui_config.json')

# 테마 팔레트 (다크 / 라이트)
THEME_LABELS = {'다크': 'dark', '라이트': 'light'}
THEME_KEY_TO_LABEL = {v: k for k, v in THEME_LABELS.items()}
THEMES = {
    'dark': {
        'bg': '#1e1e1e', 'fg': '#e6e6e6', 'entry_bg': '#2d2d2d',
        'btn_bg': '#3a3a3a', 'active': '#4a6da7', 'list_bg': '#252526',
        'frame_fg': '#c8c8c8', 'run': '#4caf50', 'pause': '#ef5350',
    },
    'light': {
        'bg': '#f2f2f2', 'fg': '#1a1a1a', 'entry_bg': '#ffffff',
        'btn_bg': '#e2e2e2', 'active': '#cfe2ff', 'list_bg': '#ffffff',
        'frame_fg': '#333333', 'run': '#0a8f2a', 'pause': '#c62828',
    },
}


def load_ui_config():
    try:
        with open(UI_CFG_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {}


def save_ui_config(cfg):
    try:
        with open(UI_CFG_PATH, 'w', encoding='utf-8') as f:
            json.dump(cfg, f, ensure_ascii=False, indent=2)
    except Exception:
        logging.exception('ui config save error')

# 화면에 보이는 이름 -> 내부 모드 키
MOVEMENT_LABELS = {
    '이동 없음 (none)': 'none',
    '8방향 랜덤': 'random_8dir',
    '상하 왕복': 'horizontal_ud',
    '좌우 왕복': 'horizontal_lr',
    '팔각형 회전': 'octagon',
    '중앙가중 랜덤': 'center_biased',
    '4방향 랜덤': 'random_simple',
}
MOVEMENT_KEY_TO_LABEL = {v: k for k, v in MOVEMENT_LABELS.items()}

# 각 이동 타입별 기본 유지시간(초). 사용자가 0을 넣으면 이 기본값을 사용.
DEFAULT_HOLD = {
    'none': 0.0,
    'random_8dir': 0.9,
    'horizontal_ud': 3.3,
    'horizontal_lr': 5.0,
    'octagon': 1.5,
    'center_biased': 0.25,
    'random_simple': 0.15,
}

# 실시간으로 바뀌는 설정 (UI에서 즉시 갱신)
state = {
    'attack_keys': ['4'],
    'movement_mode': 'none',
    'use_g': True,
    'use_jump': True,
    'use_a_find': True,
    # 이동 타입별 유지시간(초). 0 = 자동(모드 기본값 사용)
    'move_durations': {m: 0.0 for m in DEFAULT_HOLD},
}
state_lock = threading.Lock()

# set() = 동작 중, clear() = 일시중지
running_event = threading.Event()


def get_state(key):
    with state_lock:
        return state[key]


def mode_active(mode):
    """현재 이동 모드가 아직 mode 인지 확인 (모드 전환 감지용)"""
    with state_lock:
        return state['movement_mode'] == mode


def hold_duration(mode, default):
    """해당 이동 타입의 사용자 지정 유지시간. 0/미지정이면 default 사용."""
    with state_lock:
        d = state['move_durations'].get(mode, 0.0)
    return d if d and d > 0 else default


# ==========================================================================
# 저수준 입력 헬퍼 (스레드 안전 + 일시중지 존중)
# ==========================================================================

def safe_press(key):
    """pyautogui.press를 락으로 보호 (스레드 안전)"""
    with pyautogui_lock:
        pyautogui.press(key)


def interruptible_sleep(duration, mode=None):
    """일시중지를 존중하고, 모드가 바뀌면 즉시 반환하는 sleep"""
    end = time.time() + duration
    while True:
        running_event.wait()
        remaining = end - time.time()
        if remaining <= 0:
            return
        if mode is not None and not mode_active(mode):
            return
        time.sleep(min(0.08, remaining))


def press_direction(direction, duration=0.5, mode=None):
    """단일 키 또는 대각선(2키 동시) 방향 이동.
    일시중지 / 모드 전환 시 즉시 키를 떼고 빠져나온다."""
    keys = (direction,) if isinstance(direction, str) else direction
    pressed = []
    try:
        for k in keys:
            with pyautogui_lock:
                pyautogui.keyDown(k)
            pressed.append(k)
        end = time.time() + duration
        while time.time() < end:
            if not running_event.is_set():
                break
            if mode is not None and not mode_active(mode):
                break
            time.sleep(min(0.05, max(0.0, end - time.time())))
    except RuntimeError:
        pass
    finally:
        for k in reversed(pressed):
            try:
                with pyautogui_lock:
                    pyautogui.keyUp(k)
            except RuntimeError:
                pass


def release_all_keys():
    """일시중지 시 눌려있을 수 있는 키들을 모두 떼어준다."""
    for k in ('w', 'a', 's', 'd', 'g', 'space'):
        try:
            with pyautogui_lock:
                pyautogui.keyUp(k)
        except Exception:
            pass


def set_running(run):
    if run:
        running_event.set()
    else:
        running_event.clear()
        release_all_keys()


# ==========================================================================
# 이동 쓰레드들 (mode 인자를 받아 모드가 유지되는 동안만 루프)
# ==========================================================================

def movement_loop(mode):
    """8방향 랜덤 - g키(a_find)와 8방향키 처리"""
    global key_pool
    while mode_active(mode):
        running_event.wait()
        if not mode_active(mode):
            break

        if get_state('use_a_find') and do(Founder('a_find'), onlyOneTime=True):
            interruptible_sleep(random.uniform(1.35, 1.65), mode)
            continue

        with key_pool_lock:
            if not key_pool:
                key_pool = DIRECTION_POOL[:]
                random.shuffle(key_pool)
            direction = key_pool.pop(0)
        press_direction(direction, duration=hold_duration(mode, random.uniform(0.5, 1.3)), mode=mode)
        interruptible_sleep(random.uniform(0.35, 2.15), mode)


def movement_horizenal(mode):
    """상하 왕복 - 위(w)와 아래(s)를 교대로 반복"""
    directions = ['w', 's']
    idx = 0
    while mode_active(mode):
        running_event.wait()
        press_direction(directions[idx], duration=hold_duration(mode, 3.3), mode=mode)
        idx = 1 - idx
        interruptible_sleep(random.uniform(13.35, 14.15), mode)


def movement_horizontal_lr(mode):
    """좌우 왕복 - 좌(a)와 우(d)를 교대로 반복"""
    directions = ['d', 'a']
    idx = 0
    while mode_active(mode):
        running_event.wait()
        press_direction(directions[idx], duration=hold_duration(mode, 5.0), mode=mode)
        idx = 1 - idx
        interruptible_sleep(random.uniform(5.5, 10.5), mode)


def movement_octagon(mode):
    """팔각형 회전 - 8방향을 순서대로 빙글빙글 반복"""
    directions = ['w', ('w', 'd'), 'd', ('s', 'd'), 's', ('s', 'a'), 'a', ('w', 'a')]
    idx = 0
    while mode_active(mode):
        running_event.wait()
        press_direction(directions[idx], duration=hold_duration(mode, 1.5), mode=mode)
        idx = (idx + 1) % 8


def movement_center_biased(mode):
    """중앙가중 랜덤 - 짧은 burst + 관성 + 중앙 가중치로 자연스럽게 이동"""
    DIRECTION_VECTORS = {
        'a':        (-1,  0),
        'd':        ( 1,  0),
        'w':        ( 0, -1),
        's':        ( 0,  1),
        ('w', 'd'): ( 1, -1),
        ('w', 'a'): (-1, -1),
        ('s', 'd'): ( 1,  1),
        ('s', 'a'): (-1,  1),
    }

    directions = list(DIRECTION_VECTORS.keys())
    pos_x, pos_y = 0.0, 0.0
    prev_vec = (0.0, 0.0)

    while mode_active(mode):
        running_event.wait()
        to_center_x = -pos_x
        to_center_y = -pos_y
        dist = (to_center_x ** 2 + to_center_y ** 2) ** 0.5

        weights = []
        for d in directions:
            dx, dy = DIRECTION_VECTORS[d]
            dir_len = (dx ** 2 + dy ** 2) ** 0.5
            dx_n, dy_n = dx / dir_len, dy / dir_len

            if dist > 0:
                center_cos = (dx_n * to_center_x + dy_n * to_center_y) / dist
                center_w = 1.0 + center_cos * min(dist * 0.5, 3.0)
            else:
                center_w = 1.0

            prev_len = (prev_vec[0] ** 2 + prev_vec[1] ** 2) ** 0.5
            if prev_len > 0:
                momentum_cos = (dx_n * prev_vec[0] + dy_n * prev_vec[1]) / prev_len
                momentum_w = 1.0 + momentum_cos * 1.8
            else:
                momentum_w = 1.0

            weights.append(max(center_w * momentum_w, 0.05))

        direction = random.choices(directions, weights=weights, k=1)[0]

        duration = hold_duration(mode, random.uniform(0.1, 0.35))
        press_direction(direction, duration=duration, mode=mode)

        dx, dy = DIRECTION_VECTORS[direction]
        dir_len = (dx ** 2 + dy ** 2) ** 0.5
        prev_vec = (dx / dir_len, dy / dir_len)

        pos_x += dx * duration
        pos_y += dy * duration

        interruptible_sleep(random.uniform(0.0, 0.08), mode)


def movement_random_simple(mode):
    """4방향 랜덤 - 상하좌우 4방향만 랜덤 입력"""
    directions = ['w', 's', 'a', 'd']
    while mode_active(mode):
        running_event.wait()
        direction = random.choice(directions)
        press_direction(direction, duration=hold_duration(mode, random.uniform(0.1, 0.2)), mode=mode)
        interruptible_sleep(random.uniform(0.2, 5.0), mode)


def movement_none(mode):
    """이동 없이 제자리 대기"""
    while mode_active(mode):
        interruptible_sleep(1.0, mode)


MOVEMENT_MODES = {
    'none': movement_none,
    'random_8dir': movement_loop,
    'horizontal_ud': movement_horizenal,
    'horizontal_lr': movement_horizontal_lr,
    'octagon': movement_octagon,
    'center_biased': movement_center_biased,
    'random_simple': movement_random_simple,
}


# ==========================================================================
# 상시 실행 워커 쓰레드
# ==========================================================================

def movement_manager():
    """현재 이동 모드에 맞는 함수를 실행. 모드가 바뀌면 새 함수로 전환."""
    while True:
        running_event.wait()
        mode = get_state('movement_mode')
        fn = MOVEMENT_MODES.get(mode, movement_none)
        try:
            fn(mode)
        except Exception:
            logging.exception('movement error')
        time.sleep(0.05)


def attack_loop():
    """공격 쓰레드 - 설정된 공격키들을 반복 입력"""
    while True:
        running_event.wait()
        with state_lock:
            keys = list(state['attack_keys'])
            use_g = state['use_g']

        if not keys:
            time.sleep(0.2)
            continue

        if use_g and random.random() < 0.41:
            running_event.wait()
            safe_press('g')

        for key in keys:
            running_event.wait()
            safe_press(key)
            time.sleep(random.uniform(0.3, 0.7))


def jump_loop():
    """점프 쓰레드 - 긴 간격으로 한 번씩 점프"""
    while True:
        running_event.wait()
        interruptible_sleep(random.uniform(123.0, 235.0))
        if get_state('use_jump'):
            running_event.wait()
            safe_press('space')


# ==========================================================================
# 캡차 감지 (10초 주기 스크린샷 비교)
# ==========================================================================

CAPTCHA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'captchaShots')
CAPTCHA_CFG = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'captcha_config.json')
CAPTCHA_INTERVAL = 10.0        # 감지 주기(초)
CAPTCHA_ALERT_COOLDOWN = 120.0  # 동일 캡차 재알림 최소 간격(초)


def grab_region_bgr(region):
    """(x, y, w, h) 영역 스크린샷을 BGR ndarray로 반환"""
    pyautogui.FAILSAFE = False
    with pyautogui_lock:
        img = pyautogui.screenshot(region=tuple(region))
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)


def grab_screen_bgr():
    """전체 화면 스크린샷을 BGR ndarray로 반환"""
    pyautogui.FAILSAFE = False
    with pyautogui_lock:
        img = pyautogui.screenshot()
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)


class CaptchaMonitor:
    """등록된 캡차 영역들을 10초마다 스크린샷 비교로 감지하고 메일 발송."""

    def __init__(self):
        self.lock = threading.Lock()
        self.enabled = False
        self.threshold = 0.9
        self.shots = []  # [{'file','region','img','detected','last_alert'}]
        self._load()

    # ---- 저장 / 로드 ----
    def _load(self):
        try:
            with open(CAPTCHA_CFG, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception:
            return
        self.enabled = bool(data.get('enabled', False))
        self.threshold = float(data.get('threshold', 0.9))
        for s in data.get('shots', []):
            path = os.path.join(CAPTCHA_DIR, s['file'])
            img = cv2.imread(path)
            if img is None:
                continue
            self.shots.append({
                'file': s['file'], 'region': list(s['region']),
                'img': img, 'detected': False, 'last_alert': 0.0,
            })

    def _save(self):
        data = {
            'enabled': self.enabled,
            'threshold': self.threshold,
            'shots': [{'file': s['file'], 'region': s['region']} for s in self.shots],
        }
        try:
            with open(CAPTCHA_CFG, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception:
            logging.exception('captcha config save error')

    # ---- 항목 관리 ----
    def add_shot(self, region):
        """region=(x,y,w,h) 영역을 기준 스크린샷으로 등록"""
        os.makedirs(CAPTCHA_DIR, exist_ok=True)
        img = grab_region_bgr(region)
        # 파일명: 겹치지 않게 인덱스 증가
        idx = 1
        while os.path.exists(os.path.join(CAPTCHA_DIR, f'captcha_{idx}.png')):
            idx += 1
        fname = f'captcha_{idx}.png'
        cv2.imwrite(os.path.join(CAPTCHA_DIR, fname), img)
        with self.lock:
            self.shots.append({
                'file': fname, 'region': list(region),
                'img': img, 'detected': False, 'last_alert': 0.0,
            })
            self._save()
        return fname

    def remove_shot(self, index):
        with self.lock:
            if 0 <= index < len(self.shots):
                s = self.shots.pop(index)
                self._save()
                try:
                    os.remove(os.path.join(CAPTCHA_DIR, s['file']))
                except Exception:
                    pass

    def list_labels(self):
        with self.lock:
            labels = []
            for s in self.shots:
                h, w = s['img'].shape[:2]
                labels.append(f"{s['file']}  ({w}×{h})")
            return labels

    def set_enabled(self, on):
        with self.lock:
            self.enabled = bool(on)
            self._save()

    def set_threshold(self, value):
        with self.lock:
            self.threshold = float(value)
            self._save()

    # ---- 감지 ----
    @staticmethod
    def _match_score(screen_bgr, template_bgr):
        """저장한 이미지(template)가 화면(screen) 어디든 있는지 템플릿 매칭.
        좌표와 무관하게 가장 잘 맞는 위치의 유사도(0~1)를 반환."""
        sh, sw = screen_bgr.shape[:2]
        th, tw = template_bgr.shape[:2]
        # 템플릿이 화면보다 크면 매칭 불가 → 화면 안에 들어오도록 축소
        if th > sh or tw > sw:
            scale = min(sh / th, sw / tw)
            template_bgr = cv2.resize(
                template_bgr, (max(1, int(tw * scale)), max(1, int(th * scale))))
        res = cv2.matchTemplate(screen_bgr, template_bgr, cv2.TM_CCOEFF_NORMED)
        return float(res.max())

    def _alert(self, shot, score):
        subject = '[AION] 캡차 감지됨'
        body = (f"캡차 화면이 감지되었습니다.\n"
                f"시각: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"기준 이미지: {shot['file']}\n"
                f"유사도: {score:.4f} (기준 {self.threshold:.2f})")
        try:
            mailSender.sendMail(subject, body)
        except Exception:
            logging.exception('captcha mail error')

    def check_once(self):
        with self.lock:
            if not self.enabled or not self.shots:
                return
            snapshot = list(self.shots)
            threshold = self.threshold
        now = time.time()
        try:
            screen = grab_screen_bgr()
        except Exception:
            logging.exception('captcha screenshot error')
            return
        for shot in snapshot:
            try:
                # 저장한 이미지를 화면 전체에서 좌표 무관하게 탐색
                score = self._match_score(screen, shot['img'])
            except Exception:
                logging.exception('captcha compare error')
                continue
            if score >= threshold:
                # 새로 감지됐거나 쿨다운이 지났을 때만 알림
                if (not shot['detected']) and (now - shot['last_alert'] >= CAPTCHA_ALERT_COOLDOWN):
                    shot['detected'] = True
                    shot['last_alert'] = now
                    self._alert(shot, score)
                else:
                    shot['detected'] = True
            else:
                shot['detected'] = False

    def loop(self):
        while True:
            time.sleep(CAPTCHA_INTERVAL)
            try:
                self.check_once()
            except Exception:
                logging.exception('captcha loop error')


captcha_monitor = CaptchaMonitor()


# ==========================================================================
# 프리셋 저장 / 불러오기
# ==========================================================================

DEFAULT_PRESETS = {
    '공격4 / 이동없음': {
        'attack_keys': ['4'],
        'movement_mode': 'none',
        'use_g': True,
        'use_jump': True,
        'use_a_find': True,
    },
    '공격3 / 8방향': {
        'attack_keys': ['3'],
        'movement_mode': 'random_8dir',
        'use_g': True,
        'use_jump': True,
        'use_a_find': True,
    },
}


def load_presets():
    try:
        with open(PRESET_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, dict) and data:
                return data
    except Exception:
        pass
    return dict(DEFAULT_PRESETS)


def save_presets(presets):
    try:
        with open(PRESET_PATH, 'w', encoding='utf-8') as f:
            json.dump(presets, f, ensure_ascii=False, indent=2)
    except Exception:
        logging.exception('preset save error')


# ==========================================================================
# UI
# ==========================================================================

class AionUI:
    def __init__(self, root):
        self.root = root
        self.presets = load_presets()

        root.title('AION 매크로 제어판')
        root.attributes('-topmost', True)
        root.resizable(False, False)

        # 색을 자유롭게 지정하려면 네이티브 aqua 대신 clam 테마 사용
        self.style = ttk.Style()
        try:
            self.style.theme_use('clam')
        except Exception:
            pass
        self.style.configure('Big.TButton', font=('', 13, 'bold'), padding=(10, 16))
        self.theme = load_ui_config().get('theme', 'dark')

        pad = {'padx': 8, 'pady': 4}

        # ---- 상태 / 시작·중지 ----
        top = ttk.Frame(root)
        top.grid(row=0, column=0, sticky='ew', padx=10, pady=(10, 4))

        self.status_var = tk.StringVar(value='일시중지')
        self.status_lbl = tk.Label(top, textvariable=self.status_var,
                                   font=('', 14, 'bold'), width=8)
        self.status_lbl.pack(side='left')

        self.toggle_btn = ttk.Button(top, text='▶ 시작', width=12,
                                     style='Big.TButton', command=self.toggle_running)
        self.toggle_btn.pack(side='right', padx=(16, 0))

        # 테마 선택 (다크 / 라이트)
        ttk.Label(top, text='테마:').pack(side='left', padx=(12, 2))
        self.theme_var = tk.StringVar(value=THEME_KEY_TO_LABEL.get(self.theme, '다크'))
        theme_combo = ttk.Combobox(top, textvariable=self.theme_var, state='readonly',
                                   values=list(THEME_LABELS.keys()), width=6)
        theme_combo.pack(side='left')
        theme_combo.bind('<<ComboboxSelected>>', self.on_theme_change)

        # ---- 공격키 ----
        atk = ttk.LabelFrame(root, text='공격키 (쉼표로 여러 개)')
        atk.grid(row=1, column=0, sticky='ew', padx=10, pady=6)
        self.attack_var = tk.StringVar(value=','.join(state['attack_keys']))
        self.attack_var.trace_add('write', self.on_attack_change)
        ttk.Entry(atk, textvariable=self.attack_var, width=30).pack(**pad, fill='x')

        # ---- 이동 설정 ----
        mv = ttk.LabelFrame(root, text='움직임 설정')
        mv.grid(row=2, column=0, sticky='ew', padx=10, pady=6)
        self.move_var = tk.StringVar(value=MOVEMENT_KEY_TO_LABEL[state['movement_mode']])
        self.move_combo = ttk.Combobox(mv, textvariable=self.move_var, state='readonly',
                                       values=list(MOVEMENT_LABELS.keys()), width=28)
        self.move_combo.pack(**pad, fill='x')
        self.move_combo.bind('<<ComboboxSelected>>', self.on_move_change)

        # 선택한 이동 타입의 유지시간(초). 타입마다 개별 저장됨.
        dur_row = ttk.Frame(mv)
        dur_row.pack(**pad, fill='x')
        ttk.Label(dur_row, text='유지시간(초, 0=자동):').pack(side='left')
        self._loading = True
        self.dur_var = tk.StringVar()
        self.dur_var.trace_add('write', self.on_duration_change)
        ttk.Entry(dur_row, textvariable=self.dur_var, width=8).pack(side='right')
        self._loading = False
        self.refresh_duration_field()

        # ---- 옵션 체크박스 ----
        opt = ttk.LabelFrame(root, text='옵션')
        opt.grid(row=3, column=0, sticky='ew', padx=10, pady=6)
        self.use_g_var = tk.BooleanVar(value=state['use_g'])
        self.use_jump_var = tk.BooleanVar(value=state['use_jump'])
        self.use_afind_var = tk.BooleanVar(value=state['use_a_find'])
        ttk.Checkbutton(opt, text="공격 중 'g' 섞기", variable=self.use_g_var,
                        command=self.on_options_change).pack(anchor='w', **pad)
        ttk.Checkbutton(opt, text='주기적 점프 (space)', variable=self.use_jump_var,
                        command=self.on_options_change).pack(anchor='w', **pad)
        ttk.Checkbutton(opt, text='a_find 감지 (8방향 모드)', variable=self.use_afind_var,
                        command=self.on_options_change).pack(anchor='w', **pad)

        # ---- 프리셋 ----
        ps = ttk.LabelFrame(root, text='프리셋')
        ps.grid(row=4, column=0, sticky='ew', padx=10, pady=6)
        for c in range(3):
            ps.columnconfigure(c, weight=1, uniform='ps')
        self.preset_var = tk.StringVar()
        self.preset_combo = ttk.Combobox(ps, textvariable=self.preset_var, state='readonly',
                                         values=list(self.presets.keys()), width=28)
        self.preset_combo.grid(row=0, column=0, columnspan=3, sticky='ew', padx=6, pady=(6, 4))
        self.preset_combo.bind('<<ComboboxSelected>>', self.on_preset_select)

        ttk.Button(ps, text='불러오기', command=self.load_preset).grid(row=1, column=0, sticky='ew', padx=6, pady=4)
        ttk.Button(ps, text='저장', command=self.save_current_preset).grid(row=1, column=1, sticky='ew', padx=6, pady=4)
        ttk.Button(ps, text='삭제', command=self.delete_preset).grid(row=1, column=2, sticky='ew', padx=6, pady=4)

        ttk.Label(ps, text='이름:').grid(row=2, column=0, sticky='w', padx=6, pady=(4, 6))
        self.preset_name_var = tk.StringVar()
        ttk.Entry(ps, textvariable=self.preset_name_var).grid(
            row=2, column=1, columnspan=2, sticky='ew', padx=6, pady=(4, 6))

        # ---- 캡차 감지 ----
        cap = ttk.LabelFrame(root, text='캡차 감지 (10초 주기 스크린샷 비교)')
        cap.grid(row=5, column=0, sticky='ew', padx=10, pady=6)

        cap_top = ttk.Frame(cap)
        cap_top.pack(fill='x', **pad)
        self.captcha_on_var = tk.BooleanVar(value=captcha_monitor.enabled)
        ttk.Checkbutton(cap_top, text='캡차 감지 사용', variable=self.captcha_on_var,
                        command=self.on_captcha_toggle).pack(side='left')
        ttk.Label(cap_top, text='민감도:').pack(side='left', padx=(10, 2))
        self.captcha_thr_var = tk.StringVar(value=('%g' % captcha_monitor.threshold))
        thr = ttk.Entry(cap_top, textvariable=self.captcha_thr_var, width=6)
        thr.pack(side='left')
        thr.bind('<Return>', self.on_captcha_threshold)
        thr.bind('<FocusOut>', self.on_captcha_threshold)

        self.captcha_list = tk.Listbox(cap, height=4)
        self.captcha_list.pack(fill='x', padx=8, pady=4)

        cap_btns = ttk.Frame(cap)
        cap_btns.pack(fill='x', **pad)
        ttk.Button(cap_btns, text='＋ 스크린샷 추가', command=self.add_captcha_screenshot).pack(side='left')
        ttk.Button(cap_btns, text='선택 삭제', command=self.delete_captcha_shot).pack(side='left', padx=6)
        self.refresh_captcha_list()

        # 입력칸에 값 입력 후: 다른 곳 클릭 / Enter 시 포커스 아웃
        root.bind_all('<Button-1>', self._maybe_defocus, add='+')
        root.bind_all('<Return>', lambda e: self.root.focus_set(), add='+')

        root.protocol('WM_DELETE_WINDOW', self.on_close)
        self.apply_theme(self.theme)
        self.refresh_status()

    # ---- 테마 ----
    def on_theme_change(self, *_):
        self.theme = THEME_LABELS.get(self.theme_var.get(), 'dark')
        self.apply_theme(self.theme)
        cfg = load_ui_config()
        cfg['theme'] = self.theme
        save_ui_config(cfg)
        self.root.focus()

    def apply_theme(self, name):
        p = THEMES.get(name, THEMES['dark'])
        s = self.style
        self.root.configure(bg=p['bg'])
        s.configure('.', background=p['bg'], foreground=p['fg'],
                    fieldbackground=p['entry_bg'], bordercolor=p['btn_bg'],
                    lightcolor=p['btn_bg'], darkcolor=p['btn_bg'])
        s.configure('TFrame', background=p['bg'])
        s.configure('TLabel', background=p['bg'], foreground=p['fg'])
        s.configure('TLabelframe', background=p['bg'])
        s.configure('TLabelframe.Label', background=p['bg'], foreground=p['frame_fg'])
        s.configure('TCheckbutton', background=p['bg'], foreground=p['fg'])
        s.map('TCheckbutton', background=[('active', p['bg'])])
        s.configure('TButton', background=p['btn_bg'], foreground=p['fg'])
        s.configure('Big.TButton', background=p['btn_bg'], foreground=p['fg'])
        s.map('TButton', background=[('active', p['active'])])
        s.map('Big.TButton', background=[('active', p['active'])])
        s.configure('TEntry', fieldbackground=p['entry_bg'], foreground=p['fg'],
                    insertcolor=p['fg'])
        s.configure('TCombobox', fieldbackground=p['entry_bg'], foreground=p['fg'],
                    background=p['btn_bg'], arrowcolor=p['fg'])
        s.map('TCombobox', fieldbackground=[('readonly', p['entry_bg'])],
              foreground=[('readonly', p['fg'])])
        # 클래식 tk 위젯 (직접 색 지정)
        self.status_lbl.config(bg=p['bg'])
        self.captcha_list.config(bg=p['list_bg'], fg=p['fg'], selectbackground=p['active'],
                                 selectforeground=p['fg'], highlightbackground=p['bg'])
        # 콤보박스 드롭다운 목록 색
        self.root.option_add('*TCombobox*Listbox.background', p['list_bg'])
        self.root.option_add('*TCombobox*Listbox.foreground', p['fg'])
        self.root.option_add('*TCombobox*Listbox.selectBackground', p['active'])
        self.root.option_add('*TCombobox*Listbox.selectForeground', p['fg'])
        self.refresh_status()

    def _maybe_defocus(self, event):
        """입력 위젯이 아닌 곳을 클릭하면 포커스를 창으로 되돌린다(입력칸 blur)."""
        if not isinstance(event.widget, (tk.Entry, ttk.Entry, ttk.Combobox)):
            self.root.focus_set()

    # ---- 설정 변경 콜백 (즉시 반영) ----
    def on_attack_change(self, *_):
        keys = [k.strip() for k in self.attack_var.get().split(',') if k.strip()]
        with state_lock:
            state['attack_keys'] = keys

    def on_move_change(self, *_):
        mode = MOVEMENT_LABELS.get(self.move_var.get(), 'none')
        with state_lock:
            state['movement_mode'] = mode
        # 선택한 타입의 유지시간을 입력칸에 반영
        self.refresh_duration_field()
        # 선택 후 남는 파란 하이라이트 제거
        self.move_combo.selection_clear()
        self.root.focus()

    def refresh_duration_field(self):
        """현재 선택된 이동 타입의 유지시간을 입력칸에 표시"""
        mode = MOVEMENT_LABELS.get(self.move_var.get(), 'none')
        with state_lock:
            v = state['move_durations'].get(mode, 0.0)
        self._loading = True
        self.dur_var.set(('%g' % v) if v else '0')
        self._loading = False

    def on_duration_change(self, *_):
        if self._loading:
            return
        mode = MOVEMENT_LABELS.get(self.move_var.get(), 'none')
        try:
            v = max(0.0, float(self.dur_var.get()))
        except ValueError:
            return  # 입력 도중(빈 값 등)에는 무시
        with state_lock:
            state['move_durations'][mode] = v

    def on_preset_select(self, *_):
        # 콤보박스에서 프리셋을 고르는 즉시 불러오기
        self.preset_combo.selection_clear()
        self.root.focus()
        self.load_preset()

    def on_options_change(self):
        with state_lock:
            state['use_g'] = self.use_g_var.get()
            state['use_jump'] = self.use_jump_var.get()
            state['use_a_find'] = self.use_afind_var.get()

    # ---- 시작 / 일시중지 ----
    def toggle_running(self):
        set_running(not running_event.is_set())
        self.refresh_status()

    def refresh_status(self):
        p = THEMES.get(self.theme, THEMES['dark'])
        if running_event.is_set():
            self.status_var.set('동작 중')
            self.status_lbl.config(fg=p['run'])
            self.toggle_btn.config(text='⏸ 일시중지')
        else:
            self.status_var.set('일시중지')
            self.status_lbl.config(fg=p['pause'])
            self.toggle_btn.config(text='▶ 시작')

    # ---- 프리셋 ----
    def apply_config(self, cfg):
        self.attack_var.set(','.join(cfg.get('attack_keys', ['4'])))
        mode = cfg.get('movement_mode', 'none')
        self.move_var.set(MOVEMENT_KEY_TO_LABEL.get(mode, MOVEMENT_KEY_TO_LABEL['none']))
        self.use_g_var.set(cfg.get('use_g', True))
        self.use_jump_var.set(cfg.get('use_jump', True))
        self.use_afind_var.set(cfg.get('use_a_find', True))
        # 이동 타입별 유지시간 반영 (없는 타입은 0=자동)
        durs = cfg.get('move_durations', {})
        with state_lock:
            for m in DEFAULT_HOLD:
                state['move_durations'][m] = float(durs.get(m, 0.0) or 0.0)
        # trace/command 콜백을 확실히 태워 상태에 반영
        self.on_attack_change()
        self.on_move_change()  # refresh_duration_field 포함
        self.on_options_change()

    def load_preset(self):
        name = self.preset_var.get()
        if not name or name not in self.presets:
            messagebox.showinfo('프리셋', '불러올 프리셋을 선택하세요.')
            return
        self.apply_config(self.presets[name])
        self.preset_name_var.set(name)

    def save_current_preset(self):
        name = self.preset_name_var.get().strip() or self.preset_var.get().strip()
        if not name:
            messagebox.showinfo('프리셋', '저장할 프리셋 이름을 입력하세요.')
            return
        with state_lock:
            cfg = {
                'attack_keys': list(state['attack_keys']),
                'movement_mode': state['movement_mode'],
                'use_g': state['use_g'],
                'use_jump': state['use_jump'],
                'use_a_find': state['use_a_find'],
                'move_durations': dict(state['move_durations']),
            }
        self.presets[name] = cfg
        save_presets(self.presets)
        self.preset_combo['values'] = list(self.presets.keys())
        self.preset_var.set(name)
        messagebox.showinfo('프리셋', f'"{name}" 저장 완료.')

    def delete_preset(self):
        name = self.preset_var.get()
        if not name or name not in self.presets:
            messagebox.showinfo('프리셋', '삭제할 프리셋을 선택하세요.')
            return
        if not messagebox.askyesno('프리셋', f'"{name}" 프리셋을 삭제할까요?'):
            return
        del self.presets[name]
        save_presets(self.presets)
        self.preset_combo['values'] = list(self.presets.keys())
        self.preset_var.set('')

    # ---- 캡차 감지 ----
    def on_captcha_toggle(self):
        captcha_monitor.set_enabled(self.captcha_on_var.get())

    def on_captcha_threshold(self, *_):
        try:
            v = float(self.captcha_thr_var.get())
        except ValueError:
            self.captcha_thr_var.set('%g' % captcha_monitor.threshold)
            return
        v = min(1.0, max(0.1, v))
        captcha_monitor.set_threshold(v)
        self.captcha_thr_var.set('%g' % v)

    def refresh_captcha_list(self):
        self.captcha_list.delete(0, tk.END)
        for label in captcha_monitor.list_labels():
            self.captcha_list.insert(tk.END, label)

    def delete_captcha_shot(self):
        sel = self.captcha_list.curselection()
        if not sel:
            messagebox.showinfo('캡차', '삭제할 스크린샷을 목록에서 선택하세요.')
            return
        captcha_monitor.remove_shot(sel[0])
        self.refresh_captcha_list()

    def add_captcha_screenshot(self):
        """지금 화면 위에 반투명 오버레이를 덮어 드래그로 캡차 영역을 지정하고 등록.
        macOS에서 -fullscreen 은 새 Space(새 창)로 전환되므로 사용하지 않고,
        테두리 없는 창을 현재 화면 크기로 덮어씌운다."""
        self.root.withdraw()  # 제어판이 캡처에 잡히지 않도록 잠시 숨김

        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()

        ov = tk.Toplevel()
        ov.overrideredirect(True)        # 테두리 없는 창 → 현재 화면 위에 그대로 덮임
        ov.geometry(f'{sw}x{sh}+0+0')
        ov.attributes('-alpha', 0.25)
        ov.attributes('-topmost', True)
        ov.configure(bg='black', cursor='cross')
        canvas = tk.Canvas(ov, highlightthickness=0, bg='black')
        canvas.pack(fill='both', expand=True)
        canvas.create_text(
            sw // 2, 40, fill='white', font=('', 16, 'bold'),
            text='캡차가 뜨는 영역을 드래그해서 지정하세요 (ESC 또는 우클릭 취소)')

        sel = {'x0': 0, 'y0': 0, 'rect': None}

        def on_press(e):
            sel['x0'], sel['y0'] = e.x, e.y
            sel['rect'] = canvas.create_rectangle(e.x, e.y, e.x, e.y, outline='red', width=2)

        def on_drag(e):
            if sel['rect'] is not None:
                canvas.coords(sel['rect'], sel['x0'], sel['y0'], e.x, e.y)

        def cancel(_=None):
            ov.destroy()
            self.root.deiconify()

        def on_release(e):
            x, y = min(sel['x0'], e.x), min(sel['y0'], e.y)
            w, h = abs(e.x - sel['x0']), abs(e.y - sel['y0'])
            ov.destroy()
            self.root.deiconify()
            if w < 5 or h < 5:
                messagebox.showinfo('캡차', '영역이 너무 작습니다. 다시 지정하세요.')
                return
            # 오버레이가 완전히 사라진 뒤 캡처
            self.root.update()
            time.sleep(0.25)
            try:
                captcha_monitor.add_shot((x, y, w, h))
            except Exception:
                logging.exception('captcha add error')
                messagebox.showerror('캡차', '스크린샷 등록에 실패했습니다.')
                return
            self.refresh_captcha_list()

        canvas.bind('<ButtonPress-1>', on_press)
        canvas.bind('<B1-Motion>', on_drag)
        canvas.bind('<ButtonRelease-1>', on_release)
        canvas.bind('<Button-3>', cancel)      # 우클릭 취소
        ov.bind('<Escape>', cancel)
        ov.update_idletasks()
        ov.grab_set()                          # 입력을 오버레이로 집중 (ESC 인식)
        ov.focus_force()

    def on_close(self):
        set_running(False)
        self.root.destroy()


def start_workers():
    # pyautogui를 메인 쓰레드에서 미리 초기화 (스레드 동시 호출 경합 방지)
    pyautogui.position()
    pyautogui.PAUSE = 0.01

    threading.Thread(target=attack_loop, daemon=True, name='attack').start()
    threading.Thread(target=jump_loop, daemon=True, name='jump').start()
    threading.Thread(target=movement_manager, daemon=True, name='movement').start()
    # 캡차 감지는 일시중지와 무관하게 상시 감시
    threading.Thread(target=captcha_monitor.loop, daemon=True, name='captcha').start()


def main():
    start_workers()  # 시작 시엔 일시중지 상태 (running_event 미설정)
    root = tk.Tk()
    AionUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()

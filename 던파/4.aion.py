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
from datetime import datetime
import mailSender
import random
import imageFinder
import keyboard2
import sys
import threading

from tobe import *

select('보리뚜')

os.system('rm -rf imagesLog/*')

# 키 풀: 8방향이 모두 한 번씩 실행되도록 보장
# 단일 키: 4방향(동서남북), 튜플: 4방향(대각선)
DIRECTION_POOL = ['a', 'd', 's', 'w', ('w','d'), ('w','a'), ('s','d'), ('s','a')]
key_pool = []
key_pool_lock = threading.Lock()

pyautogui_lock = threading.Lock()

def press_direction(direction, duration=0.5):
    """단일 키 또는 대각선(2키 동시) 방향 이동"""
    keys = (direction,) if isinstance(direction, str) else direction
    pressed = []
    try:
        for k in keys:
            pyautogui.keyDown(k)
            pressed.append(k)
        time.sleep(duration)
    except RuntimeError:
        pass
    finally:
        for k in reversed(pressed):
            try:
                pyautogui.keyUp(k)
            except RuntimeError:
                pass

def movement_loop():
    """이동 쓰레드 - g키와 8방향키 처리"""
    global key_pool
    while True:

        if(do(Founder('a_find'), onlyOneTime=True)):
            time.sleep(random.uniform(1.35, 1.65))
            continue

        with key_pool_lock:
            # key_pool이 비어있으면 새로 채우고 섞기
            if not key_pool:
                key_pool = DIRECTION_POOL[:]
                random.shuffle(key_pool)
            # 리스트에서 하나 꺼내서 사용
            direction = key_pool.pop(0)
        press_direction(direction, duration=random.uniform(0.5, 1.3))
        time.sleep(random.uniform(0.35, 2.15))

def movement_horizenal():
    """이동 쓰레드 - 위(w)와 아래(s)를 3초씩 교대로 반복"""
    directions = ['w', 's']
    idx = 0
    while True:
        press_direction(directions[idx], duration=0.3)
        idx = 1 - idx
        time.sleep(random.uniform(13.35, 14.15))

def movement_horizontal_lr():
    """좌우 이동 쓰레드 - 좌(a)와 우(d)를 0.5초씩 0.5~1.5초 간격으로 교대 반복"""
    directions = ['d', 'a']
    idx = 0
    while True:
        press_direction(directions[idx], duration=5.0)
        idx = 1 - idx
        time.sleep(random.uniform(5.5, 10.5))

def movement_octagon():
    """팔각형 이동 쓰레드 - 8방향을 순서대로 각 1초씩 빙글빙글 반복"""
    # 시계방향: 위 → 우상 → 우 → 우하 → 아래 → 좌하 → 좌 → 좌상
    directions = ['w', ('w', 'd'), 'd', ('s', 'd'), 's', ('s', 'a'), 'a', ('w', 'a')]
    idx = 0
    while True:
        try:
            press_direction(directions[idx], duration=1.5)
        except Exception:
            pass
        idx = (idx + 1) % 8
        # time.sleep(random.uniform(0.05, 0.15))

def movement_center_biased():
    """랜덤 이동 - 짧은 burst + 관성 + 중앙 가중치로 자연스럽게 움직임"""
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
    prev_vec = (0.0, 0.0)  # 이전 이동 방향 벡터 (관성용)

    while True:
        to_center_x = -pos_x
        to_center_y = -pos_y
        dist = (to_center_x ** 2 + to_center_y ** 2) ** 0.5

        weights = []
        for d in directions:
            dx, dy = DIRECTION_VECTORS[d]
            dir_len = (dx ** 2 + dy ** 2) ** 0.5
            dx_n, dy_n = dx / dir_len, dy / dir_len

            # 1) 중앙 가중치: 중앙 방향과 얼마나 일치하는지
            if dist > 0:
                center_cos = (dx_n * to_center_x + dy_n * to_center_y) / dist
                center_w = 1.0 + center_cos * min(dist * 0.5, 3.0)
            else:
                center_w = 1.0

            # 2) 관성 가중치: 이전 방향과 얼마나 가까운지 (급격한 전환 억제)
            prev_len = (prev_vec[0] ** 2 + prev_vec[1] ** 2) ** 0.5
            if prev_len > 0:
                momentum_cos = (dx_n * prev_vec[0] + dy_n * prev_vec[1]) / prev_len
                momentum_w = 1.0 + momentum_cos * 1.8
            else:
                momentum_w = 1.0

            weights.append(max(center_w * momentum_w, 0.05))

        direction = random.choices(directions, weights=weights, k=1)[0]

        # 짧은 burst로 끊김 없이 연속 이동
        duration = random.uniform(0.1, 0.35)
        press_direction(direction, duration=duration)

        dx, dy = DIRECTION_VECTORS[direction]
        dir_len = (dx ** 2 + dy ** 2) ** 0.5
        prev_vec = (dx / dir_len, dy / dir_len)

        pos_x += dx * duration
        pos_y += dy * duration

        # 이동 사이 거의 끊김 없음 (자연스러운 흐름)
        time.sleep(random.uniform(0.0, 0.08))


def attack_loop(key='3'):
    """공격 쓰레드 - key 반복 입력"""
    while True:
        if random.random() < 0.41:
            pyautogui.press('g')

        pyautogui.press(key)
        time.sleep(random.uniform(0.3, 0.7))

def jump_loop():
    """점프 쓰레드 - 3~5초 간격으로 한 번씩 점프"""
    while True:
        time.sleep(random.uniform(23.0, 35.0))
        pyautogui.press('space')

def infinity():
    # key='1'
    key='3'
    """프로그 무한 - 이동과 공격을 별도 쓰레드로 동시 실행"""
    attack_thread = threading.Thread(target=attack_loop, args=(key,), daemon=True, name='attack')
    attack_thread.start()

    jump_thread = threading.Thread(target=jump_loop, daemon=True, name='jump')
    jump_thread.start()

    # lr_thread = threading.Thread(target=movement_horizontal_lr, daemon=True, name='move_lr')
    # lr_thread.start()

    # 메인 쓰레드(이동)가 종료되면 데몬 쓰레드(공격)도 자동 종료
    # movement_loop()
    movement_horizontal_lr()
    # movement_octagon()
    # movement_center_biased()
infinity()

mailSender.sendMail("[7] Deily Practice Done" , "-")



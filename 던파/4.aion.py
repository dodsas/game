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

def press_direction(direction, duration=0.5):
    """단일 키 또는 대각선(2키 동시) 방향 이동"""
    if isinstance(direction, tuple):
        for k in direction:
            pyautogui.keyDown(k)
        time.sleep(duration)
        for k in reversed(direction):
            pyautogui.keyUp(k)
    else:
        robot.pressKey(direction, sleep=0, duration=duration)

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
        press_direction(directions[idx], duration=5)
        idx = 1 - idx
        time.sleep(random.uniform(2.35, 3.15))

def movement_horizontal_lr():
    """좌우 이동 쓰레드 - 좌(a)와 우(d)를 0.5초씩 0.5~1.5초 간격으로 교대 반복"""
    directions = ['a', 'd']
    idx = 0
    while True:
        press_direction(directions[idx], duration=0.5)
        idx = 1 - idx
        time.sleep(random.uniform(0.5, 1.5))

def attack_loop():
    """공격 쓰레드 - 3번 키 반복 입력"""
    while True:
        if random.random() < 0.21:
            pyautogui.press('g')

        # pyautogui.press('`')
        pyautogui.press('1')
        time.sleep(random.uniform(0.3, 0.7))

def infinity():
    """프로그 무한 - 이동과 공격을 별도 쓰레드로 동시 실행"""
    attack_thread = threading.Thread(target=attack_loop, daemon=True, name='attack')
    attack_thread.start()

    lr_thread = threading.Thread(target=movement_horizontal_lr, daemon=True, name='move_lr')
    lr_thread.start()

    # 메인 쓰레드(이동)가 종료되면 데몬 쓰레드(공격)도 자동 종료
    # movement_loop()
    movement_horizenal()

infinity()

mailSender.sendMail("[7] Deily Practice Done" , "-")



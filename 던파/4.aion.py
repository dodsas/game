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

from tobe import * 

select('보리뚜')

os.system('rm -rf imagesLog/*')

# 키 풀: 4번마다 a, s, d, w가 모두 한 번씩 실행되도록 보장
key_pool = []

def infinity():
    """프로그 무한 - 1을 무한 누르기"""
    global key_pool

    while True:

        if(random.random() < 0.21):
            print('aaaa')
            pyautogui.press('g')

            if(random.random() < 0.95):
                # key_pool이 비어있으면 새로 채우고 섞기
                if not key_pool:
                    key_pool = ['a', 's', 'd', 'w']
                    random.shuffle(key_pool)

                # 리스트에서 하나 꺼내서 사용
                key_to_press = key_pool.pop(0)
                robot.pressKey(key_to_press, duration=1)

        pyautogui.press('3')
        time.sleep(random.uniform(0.5,1.3))

infinity()

mailSender.sendMail("[7] Deily Practice Done" , "-")



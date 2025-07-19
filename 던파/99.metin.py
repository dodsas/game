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
sys.path.append('tobe')
from image_robot import * 

os.system('rm -rf imagesLog/*')

# 토글 상태와 마지막 실행 시간을 저장하는 변수
toggle_state = True
last_execution_time = None

def doDirect(x, y, delay=1):
    do(Direct(x, y),printFail2=False,onlyOneTime=True,delay=delay) 

def goToHunting():
    global toggle_state

    # 동작 수행
    do(Direct(1801, 730))  # auto
    time.sleep(1)
    if toggle_state:
        # do(Direct(1382, 548))  # 1st
        do(Direct(1371, 595))  # 3nd
    else:
        # do(Direct(1382, 548))  # 1st
        do(Direct(1371, 595))  # 3nd
    # 토글 상태 변경
    toggle_state = not toggle_state
    time.sleep(2)
    do(Direct(1667, 660))  # ok

def recoverItem():
    do(Direct(1733, 461),delay=1) # 복구 
    do(Direct(1394, 737),delay=1) # 복구확인
    do(Direct(1667, 660),delay=1) # ok 
    do(Direct(1460, 509),delay=1) # x

def mac2():
    global last_execution_time

    if(do(Clicker('mac2', threshold=0.90), onlyOneTime=True, fallbackSkip=True, printFail2=False)):
        # 현재 시간을 기록
        current_time = time.time()

        # 이전 실행 시간 출력 (첫 실행 시에는 출력하지 않음)
        if last_execution_time is not None:
            elapsed_time = current_time - last_execution_time
            print(f"이전 실행부터 걸린 시간: {elapsed_time:.2f}초")
        else:
            print("첫 실행입니다.")

        # 현재 실행 기록 저장
        last_execution_time = current_time

        doDirect(1859, 678) # skip 
        # doDirect(1596, 608) # center 
        doDirect(1322, 522) # center 

        doDirect(1876, 463,delay=1.5) # menu 
        doDirect(1889, 501,delay=1) # menu - quest 
        doDirect(1889, 501) # menu - quest 
        doDirect(1412, 495,delay=1) # menu - quest - sub
        doDirect(1344, 623) # menu - quest - sub - nagira
        doDirect(1452, 571) # menu - quest - sub - nagira - bad girl
        doDirect(1781, 744) # menu - quest - accept
        doDirect(1859, 678) # skip 
        doDirect(1646, 722) # ok bottom
        doDirect(1876, 463) # menu 

# i = 0
while True:
    time.sleep(1)
    if(do(Clicker('die', threshold=0.95), onlyOneTime=True, fallbackSkip=True, printFail2=False)):
        time.sleep(20)
        print('send mail')
        mailSender.sendMail("[METIN] DIE" , "-")
        time.sleep(20)
        recoverItem()
        time.sleep(40)
        goToHunting()

    mac2()

    # every 1 minuate call functio        
    # if i % 20 == 0 :
    #     do(Direct(1856, 729)) # attack
    # i = i + 1

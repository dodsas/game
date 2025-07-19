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

os.system('rm -rf imagesLog/*')

# 토글 상태를 저장하는 변수
toggle_state = True

def goToHunting():
    global toggle_state
    do(Direct(1801, 730))  # auto
    time.sleep(1)
    if toggle_state:
        do(Direct(1382, 548))  # 1st
    else:
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
    if(do(Clicker('mac2', threshold=0.90), onlyOneTime=True)):
        do(Direct(1859, 678),delay=1) # skip 
        do(Direct(1859, 678),delay=1) # skip 

        do(Direct(1876, 463),delay=1) # menu 
        do(Direct(1889, 501),delay=1) # menu - quest 
        do(Direct(1412, 495),delay=1) # menu - quest - sub
        do(Direct(1344, 623),delay=1) # menu - quest - sub - nagira
        do(Direct(1452, 571),delay=1) # menu - quest - sub - nagira - bad girl
        do(Direct(1781, 744),delay=1) # menu - quest - accept
        do(Direct(1859, 678),delay=1) # skip 
        do(Direct(1646, 722),delay=1) # ok bottom
        do(Direct(1876, 463),delay=1) # menu 
    
# i = 0
while True:
    time.sleep(1)
    if(do(Clicker('die', threshold=0.95), onlyOneTime=True)):
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

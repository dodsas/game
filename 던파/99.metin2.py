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
    time.sleep(1)
    do(Direct(x, y),printFail2=False,onlyOneTime=True,delay=delay) 

def goToHunting():
    global toggle_state

    # 동작 수행
    do(Direct(1801, 730))  # auto
    time.sleep(1)
    if toggle_state:
        do(Direct(1382, 548))  # 1st
        # do(Direct(1371, 595))  # 3nd
    else:
        do(Direct(1382, 548))  # 1st
        # do(Direct(1371, 595))  # 3nd
    # 토글 상태 변경
    toggle_state = not toggle_state
    time.sleep(2)
    do(Direct(1667, 660))  # ok

def recoverItem():
    do(Direct(1733, 461),delay=1) # 복구 
    do(Direct(1394, 737),delay=1) # 복구확인
    do(Direct(1667, 660),delay=1) # ok 
    do(Direct(1460, 509),delay=1) # x

def tree():
    if(do(Clicker('tree', threshold=0.90), onlyOneTime=True, fallbackSkip=True, printFail2=False)):

        doDirect(1859, 678) # skip 
        doDirect(1859, 678) # skip 
        doDirect(1322, 522) # heartbeat for main frame 

        # doDirect(1876, 463) # menu
        # doDirect(1889, 501,delay=1) # menu - quest 
        do(Clicker('mquest'), fallbackSkip=True)
        do(Clicker('msquest'))
        do(Founder('mscheck'))
        
        doDirect(1349, 595,delay=1) # menu - quest - sub - tree
        do(Founder('msquesttree'))

        # doDirect(1781, 744) # menu - quest - accept
        do(Clicker('mquestaccept'))

        # doDirect(1859, 678) # skip 
        do(Clicker('mquestskip'))

        # doDirect(1646, 722) # ok bottom
        do(Clicker('mquestok'))
        doDirect(1643, 726) # ok bottom
        doDirect(1643, 726, delay=1) # ok bottom


def mac2():
    global last_execution_time

    if(do(Clicker('mac2', threshold=0.90), onlyOneTime=True, fallbackSkip=True, printFail2=False)):
        delay = 0.1
        doDirect(1859, 678, delay=delay) # skip 
        doDirect(1322, 522, delay=delay) # heartbeat for main frame 

        # doDirect(1876, 463) # menu
        # doDirect(1889, 501,delay=1) # menu - quest 
        #if(do(Clicker('mquest'), canSkip=True) is False):
        #    image_clicker.clickDirect(1876, 463)
        #    do(Clicker('mquest')
        do(Clicker('mquest'), delay=delay)
        do(Clicker('msquest'), delay=delay)
        do(Founder('mscheck'), delay=delay)
        
        doDirect(1349, 623, delay=0.1) # menu - quest - sub - nagira
        # do(Founder('msquesttree'))
        do(Founder('mquestbadw'), delay=delay)

        # doDirect(1781, 744) # menu - quest - accept
        do(Clicker('mquestaccept'), delay=delay)

        # doDirect(1859, 678) # skip 
        do(Clicker('mquestskip'), delay=delay)

        do(Clicker('mquestok'), delay=delay)
        doDirect(1643, 726) # ok bottom
        # doDirect(1643, 726, delay=1) # ok bottom

i = 0
while True:

    if(do(Clicker('die', threshold=0.95), onlyOneTime=True, fallbackSkip=True, printFail2=False)):
        time.sleep(20)
        print('send mail')
        mailSender.sendMail("[METIN] DIE" , "-")
        time.sleep(20)
        recoverItem()
        time.sleep(40)
        goToHunting()

    mac2()
    # tree()

    # tree fallback

    # every 1 minuate call functio        
    #if i % 20 == 0 :
    #    doDirect(1322, 522) # heartbeat for main frame 
    #i = i + 1

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

def infinity():
    """프로그 무한 - 1을 무한 누르기"""
    while True:
        if(do(Founder('a_root2', threshold=0.86), onlyOneTime=True, printFail2=False)):
            pyautogui.press('g')

        # time.sleep(abs(random.random() * 3))
        if do(Founder('a_find'), onlyOneTime=True, printFail2=False) == False :
            # robot.pressKey(random.choice(['a', 's', 'd', 'w']), duration=2)
            pyautogui.press('`')
            if do(Founder('a_find'), onlyOneTime=True, printFail2=False) == False :
                time.sleep(random.uniform(0.01, 0.5))
            else :
                continue

        pyautogui.press('3')
        if random.random() < 0.58:
            pyautogui.press('1')

infinity()

mailSender.sendMail("[7] Deily Practice Done" , "-")



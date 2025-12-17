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
        time.sleep(random.uniform(1, 3))
        pyautogui.press('1')
        if(do(Founder('a_root', threshold=0.88), onlyOneTime=True)):
            pyautogui.press('g')



infinity()

mailSender.sendMail("[7] Deily Practice Done" , "-")



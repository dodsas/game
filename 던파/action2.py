import sys
sys.path.append('tobe')
from image_robot import * 
import image_finder
import image_clicker 

from unit import Unit
import pyautogui
import imageFinder
import imageFinderBulk
import threading
import time
import random
import keyboard2
import robot 
import unit
from datetime import datetime
from functools import wraps
# import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Log before and after decorator
def log_before_and_after(func):
    def wrapper(*args, **kwargs):
        # print("Original Path {image_finder.imgPath}")
        imgPathBackup = image_finder.imgPath

        result = func(*args, **kwargs)
        # print(f"Modified Path {image_finder.imgPath}")

        image_finder.imgPath = imgPathBackup
        # print(f"Recovered Path {image_finder.imgPath}")
        return result
    return wrapper

@log_before_and_after
def 카드합성():
    image_finder.imgPath = 'Image/카드합성/'
    char = unit.selected

    do(Clicker('인벤'))
    do(Clicker('인벤카드'))
    do(Clicker('합성'))

    time.sleep(2)
    do(Clicker('투입선택여부'), onlyOneTime=True)
    do(Clicker('레어'))
    do(Clicker('찐합성'))
    do(Clicker('합성경고'), canSkip=True, okSkip=True)
    do(Clicker('합성결과', threshold=0.83))

    # _카드반복합성()
    # do(Clicker('언커먼'))
    # _카드반복합성()
    # do(Clicker('레어'))
    _카드반복합성()

    do(Clicker('x'))
    do(Clicker('뒤로가기'), okSkip=True)
    # do(Clicker('뒤로가기'), okSkip=True)
    do(Founder('스케쥴러'))
    dun_print.printf(f'카드합성완료')

def _카드반복합성():
    do(Clicker('투입선택여부'), onlyOneTime=True)
    while(True):
        image_clicker.clickDirect(1647, 669)
        image_clicker.clickDirect(1822, 749)

        if(do(Founder('카드소진'), onlyOneTime=True)):
            dun_print.printf(f'소진완료')
            return

@log_before_and_after
def 캐릭터선택2():
    image_finder.imgPath = 'Images/'
    char = unit.selected

    do(Clicker('캐릭_선택', threshold=0.97))
    time.sleep(3)
    do(Founder('캐릭_선택확인'))

    image_clicker.clickDirect(1352, 522)

    for i in range(100):
        if Clicker('캐릭_' + char.name, threshold=0.75).action(printFail=True) :
            break
        pyautogui.sleep(0.5)
        pyautogui.scroll(20000)
    
    if(do(Founder('게임시작_이미접속중', threshold=0.77), onlyOneTime=True, canSkip=True)):
        do(Presser('ESC', fallbackSkip=True))
    else:
        do(Clicker('캐릭_게임시작', threshold=0.80))
        pyautogui.sleep(1)

    do(Founder('스케쥴러'))
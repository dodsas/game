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

# image_finder.imgPath = 'Image/강림로터스/'


os.system('rm -rf imagesLog/*')
for key in map:
    unit.select(key)
    char = map[key]

    if(len(map) != 1):
        action2.캐릭터선택2()

    action.우편함()        
    do(Clicker('모험'))
    do(Clicker('업적'))
    do(Clicker('일괄받기'), canSkip=True)
    do(Clicker('ok'), onlyOneTime=True)
    do(Clicker('뒤로가기'))

    do(Clicker('store'))
    do(Clicker('exchange'))
    do(Clicker('favorite'))
    do(Clicker('buy'), canSkip=True)
    do(Clicker('buyok'), canSkip=True)
    do(Clicker('뒤로가기'))
    
mailSender.sendMail("[DNF] 비밀작전 완료" , "-")


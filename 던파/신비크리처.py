# pyautogui is a module that allows you to control the mouse and keyboard
import pyautogui
import robot
import time
import action
import unit
import os
from datetime import datetime
import mailSender

# import 회수우포
# romove all files in imagesLog folder on osx
os.system('rm -rf imagesLog/*')

map = unit.map
for key in map:
    unit.select(key)
    char = map[key]
    robot.charName = char.name
    action.캐릭터선택(char)
    # action.크리처()
    action.신비상점구매(char)

mailSender.sendMail("[DNF] 신비상점 완료" , "-")
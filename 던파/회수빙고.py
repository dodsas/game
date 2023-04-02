# pyautogui is a module that allows you to control the mouse and keyboard
import pyautogui
import robot
import time
import action
import unit
import os
from datetime import datetime
import imageFinder
import mailSender

import 신비크리처
# map of Unit objects
os.system('rm -rf imagesLog/*')

map = unit.map
for key in map:
    unit.select(key)
    char = map[key]
    robot.charName = char.name
    action.캐릭터선택(char)

    robot.pressKey(';')
    imageFinder.waitAndClick('길드활동')
    imageFinder.waitAndClick('길드빙고')
    imageFinder.waitAndClick('빙고보상모두받기', error=False)
    imageFinder.waitAndClick('확인', error=False, maxWait=1)
    robot.pressKey('esc')
    robot.pressKey('esc')

mailSender.sendMail("[DNF] bingo 완료" , "-")
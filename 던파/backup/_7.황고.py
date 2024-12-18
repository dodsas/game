import pyautogui
import robot
import time
import action
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

# import 신비크리처
# import 기본사냥 
loop=13
map = {
    "보리성": Unit("보리성", s='안톤무기바지벨트목걸이반지', buffIndex=4),
    "베인뚜": Unit("베인뚜", s='안톤상의어깨신발팔찌보장'),
    "보리빵떡": Unit("보리빵떡", s='안톤상의어깨신발팔찌보장'),
    "보리뚜": Unit("보리뚜", s='안톤무기바지벨트목걸이반지'),
    "보리세이더": Unit("보리세이더", s='안톤무기바지벨트목걸이반지'),
    "보리뚜뚜": Unit("보리뚜뚜", s='안톤상의어깨신발팔찌보장'),
    "보리템플러": Unit("보리템플러", s='안톤상의어깨신발팔찌보장'),
    "무녀뚜": Unit("무녀뚜", s='안톤무기바지벨트목걸이반지'),

    "지짱보": Unit("지짱보", s='반지상의하의보장팔찌벨트2'),
    "강한보리": Unit("강한보리"),
    "런처꾸꾸": Unit("런처꾸꾸", s='무기목걸이어깨신발2'),
    "보리꾸꾸": Unit("보리꾸꾸", s='무기목걸이어깨신발2'),
    "건꾸꾸": Unit("건꾸꾸", s='무기목걸이어깨신발2'),
    "보리뚜킥": Unit("보리뚜킥", s='무기목걸이어깨신발2'),
    "보리술사": Unit("보리술사", s='반지상의하의보장팔찌벨트2'),
    "보리심판관": Unit("보리심판관", s='반지상의하의보장팔찌벨트2'),
    "서큐버뚜": Unit("서큐버뚜", s='반지상의하의보장팔찌벨트2'),
    "보리메이지": Unit("보리메이지", s='반지상의하의보장팔찌벨트2'),

    "인챈뚜": Unit("인챈뚜", s='반지상의하의보장팔찌벨트2'),
    "소울뚜": Unit("소울뚜", s='반지상의하의보장팔찌벨트2'),
    "보리핏": Unit("보리핏", s='반지상의하의보장팔찌벨트2'),
    "보리파": Unit("보리파", s='반지상의하의보장팔찌벨트2'),
    "보리커": Unit("보리커", s='무기목걸이어깨신발2'),
    "보리뚜비": Unit("보리뚜비", s='반지상의하의보장팔찌벨트2'),
    "웨펀꾸꾸": Unit("웨펀꾸꾸", s='무기목걸이어깨신발2'),
    "윈드꾸꾸": Unit("윈드꾸꾸"),
    "보리닉": Unit("보리닉"),
}

#map = unit.map
#map = { "보리뚜": Unit("보리뚜", 신비전체구매=True, buffIndex=4, loopCount=loop, epicDone=True) }
for key in map:
    select(key)
    char = map[key]
    robot.charName = char.name
    action.캐릭터선택2()

    do(Clicker('스케쥴러'))
    do(Clicker('서던데일'))
    do(Clicker('입장', threshold=0.81))

    do(Founder('서던데일_입장확인'))
    do(Presser(str(char.buffIndex)))

    isBossFound = False
    for i in range(200):
        if(i%30 == 0 and i != 0):
            # random move with seed
            random.seed(i)
            robot.pressKey('right', duration=2)
            imageFinder.findAndClick('부활', 1, 0.75, error=False)

        if(isBossFound == False and do(Founder('서던데일_보스확인'), onlyOneTime=True)):
            # pyautogui.press(char.finalIndex)
            keyboard2.pressKey(char.finalIndex, sleep=0, duration=0.1)
            isBossFound = True

        # swtich case with random value
        switcher = {
            0: 'q',
            1: 'w',
            2: 'e',
            3: 'r',
        }
        keyboard2.pressKey(switcher.get(random.randint(0,3)), sleep=0, duration=0.1, printLog=False)

        pyautogui.keyDown('x')
        pyautogui.sleep(1.5)

        if(do(Founder('다른긴급의뢰선택', threshold=0.87), onlyOneTime=True)):
        # if(imageFinder.isFound('다른긴급의뢰선택', threshold=0.88, printLog=False) != None):
            pyautogui.keyUp('x')
            # for loop 2 times
            for i in range(2):
                robot.pressKey('left', sleep=0.2)
                pyautogui.keyDown('x')
                pyautogui.sleep(3)
                pyautogui.keyUp('x')
            break
        pyautogui.keyUp('x')
    robot.pressKey('f7', sleep=2)

    do(Clicker('이계운석'))
    do(Clicker('입장', threshold=0.81))

    for i in range(200):
        if(i%30 == 0 and i != 0):
            # random move with seed
            random.seed(i)
            robot.pressKey('right', duration=2)
            imageFinder.findAndClick('부활', 1, 0.75, error=False)

        if(i==5):
            # pyautogui.press(char.finalIndex)
            keyboard2.pressKey(char.finalIndex, sleep=0, duration=0.1)

        # swtich case with random value
        switcher = {
            0: 'q',
            1: 'w',
            2: 'e',
            3: 'r',
        }
        keyboard2.pressKey(switcher.get(random.randint(0,3)), sleep=0, duration=0.1, printLog=False)

        pyautogui.keyDown('x')
        pyautogui.sleep(1.5)

        if(do(Founder('다른긴급의뢰선택', threshold=0.87), onlyOneTime=True)):
        # if(imageFinder.isFound('다른긴급의뢰선택', threshold=0.88, printLog=False) != None):
            pyautogui.keyUp('x')
            # for loop 2 times
            for i in range(2):
                robot.pressKey('left', sleep=0.2)
                pyautogui.keyDown('x')
                pyautogui.sleep(3)
                pyautogui.keyUp('x')
            break
        pyautogui.keyUp('x')
    robot.pressKey('f7', sleep=2)

    do(Clicker('황금고블'))
    do(Clicker('입장', threshold=0.81))

    for i in range(200):
        if(i%30 == 0 and i != 0):
            # random move with seed
            random.seed(i)
            robot.pressKey('right', duration=2)
            imageFinder.findAndClick('부활', 1, 0.75, error=False)

        if(i==5):
            # pyautogui.press(char.finalIndex)
            keyboard2.pressKey(char.finalIndex, sleep=0, duration=0.1)

        # swtich case with random value
        switcher = {
            0: 'q',
            1: 'w',
            2: 'e',
            3: 'r',
        }
        keyboard2.pressKey(switcher.get(random.randint(0,3)), sleep=0, duration=0.1, printLog=False)

        pyautogui.keyDown('x')
        pyautogui.sleep(1.5)

        if(do(Clicker('황금고블_완료', threshold=0.87), onlyOneTime=True)):
            pyautogui.keyUp('x')
            break
        pyautogui.keyUp('x')
    robot.pressKey('f8', sleep=2)

    do(Clicker('의뢰_뒤로가기'))

mailSender.sendMail("[DNF] 완료" , "-")
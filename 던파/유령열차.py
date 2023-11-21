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

image_finder.imgPath = 'Image/유령열차/'

map = {
    # ##  "보리성": Unit("보리성"),
    # #"보리뚜": Unit("보리뚜", s='보장팔찌허리'),
    # #"보리세이더": Unit("보리세이더", s='안톤무기바지벨트목걸이반지'),
    # #"베인뚜": Unit("베인뚜"),
    # #"보리빵떡": Unit("보리빵떡", s='보장팔찌허리'),
    # "보리뚜뚜": Unit("보리뚜뚜", s='안톤무기바지벨트목걸이반지'),
    # "보리템플러": Unit("보리템플러", s='반지상의하의보장팔찌벨트2'),
    # "무녀뚜": Unit("무녀뚜", s='안톤상의어깨신발팔찌보장'),
    # #  "인챈뚜": Unit("인챈뚜"),
    # "소울뚜": Unit("소울뚜", s='반지상의하의보장팔찌벨트2'),
    # "런처꾸꾸": Unit("런처꾸꾸", s='무기목걸이어깨신발2'),
    # "보리술사": Unit("보리술사", s='반지상의하의보장팔찌벨트2'),
    # "보리커": Unit("보리커", s='무기목걸이어깨신발2'),
    # "보리꾸꾸": Unit("보리꾸꾸", s='무기목걸이어깨신발2'),
    # "건꾸꾸": Unit("건꾸꾸", s='무기목걸이어깨신발2'),
    # "보리뚜킥": Unit("보리뚜킥", s='무기목걸이어깨신발2'),
    # # "보리핏": Unit("보리핏", s='반지상의하의보장팔찌벨트2'),
    # "보리심판관": Unit("보리심판관", s='반지상의하의보장팔찌벨트2'),
    # "보리파": Unit("보리파", s='반지상의하의보장팔찌벨트2'),
    # "보리뚜비": Unit("보리뚜비", s='반지상의하의보장팔찌벨트2'),
    "웨펀꾸꾸": Unit("웨펀꾸꾸", s='무기목걸이어깨신발2'),
    "보리메이지": Unit("보리메이지", s='반지상의하의보장팔찌벨트'),
    "지짱보": Unit("지짱보", s='반지상의하의보장팔찌벨트2'),
    "서큐버뚜": Unit("서큐버뚜", s='반지상의하의보장팔찌벨트2'),
    # "보리닉": Unit("보리닉"),
    # "윈드꾸꾸": Unit("윈드꾸꾸"),
}

# map = unit.map
# map = { "보리뚜": Unit("보리뚜") }

os.system('rm -rf imagesLog/*')
for key in map:
    select(key)
    char = map[key]
    robot.charName = char.name
    time.sleep(1)
    pyautogui.keyUp('letf')
    if(len(map) != 1):
        action.캐릭터선택2()
    
    do(Clicker('모험'))
    do(Clicker('의뢰'))
    do(Clicker('의뢰던전'))
    do(Clicker('유령열차'))
    do(Clicker('입장가능지역으로이동'))
    do(Clicker('입장'))
    do(Founder('다음던전입장확인'))
    do(Presser(str(char.buffIndex)))
    pyautogui.keyDown('right')
    time.sleep(1)
    pyautogui.keyUp('right')
    pyautogui.keyDown('x')
    time.sleep(2)
    pyautogui.keyUp('x')
    pyautogui.keyDown('right')
    time.sleep(1)
    pyautogui.keyUp('right')
    pyautogui.keyDown('x')
    time.sleep(2)
    pyautogui.keyUp('x')

    forLoop = 0
    findBoss = False
    # infinite loop
    while True:
        forLoop += 1
        attackLoop = 2
        if findBoss:
            attackLoop = 4
        for i in range(attackLoop):
            if(findBoss is True):
                keyboard2.pressKey2(char.finalIndex)
            pyautogui.keyDown('x')
            if(findBoss):
                time.sleep(1.5)
            else:
                time.sleep(2.5)
            pyautogui.keyUp('x')
            keyboard2.pressKey2('r')
            keyboard2.pressKey2('s')
            keyboard2.pressKey2('d')
            keyboard2.pressKey2('f')
            keyboard2.pressKey2('g')
            keyboard2.pressKey2('t')
            keyboard2.pressKey2('b')
            keyboard2.pressKey2('v')
            keyboard2.pressKey2('q')
            keyboard2.pressKey2('w')
            keyboard2.pressKey2('e')

        if(findBoss is False and do(Founder('보스발견'), onlyOneTime=True)):
            do(Presser(str(char.finalIndex)))
            findBoss = True

        screenShot = image_finder.getScreenShotToGray()
        if(do(Founder('던전완료'), screenShot=screenShot, onlyOneTime=True)):
            pyautogui.keyDown('x')
            time.sleep(3)
            pyautogui.keyUp('x')

            pyautogui.keyDown('right')
            time.sleep(0.5)
            pyautogui.keyUp('right')

            pyautogui.keyDown('x')
            time.sleep(3)
            pyautogui.keyUp('x')

            do(Clicker('던전완료'), onlyOneTime=True, canSkip=True)
            time.sleep(2) 
            if(do(Founder('던전완료'), screenShot=screenShot, onlyOneTime=True) is False):
                pyautogui.keyDown('x')
                time.sleep(3)
                pyautogui.keyUp('x')
                pyautogui.keyDown('left')
                time.sleep(0.5)
                pyautogui.keyUp('left')
                pyautogui.keyDown('x')
                time.sleep(3)
                pyautogui.keyUp('x')
                do(Clicker('던전완료'), canSkip=True)
            break 

        if(forLoop > 225):
            dun_print.errorf(char.name + "실패")

    do(Clicker('뒤로가기'))
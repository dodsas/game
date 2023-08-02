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

def 반지상의하의보장팔찌목걸이():
    do(Clicker('파워스테이션'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('파워스테이션_코레')) # 반지 상의 하의 보장 팔찌 목걸이

def 무기반지어깨신발():
    do(Clicker('파워스테이션'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('파워스테이션_푸르츠')) # 무기 반지 어깨 신발 

def 무기반지어깨신발30():
    do(Clicker('파워스테이션'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('파워스테이션_푸르츠30', threshold=0.7)) # 무기 반지 어깨 신발 

def 무기():
    do(Clicker('원데과학단지'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('원데과학단지_옵티머스')) # 무기

# import 신비크리처
# import 기본사냥 
loop=13
map = {
    # "보리성": Unit("보리성", 신비전체구매=True, buffIndex=4, loopCount=loop, epicDone=True),
    # "보리뚜": Unit("보리뚜", 신비전체구매=True, loopCount=12, sunganDone=False, epicDone=True),
    # "보리세이더": Unit("보리세이더", 신비전체구매=True, loopCount=loop, sunganDone=True, epicDone=True),
    # "베인뚜": Unit("베인뚜", 신비전체구매=True, loopCount=loop, finalIndex='f', epicDone=True),
    # "보리빵떡": Unit("보리빵떡", 신비전체구매=True, loopCount=loop, sunganDone=True, epicDone=True),
    # "보리메이지": Unit("보리메이지", 신비전체구매=False, loopCount=loop),

    "보리템플러": Unit("보리템플러", 신비전체구매=True, loopCount=loop, sunganDone=True, epicDone=True),
    "보리뚜뚜": Unit("보리뚜뚜", 신비전체구매=True, loopCount=loop, epicDone=True),
    "무녀뚜": Unit("무녀뚜", 신비전체구매=False, loopCount=loop, epicDone=True),
    "런처꾸꾸": Unit("런처꾸꾸", 신비전체구매=True, loopCount=loop, sunganDone=True),
    "보리술사": Unit("보리술사", loopCount=loop, sunganDone=True),
    "보리꾸꾸": Unit("보리꾸꾸"),
    "보리뚜킥": Unit("보리뚜킥", loopCount=loop, sunganDone=True, epicDone=True),
    "건꾸꾸": Unit("건꾸꾸", 신비전체구매=False, loopCount=loop),
    "보리핏": Unit("보리핏", 신비전체구매=False, loopCount=loop, sunganDone=True, epicDone=True),
    "보리심판관": Unit("보리심판관", 신비전체구매=False, loopCount=13, epicDone=True),
    "보리커": Unit("보리커", 신비전체구매=True, loopCount=13),
    "소울뚜": Unit("소울뚜", loopCount=loop, sunganDone=True),
    "보리뚜비": Unit("보리뚜비", loopCount=loop, sunganDone=True),
    "보리파": Unit("보리파", 신비전체구매=False, loopCount=loop, sunganDone=True),
    "웨펀꾸꾸": Unit("웨펀꾸꾸", loopCount=loop),

    # "지짱보": Unit("지짱보", 신비전체구매=False, loopCount=loop),
    # "서큐버뚜": Unit("서큐버뚜", 신비전체구매=False, loopCount=loop, finalIndex='3'),
    # "보리닉": Unit("보리닉", 신비전체구매=False, loopCount=loop),
    # "인챈뚜": Unit("인챈뚜", 신비전체구매=False, loopCount=loop),
    # "윈드꾸꾸": Unit("윈드꾸꾸", 신비전체구매=False, finalIndex='f', loopCount=loop, sunganDone=True, epicDone=True),
}

#map = unit.map
# map = { "보리뚜": Unit("보리뚜") }

os.system('rm -rf imagesLog/*')
for key in map:
    select(key)
    char = map[key]
    robot.charName = char.name

    if(len(map) != 1):
        action.캐릭터선택2()

    do(Clicker('모험'))
    do(Clicker('모험_상급던전'))
    # 반지상의하의보장팔찌목걸이()
    무기반지어깨신발()
    # 무기반지어깨신발30()
    do(Clicker('상급던전_입장'))
    do(Founder('상급던전_입장완료'))

    while True:
        do(Presser(str(char.buffIndex)))
        forLoop = 0
        findBoss = False
        # infinite loop
        while True:
            forLoop += 1
            # loop 3 times
            for i in range(4):
                if(findBoss is True):
                    keyboard2.pressKey2(char.finalIndex)
                pyautogui.keyDown('x')
                time.sleep(1.5)
                pyautogui.keyUp('x')
                keyboard2.pressKey2('q')
                keyboard2.pressKey2('w')
                keyboard2.pressKey2('e')
                keyboard2.pressKey2('r')
                keyboard2.pressKey2('s')
                keyboard2.pressKey2('d')
                keyboard2.pressKey2('f')
                keyboard2.pressKey2('g')
                keyboard2.pressKey2('t')
                keyboard2.pressKey2('b')
                keyboard2.pressKey2('v')
            if(findBoss is False and do(Founder('상급던전_보스'), onlyOneTime=True)):
                do(Presser(str(char.finalIndex)))
                findBoss = True

            screenShot = image_finder.getScreenShotToGray()

            if(do(Founder('상급던전_완료'), screenShot=screenShot, onlyOneTime=True)):
                do(Clicker('상급던전_완료'))
                time.sleep(3)
                pyautogui.keyDown('x')
                time.sleep(3)
                pyautogui.keyUp('x')
                pyautogui.keyDown('x')
                time.sleep(3)
                pyautogui.keyUp('x')
                break 

            if(do(Clicker('재도전_수리', screenShot=screenShot, threshold=0.75), onlyOneTime=True)):
                imageFinder.waitAndClick('장비수리확인', maxWait=3, error=False)
                robot.pressKey('ESC', sleep=4)
            
            if(forLoop % 20 == 0):
                Clicker('부활', screenShot=screenShot, threshold=0.75).action()

            if(forLoop > 125):
                dun_print.errorf(char.name + " 상급던전 실패")

        if(do(Clicker('상급던전_재도전'))):
            time.sleep(1)
            if(do(Founder('상급던전_피로도부족'), onlyOneTime=True, canSkip=True)):
                keyboard2.pressKey2('f8')
                break
            do(Founder('상급던전_입장완료'))


mailSender.sendMail("[DNF] 상던완료" , "-")
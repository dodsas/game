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


map = {
    #"보리성": Unit("보리성", s='안톤상의어깨신발팔찌보장', buffIndex=4),
    #"베인뚜": Unit("베인뚜", s='안톤상의어깨신발팔찌보장'),
    "보리빵떡": Unit("보리빵떡", s='안톤상의어깨신발팔찌보장'),
    "지짱보": Unit("지짱보", s='반지상의하의보장팔찌벨트2'),
    "강한보리": Unit("강한보리"),
    "보리뚜": Unit("보리뚜", s='안톤상의어깨신발팔찌보장'),
    "보리세이더": Unit("보리세이더", s='안톤상의어깨신발팔찌보장'),
    "보리뚜뚜": Unit("보리뚜뚜", s='안톤상의어깨신발팔찌보장'),
    "보리템플러": Unit("보리템플러", s='안톤상의어깨신발팔찌보장'),
    "무녀뚜": Unit("무녀뚜", s='안톤상의어깨신발팔찌보장'),

    "런처꾸꾸": Unit("런처꾸꾸", s='무기목걸이어깨신발2'),
    "보리뚜킥": Unit("보리뚜킥", s='무기목걸이어깨신발2'),
    "보리술사": Unit("보리술사", s='반지상의하의보장팔찌벨트2'),
    "보리심판관": Unit("보리심판관", s='반지상의하의보장팔찌벨트2'),
    "보리꾸꾸": Unit("보리꾸꾸", s='무기목걸이어깨신발2'),
    "보리메이지": Unit("보리메이지", s='반지상의하의보장팔찌벨트2'),
    "보리핏": Unit("보리핏", s='반지상의하의보장팔찌벨트2'),
    "건꾸꾸": Unit("건꾸꾸", s='무기목걸이어깨신발2'),

    # "서큐버뚜": Unit("서큐버뚜", s='반지상의하의보장팔찌벨트2'),
    # "보리파": Unit("보리파", s='반지상의하의보장팔찌벨트2'),
    # "보리커": Unit("보리커", s='무기목걸이어깨신발2'),
    # "보리뚜비": Unit("보리뚜비", s='반지상의하의보장팔찌벨트2'),
    # "웨펀꾸꾸": Unit("웨펀꾸꾸", s='무기목걸이어깨신발2'),
    # "윈드꾸꾸": Unit("윈드꾸꾸"),
    # "보리닉": Unit("보리닉"),
    # "보리뱅": Unit("보리뱅"),
    # "인챈뚜": Unit("인챈뚜", s='반지상의하의보장팔찌벨트2'),
    # "소울뚜": Unit("소울뚜", s='반지상의하의보장팔찌벨트2'),
}

maxLoop=10
# maxLoop=2

def zupzup(direction) :
    pyautogui.keyDown('x')
    time.sleep(3)
    pyautogui.keyUp('x')
    pyautogui.keyDown(direction)
    # pyautogui.keyDown('right')
    time.sleep(0.5)
    pyautogui.keyUp(direction)
    # pyautogui.keyUp('right')
    pyautogui.keyDown('x')
    time.sleep(3)
    pyautogui.keyUp('x')

def retry(loopCount):
    if(loopCount >= maxLoop):
        if(do(Clicker('마을로가기', threshold=0.90))):
            time.sleep(2)
            if(do(Founder('마을로가기', threshold=0.90), onlyOneTime=True)):
                zupzup('right')
                zupzup('left')
                zupzup('right')
                do(Clicker('마을로가기', threshold=0.90))
            return True
    do(Clicker('던전재도전하기'), onlyOneTime=True, canSkip=True)
    time.sleep(2) 
    if(do(Founder('피로도가부족합니다'), onlyOneTime=True, canSkip=True)):
        if(do(Clicker('마을로가기', threshold=0.90))):
            return True
    return False
# map = unit.map
# map = { "보리성": Unit("보리성") }
# map = { "보리뚜": Unit("보리뚜") }

os.system('rm -rf imagesLog/*')
for key in map:
    unit.select(key)
    char = map[key]

    if(len(map) != 1):
        action2.캐릭터선택2()

    do(Clicker('모험'))
    do(Clicker('비밀작전'))
    do(Clicker('비밀작전입장'))
    # if(do(Clicker('비밀작전입장2', threshold=0.80), canSkip=True) is False):
    #     if(do(Clicker('비밀작전입장2_2', threshold=0.80), canSkip=True) is False):
    #         do(Clicker('비밀작전입장2_3', threshold=0.80))

    do(Clicker('모험'))
    do(Clicker('비밀작전'))
    do(Clicker('비밀작전입장'))
    
    # do(Direct(1824, 599))
    # do(Clicker('비밀작전입장3'))
    do(Clicker('비밀작전_제국'))
    do(Clicker('비밀작전_동토2'))
    do(Clicker('비밀작전_입장'))

    endLoop = False
    loop = 0
    while True:
        loop = loop+1
        if(endLoop is True):
            break
        do(Founder('입장완료'))
        
        dun_print.printf('요이땅')

        # 사냥
        do(Presser(str(char.buffIndex)))
        if(char.name == '보리성'):
            time.sleep(0.2)
            pyautogui.keyDown('3')
            time.sleep(0.1)
            pyautogui.keyDown('up')
            pyautogui.keyUp('up')
            pyautogui.keyUp('3')

        forLoop = 0
        findBoss = False
        # infinite loop
        while True:
            forLoop += 1
            # loop 3 times
            attackLoop = 2
            if findBoss:
                attackLoop = 2
            for i in range(attackLoop):
                if (findBoss is True):
                    keyboard2.pressKey2(char.finalIndex)
                pyautogui.keyDown('x')
                if (findBoss):
                    time.sleep(1.0)
                else:
                    time.sleep(2)
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

            if (findBoss is False and do(Founder('비밀작전_보스발견_동토', threshold=0.9), onlyOneTime=True)):
                do(Presser(str(char.finalIndex)))
                findBoss = True

            screenShot = image_finder.getScreenShotToGray()

            if(do(Founder('던전재도전하기'), screenShot=screenShot, onlyOneTime=True)):
                zupzup('right')

                if(retry(loop)):
                    endLoop = True 
                    break

                if(do(Founder('던전재도전하기'), onlyOneTime=True, canSkip=True)):
                    zupzup('right')
                    zupzup('left')
                    zupzup('right')

                    if(retry(loop)):
                        endLoop = True 
                        break
                break 
                
            if (forLoop > 120):
                dun_print.errorf(char.name + " 상급던전 실패")
                break

    # 마무리
    # do(Clicker('뒤로가기'))
    # do(Clicker('나가기'))
    # do(Clicker('확인'), okSkip=True)

mailSender.sendMail("[DNF] 비밀작전 완료" , "-")


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
sys.path.append('tobe')
from image_robot import * 

image_finder.imgPath = 'Image/강림로터스/'

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
    "보리뚜킥": Unit("보리뚜킥", s='무기목걸이어깨신발2'),
    "보리술사": Unit("보리술사", s='반지상의하의보장팔찌벨트2'),
    "보리심판관": Unit("보리심판관", s='반지상의하의보장팔찌벨트2'),
    "보리꾸꾸": Unit("보리꾸꾸", s='무기목걸이어깨신발2'),
    "보리메이지": Unit("보리메이지", s='반지상의하의보장팔찌벨트2'),
    "서큐버뚜": Unit("서큐버뚜", s='반지상의하의보장팔찌벨트2'),
    "보리핏": Unit("보리핏", s='반지상의하의보장팔찌벨트2'),
    "보리파": Unit("보리파", s='반지상의하의보장팔찌벨트2'),
    "건꾸꾸": Unit("건꾸꾸", s='무기목걸이어깨신발2'),
    "보리커": Unit("보리커", s='무기목걸이어깨신발2'),
    "보리뚜비": Unit("보리뚜비", s='반지상의하의보장팔찌벨트2'),
    "웨펀꾸꾸": Unit("웨펀꾸꾸", s='무기목걸이어깨신발2'),
    "윈드꾸꾸": Unit("윈드꾸꾸"),
    "보리닉": Unit("보리닉"),
    "인챈뚜": Unit("인챈뚜", s='반지상의하의보장팔찌벨트2'),
    "소울뚜": Unit("소울뚜", s='반지상의하의보장팔찌벨트2'),
}

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
    do(Clicker('레이드'))
    do(Clicker('강림로터스'))
    do(Clicker('입문'), canSkip=True)
    do(Clicker('입장'))
    time.sleep(4)
    if(do(Founder('재료부족'), okSkip=True, onlyOneTime=True)):
        do(Clicker('제작'))
        do(Clicker('제작_하이퍼재머'))
        do(Clicker('+'))
        do(Clicker('찐제작', threshold=0.87))
        do(Clicker('확인'), okSkip=True)
        do(Clicker('확인'), okSkip=True, onlyOneTime=True)
        time.sleep(2)
        do(Clicker('확인'), okSkip=True, canSkip=True, fallbackSkip=True)
        do(Clicker('뒤로가기'))
        do(Clicker('입장'), fallbackSkip=True)
        
    do(Clicker('확인'), okSkip=True)
    do(Clicker('확인'), onlyOneTime=True)
    
    do(Clicker('공격대생성'))
    do(Clicker('공격대생성2'))
    do(Clicker('레이드시작'))
    do(Clicker('페이즈시작'))
    time.sleep(4)
    do(Clicker('확인'), okSkip=True, onlyOneTime=True)
    time.sleep(1)
    do(Presser('ESC'))

    do(Founder('입장완료'))

    time.sleep(5)
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
            attackLoop = 3
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

        if (findBoss is False and do(Founder('보스발견', threshold=0.9), onlyOneTime=True)):
            do(Presser(str(char.finalIndex)))
            findBoss = True

        screenShot = image_finder.getScreenShotToGray()

        if(do(Clicker('사냥완료'), onlyOneTime=True, screenShot=screenShot)):
            dun_print.printf("사냥완료카운트", str(forLoop))
            break

        if (forLoop > 120):
            dun_print.errorf(char.name + " 상급던전 실패")

    # 마무리
    do(Clicker('뒤로가기'))
    do(Clicker('나가기'))
    do(Clicker('확인'), okSkip=True)

mailSender.sendMail("[DNF] 강림로터스 완료" , "-")
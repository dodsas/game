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
    #"베인뚜": Unit("베인뚜"),
    #"보리성": Unit("보리성", buffIndex=4),
    #"보리빵떡": Unit("보리빵떡"),
    #"지짱보": Unit("지짱보"),
    #"강한보리": Unit("강한보리"),
    "보리뚜": Unit("보리뚜"),
    "보리세이더": Unit("보리세이더"),
    "보리템플러": Unit("보리템플러"),
    "보리뚜뚜": Unit("보리뚜뚜"),
    "무녀뚜": Unit("무녀뚜"),
    "인챈뚜": Unit("인챈뚜"),
    "소울뚜": Unit("소울뚜"),
    "런처꾸꾸": Unit("런처꾸꾸"),
    "보리꾸꾸": Unit("보리꾸꾸"),
    "웨펀꾸꾸": Unit("웨펀꾸꾸"),
    "보리치료사": Unit("보리치료사", attackMode=True, plan='b'),
    "맥보리": Unit("맥보리", attackMode=True, plan='b'),
    "건꾸꾸": Unit("건꾸꾸", attackMode=True, plan='b'),
    "보리핏": Unit("보리핏", attackMode=True, plan='b'),
    "보리뚜킥": Unit("보리뚜킥", attackMode=True, plan='b'),
    "보리술사": Unit("보리술사", attackMode=True, plan='b'),
    "보리파": Unit("보리파", attackMode=True, plan='b'),
    "보리심판관": Unit("보리심판관", attackMode=True, plan='b'),
    "보리뚜비": Unit("보리뚜비", attackMode=True, plan='b'),
    "보리메이지": Unit("보리메이지", attackMode=True, plan='b'),
    "서큐버뚜": Unit("서큐버뚜", attackMode=True, plan='b'),
    "보리커": Unit("보리커", attackMode=True, plan='b'),
    "윈드꾸꾸": Unit("윈드꾸꾸", attackMode=True, plan='b'),
    "보리뱅": Unit("보리뱅", attackMode=True, plan='b'),
    "보리닉": Unit("보리닉", attackMode=True, plan='b'),
    "보리왕": Unit("보리왕", plan='b'),
    "보리샷": Unit("보리샷", attackMode=True, plan='b'),
}

maxLoop=10

def after():
    # action.우편함()

    time.sleep(2)
    do(Clicker('인벤토리', threshold=0.70))
    do(Clicker('장비수리'))
    do(Clicker('장비수리확인'), onlyOneTime=True)
    time.sleep(1)
    do(Clicker('x', threshold=0.83))

    # 판매
    do(Clicker('판매'))
    do(Clicker('판매노말해제'), onlyOneTime=True)
    do(Clicker('판매에픽해제'), onlyOneTime=True)
    # do(Clicker('판매유니크해제'), onlyOneTime=True)
    do(Clicker('판매2'))
    if(do(Founder('알림', threshold=0.76), onlyOneTime=True, okSkip=True)):
        do(Clicker('알림취소', threshold=0.86))
    do(Clicker('확인', 0.81), onlyOneTime=True, okSkip=True)
    time.sleep(1)
    do(Clicker('x', threshold=0.83), fallbackSkip=True)

    do(Clicker('판매'))
    do(Clicker('판매2'))
    if(do(Founder('알림', threshold=0.76), onlyOneTime=True, okSkip=True)):
        do(Clicker('알림취소', threshold=0.86))
    do(Clicker('확인', 0.81), onlyOneTime=True, okSkip=True)
    time.sleep(1)
    do(Clicker('x', threshold=0.83), fallbackSkip=True)

    do(Clicker('해체', threshold=0.85))
    do(Clicker('판매노말선택'), onlyOneTime=True)
    # do(Clicker('판매에픽선택'), onlyOneTime=True)
    # do(Clicker('판매에픽해제'), onlyOneTime=True)
    do(Clicker('해체2', 0.83))
    # do(Clicker('확인', 0.81), onlyOneTime=True)
    do(Clicker('확인', 0.81), onlyOneTime=True, okSkip=True)
    do(Clicker('x', threshold=0.83))

    # 금고보관
    do(Clicker('금고', 0.81))
    do(Clicker('모험단금고'))
    do(Clicker('자동보관'))
    do(Clicker('확인', 0.81), onlyOneTime=True)

    do(Clicker('뒤로가기'))

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
                # zupzup('right')
                # do(Clicker('마을로가기', threshold=0.90))
            return True
    #do(Clicker('던전재도전하기', threshold=0.85), onlyOneTime=True, canSkip=True)
    time.sleep(2) 
    if(do(Founder('피로도가부족합니다'), onlyOneTime=True, canSkip=True)):
        # if(do(Clicker('마을로가기', threshold=0.90))):
        return True
    return False

def b():
    """비하이브 던전 입장 시퀀스"""
    do(Clicker('모험'))
    do(Clicker('비밀작전'))
    do(Clicker('비밀작전입장', threshold=0.85))
    time.sleep(2)
    do(Clicker('모험'))
    time.sleep(1)
    do(Clicker('비밀작전', fallbackDelay=0.5))
    do(Direct(1465, 684)) # 비하이브
    do(Clicker('비하이브2'))
    do(Clicker('비하이브2_입장'))

def n():
    """일반던전 입장 시퀀스"""
    do(Clicker('모험'))
    do(Clicker('모험보상'))
    image_clicker.clickDirect(1494, 608)
    pyautogui.scroll(-400000)
    time.sleep(1)
    # do(Clicker('모험보상지젤연구소'))
    do(Clicker('흑룡해적그림'))
    do(Clicker('지역이동'))

    time.sleep(20)
    # time.sleep(60)

    # do(Clicker('패기물처리장그림'))
    # do(Clicker('글라시알'), canSkip=True)
    do(Clicker('글라시알'))
    # 난이도조절 
    do(Clicker('expert'), canSkip=True)
    do(Clicker('일던입장', threshold=0.85))

def handle_dungeon_clear_with_retry(loop, max_retry_attempts=8):
    """던전 클리어 후 재도전 로직을 최대 5번 시도"""
    do(Clicker('비작확인'), canSkip=True)
    
    for attempt in range(max_retry_attempts):
        dun_print.printf(f'재도전 시도 {attempt + 1}/{max_retry_attempts}')
        zupzup('right')
        zupzup('left')
        zupzup('right')
        
        do(Clicker('던전재도전하기', threshold=0.85), onlyOneTime=True, canSkip=True)
        time.sleep(2) 
        if(do(Founder('피로도가부족합니다'), onlyOneTime=True, canSkip=True)):
            do(Clicker('마을로가기', threshold=0.90))
            time.sleep(4) 
            if(do(Founder('마을로가기', threshold=0.90), onlyOneTime=True) == False ):
                return True

        if(do(Clicker('던전재도전하기', threshold=0.85), onlyOneTime=True, canSkip=True) == False):
            return False 

    # 모든 시도 실패 시 마을로 가기
    dun_print.printf('모든 재도전 시도 실패, 마을로 이동')
    do(Clicker('마을로가기', threshold=0.85))

os.system('rm -rf imagesLog/*')
for key in map:
    unit.select(key)
    char = map[key]

    if(len(map) != 1):
        action2.캐릭터선택2()
    if(do(Founder('피로도소모'), onlyOneTime=True, canSkip=True)):
        continue

    # char.plan에 따른 던전 입장 계획 실행
    plan_function = globals().get(char.plan)
    if plan_function and callable(plan_function):
        plan_function()
    else:
        dun_print.errorf(f"Unknown plan: {char.plan}")

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
                    keyboard2.pressKey2('5')
                    keyboard2.pressKey2(char.finalIndex)
                
                pyautogui.keyDown('x')
                if (findBoss):
                    time.sleep(1.0)
                else:
                    time.sleep(2)
                # attackMode에 따른 공격 방식 분기
                if char.attackMode is False: 
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
                
                if (forLoop > 30):
                    pyautogui.keyUp('x')

            # if (findBoss is False and do(Founder('비하이브2_보스', threshold=0.9), onlyOneTime=True)):
            if (findBoss is False and do(Founder('보스발견', threshold=0.9), onlyOneTime=True)):
                do(Presser(str(char.finalIndex)))
                do(Presser(str(char.finalIndex)))
                findBoss = True

            screenShot = image_finder.getScreenShotToGray()

            if(do(Founder('비작리워드'), screenShot=screenShot, onlyOneTime=True)):
                do(Clicker('비작리워드클릭'), canSkip=True)

            if(do(Founder('던전재도전하기'), screenShot=screenShot, onlyOneTime=True) or 
               do(Founder('비작클리어'), screenShot=screenShot, onlyOneTime=True) 
            ):
                if handle_dungeon_clear_with_retry(loop):
                    endLoop = True
                    break
                break 
            if (forLoop % 5 == 0):
                if(do(Clicker('부활', screenShot=screenShot, threshold=0.75), onlyOneTime=True)):
                    mailSender.sendMail("[DNF] die " + char.name, "-")
            if (forLoop > 120):
                dun_print.errorf(char.name + "던전 실패")
                break
    
    after()
    # 마무리
    # do(Clicker('뒤로가기'))
    # do(Clicker('나가기'))
    # do(Clicker('확인'), okSkip=True)

mailSender.sendMail("[DNF] 비밀작전 완료" , "-")


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
    "보리치료사": Unit("보리치료사"),
    "맥보리": Unit("맥보리"),
    "건꾸꾸": Unit("건꾸꾸", s='안톤상의어깨신발팔보장'),
    "보리핏": Unit("보리핏", s='안톤상의어깨신발팔찌보장'),
    "보리뚜킥": Unit("보리뚜킥", s='안톤상의어깨신발팔찌보장'),
    "보리술사": Unit("보리술사", s='안톤상의어깨신발팔찌보장'),
    "보리파": Unit("보리파", s='안톤상의어깨신발팔찌보장'),
    "보리심판관": Unit("보리심판관", s='안톤상의어깨신발팔찌보장'),
    "보리뚜비": Unit("보리뚜비", s='안톤상의어깨신발팔찌보장'),
    "보리메이지": Unit("보리메이지", s='안톤상의어깨신발팔찌보장'),
    "서큐버뚜": Unit("서큐버뚜", s='안톤상의어깨신발팔찌보장'),
    "보리커": Unit("보리커", s='안톤상의어깨신발팔찌보장'),
    "윈드꾸꾸": Unit("윈드꾸꾸"),
    "보리뱅": Unit("보리뱅"),
    "보리닉": Unit("보리닉"),
    # "보리왕": Unit("보리왕"),
    # "보리샷": Unit("보리샷"),
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
    do(Clicker('판매에픽해제'), onlyOneTime=True)
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
                zupzup('right')
                # do(Clicker('마을로가기', threshold=0.90))
            return True
    do(Clicker('던전재도전하기', threshold=0.85), onlyOneTime=True, canSkip=True)
    time.sleep(2) 
    if(do(Founder('피로도가부족합니다'), onlyOneTime=True, canSkip=True)):
        # if(do(Clicker('마을로가기', threshold=0.90))):
        return True
    return False

os.system('rm -rf imagesLog/*')
for key in map:
    unit.select(key)
    char = map[key]

    if(len(map) != 1):
        action2.캐릭터선택2()
    if(do(Founder('피로도소모'), onlyOneTime=True, canSkip=True)):
        continue

    do(Clicker('모험'))
    do(Clicker('비밀작전'))
    do(Clicker('비밀작전입장', threshold=0.85))

    do(Clicker('모험'))
    do(Clicker('비밀작전'))

    do(Direct(1465, 684)) # 비하이브
    do(Clicker('비하이브2'))
    do(Clicker('비하이브2_입장'))

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
                if (forLoop > 120):
                    pyautogui.keyUp('x')


            if (findBoss is False and do(Founder('비하이브2_보스', threshold=0.9), onlyOneTime=True)):
                do(Presser(str(char.finalIndex)))
                do(Presser(str(char.finalIndex)))
                findBoss = True

            screenShot = image_finder.getScreenShotToGray()

            if(do(Founder('비작리워드'), screenShot=screenShot, onlyOneTime=True)):
                do(Clicker('비작리워드클릭'), canSkip=True)

            if(do(Founder('던전재도전하기'), screenShot=screenShot, onlyOneTime=True) or 
               do(Founder('비작클리어'), screenShot=screenShot, onlyOneTime=True) 
            ):
                do(Clicker('비작확인'), canSkip=True) #check
                zupzup('right')

                if(retry(loop)):
                    dun_print.printf('go to home 1')
                    do(Clicker('마을로가기', threshold=0.85), canSkip=True) #check
                    endLoop = True 
                    break

                if(do(Founder('던전재도전하기', threshold=0.85), onlyOneTime=True, canSkip=True)):
                    zupzup('right')
                    zupzup('left')
                    zupzup('right')

                    print('zupzup end')
                    if(retry(loop) or do(Clicker('던전재도전하기', threshold=0.85), onlyOneTime=True, canSkip=True)):
                        dun_print.printf('go to home 2')
                        do(Clicker('마을로가기', threshold=0.85))
                        endLoop = True 
                        break
                break 
            if (forLoop % 20 == 0):
                Clicker('부활', screenShot=screenShot, threshold=0.75).action()
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


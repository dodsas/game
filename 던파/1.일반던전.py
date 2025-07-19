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

maxLoop=20
# maxLoop=2

map = {
    "베인뚜": Unit("베인뚜", s='master'),
    "보리성": Unit("보리성", buffIndex=4, s='master'),
    "보리빵떡": Unit("보리빵떡", s='master'),
    "지짱보": Unit("지짱보", s='master'),
    "강한보리": Unit("강한보리", s='master'),
    "보리뚜": Unit("보리뚜", s='master'),
    "보리세이더": Unit("보리세이더", s='master'),
    "보리뚜뚜": Unit("보리뚜뚜"),
    "보리템플러": Unit("보리템플러", s='master'),
    "인챈뚜": Unit("인챈뚜"),
    "무녀뚜": Unit("무녀뚜"),
    "소울뚜": Unit("소울뚜"),
    "런처꾸꾸": Unit("런처꾸꾸", s='master'),
    "보리꾸꾸": Unit("보리꾸꾸", s='master'),
    "웨펀꾸꾸": Unit("웨펀꾸꾸", s='master'),

}

# map = unit.map
# map = { "보리뚜": Unit("보리뚜") }

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
    if(do(Founder('피로도소모'))):
        continue

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
    do(Clicker('글라시알'), canSkip=True)
    # 난이도조절 
    do(Clicker('expert'), canSkip=True)
    if(char.s == 'master'):
        do(Clicker('폐기물마스터'), canSkip=True)

    do(Clicker('일던입장', threshold=0.85))

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


            # if (findBoss is False and do(Founder('빛나는밀림보스', threshold=0.9), onlyOneTime=True)):
            # if (findBoss is False and do(Founder('폐기물처리장보스', threshold=0.9), onlyOneTime=True)):
            if (findBoss is False and do(Founder('글라시엘보스', threshold=0.9), onlyOneTime=True)):
                do(Presser(str(char.finalIndex)))
                findBoss = True

            screenShot = image_finder.getScreenShotToGray()

            if(do(Founder('던전재도전하기', threshold=0.85), screenShot=screenShot, onlyOneTime=True)):
                zupzup('right')

                if(retry(loop)):
                    do(Clicker('마을로가기', threshold=0.85)) #check
                    endLoop = True 
                    break

                if(do(Founder('던전재도전하기', threshold=0.85), onlyOneTime=True, canSkip=True)):
                    zupzup('right')
                    zupzup('left')
                    zupzup('right')

                    print('zupzup end')
                    if(retry(loop) or do(Clicker('던전재도전하기', threshold=0.85), onlyOneTime=True, canSkip=True)):
                        do(Clicker('마을로가기', threshold=0.85))
                        endLoop = True 
                        break
                break 
            if (forLoop % 20 == 0):
                Clicker('부활', screenShot=screenShot, threshold=0.75).action()
                mailSender.sendMail("[DNF] die " + char.name, "-")
    
            if (forLoop > 120):
                dun_print.errorf(char.name + " 상급던전 실패")
                break

    # 마무리
    # do(Clicker('뒤로가기'))
    # do(Clicker('나가기'))
    # do(Clicker('확인'), okSkip=True)
do(Clicker('menu'))
do(Clicker('캐릭터선택'))
mailSender.sendMail("[DNF] 비밀작전 완료" , "-")


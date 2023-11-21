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

map = {
    # "보리성": Unit("보리성"),
    # "보리뚜": Unit("보리뚜"),
    # "보리세이더": Unit("보리세이더"),
    # "베인뚜": Unit("베인뚜"),
    # "보리빵떡": Unit("보리빵떡"),
  # "보리메이지": Unit("보리메이지"),
#     "보리템플러": Unit("보리템플러"),
#    "보리뚜뚜": Unit("보리뚜뚜"),
#    "무녀뚜": Unit("무녀뚜"),
#    "런처꾸꾸": Unit("런처꾸꾸", s10='반지상의하의보장팔찌목걸이', s30='반지상의하의보장팔찌목걸이30'),
#   "보리술사": Unit("보리술사"),
#   "보리꾸꾸": Unit("보리꾸꾸"),
#   "보리뚜킥": Unit("보리뚜킥"),
#    "건꾸꾸": Unit("건꾸꾸", s10='반지상의하의보장팔찌목걸이', s30='반지상의하의보장팔찌목걸이30'),
#    "보리핏": Unit("보리핏"),
#    "보리심판관": Unit("보리심판관"),
#    "보리커": Unit("보리커", s10='반지상의하의보장팔찌목걸이', s30='반지상의하의보장팔찌목걸이30'),
#    "소울뚜": Unit("소울뚜", s10='반지상의하의보장팔찌목걸이', s30='반지상의하의보장팔찌목걸이30'),
#    "보리뚜비": Unit("보리뚜비"),
#    "보리파": Unit("보리파"),
#    "웨펀꾸꾸": Unit("웨펀꾸꾸"),
#     "지짱보": Unit("지짱보"),
#     "서큐버뚜": Unit("서큐버뚜"),
    # "보리닉": Unit("보리닉"),
    # "인챈뚜": Unit("인챈뚜"),
    # "윈드꾸꾸": Unit("윈드꾸꾸"),
}

map = unit.map
map = { "보리뚜": Unit("보리뚜") }

os.system('rm -rf imagesLog/*')
for key in map:
    select(key)
    char = map[key]
    charName = char.name

    if(len(map) != 1):
        action.캐릭터선택2()

    do(Clicker('모험', threshold=0.8))
    do(Clicker('모험_의뢰'))
    time.sleep(1)
    do(Clicker('의뢰던전'))
    do(Clicker('지옥선택'))
    do(Clicker('입장가능지역으로이동'), canSkip=True)
    do(Clicker('입장', threshold=0.75))
    do(Founder('상급던전_입장완료'))

    while True:
        do(Presser(str(char.buffIndex)))
        forLoop = 0
        findBoss = False
        done=False
        # infinite loop
        while True:
            forLoop += 1
            # loop 3 times
            for i in range(1):
                if(findBoss is True):
                    keyboard2.pressKey2(char.finalIndex)
                pyautogui.keyDown('x')
                time.sleep(3)
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
            if(findBoss is False and do(Founder('지옥파티_보스발견'), onlyOneTime=True)):
                pyautogui.keyDown('x')
                time.sleep(3)
                pyautogui.keyUp('x')
                do(Presser(str(char.finalIndex)))
                findBoss = True

            screenShot = image_finder.getScreenShotToGray()

            timeInterval = 0.5
            if(do(Founder('지옥재도전하기'), screenShot=screenShot, onlyOneTime=True)):
                pyautogui.keyDown('x')
                time.sleep(2.5 + timeInterval)
                pyautogui.keyUp('x')
                # pyautogui.keyDown('right')
                # time.sleep(0.2)
                # pyautogui.keyUp('right')
                # pyautogui.keyDown('x')
                # time.sleep(2 + timeInterval)
                # pyautogui.keyUp('x')
                # pyautogui.keyDown('left')
                # time.sleep(0.2)
                # pyautogui.keyUp('left')
                # pyautogui.keyDown('x')
                # time.sleep(2 + timeInterval)
                # pyautogui.keyUp('x')
                break 

            if(do(Clicker('지옥파티피로도끝'), screenShot=screenShot, onlyOneTime=True)):
                pyautogui.keyDown('x')
                time.sleep(2.5 + timeInterval)
                pyautogui.keyUp('x')

                pyautogui.keyDown('right')
                time.sleep(0.2)
                pyautogui.keyUp('right')

                pyautogui.keyDown('x')
                time.sleep(2 + timeInterval)
                pyautogui.keyUp('x')

                pyautogui.keyDown('left')
                time.sleep(0.2)
                pyautogui.keyUp('left')

                pyautogui.keyDown('x')
                time.sleep(2 + timeInterval)
                pyautogui.keyUp('x')

                pyautogui.keyDown('x')
                time.sleep(2.5 + timeInterval)
                pyautogui.keyUp('x')
                done=True
                break

            if(do(Clicker('재도전_수리', screenShot=screenShot, threshold=0.75), onlyOneTime=True)):
                imageFinder.waitAndClick('장비수리확인', maxWait=3, error=False)
                robot.pressKey('ESC', sleep=4)
            
            if(forLoop % 20 == 0):
                Clicker('부활', screenShot=screenShot, threshold=0.75).action()

            if(forLoop > 125):
                dun_print.errorf(char.name + " 상급던전 실패")
        
        if(done):
            break
  
        # do(Clicker('지옥재도전하기'))
        # do(Founder('상급던전_입장완료'))

        do(Clicker('지옥재도전하기'), canSkip=True)
        time.sleep(3)
        if(do(Founder('상급던전_입장완료'), canSkip=True) is False):
            print("not found!!!!!!!!!! retry")
            pyautogui.keyDown('x')
            time.sleep(4)
            pyautogui.keyUp('x')
            robot.pressKey('x', sleep=0)

            pyautogui.keyDown('right')
            time.sleep(0.2)
            pyautogui.keyUp('right')
            robot.pressKey('x', sleep=0)

            pyautogui.keyDown('x')
            time.sleep(4)
            pyautogui.keyUp('x')
            robot.pressKey('x', sleep=0)

            pyautogui.keyDown('left')
            time.sleep(0.2)
            pyautogui.keyUp('left')
            robot.pressKey('x', sleep=0)

            pyautogui.keyDown('x')
            time.sleep(4)
            pyautogui.keyUp('x')
            do(Clicker('지옥재도전하기'))
            do(Founder('상급던전_입장완료'))

    do(Clicker('뒤로가기'))
mailSender.sendMail("[DNF] 지옥완료" , "-")
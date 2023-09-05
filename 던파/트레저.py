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

image_finder.imgPath = 'Image/트레저/'

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
    "인챈뚜": Unit("인챈뚜"),

    # "윈드꾸꾸": Unit("윈드꾸꾸"),
}

map = unit.map
map = { "보리뚜": Unit("보리뚜") }

def selectMap(i):
    if(i != 1):
        screenShot = image_finder.getScreenShotToGray()

        do(Clicker('맵_레어_스카디'), screenShot=screenShot, onlyOneTime=True)
        do(Clicker('맵_유니크_스카디'), screenShot=screenShot, onlyOneTime=True)
        do(Clicker('맵_에픽_스카디'), screenShot=screenShot, onlyOneTime=True)

        do(Clicker('맵_레어_초대장'), screenShot=screenShot, onlyOneTime=True)
        do(Clicker('맵_유니크_초대장'), screenShot=screenShot, onlyOneTime=True)
        do(Clicker('맵_에픽_초대장'), screenShot=screenShot, onlyOneTime=True)

        do(Clicker('맵_레어_골드'), screenShot=screenShot, onlyOneTime=True)
        do(Clicker('맵_유니크_변환석'), screenShot=screenShot, onlyOneTime=True)
        do(Clicker('맵_유니크_골드'), screenShot=screenShot, onlyOneTime=True)
        do(Clicker('맵_에픽_골드'), screenShot=screenShot, onlyOneTime=True)
        do(Clicker('맵_에픽_변환석'), screenShot=screenShot, onlyOneTime=True)

        do(Clicker('맵_레어_라코'), screenShot=screenShot, onlyOneTime=True)
        do(Clicker('맵_유니크_라코'), screenShot=screenShot, onlyOneTime=True)
        do(Clicker('맵_에픽_라코'), screenShot=screenShot, onlyOneTime=True)

        do(Clicker('맵_확인'))
        pyautogui.keyDown('x')
        time.sleep(3)
        pyautogui.keyUp('x')
        pyautogui.keyDown('right')
        time.sleep(0.2)
        pyautogui.keyUp('right')
        pyautogui.keyDown('x')
        time.sleep(3)
        pyautogui.keyUp('x')
        do(Clicker('다음던전진행'))
    do(Founder('다음던전입장확인'))

os.system('rm -rf imagesLog/*')
for key in map:
    select(key)
    char = map[key]
    robot.charName = char.name
    time.sleep(1)
    if(len(map) != 1):
        action.캐릭터선택2()

    # do(Clicker('모험'))
    # do(Clicker('의뢰'))
    # do(Clicker('트레저'))
    # do(Clicker('입장'))

    i=1
    while True:
        i=i+1
        selectMap(i)

        do(Presser(str(char.buffIndex)))
        forLoop = 0
        findBoss = False
        # infinite loop
        while True:
            forLoop += 1
            # loop 3 
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
            if(do(Founder('리워드'), screenShot=screenShot, onlyOneTime=True)):
                # do(Clicker('골드카드'), canSkip=True)
                keyboard2.pressKey2('5')
                time.sleep(4)
                break 

        if(do(Founder('SELECT'), canSkip=True) is False):
            pyautogui.keyDown('x')
            time.sleep(3)
            pyautogui.keyUp('x')
            pyautogui.keyDown('right')
            time.sleep(0.2)
            pyautogui.keyUp('right')
            pyautogui.keyDown('x')
            time.sleep(3)
            pyautogui.keyUp('x')
            do(Clicker('마을로가기'))
            break

        #     if(do(Clicker('재도전_수리', screenShot=screenShot, threshold=0.75), onlyOneTime=True)):
        #         imageFinder.waitAndClick('장비수리확인', maxWait=3, error=False)
        #         robot.pressKey('ESC', sleep=4)
            
        #     if(forLoop % 20 == 0):
        #         Clicker('부활', screenShot=screenShot, threshold=0.75).action()

        #     if(forLoop > 125):
        #         dun_print.errorf(char.name + " 상급던전 실패")

        # if(do(Clicker('상급던전_재도전'))):
        #     time.sleep(1)
        #     if(do(Founder('상급던전_피로도부족'), onlyOneTime=True, canSkip=True)):
        #         keyboard2.pressKey2('f8')
        #         break
        #     if(do(Founder('상급던전_입장재료부족'), onlyOneTime=True, canSkip=True)):
        #         keyboard2.pressKey2('f8')
        #         break

        #     do(Founder('상급던전_입장완료'))

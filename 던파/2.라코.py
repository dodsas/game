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

image_finder.imgPath = 'Image/라코/'

maxLoop=13
map = {
    # "보리빵떡": Unit("보리빵떡", s='안톤상의어깨신발팔찌보장'),
    # "보리성": Unit("보리성", s='안톤무기바지벨트목걸이반지', buffIndex=4),
    # "베인뚜": Unit("베인뚜", s='안톤무기바지벨트목걸이반지'),
    # "보리뚜": Unit("보리뚜", s='안톤상의어깨신발팔찌보장'),
    # "보리세이더": Unit("보리세이더", s='안톤무기바지벨트목걸이반지'),
    # "보리뚜뚜": Unit("보리뚜뚜", s='안톤상의어깨신발팔찌보장'),
    # "보리템플러": Unit("보리템플러", s='안톤상의어깨신발팔찌보장'),
    # "무녀뚜": Unit("무녀뚜", s='안톤무기바지벨트목걸이반지'),

    #"인챈뚜": Unit("인챈뚜", s='반지상의하의보장팔찌벨트2'),
   # "소울뚜": Unit("소울뚜", s='반지상의하의보장팔찌벨트2'),
    
   # "지짱보": Unit("지짱보", s='반지상의하의보장팔찌벨트2'),
   # "보리술사": Unit("보리술사", s='반지상의하의보장팔찌벨트2'),
   # "런처꾸꾸": Unit("런처꾸꾸", s='무기목걸이어깨신발2'),
 #   "보리뚜킥": Unit("보리뚜킥", s='무기목걸이어깨신발2'),
 #   "건꾸꾸": Unit("건꾸꾸", s='무기목걸이어깨신발2'),
  #  "보리꾸꾸": Unit("보리꾸꾸", s='무기목걸이어깨신발2'),
  #  "보리핏": Unit("보리핏", s='반지상의하의보장팔찌벨트2'),
   # "보리심판관": Unit("보리심판관", s='반지상의하의보장팔찌벨트2'),
   # "보리커": Unit("보리커", s='무기목걸이어깨신발2'),
    "보리파": Unit("보리파", s='반지상의하의보장팔찌벨트2'),
    "보리뚜비": Unit("보리뚜비", s='반지상의하의보장팔찌벨트2'),
    "웨펀꾸꾸": Unit("웨펀꾸꾸", s='무기목걸이어깨신발2'),
    "보리메이지": Unit("보리메이지", s='반지상의하의보장팔찌벨트2'),
    "서큐버뚜": Unit("서큐버뚜", s='반지상의하의보장팔찌벨트2'),
    "보리닉": Unit("보리닉"),
    "윈드꾸꾸": Unit("윈드꾸꾸"),
}

# map = unit.map
#map = { "보리뚜": Unit("보리뚜") }

os.system('rm -rf imagesLog/*')
for key in map:
    unit.select(key)
    char = map[key]

    if(len(map) != 1):
        action2.캐릭터선택2()

    do(Clicker('모험'))
    do(Clicker('모험보상'))
    image_clicker.clickDirect(1494, 608)
    pyautogui.scroll(-300000)
    time.sleep(1)
    do(Clicker('무법지대'))
    do(Clicker('지역이동'))
    time.sleep(12)
    do(Clicker('협곡돌파'))
    image_clicker.clickDirect(1405, 635)
    do(Clicker('전투시작'))


    loop = 0
    while True:
        do(Founder('입장완료'))
        loop += 1
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
                attackLoop = 4
            for i in range(attackLoop):
                pyautogui.keyUp('x')
                pyautogui.keyDown('x')
                if (findBoss):
                    time.sleep(1.5)
                else:
                    time.sleep(2.0)

            if (findBoss is False and do(Founder('보스발견', threshold=0.9), onlyOneTime=True)):
                do(Presser('q'), fallbackSkip=True)
                findBoss = True

            screenShot = image_finder.getScreenShotToGray()

            if(do(Clicker('골카', threshold=0.82), onlyOneTime=True, screenShot=screenShot)):
                keyboard2.pressKey2('5')
                do(Clicker('reward'), onlyOneTime=True) 
                pyautogui.keyDown('left')
                time.sleep(0.2)
                pyautogui.keyUp('left')
                pyautogui.keyDown('x')
                time.sleep(3)
                pyautogui.keyUp('x')
                pyautogui.keyDown('right')
                time.sleep(0.2)
                pyautogui.keyUp('right')
                pyautogui.keyDown('x')
                time.sleep(3)
                pyautogui.keyUp('x')
                break

            # if (do(Clicker('재도전_수리', screenShot=screenShot, threshold=0.75), onlyOneTime=True)):
            #     imageFinder.waitAndClick('장비수리확인', maxWait=3, error=False)
            #     robot.pressKey('ESC', sleep=4)

            if (forLoop % 20 == 0):
                pyautogui.keyDown('up')
                time.sleep(0.2)
                pyautogui.keyUp('up')
                pyautogui.keyDown('left')
                time.sleep(0.2)
                pyautogui.keyUp('left')
            #     Clicker('부활', screenShot=screenShot, threshold=0.75).action()

            if (forLoop > 30):
                dun_print.errorf(char.name + " 상급던전 실패")

        pyautogui.keyUp('x')
        if (do(Founder('재도전', threshold=0.85))):
            dun_print.printf("사냥완료카운트", str(forLoop))
            if (loop >= maxLoop):
                keyboard2.pressKey2('f8')
                break
            do(Clicker('재도전', threshold=0.85))
            time.sleep(1)
            screenShot = image_finder.getScreenShotToGray()
            if (do(Founder('상급던전_피로도부족', threshold=0.85), screenShot=screenShot, onlyOneTime=True)):
                keyboard2.pressKey2('f8')
                break

mailSender.sendMail("[DNF] 라코 완료" , "-")
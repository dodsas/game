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

def 반지상의하의보장팔찌벨트():
    do(Clicker('파워스테이션'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('파워스테이션_코레')) # 반지 상의 하의 보장 팔찌 벨트 

def 반지상의하의보장팔찌벨트30():
    do(Clicker('파워스테이션'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('파워스테이션_코레30')) # 반지 상의 하의 보장 팔찌 벨트 

def 무기목걸이어깨신발():
    do(Clicker('파워스테이션'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('파워스테이션_푸르츠')) # 무기 목걸이 어깨 신발 

def 무기목걸이어깨신발30():
    do(Clicker('파워스테이션'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('파워스테이션_푸르츠30', threshold=0.7)) # 무기 목걸이 어깨 신발 

def 무기():
    do(Clicker('원데과학단지'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('원데과학단지_옵티머스')) # 무기

map = {
    # "보리성": Unit("보리성"),
    # "보리뚜": Unit("보리뚜"),
    # "보리세이더": Unit("보리세이더"),
    # "베인뚜": Unit("베인뚜"),
    # "보리빵떡": Unit("보리빵떡"),

   "보리메이지": Unit("보리메이지", s10='반지상의하의보장팔찌벨트', s30='반지상의하의보장팔찌벨트30'),
   "보리템플러": Unit("보리템플러", s10='반지상의하의보장팔찌벨트', s30='반지상의하의보장팔찌벨트30'),
  "보리뚜뚜": Unit("보리뚜뚜", s10='반지상의하의보장팔찌벨트', s30='반지상의하의보장팔찌벨트30'),
  "무녀뚜": Unit("무녀뚜",s10='반지상의하의보장팔찌벨트', s30='반지상의하의보장팔찌벨트30'),
  "런처꾸꾸": Unit("런처꾸꾸"),
   "보리술사": Unit("보리술사", s10='반지상의하의보장팔찌벨트', s30='반지상의하의보장팔찌벨트30'),
  "보리꾸꾸": Unit("보리꾸꾸"),
  "보리뚜킥": Unit("보리뚜킥"),
   "건꾸꾸": Unit("건꾸꾸"),
    "보리핏": Unit("보리핏", s10='반지상의하의보장팔찌벨트', s30='반지상의하의보장팔찌벨트30'),
   "보리심판관": Unit("보리심판관", s10='반지상의하의보장팔찌벨트', s30='반지상의하의보장팔찌벨트30'),
   "보리커": Unit("보리커"),
  "소울뚜": Unit("소울뚜", s10='반지상의하의보장팔찌벨트', s30='반지상의하의보장팔찌벨트30'),
  "보리뚜비": Unit("보리뚜비", s10='반지상의하의보장팔찌벨트', s30='반지상의하의보장팔찌벨트30'),
   "보리파": Unit("보리파", s10='반지상의하의보장팔찌벨트', s30='반지상의하의보장팔찌벨트30'),
   "웨펀꾸꾸": Unit("웨펀꾸꾸"),
   "지짱보": Unit("지짱보", s10='반지상의하의보장팔찌벨트', s30='반지상의하의보장팔찌벨트30'),
    "서큐버뚜": Unit("서큐버뚜", s10='반지상의하의보장팔찌벨트', s30='반지상의하의보장팔찌벨트30'),

    # "보리닉": Unit("보리닉"인챈뚜": Unit("인챈뚜"),
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
    if(len(map) != 1):
        action.캐릭터선택2()

    do(Clicker('모험'))
    do(Clicker('모험_상급던전'))
    # 반지상의하의보장팔찌목걸이()
    # 무기반지어깨신발()
    # 무기반지어깨신발30()
    # globals()[char.s30]()
    globals()[char.s10]()

    if(do(Founder('상급던전_입장재료소진', threshold=0.99), onlyOneTime=True)
    or do(Founder('피로도0', threshold=0.97), onlyOneTime=True)
    or do(Founder('피로도10', threshold=0.97), onlyOneTime=True)
    ):
        print('재료소진')
        do(Clicker('뒤로가기'))
        do(Clicker('뒤로가기'))
        do(Clicker('뒤로가기'))
    else:
        do(Clicker('상급던전_입장', threshold=0.84))
        do(Founder('상급던전_입장완료'))

        while True:
            do(Presser(str(char.buffIndex)))
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
                    if(findBoss is True):
                        keyboard2.pressKey2(char.finalIndex)
                    pyautogui.keyDown('x')
                    if(findBoss):
                        time.sleep(2.0)
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
                    pyautogui.keyDown('right')
                    time.sleep(0.2)
                    pyautogui.keyUp('right')
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
                screenShot = image_finder.getScreenShotToGray()
                if(do(Founder('상급던전_피로도부족'), screenShot=screenShot, onlyOneTime=True)):
                    keyboard2.pressKey2('f8')
                    break
                if(do(Founder('상급던전_입장재료부족'), screenShot=screenShot, onlyOneTime=True)):
                    keyboard2.pressKey2('f8')
                    break

                do(Founder('상급던전_입장완료'))


mailSender.sendMail("[DNF] 상던완료" , "-")
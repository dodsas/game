from image_robot import *
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

def 반지상의하의보장팔찌벨트210():
    do(Clicker('파워스테이션', threshold=0.85))
    # do(Clicker('상급던전_다음표시'))
    # do(Clicker('상급던전_다음표시'))
    # do(Clicker('파워스테이션_트롬베10'))
    do(Clicker('상급던전_네비게이션'))
    do(Clicker('파워스테이션_트롬베10_2'))

def 반지상의하의보장팔찌벨트230():
    do(Clicker('파워스테이션', threshold=0.85))
    # do(Clicker('상급던전_다음표시'))
    # do(Clicker('상급던전_다음표시'))
    do(Clicker('상급던전_네비게이션'))
    do(Clicker('파워스테이션_트롬베30_2'))

def 반지상의하의보장팔찌벨트10():
    do(Clicker('파워스테이션', threshold=0.85))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('파워스테이션_코레', threshold=0.7))  # 반지 상의 하의 보장 팔찌 벨트
def 반지상의하의보장팔찌벨트30():
    do(Clicker('파워스테이션', threshold=0.85))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('파워스테이션_코레30', threshold=0.7))  # 반지 상의 하의 보장 팔찌 벨트
def 무기목걸이어깨신발10():
    do(Clicker('상급던전_다음표시'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('파워스테이션_푸르츠', threshold=0.7))  # 무기 목걸이 어깨 신발
def 무기목걸이어깨신발30():
    do(Clicker('파워스테이션', threshold=0.85))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('파워스테이션_푸르츠30', threshold=0.7))  # 무기 목걸이 어깨 신발

def 무기목걸이어깨신발210():
    do(Clicker('파워스테이션', threshold=0.85))
    # do(Clicker('상급던전_다음표시'))
    do(Clicker('상급던전_네비게이션'))
    do(Clicker('파워스테이션_그란디네10_2'))
def 무기목걸이어깨신발230():
    do(Clicker('파워스테이션', threshold=0.85))
    # do(Clicker('상급던전_다음표시'))
    do(Clicker('상급던전_네비게이션'))
    do(Clicker('파워스테이션_그란디네30_2'))

def 보장팔찌허리10():
    do(Clicker('원데과학단지', threshold=0.85))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('원데과학단지_토스텐', threshold=0.85))
def 보장팔찌허리30():
    do(Clicker('원데과학단지', threshold=0.85))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('원데과학단지_토스텐30', threshold=0.85))
def 신발목걸이어깨10():
    do(Clicker('원데과학단지'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('원데과학단지_구스타프'))
def 신발목걸이어깨30():
    do(Clicker('원데과학단지'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('원데과학단지_구스타프30'))
def 무기10():
    do(Clicker('원데과학단지'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('원데과학단지_옵티머스'))  # 무기
def 무기30():
    do(Clicker('원데과학단지'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('상급던전_다음표시'))
    do(Clicker('원데과학단지_옵티머스30'))

def 안톤무기바지벨트목걸이반지10():
    do(Clicker('상던안톤', threshold=0.72))
    # do(Clicker('상급던전_다음표시'))
    # do(Clicker('상급안톤_검은화산10'))
    do(Clicker('상급던전_네비게이션'))
    do(Clicker('상급안톤_검은화산10_2'))
def 안톤무기바지벨트목걸이반지30():
    do(Clicker('상던안톤', threshold=0.72))
    # do(Clicker('상급던전_다음표시'))
    # do(Clicker('상급안톤_검은화산30'))
    do(Clicker('상급던전_네비게이션'))
    do(Clicker('상급안톤_검은화산30_2'))
def 안톤상의어깨신발팔찌보장10():
    do(Clicker('상던안톤', threshold=0.72))
    # do(Clicker('상급던전_다음표시'))
    # do(Clicker('상급던전_다음표시'))
    # do(Clicker('상급던전_다음표시'))
    # do(Clicker('상급던전_검은연기10'))
    do(Clicker('상급던전_네비게이션'))
    do(Clicker('상급던전_검은연기10_2'))
def 안톤상의어깨신발팔찌보장30():
    do(Clicker('상던안톤', threshold=0.72))
    # do(Clicker('상급던전_다음표시'))
    # do(Clicker('상급던전_다음표시'))
    # do(Clicker('상급던전_다음표시'))
    # do(Clicker('상급던전_검은연기30'))
    do(Clicker('상급던전_네비게이션'))
    do(Clicker('상급던전_검은연기30_2'))
    
piro='10'
# maxLoop=10
maxLoop=30
# maxLoop=4
map = {
    "보리성": Unit("보리성", s='안톤무기바지벨트목걸이반지', buffIndex=4),
   "베인뚜": Unit("베인뚜", s='안톤상의어깨신발팔찌보장'),
   "보리빵떡": Unit("보리빵떡", s='안톤상의어깨신발팔찌보장'),
   "보리뚜": Unit("보리뚜", s='안톤무기바지벨트목걸이반지'),
   "보리세이더": Unit("보리세이더", s='안톤무기바지벨트목걸이반지'),
    "보리뚜뚜": Unit("보리뚜뚜", s='안톤상의어깨신발팔찌보장'),
    "보리템플러": Unit("보리템플러", s='안톤상의어깨신발팔찌보장'),
    "무녀뚜": Unit("무녀뚜", s='안톤무기바지벨트목걸이반지'),

    # "인챈뚜": Unit("인챈뚜", s='반지상의하의보장팔찌벨트2'),
    # "소울뚜": Unit("소울뚜", s='반지상의하의보장팔찌벨트2'),
    
    # "지짱보": Unit("지짱보", s='반지상의하의보장팔찌벨트2'),
    # "강한보리": Unit("강한보리"),
    # "보리술사": Unit("보리술사", s='반지상의하의보장팔찌벨트2'),
    # "런처꾸꾸": Unit("런처꾸꾸", s='무기목걸이어깨신발2'),
    # "건꾸꾸": Unit("건꾸꾸", s='무기목걸이어깨신발2'),
    # "보리뚜킥": Unit("보리뚜킥", s='무기목걸이어깨신발2'),
    # "보리꾸꾸": Unit("보리꾸꾸", s='무기목걸이어깨신발2'),
    # "보리핏": Unit("보리핏", s='반지상의하의보장팔찌벨트2'),
    # "보리심판관": Unit("보리심판관", s='반지상의하의보장팔찌벨트2'),
    # "보리뚜비": Unit("보리뚜비", s='반지상의하의보장팔찌벨트2'),
    # "보리메이지": Unit("보리메이지", s='반지상의하의보장팔찌벨트2'),
    # "보리파": Unit("보리파", s='반지상의하의보장팔찌벨트2'),
    # "보리커": Unit("보리커", s='무기목걸이어깨신발2'),
    # "웨펀꾸꾸": Unit("웨펀꾸꾸", s='무기목걸이어깨신발2'),
    # "서큐버뚜": Unit("서큐버뚜", s='반지상의하의보장팔찌벨트2'),
    # "윈드꾸꾸": Unit("윈드꾸꾸"),
    # "보리닉": Unit("보리닉"),
}

# map = unit.map
# map = {  "보리성": Unit("보리성", s='안톤무기바지벨트목걸이반지', buffIndex=4), }

os.system('rm -rf imagesLog/*')

# def core(type: str):
for key in map:
    select(key)
    char = map[key]
    robot.charName = char.name
    time.sleep(1)
    if (len(map) != 1):
        action.캐릭터선택2()

    do(Clicker('모험'))
    do(Clicker('모험_상급던전'))
    globals()[char.s+piro]()

    do(Clicker('상급던전_입장', threshold=0.84), canSkip=True)
    do(Clicker('확인'), canSkip=True)

    # time.sleep(2)
    if (do(Founder('상급던전_입장', threshold=0.84), onlyOneTime=True)):
        print('재료소진')
        do(Clicker('뒤로가기'))
        do(Clicker('뒤로가기'))
        do(Clicker('뒤로가기'))
        continue

    do(Founder('상급던전_입장완료'))

    loop = 0
    while True:
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
                if (findBoss is True):
                    keyboard2.pressKey2(char.finalIndex)
                pyautogui.keyDown('x')
                if (findBoss):
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

            if (findBoss is False and do(Founder('상급던전_보스', threshold=0.9), onlyOneTime=True)):
                do(Presser(str(char.finalIndex)))
                findBoss = True

            screenShot = image_finder.getScreenShotToGray()

            # if (do(Founder('상급던전_완료'), screenShot=screenShot, onlyOneTime=True)):
                # do(Founder('상던_재도전하기'),screenShot=screenShot, onlyOneTime=True) ):
            if(do(Clicker('상급던전_완료'), onlyOneTime=True, screenShot=screenShot)):
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

            if (do(Clicker('재도전_수리', screenShot=screenShot, threshold=0.75), onlyOneTime=True)):
                imageFinder.waitAndClick('장비수리확인', maxWait=3, error=False)
                robot.pressKey('ESC', sleep=4)

            if (forLoop % 20 == 0):
                Clicker('부활', screenShot=screenShot, threshold=0.75).action()

            if (forLoop > 125):
                dun_print.errorf(char.name + " 상급던전 실패")

        if (do(Founder('상급던전_재도전'))):
            if (loop >= maxLoop):
                keyboard2.pressKey2('f8')
                break
            do(Clicker('상급던전_재도전'))
            time.sleep(1)
            screenShot = image_finder.getScreenShotToGray()
            if (do(Founder('상급던전_피로도부족', threshold=0.85), screenShot=screenShot, onlyOneTime=True)):
                keyboard2.pressKey2('f8')
                break
            if (do(Founder('상급던전_입장재료부족'), screenShot=screenShot, onlyOneTime=True)):
                keyboard2.pressKey2('f8')
                break

            do(Founder('상급던전_입장완료'))

# core('30')
# core('10')

mailSender.sendMail("[DNF] 상던완료", "-")

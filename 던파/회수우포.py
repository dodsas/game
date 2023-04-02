import pyautogui
import robot
import time
import action
import unit
import os
from datetime import datetime
import imageFinder
import mailSender
from unit import Unit

# import 신비크리처
# map of Unit objects
os.system('rm -rf imagesLog/*')

def 우포상점구매():
    imageFinder.waitAndClick('상점')
    imageFinder.waitAndClick('상점_기타')
    imageFinder.waitAndClick('상점_우포')
    pyautogui.sleep(2)

    upo('상점_우포_촉매')
    upo('상점_우포_함성')

    imageFinder.waitAndClick('상점_우포_크리처')
    pyautogui.sleep(0.5)
    upo('상점_우포_진화용')

    imageFinder.waitAndClick('상점_우포_크리처_소모폼')
    pyautogui.sleep(0.5)
    upo('상점_우포_쿠키')
    upo('상점_우포_타코')
    # upo('상점_우포_아티')

    robot.pressKey('esc')
    robot.pressKey('esc')

def upo(imageName):
    if(imageFinder.isFound(imageName, threshold=0.97)):
        imageFinder.waitAndClick(imageName)
        imageFinder.waitAndClick('상점_우포_최대입력')
        imageFinder.waitAndClick('구입')
        imageFinder.waitAndClick('확인')



loop = 1
mapInit = {
    "보리성": Unit("보리성", 신비전체구매=True, buffIndex=4, loopCount=2),
   "보리뚜": Unit("보리뚜", 신비전체구매=True),
    "보리세이더": Unit("보리세이더", 신비전체구매=True, loopCount=3),
   "보리빵떡": Unit("보리빵떡", 신비전체구매=True, loopCount=2),
    "보리템플러": Unit("보리템플러", 신비전체구매=True),
    "보리술사": Unit("보리술사", loopCount=11),
    "런처꾸꾸": Unit("런처꾸꾸", 신비전체구매=True, loopCount=13),
    "보리꾸꾸": Unit("보리꾸꾸", 신비전체구매=True, buffIndex=6, loopCount=13),
    "보리뚜뚜": Unit("보리뚜뚜", 신비전체구매=True, buffIndex=2),
    "소울뚜": Unit("소울뚜", loopCount=loop),

    "보리뚜비": Unit("보리뚜비", loopCount=12),
    "보리뚜킥": Unit("보리뚜킥", loopCount=13),
    "보리핏": Unit("보리핏", 신비전체구매=False, loopCount=loop),
    "베인뚜": Unit("베인뚜", 신비전체구매=False, loopCount=loop, finalIndex='f'),
    "보리커": Unit("보리커", 신비전체구매=True, loopCount=13),
    "보리파": Unit("보리파", 신비전체구매=False, loopCount=11),
    "윈드꾸꾸": Unit("윈드꾸꾸", 신비전체구매=False, finalIndex='f', loopCount=11),
    "무녀뚜": Unit("무녀뚜", 신비전체구매=False, loopCount=12),

    "웨펀꾸꾸": Unit("웨펀꾸꾸", loopCount=loop),
    "서큐버뚜": Unit("서큐버뚜", 신비전체구매=False, loopCount=loop, finalIndex='3'),
    "보리심판관": Unit("보리심판관", 신비전체구매=False, loopCount=loop),
}

map = unit.map
# map = mapInit 
for key in map:
    unit.select(key)
    char = map[key]
    robot.charName = char.name
    action.캐릭터선택(char)
    우포상점구매()
# 우포상점구매()

mailSender.sendMail("[DNF] 우포 완료" , "-")
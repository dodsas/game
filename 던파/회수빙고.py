# pyautogui is a module that allows you to control the mouse and keyboard
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

#import 신비크리처
# map of Unit objects
os.system('rm -rf imagesLog/*')

loop = 0
mapInit = {
    "보리성": Unit("보리성", 신비전체구매=True, buffIndex=4, loopCount=loop, epicDone=True),
    "보리뚜": Unit("보리뚜", 신비전체구매=True, loopCount=12, sunganDone=False, epicDone=True),
    "보리세이더": Unit("보리세이더", 신비전체구매=True, loopCount=loop, sunganDone=True, epicDone=True),
    "베인뚜": Unit("베인뚜", 신비전체구매=True, loopCount=loop, finalIndex='f', epicDone=True),
     "보리빵떡": Unit("보리빵떡", 신비전체구매=True, loopCount=loop, sunganDone=True, epicDone=True),
    "보리메이지": Unit("보리메이지", 신비전체구매=False, loopCount=loop),

     "보리템플러": Unit("보리템플러", 신비전체구매=True, loopCount=loop, sunganDone=True, epicDone=True),
     "보리뚜뚜": Unit("보리뚜뚜", 신비전체구매=True, loopCount=loop, epicDone=True),
     "무녀뚜": Unit("무녀뚜", 신비전체구매=False, loopCount=loop, epicDone=True),
     "런처꾸꾸": Unit("런처꾸꾸", 신비전체구매=True, loopCount=loop, sunganDone=True),
     "보리술사": Unit("보리술사", loopCount=loop, sunganDone=True),
     "보리꾸꾸": Unit("보리꾸꾸"),
     "보리뚜킥": Unit("보리뚜킥", loopCount=loop, sunganDone=True, epicDone=True),
     "건꾸꾸": Unit("건꾸꾸", 신비전체구매=False, loopCount=loop),
     "보리핏": Unit("보리핏", 신비전체구매=False, loopCount=loop, sunganDone=True, epicDone=True),
     "보리심판관": Unit("보리심판관", 신비전체구매=False, loopCount=13, epicDone=True),
    "보리커": Unit("보리커", 신비전체구매=True, loopCount=13),
    "소울뚜": Unit("소울뚜", loopCount=loop, sunganDone=True),
    "보리뚜비": Unit("보리뚜비", loopCount=loop, sunganDone=True),
    "보리파": Unit("보리파", 신비전체구매=False, loopCount=loop, sunganDone=True),
    "웨펀꾸꾸": Unit("웨펀꾸꾸", loopCount=loop),

    "지짱보": Unit("지짱보", 신비전체구매=False, loopCount=loop),
    "서큐버뚜": Unit("서큐버뚜", 신비전체구매=False, loopCount=loop, finalIndex='3'),
    "보리닉": Unit("보리닉", 신비전체구매=False, loopCount=loop),
    "인챈뚜": Unit("인챈뚜", 신비전체구매=False, loopCount=loop),
    "윈드꾸꾸": Unit("윈드꾸꾸", 신비전체구매=False, finalIndex='f', loopCount=loop, sunganDone=True, epicDone=True),
}

map = mapInit
# map = unit.map
for key in map:
    unit.select(key)
    char = map[key]
    robot.charName = char.name
    action.캐릭터선택2()
    imageFinder.waitAndClick('확인', error=False, maxWait=3)
    robot.pressKey(';')
    imageFinder.waitAndClick('길드활동')
    imageFinder.waitAndClick('길드빙고')
    imageFinder.waitAndClick('빙고보상모두받기', error=False)
    imageFinder.waitAndClick('확인', error=False, maxWait=1)
    robot.pressKey('esc')
    robot.pressKey('esc')

mailSender.sendMail("[DNF] bingo 완료" , "-")
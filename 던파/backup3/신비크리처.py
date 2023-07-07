# pyautogui is a module that allows you to control the mouse and keyboard
# import pyautogui
import robot
# import time
import action
import unit
from unit import Unit
import os
# from datetime import datetime
import mailSender

# import 회수우포
# romove all files in imagesLog folder on osx
os.system('rm -rf imagesLog/*')

loop=0
mapInit = {
    "보리성": Unit("보리성", 신비전체구매=True, buffIndex=4, loopCount=loop, epicDone=True),
    "보리뚜": Unit("보리뚜", 신비전체구매=True, loopCount=loop, sunganDone=False, epicDone=True),
    "보리세이더": Unit("보리세이더", 신비전체구매=True, loopCount=loop, sunganDone=True, epicDone=True),
    "베인뚜": Unit("베인뚜", 신비전체구매=True, loopCount=4, finalIndex='f', epicDone=True),

    "보리빵떡": Unit("보리빵떡", 신비전체구매=True, loopCount=loop, sunganDone=True, epicDone=True),
    "보리템플러": Unit("보리템플러", 신비전체구매=True, loopCount=loop, sunganDone=True, epicDone=True),
    "보리뚜뚜": Unit("보리뚜뚜", 신비전체구매=True, buffIndex=2, loopCount=loop, epicDone=True),
    "무녀뚜": Unit("무녀뚜", 신비전체구매=False, loopCount=loop, epicDone=True),

    "보리뚜킥": Unit("보리뚜킥", loopCount=loop, sunganDone=True, epicDone=True),
    "보리핏": Unit("보리핏", 신비전체구매=False, loopCount=loop, sunganDone=True, epicDone=True),
    "윈드꾸꾸": Unit("윈드꾸꾸", 신비전체구매=False, finalIndex='f', loopCount=loop, sunganDone=True, epicDone=True),
    "보리심판관": Unit("보리심판관", 신비전체구매=False, loopCount=loop, sunganDone=True, epicDone=True),

    "보리커": Unit("보리커", 신비전체구매=True, loopCount=loop, sunganDone=True),
    "보리파": Unit("보리파", 신비전체구매=False, loopCount=loop, sunganDone=True),
    "런처꾸꾸": Unit("런처꾸꾸", 신비전체구매=True, loopCount=loop, sunganDone=True),
    "보리꾸꾸": Unit("보리꾸꾸", 신비전체구매=True, buffIndex=6, loopCount=loop, sunganDone=True),
    "보리술사": Unit("보리술사", loopCount=loop, sunganDone=True),
    "소울뚜": Unit("소울뚜", loopCount=loop, sunganDone=True),
    "보리뚜비": Unit("보리뚜비", loopCount=loop, sunganDone=True),
    "웨펀꾸꾸": Unit("웨펀꾸꾸", loopCount=loop),
    "서큐버뚜": Unit("서큐버뚜", 신비전체구매=False, loopCount=loop, finalIndex='3'),
    "지짱보": Unit("지짱보", 신비전체구매=False, loopCount=loop),
    "건꾸꾸": Unit("건꾸꾸", 신비전체구매=False, loopCount=loop),
    "보리닉": Unit("보리닉", 신비전체구매=False, loopCount=0),
}

map = unit.map
# map = mapInit 

for key in map:
    unit.select(key)
    char = map[key]
    robot.charName = char.name
    # action.캐릭터선택(char)
    # action.신비상점구매(char)

    print("****")
    action.캐릭터선택2()
    action.신비상점구매2()

    # action.크리처()
mailSender.sendMail("[DNF] 신비상점 완료" , "-")
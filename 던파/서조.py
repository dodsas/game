# pyautogui is a module that allows you to control the mouse and keyboard
import pyautogui
import robot
import time
import action
from unit import Unit
from unit import select
import os
from datetime import datetime
import mailSender

#import 신비크리처

map = {
  #  "보리성": Unit("보리성", 신비전체구매=True, buffIndex=4, loopCount=13),
  # "보리뚜": Unit("보리뚜", 신비전체구매=True, loopCount=13),
#    "보리세이더": Unit("보리세이더", 신비전체구매=True, loopCount=13),
    "보리빵떡": Unit("보리빵떡", 신비전체구매=True, loopCount=13),
    "보리템플러": Unit("보리템플러", 신비전체구매=True, loopCount=13),
    "보리뚜뚜": Unit("보리뚜뚜", 신비전체구매=True, buffIndex=2, loopCount=13),
    "베인뚜": Unit("베인뚜", 신비전체구매=False, loopCount=0, finalIndex='f'),
    "보리뚜킥": Unit("보리뚜킥", loopCount=13),
    "보리핏": Unit("보리핏", 신비전체구매=False, loopCount=13),
    "보리커": Unit("보리커", 신비전체구매=True, loopCount=13),
    "윈드꾸꾸": Unit("윈드꾸꾸", 신비전체구매=False, finalIndex='f', loopCount=13),
    "보리파": Unit("보리파", 신비전체구매=False, loopCount=13),
    "런처꾸꾸": Unit("런처꾸꾸", 신비전체구매=True, loopCount=13),
    "보리꾸꾸": Unit("보리꾸꾸", 신비전체구매=True, buffIndex=6, loopCount=13),
    "보리술사": Unit("보리술사", loopCount=13),
    "소울뚜": Unit("소울뚜", loopCount=13),
    "보리심판관": Unit("보리심판관", 신비전체구매=False, loopCount=13),
    "보리뚜비": Unit("보리뚜비", loopCount=13),
    "웨펀꾸꾸": Unit("웨펀꾸꾸", loopCount=13),
    "무녀뚜": Unit("무녀뚜", 신비전체구매=False, loopCount=13),
    "서큐버뚜": Unit("서큐버뚜", 신비전체구매=False, loopCount=13, finalIndex='3'),
    "보리닉": Unit("보리닉", 신비전체구매=False, loopCount=0, finalIndex='3')
}

# map = unit.map
for key in map:
    select(key)
    char = map[key]
    robot.charName = char.name
    action.캐릭터선택(char)
    action.서조(char)

# action.서조(map["보리심판관"])

mailSender.sendMail("[DNF] 서조 완료" , "-")
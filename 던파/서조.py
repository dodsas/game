# pyautogui is a module that allows you to control the mouse and keyboard
import pyautogui
import robot
import time
import action
import unit
import os
from datetime import datetime
import mailSender

#import 신비크리처

map = {
 "보리성": unit.Unit("보리성", 신비전체구매=True, buffIndex=4),
    "보리뚜": unit.Unit("보리뚜", 신비전체구매=True),
     "보리세이더": unit.Unit("보리세이더", 신비전체구매=True, loopCount=3),
     "보리빵떡": unit.Unit("보리빵떡", 신비전체구매=True, loopCount=3),
     "보리뚜뚜": unit.Unit("보리뚜뚜", 신비전체구매=True, buffIndex=6),
     "보리템플러": unit.Unit("보리템플러", 신비전체구매=True) ,
     "보리뚜킥": unit.Unit("보리뚜킥"),  
     "보리핏": unit.Unit("보리핏", 신비전체구매=False, loopCount=13),
     "베인뚜": unit.Unit("베인뚜", 신비전체구매=False, loopCount=13, finalIndex='f'),
     "보리뚜비": unit.Unit("보리뚜비"),
     "보리커": unit.Unit("보리커", 신비전체구매=True),
     "런처꾸꾸": unit.Unit("런처꾸꾸", 신비전체구매=True),
    "보리꾸꾸": unit.Unit("보리꾸꾸", 신비전체구매=True, buffIndex=6),
    "보리술사": unit.Unit("보리술사"),
     "소울뚜": unit.Unit("소울뚜"),
    "웨펀꾸꾸": unit.Unit("웨펀꾸꾸"),
     "무녀뚜": unit.Unit("무녀뚜", 신비전체구매=False, loopCount=13),
     "보리파": unit.Unit("보리파", 신비전체구매=False, loopCount=13),
     "서큐버뚜": unit.Unit("서큐버뚜", 신비전체구매=False, loopCount=13, finalIndex='3'),
     "윈드꾸꾸": unit.Unit("윈드꾸꾸", 신비전체구매=False, finalIndex='f'),
    "보리심판관": unit.Unit("보리심판관", 신비전체구매=False, loopCount=13),
}

# map = unit.map
for key in map:
    unit.select(key)
    char = map[key]
    robot.charName = char.name
    action.캐릭터선택(char)
    action.서조(char)

# action.서조(map["보리심판관"])

mailSender.sendMail("[DNF] 서조 완료" , "-")
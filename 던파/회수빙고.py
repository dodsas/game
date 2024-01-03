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
    # "보리성": Unit("보리성", s='안톤무기바지벨트목걸이반지', buffIndex=4),
    # "베인뚜": Unit("베인뚜", s='안톤상의어깨신발팔찌보장'),
    # "보리빵떡": Unit("보리빵떡", s='안톤상의어깨신발팔찌보장'),
    #"보리뚜": Unit("보리뚜", s='안톤무기바지벨트목걸이반지'),
    #"보리세이더": Unit("보리세이더", s='안톤무기바지벨트목걸이반지'),
    #"보리뚜뚜": Unit("보리뚜뚜", s='안톤상의어깨신발팔찌보장'),
    #"보리템플러": Unit("보리템플러", s='안톤상의어깨신발팔찌보장'),
    #"무녀뚜": Unit("무녀뚜", s='안톤무기바지벨트목걸이반지'),

    #"인챈뚜": Unit("인챈뚜", s='반지상의하의보장팔찌벨트2'),
    #"소울뚜": Unit("소울뚜", s='반지상의하의보장팔찌벨트2'),
    
    "지짱보": Unit("지짱보", s='반지상의하의보장팔찌벨트2'),
    "보리술사": Unit("보리술사", s='반지상의하의보장팔찌벨트2'),
    "런처꾸꾸": Unit("런처꾸꾸", s='무기목걸이어깨신발2'),
    "보리뚜킥": Unit("보리뚜킥", s='무기목걸이어깨신발2'),
    "건꾸꾸": Unit("건꾸꾸", s='무기목걸이어깨신발2'),
    "보리꾸꾸": Unit("보리꾸꾸", s='무기목걸이어깨신발2'),
    "보리핏": Unit("보리핏", s='반지상의하의보장팔찌벨트2'),
    "보리심판관": Unit("보리심판관", s='반지상의하의보장팔찌벨트2'),
    "보리커": Unit("보리커", s='무기목걸이어깨신발2'),
    "보리파": Unit("보리파", s='반지상의하의보장팔찌벨트2'),
    "보리뚜비": Unit("보리뚜비", s='반지상의하의보장팔찌벨트2'),
    "웨펀꾸꾸": Unit("웨펀꾸꾸", s='무기목걸이어깨신발2'),
    "보리메이지": Unit("보리메이지", s='반지상의하의보장팔찌벨트2'),
    "서큐버뚜": Unit("서큐버뚜", s='반지상의하의보장팔찌벨트2'),
    "보리닉": Unit("보리닉"),
    "윈드꾸꾸": Unit("윈드꾸꾸"),
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
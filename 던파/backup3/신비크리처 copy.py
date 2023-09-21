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
    "보리성": Unit("보리성"),
    "보리뚜": Unit("보리뚜", s10='신발목걸이어깨10', s30='신발목걸이어깨30'),
    "보리세이더": Unit("보리세이더", s10='무기10', s30='무기30'),
    "베인뚜": Unit("베인뚜"),
    "보리빵떡": Unit("보리빵떡", s10='신발목걸이어깨10', s30='신발목걸이어깨30'),
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
    "보리닉": Unit("보리닉"),
    "인챈뚜": Unit("인챈뚜"),
    "윈드꾸꾸": Unit("윈드꾸꾸"),
}

# map = unit.map
map = mapInit 

for key in map:
    unit.select(key)
    char = map[key]
    robot.charName = char.name
    # action.캐릭터선택(char)
    action.신비상점구매(char)

    print("****")
    action.캐릭터선택2()
    action.신비상점구매2()

    # action.크리처()
mailSender.sendMail("[DNF] 신비상점 완료" , "-")
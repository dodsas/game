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

from tobe import * 

# image_finder.imgPath = 'Image/강림로터스/'


map = {
    # "베인뚜": Unit("베인뚜", attackMode='True', plan='z'),
    # "보리성": Unit("보리성", buffIndex=4),
    #  "보리빵떡": Unit("보리빵떡"),
    #  "지짱보": Unit("지짱보", attackMode='True', plan='z'),
    #  "강한보리": Unit("강한보리"),
    #  "보리뚜": Unit("보리뚜"),
    #  "보리세이더": Unit("보리세이더", attackMode='True', plan='z'),
    # "보리템플러": Unit("보리템플러", attackMode='True', plan='z'),
    # "보리뚜뚜": Unit("보리뚜뚜", attackMode=True, plan='z'),
    # "인챈뚜": Unit("인챈뚜", attackMode=True, plan='z'),
    # "무녀뚜": Unit("무녀뚜", attackMode=True, plan='z'),
    # "소울뚜": Unit("소울뚜", attackMode=True, plan='z'),
    # "런처꾸꾸": Unit("런처꾸꾸"),
    # "보리꾸꾸": Unit("보리꾸꾸"),
    # "웨펀꾸꾸": Unit("웨펀꾸꾸"),
    "보리치료사": Unit("보리치료사", attackMode=True, plan='z'),
    "맥보리": Unit("맥보리", attackMode=True, plan='z'),
    "건꾸꾸": Unit("건꾸꾸", attackMode=True, plan='z'),
    "보리핏": Unit("보리핏", attackMode=True, plan='b'),
    "보리뚜킥": Unit("보리뚜킥", attackMode=True, plan='b'),
    "보리술사": Unit("보리술사", attackMode=True, plan='b'),
    "보리파": Unit("보리파", attackMode=True, plan='b'),
    "보리심판관": Unit("보리심판관", attackMode=True, plan='b'),
    "보리뚜비": Unit("보리뚜비", attackMode=True, plan='b'),
    "보리메이지": Unit("보리메이지", attackMode=True, plan='b'),
    "서큐버뚜": Unit("서큐버뚜", attackMode=True, plan='b'),
    "보리커": Unit("보리커", attackMode=True, plan='b'),
    "윈드꾸꾸": Unit("윈드꾸꾸", attackMode=True, plan='b'),
    "보리뱅": Unit("보리뱅", attackMode=True, plan='b'),
    "보리닉": Unit("보리닉", attackMode=True, plan='b'),
    "보리왕": Unit("보리왕", plan='b'),
    "보리샷": Unit("보리샷", attackMode=True, plan='b'),
}


os.system('rm -rf imagesLog/*')
for key in map:
    unit.select(key)
    char = map[key]

    if(len(map) != 1):
        action2.캐릭터선택2()

    # action2.즐겨찾기구매()
    do(Clicker('모험'))
    do(Clicker('업적'))
    do(Clicker('일괄받기'))
    do(Clicker('ok'), onlyOneTime=True)
    do(Clicker('뒤로가기'))

    
mailSender.sendMail("[DNF] 비밀작전 완료" , "-")


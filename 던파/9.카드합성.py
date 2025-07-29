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

image_finder.imgPath = 'Image/카드합성/'

map = {
    "보리성": Unit("보리성", buffIndex=4),
    "베인뚜": Unit("베인뚜"),
    "보리빵떡": Unit("보리빵떡"),
    "지짱보": Unit("지짱보"),
    "강한보리": Unit("강한보리"),
    "보리뚜": Unit("보리뚜"),
    "보리세이더": Unit("보리세이더"),

    "보리뚜뚜": Unit("보리뚜뚜"),
    "보리템플러": Unit("보리템플러"),
    "인챈뚜": Unit("인챈뚜"), 
    "무녀뚜": Unit("무녀뚜"),
    "소울뚜": Unit("소울뚜"),

    "런처꾸꾸": Unit("런처꾸꾸"), #--
    "보리꾸꾸": Unit("보리꾸꾸"), #--
    "웨펀꾸꾸": Unit("웨펀꾸꾸"), #--
    "보리뚜킥": Unit("보리뚜킥"),
    "보리술사": Unit("보리술사"),
    "보리메이지": Unit("보리메이지"),
    "보리핏": Unit("보리핏"),
    "건꾸꾸": Unit("건꾸꾸"),
    "서큐버뚜": Unit("서큐버뚜"),
    "보리커": Unit("보리커"),
    "보리심판관": Unit("보리심판관"),
    "보리파": Unit("보리파"),
    "보리뚜비": Unit("보리뚜비"),
    "윈드꾸꾸": Unit("윈드꾸꾸"),
    "보리닉": Unit("보리닉"),
    # "보리뱅": Unit("보리뱅"),
}

# map = unit.map
map = { "보리뚜": Unit("보리뚜") }

os.system('rm -rf imagesLog/*')
for key in map:
    unit.select(key)
    char = map[key]

    if(len(map) != 1):
        action2.캐릭터선택2()
    action2.카드합성()

mailSender.sendMail("[DNF] 카드합성 완료" , "-")
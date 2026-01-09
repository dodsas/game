import logging
import pyautogui
import robot
import time
import action
import action2
from unit import Unit, select, map
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
    "베인뚜": Unit("베인뚜", attackMode=True, plan='h', level='M'),
    "보리성": Unit("보리성", buffIndex=4, plan='h', level='M'),
    "보리빵떡": Unit("보리빵떡", plan='k', level='M'),
    "지짱보": Unit("지짱보", plan='k', level='M'),
    "강한보리": Unit("강한보리", plan='k', level='M'),
    "보리뚜": Unit("보리뚜", plan='s', level='M'),
    "보리세이더": Unit("보리세이더", plan='s', level='M'),
    "보리뚜뚜": Unit("보리뚜뚜", attackMode=False, plan='s', level='M'),
    "보리템플러": Unit("보리템플러", attackMode=False, plan='s', level='E'),
    "인챈뚜": Unit("인챈뚜", attackMode=False, plan='s', level='E'),
    "무녀뚜": Unit("무녀뚜", attackMode=False, plan='s', level='E'),
    "소울뚜": Unit("소울뚜", attackMode=False, plan='s', level='E'),
    "보리치료사": Unit("보리치료사", attackMode=False, plan='s', level='E'),
    "런처꾸꾸": Unit("런처꾸꾸", attackMode=False, plan='r', level='E'),
    "보리꾸꾸": Unit("보리꾸꾸", attackMode=False, plan='r', level='E'),
    "웨펀꾸꾸": Unit("웨펀꾸꾸", attackMode=False, plan='r', level='E'),
    "블레이뚜": Unit("블레이뚜", attackMode=False, plan='r', level='E'),
    "불보리뚜": Unit("불보리뚜", attackMode=False, plan='r', level='E'),
    "맥보리": Unit("맥보리", attackMode=False, plan='r', level='E'),
    "건꾸꾸": Unit("건꾸꾸", attackMode=False, plan='r', level='E'),
    "보리핏": Unit("보리핏", attackMode=False, plan='r', level='E'),
    "보리뚜킥": Unit("보리뚜킥", attackMode=False, plan='r', level='E'),
    "보리술사": Unit("보리술사", attackMode=False, plan='r', level='E'),
    "보리파": Unit("보리파", attackMode=False, plan='r', level='E'),
    "보리심판관": Unit("보리심판관", attackMode=False, plan='r', level='E'),
    "보리뚜비": Unit("보리뚜비", attackMode=False, plan='r', level='E'),
    "보리메이지": Unit("보리메이지", attackMode=False, plan='r', level='E'),
    "서큐버뚜": Unit("서큐버뚜", attackMode=False, plan='r', level='E'),
    "보리커": Unit("보리커", attackMode=False, plan='r', level='E'),
    "윈드꾸꾸": Unit("윈드꾸꾸", attackMode=False, plan='r', level='E'),
    "보리뱅": Unit("보리뱅", attackMode=False, plan='r', level='E'),
    "보리닉": Unit("보리닉", attackMode=False, plan='r', level='E'),
    "보리왕": Unit("보리왕", attackMode=False, plan='r', level='E'),
    "보리샷": Unit("보리샷", attackMode=False, plan='r', level='E'),
}

os.system('rm -rf imagesLog/*')
for key in map:
    unit.select(key)
    char = map[key]

    if(len(map) != 1):
        action2.캐릭터선택2()

    action.우편함()        
    do(Clicker('모험'))
    do(Clicker('업적'))
    do(Clicker('일괄받기'), canSkip=True)
    do(Clicker('ok'), onlyOneTime=True)
    do(Clicker('뒤로가기'))

    do(Clicker('store'))
    do(Clicker('exchange'))
    do(Clicker('favorite'))
    do(Clicker('buy'), canSkip=True)
    do(Clicker('buyok'), canSkip=True)
    do(Clicker('뒤로가기'))
    
mailSender.sendMail("[DNF] 비밀작전 완료" , "-")


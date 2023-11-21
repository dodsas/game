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
sys.path.append('tobe')
from image_robot import * 

image_finder.imgPath = 'Image/카드합성/'

map = {
    # "보리성": Unit("보리성"),
    # "보리뚜": Unit("보리뚜", s='보장팔찌허리'),
    # "보리세이더": Unit("보리세이더", s='안톤무기바지벨트목걸이반지'),
    # "베인뚜": Unit("베인뚜"),
    # "보리빵떡": Unit("보리빵떡", s='보장팔찌허리'),
    # "보리뚜뚜": Unit("보리뚜뚜", s='안톤무기바지벨트목걸이반지'),
    # "보리템플러": Unit("보리템플러", s='반지상의하의보장팔찌벨트2'),
    # "무녀뚜": Unit("무녀뚜", s='안톤상의어깨신발팔찌보장'),
    # "인챈뚜": Unit("인챈뚜"),
    # "소울뚜": Unit("소울뚜", s='반지상의하의보장팔찌벨트2'),
    "런처꾸꾸": Unit("런처꾸꾸", s='무기목걸이어깨신발2'),
    "보리술사": Unit("보리술사", s='반지상의하의보장팔찌벨트2'),
    "보리커": Unit("보리커", s='무기목걸이어깨신발2'),
    "보리꾸꾸": Unit("보리꾸꾸", s='무기목걸이어깨신발2'),
    "건꾸꾸": Unit("건꾸꾸", s='무기목걸이어깨신발2'),
    "보리뚜킥": Unit("보리뚜킥", s='무기목걸이어깨신발2'),
    "보리핏": Unit("보리핏", s='반지상의하의보장팔찌벨트2'),
    "보리심판관": Unit("보리심판관", s='반지상의하의보장팔찌벨트2'),
    "보리파": Unit("보리파", s='반지상의하의보장팔찌벨트2'),
    "보리뚜비": Unit("보리뚜비", s='반지상의하의보장팔찌벨트2'),
    "웨펀꾸꾸": Unit("웨펀꾸꾸", s='무기목걸이어깨신발2'),
    "보리메이지": Unit("보리메이지", s='반지상의하의보장팔찌벨트'),
    "지짱보": Unit("지짱보", s='반지상의하의보장팔찌벨트2'),
    "서큐버뚜": Unit("서큐버뚜", s='반지상의하의보장팔찌벨트2'),
    "보리닉": Unit("보리닉"),
    "윈드꾸꾸": Unit("윈드꾸꾸"),
}

# map = unit.map
# map = { "보리뚜": Unit("보리뚜") }

os.system('rm -rf imagesLog/*')
for key in map:
    unit.select(key)
    char = map[key]

    if(len(map) != 1):
        action2.캐릭터선택2()
    action2.카드합성()

mailSender.sendMail("[DNF] 카드합성 완료" , "-")
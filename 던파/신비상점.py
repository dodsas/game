import pyautogui
import robot
import time
import action
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
import imageFinderBulk

sys.path.append('tobe')
from image_robot import * 

image_finder.imgPath = 'Image/신비상점/'
# imageFinderBulk.imgPath = 'Image/신비상점/'

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

os.system('rm -rf imagesLog/*')

map = mapInit 
# map = unit.map
map = { "보리뚜": Unit("보리뚜", s10='신발목걸이어깨10', s30='무기30') }

for key in map:
    select(key)
    char = map[key]
    charName = char.name
    if(len(map) != 1):
        action.캐릭터선택2()

    do(Clicker('상점'))
    do(Clicker('상점_신비'))

    do(Founder('신비상점입장'))
    pyautogui.sleep(3) 

    buyList = []
    buyList.append('라코13개')
    buyList.append('수리망치')
    # buyList.append('상점_신비뼈')
    # buyList.append('상점_신비철')
    # buyList.append('상점_신비')
    # buyList.append('상점_신비연석')
    # buyList.append('상점_신비라코')
    # buyList.append('상점_신비가죽')
    # buyList.append('상점_신비원소')
    # buyList.append('상점_신비경화제')
    # buyList.append('상점_신비다이야')

    if(char.신비전체구매 == True):
        buyList.append('상점_신비칼박')
    # else:
        # buyList.append('상점_신비테라')
        # buyList.append('상점_신비테라2')
    
    imageFinderBulk.findAndClick('신비로그_' + charName, buyList)

    if(do(Clicker('구매하기'), onlyOneTime=True)):
        do(Clicker('구입'))

    # if(imageFinder.waitAndClick('구매하기', maxWait=2, threshold=0.85, error=False) == True) :
    #     imageFinder.waitAndClick('구입', maxWait=3, threshold=0.85, error=False)
    #     imageFinder.waitAndClick('확인', maxWait=3, threshold=0.91, error=False)

    # if(imageFinder.isFound('신비_소지금액부족') != None):
    #     robot.pressKey('ESC')
    
    do(Clicker('뒤로가기'))


    # robot.pressKey('ESC')
    # waitToHomeWithKey('ESC')


# mailSender.sendMail("[DNF] 신비상점 완료" , "-")
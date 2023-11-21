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
    "보리뚜": Unit("보리뚜", s='보장팔찌허리'),
    "보리세이더": Unit("보리세이더", s='안톤상의어깨신발팔찌보장'),
    "베인뚜": Unit("베인뚜"),
    "보리빵떡": Unit("보리빵떡", s='보장팔찌허리'),
    "보리뚜뚜": Unit("보리뚜뚜", s='안톤무기바지벨트목걸이반지'),
    "보리템플러": Unit("보리템플러", s='반지상의하의보장팔찌벨트2'),
    "무녀뚜": Unit("무녀뚜", s='안톤상의어깨신발팔찌보장'),
    "인챈뚜": Unit("인챈뚜"),
    "소울뚜": Unit("소울뚜", s='반지상의하의보장팔찌벨트2'),
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

os.system('rm -rf imagesLog/*')

map = mapInit 
# map = unit.map
# map = { "보리뚜": Unit("보리뚜", s10='신발목걸이어깨10', s30='무기30') }

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
    buyList.append('라코10개')
    buyList.append('라코13개')
    buyList.append('라코15개')
    buyList.append('라코20개')
    buyList.append('라코30개')
    buyList.append('라코100개')
    buyList.append('라코200개')
    # buyList.append('수리망치')
    
    buyList.append('경화제10개')
    buyList.append('다이아10개')
    buyList.append('칼박1개_가브')
    buyList.append('칼박1개_가브_44500')
    buyList.append('칼박조각5개')
    buyList.append('촉매제조각15개')


    if(char.신비전체구매 == True):
        buyList.append('상점_신비칼박')
    # else:
        # buyList.append('상점_신비테라')
        # buyList.append('상점_신비테라2')
    
    imageFinderBulk.findAndClick('신비로그_' + charName, buyList)

    if(do(Clicker('구매하기', threshold=0.83), onlyOneTime=True)):
        do(Clicker('구입'))

    # if(imageFinder.waitAndClick('구매하기', maxWait=2, threshold=0.85, error=False) == True) :
    #     imageFinder.waitAndClick('구입', maxWait=3, threshold=0.85, error=False)
    #     imageFinder.waitAndClick('확인', maxWait=3, threshold=0.91, error=False)

    # if(imageFinder.isFound('신비_소지금액부족') != None):
    #     robot.pressKey('ESC')
    
    do(Clicker('뒤로가기'))


    # robot.pressKey('ESC')
    # waitToHomeWithKey('ESC')


mailSender.sendMail("[DNF] 신비상점 완료" , "-")
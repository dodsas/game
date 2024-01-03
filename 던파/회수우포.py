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

# import 신비크리처
# map of Unit objects
os.system('rm -rf imagesLog/*')

def 우포상점구매():
    pyautogui.sleep(4)
    imageFinder.waitAndClick('상점')
    pyautogui.sleep(2)
    imageFinder.waitAndClick('상점_기타')
    pyautogui.sleep(2)
    imageFinder.waitAndClick('상점_우포')
    pyautogui.sleep(4)

    upo('상점_우포_촉매')
    upo('상점_우포_함성')

    imageFinder.waitAndClick('상점_우포_크리처')
    pyautogui.sleep(0.5)
    upo('상점_우포_진화용')

    # imageFinder.waitAndClick('상점_우포_크리처_소모폼')
    # pyautogui.sleep(0.5)
    upo('상점_우포_쿠키')
    upo('상점_우포_타코')
    # upo('상점_우포_아티')

    robot.pressKey('esc')
    robot.pressKey('esc')

def upo(imageName):
    if(imageFinder.isFound(imageName, threshold=0.68)):
        imageFinder.waitAndClick(imageName, threshold=0.68, error=False)
        imageFinder.waitAndClick('상점_우포_최대입력', error=False)
        imageFinder.waitAndClick('구입', error=False)
        imageFinder.waitAndClick('확인', error=False)



loop = 1
mapInit = {
    "보리성": Unit("보리성", s='안톤무기바지벨트목걸이반지', buffIndex=4),
    "베인뚜": Unit("베인뚜", s='안톤상의어깨신발팔찌보장'),
    "보리빵떡": Unit("보리빵떡", s='안톤상의어깨신발팔찌보장'),
    "보리뚜": Unit("보리뚜", s='안톤무기바지벨트목걸이반지'),
    "보리세이더": Unit("보리세이더", s='안톤무기바지벨트목걸이반지'),
    "보리뚜뚜": Unit("보리뚜뚜", s='안톤상의어깨신발팔찌보장'),
    "보리템플러": Unit("보리템플러", s='안톤상의어깨신발팔찌보장'),
    "무녀뚜": Unit("무녀뚜", s='안톤무기바지벨트목걸이반지'),

    "인챈뚜": Unit("인챈뚜", s='반지상의하의보장팔찌벨트2'),
    "소울뚜": Unit("소울뚜", s='반지상의하의보장팔찌벨트2'),
    
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
map = unit.map
map = mapInit 
for key in map:
    unit.select(key)
    char = map[key]
    robot.charName = char.name
    action.캐릭터선택2()
    우포상점구매()
# 우포상점구매()

mailSender.sendMail("[DNF] 우포 완료" , "-")
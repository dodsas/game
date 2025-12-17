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
    "베인뚜": Unit("베인뚜", attackMode='True', plan='h', level='M'),
    "보리성": Unit("보리성", buffIndex=4, plan='h', level='M'),
    "보리빵떡": Unit("보리빵떡", plan='k', level='M'),
    "지짱보": Unit("지짱보", plan='r', level='M'),
    "강한보리": Unit("강한보리", plan='r', level='M'),
    "보리뚜": Unit("보리뚜", plan='s', level='M'),
    "보리세이더": Unit("보리세이더", plan='s', level='M'),
    "보리뚜뚜": Unit("보리뚜뚜", attackMode=False, plan='s', level='M'),
    "보리템플러": Unit("보리템플러", attackMode=False, plan='s', level='E'),
    "인챈뚜": Unit("인챈뚜", attackMode=False, plan='s', level='E'),
    "무녀뚜": Unit("무녀뚜", attackMode=False, plan='s', level='E'),
    "소울뚜": Unit("소울뚜", attackMode=False, plan='s', level='E'),
    "보리치료사": Unit("보리치료사", attackMode=False, plan='s', level='E'),
    "런처꾸꾸": Unit("런처꾸꾸", attackMode=False, plan='d', level='E'),
    "보리꾸꾸": Unit("보리꾸꾸", attackMode=False, plan='d', level='E'),
    "웨펀꾸꾸": Unit("웨펀꾸꾸", attackMode=False, plan='d', level='E'),
    "블레이뚜": Unit("블레이뚜", attackMode=False, plan='d', level='E'),
    "불보리뚜": Unit("불보리뚜", attackMode=False, plan='d', level='E'),
    "맥보리": Unit("맥보리", attackMode=False, plan='d', level='E'),
    "건꾸꾸": Unit("건꾸꾸", attackMode=False, plan='d', level='E'),
    "보리핏": Unit("보리핏", attackMode=False, plan='d', level='E'),
    "보리뚜킥": Unit("보리뚜킥", attackMode=False, plan='d', level='E'),
    "보리술사": Unit("보리술사", attackMode=False, plan='d', level='E'),
    "보리파": Unit("보리파", attackMode=False, plan='d', level='E'),
    "보리심판관": Unit("보리심판관", attackMode=False, plan='d', level='E'),
    "보리뚜비": Unit("보리뚜비", attackMode=False, plan='d', level='E'),
    "보리메이지": Unit("보리메이지", attackMode=False, plan='d', level='E'),
    "서큐버뚜": Unit("서큐버뚜", attackMode=False, plan='d', level='E'),
    "보리커": Unit("보리커", attackMode=False, plan='d', level='E'),
    "윈드꾸꾸": Unit("윈드꾸꾸", attackMode=False, plan='d', level='E'),
    "보리뱅": Unit("보리뱅", attackMode=False, plan='d', level='E'),
    "보리닉": Unit("보리닉", attackMode=False, plan='d', level='E'),
    "보리왕": Unit("보리왕", attackMode=False, plan='d', level='E'),
    "보리샷": Unit("보리샷", attackMode=False, plan='d', level='N'),
}

maxLoop=10
def after(char):
    # action.우편함()

    time.sleep(2)
    do(Clicker('인벤토리', threshold=0.70))
    do(Clicker('장비수리'))
    do(Clicker('장비수리확인'), onlyOneTime=True)
    time.sleep(1)
    do(Clicker('x', threshold=0.83))

    # 판매
    do(Clicker('판매'))
    do(Clicker('판매노말해제'), onlyOneTime=True)
    # do(Clicker('판매에픽해제'), onlyOneTime=True)
    # do(Clicker('판매유니크해제'), onlyOneTime=True)
    do(Clicker('판매2'))
    if(do(Founder('알림', threshold=0.76), onlyOneTime=True, okSkip=True)):
        do(Clicker('알림취소', threshold=0.86))
    do(Clicker('확인', 0.81), onlyOneTime=True, okSkip=True)
    time.sleep(1)
    do(Clicker('x', threshold=0.83), fallbackSkip=True)

    do(Clicker('해체', threshold=0.85))
    do(Clicker('판매노말선택'), onlyOneTime=True)
    do(Clicker('해체에픽해제'), onlyOneTime=True)
    do(Clicker('해체2', 0.83))
    do(Clicker('확인', 0.81), onlyOneTime=True, okSkip=True)
    do(Clicker('x', threshold=0.83))

    # 금고보관
    do(Clicker('금고', 0.81))
    do(Clicker('모험단금고'))
    do(Clicker('자동보관'))
    do(Clicker('확인', 0.81), onlyOneTime=True)
    do(Clicker('뒤로가기'))

def zupzup(direction) :
    pyautogui.keyDown('x')
    time.sleep(2)
    pyautogui.keyUp('x')
    pyautogui.keyDown(direction)
    # pyautogui.keyDown('right')
    time.sleep(0.5)
    pyautogui.keyUp(direction)
    # pyautogui.keyUp('right')
    pyautogui.keyDown('x')
    time.sleep(2)
    pyautogui.keyUp('x')

def z():
    """제국 던전 입장 시퀀스"""
    do(Clicker('모험'))
    time.sleep(2)
    do(Clicker('비밀작전', threshold=0.88))
    do(Clicker('비밀작전입장', threshold=0.85))
    
    secret_mission_found = False
    max_attempts = 10
    
    do(Founder('모험', threshold=0.85))

    for attempt in range(max_attempts):
        do(Direct(1860, 772))
        time.sleep(3)
        if do(Founder('비밀작전', threshold=0.85), onlyOneTime=True):
            secret_mission_found = True
            break
    if not secret_mission_found:
        return False

    do(Clicker('비밀작전', threshold=0.85))
    do(Direct(1570, 546)) # 비하이브
    do(Clicker('z4'))
    do(Clicker('비하이브2_입장'))
    time.sleep(3)
    if(do(Founder('비하이브2_입장'), onlyOneTime=True)):
        return False
    return True

def h(char):
    do(Clicker('모험'))
    do(Clicker('의뢰'))
    do(Clicker('의뢰지옥'))
    do(Clicker('의뢰지옥2'), canSkip=True)
    do(Clicker('의뢰지옥입장'))

def d(char):
    """일반던전 입장 시퀀스"""
    do(Clicker('모험'))

    do(Clicker('의뢰'))
    do(Clicker('의뢰파밍'))
    do(Clicker('의뢰파밍샐러'))
    do(Clicker('의뢰파밍샐러화로'))

    select_difficulty(char)
    do(Clicker('일던입장', threshold=0.85))
    return True

def k(char):
    """일반던전 입장 시퀀스"""
    do(Clicker('모험'))

    do(Clicker('의뢰'))
    do(Clicker('의뢰파밍'))
    do(Clicker('의뢰king'))
    do(Founder('의뢰kingcheck'))

    select_difficulty(char)
    do(Clicker('일던입장', threshold=0.85))
    return True

# giant / dart ssoja
def r(char):
    """일반던전 입장 시퀀스"""
    do(Clicker('모험'))

    do(Clicker('의뢰'))
    do(Clicker('의뢰파밍'))
    do(Clicker('의뢰ruke'))
    do(Founder('의뢰kingcheck'))

    select_difficulty(char)
    do(Clicker('일던입장', threshold=0.85))
    return True

def s(char):
    """일반던전 입장 - Support 시퀀스"""
    do(Clicker('모험'))

    do(Clicker('의뢰'))
    do(Clicker('의뢰파밍'))
    do(Clicker('의뢰파밍강철'))
    do(Clicker('의뢰파밍강철체크'))

    select_difficulty(char)
    do(Clicker('일던입장', threshold=0.85))
    return True

def select_difficulty(char):
    """난이도 선택 시퀀스"""
    do(Direct(1700, 737), delay=1)
    do(Direct(1700, 737), delay=1)
    do(Direct(1700, 737), delay=1)
    if char.level == 'E':
        do(Direct(1886, 735), delay=1)
    elif char.level == 'M':
        do(Direct(1886, 735), delay=1)
        do(Direct(1886, 735), delay=1)

def detect_boss(char, findBoss):
    """보스 감지 및 보스 스킬 사용"""
    if findBoss:
        return findBoss
    
    # plan에 따른 보스 감지 이미지 분기
    if char.plan == 'b':
        boss_image = '비하이브2_보스'
    elif char.plan == 'z':
        boss_image = 'z4boss'
    elif char.plan == 's':
        boss_image = 's4boss'
    elif char.plan == 'd':
        boss_image = 'd4boss'
    elif char.plan == 'k':
        boss_image = 'k4boss'
    elif char.plan == 'r':
        boss_image = 'r4boss'
    else:
        boss_image = '글라보스'
    
    if do(Founder(boss_image, threshold=0.95), onlyOneTime=True):
        do(Presser(str(char.finalIndex)))
        do(Presser(str(5)))
        return True
    
    return False

def skill_combo(findBoss=False, char=None):
    """스킬 콤보 함수 - 여러 스킬키를 순차적으로 누름"""
    # 보스를 찾았으면 보스 스킬 사용
    if findBoss is True and char is not None:
        keyboard2.pressKey2('5')
        keyboard2.pressKey2(char.finalIndex)
    
    keyboard2.pressKey2('r')
    keyboard2.pressKey2('s')
    keyboard2.pressKey2('d')
    keyboard2.pressKey2('f')
    keyboard2.pressKey2('g')
    keyboard2.pressKey2('t')
    keyboard2.pressKey2('b')
    keyboard2.pressKey2('v')
    keyboard2.pressKey2('e')
    keyboard2.pressKey2('w')
    keyboard2.pressKey2('q')

def handle_dungeon_clear_with_retry(loop, max_retry_attempts=10):
    """던전 클리어 후 재도전 로직을 최대 5번 시도"""
    do(Clicker('비작확인'), canSkip=True)
    
    for attempt in range(max_retry_attempts):
        dun_print.printf(f'재도전 시도 {attempt + 1}/{max_retry_attempts}')
        zupzup('right')
        zupzup('left')
        
        do(Clicker('던전재도전하기', threshold=0.85), onlyOneTime=True, canSkip=True)
        time.sleep(2) 
        if(do(Founder('피로도가부족합니다'), onlyOneTime=True, canSkip=True)):
            do(Clicker('마을로가기', threshold=0.90))
            time.sleep(4) 
            if(do(Founder('마을로가기', threshold=0.90), onlyOneTime=True) == False ):
                return True

        if(do(Clicker('던전재도전하기', threshold=0.85), onlyOneTime=True, canSkip=True) == False):
            return False 

    # 모든 시도 실패 시 마을로 가기
    dun_print.printf('모든 재도전 시도 실패, 마을로 이동')
    do(Clicker('마을로가기', threshold=0.85))
    return True

def login():
    if do(Founder('gamestart'), canSkip=True, onlyOneTime=True) :
        do(Direct(1598, 439))
    if do(Clicker('gamestart'), canSkip=True, onlyOneTime=True) :
        time.sleep(20)
        if(do(Founder('main'))):
            do(Direct(1600, 615))
        do(Clicker('gamestart2'))
        do(Founder('스케쥴러'), customFallbackCount=80)

# login()

os.system('rm -rf imagesLog/*')
for key in map:
    unit.select(key)
    char = map[key]

    if(unit.selected.workingDone):
        continue

    if(len(map) != 1):
        try:
            action2.캐릭터선택2()
        except Exception as e:
            dun_print.errorf(f'캐릭터선택2 실패: {e}')
            login()
            action2.캐릭터선택2()
    if(do(Founder('피로도소모', threshold=0.80), onlyOneTime=True, canSkip=True) or 
       do(Founder('피로도소모2', threshold=0.83), onlyOneTime=True, canSkip=True) or
       do(Founder('피로도소모4', threshold=0.83), onlyOneTime=True, canSkip=True) or
       do(Founder('피로도소모5', threshold=0.89), onlyOneTime=True, canSkip=True) or
       do(Founder('피로도소모3', threshold=0.83), onlyOneTime=True, canSkip=True)):
        unit.workingDone()
        continue

    plan_function = globals().get(char.plan)
    if plan_function and callable(plan_function):
        result = plan_function(char)
        if result is False:
            error_message = f'{char.name} - plan {char.plan} 입장 실패'
            mailSender.sendMail("[DNF] 비밀작전 ", error_message)
            unit.workingDone()
            continue 
    else:
        mailSender.sendMail("[DNF] 비밀작전 - 알수없는 플렌")
        sys.exit(1)

    endLoop = False
    loop = 0
    while True:
        loop = loop+1
        if(endLoop is True):
            break
        do(Founder('입장완료'))

        # 사냥
        action2.캐릭터버프(char)

        forLoop = 0
        findBoss = False
        # infinite loop
        while True:
            forLoop += 1
            # loop 3 times
            attackLoop = 2
            if findBoss:
                attackLoop = 2
            findBoss = detect_boss(char, findBoss) 
            for i in range(attackLoop):
                pyautogui.keyDown('x')
                if (findBoss):
                    keyboard2.pressKey2('5')
                    keyboard2.pressKey2(char.finalIndex)
                    time.sleep(1.0)
                else:
                    time.sleep(2)
                # attackMode에 따른 공격 방식 분기
                if char.attackMode is False: 
                    pyautogui.keyUp('x')
                    skill_combo(findBoss, char)
                    pyautogui.keyDown('x')
                
                if (forLoop > 30):
                    pyautogui.keyUp('x')

            pyautogui.keyUp('x')

            screenShot = image_finder.getScreenShotToGray()
            pyautogui.keyDown('x')

            if(do(Founder('비작리워드'), screenShot=screenShot, onlyOneTime=True)):
                do(Clicker('비작리워드클릭'), canSkip=True)

            if(do(Founder('던전재도전하기', threshold=0.91), screenShot=screenShot, onlyOneTime=True) or 
               do(Founder('비작클리어'), screenShot=screenShot, onlyOneTime=True) 
            ):
                if handle_dungeon_clear_with_retry(loop):
                    endLoop = True
                    break
                break 

            if(char.plan=='h'):
                if(do(Founder('지옥완료'), screenShot=screenShot, onlyOneTime=True)==True and 
                   do(Founder('던전재도전하기'), onlyOneTime=True)==False) :
                    do(Clicker('마을로가기', threshold=0.90))
                    endLoop = True
                    break
                

            pyautogui.keyDown('x')
            # if (forLoop % 5 == 0):
            if(do(Clicker('부활', screenShot=screenShot, threshold=0.75), onlyOneTime=True)):
                time.sleep(1)
                skill_combo(findBoss, char)
                skill_combo(findBoss, char)
                skill_combo(findBoss, char)
                skill_combo(findBoss, char)
                pyautogui.keyUp('x') 
                pyautogui.keyDown('x') 
                mailSender.sendMail("[DNF] die " + char.name, "-")

            if (forLoop > 120):
                dun_print.errorf(char.name + "던전 실패")
                break
    
    if(char.plan == 'h'):
        do(Presser('esc'))

    after(char)
    
    # workingDone 설정 - 작업 완료 표시
    unit.workingDone()
    dun_print.printf(f'{char.name} - 작업 완료!')
    
    # 마무리
    # do(Clicker('뒤로가기'))
    # do(Clicker('나가기'))
    # do(Clicker('확인'), okSkip=True)

mailSender.sendMail("[DNF] 비밀작전 완료" , "-")


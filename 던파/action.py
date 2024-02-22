import sys
sys.path.append('tobe')
from image_robot import * 
import image_finder

from unit import Unit
import pyautogui
import imageFinder
import imageFinderBulk
import threading
import time
import random
import keyboard2
import robot 
import unit
from datetime import datetime
from robot import printf

def uprint(unit: Unit, msg: str):
    # print with unit name f-string
    print(f'[{unit.name}] {msg}')

char=Unit("보리파")

def waitToHome():
    imageFinder.wait('스케쥴러', maxWait=7, error=True, threshold=0.97)

def waitToHomeWithKey(key):
    imageFinder.pressAndWait(key, '스케쥴러', maxWait=7, error=True, threshold=0.95)
    # imageFinder.wait('스케쥴러', maxWait=7, error=True, threshold=0.97)

def 일최초시작(hhmm: str):
    # split hhmm to hh and mm
    hh = int(hhmm[0:2])
    mm = int(hhmm[2:4])

    # start on every 06:00 AM
    while True:
        now = datetime.now()
        if now.hour == hh and now.minute >= mm:
            break
        print('sleep...')
        time.sleep(60)

    imageFinder.findAndClick('일최초캐선_오늘그만보기', error=False)
    imageFinder.waitAndClick('일최초게임시작', error=False)
    imageFinder.clickDirect(1870, 476)
    # imageFinder.waitAndClick('일최초팝업', error=False)

def 장비해체():
    imageFinder.waitAndClick('장비해체')
    imageFinder.waitAndClick('장비해체클릭', maxWait=2, error=False)
    imageFinder.waitAndClick('확인', maxWait=2, error=False)
    imageFinder.waitAndClick('확인', maxWait=2, error=False)
    robot.pressKey('ESC')

def 장비해체2():
    do(Clicker('장비해체'), fallbackSkip=True)
    if(do(Clicker('장비해체클릭'), canSkip=True)):
        do(Clicker('확인'), canSkip=True)
    do(Presser('ESC', fallbackSkip=True))

def 수리및보관():
    pyautogui.sleep(2)
    robot.pressKey('i')
    imageFinder.waitAndClick('장비수리')
    imageFinder.waitAndClick('장비수리확인',maxWait=3, error=False)
    robot.pressKey('ESC', sleep=8)
    time.sleep(1)
    robot.pressKey('ESC', sleep=8)

    # # 해체
    # 장비해체()

    # # 판매
    # imageFinder.waitAndClick('판매')
    # for i in range(2):
    #     imageFinder.findAndClick('판매확인', sleep=1, error=False)
    #     imageFinder.findAndClick('확인', sleep=1, threshold=0.91, error=False)
    #     imageFinder.findAndClick('확인', sleep=1, threshold=0.91, error=False)
    # robot.pressKey('ESC', sleep=4)

    # # 보관
    # imageFinder.waitAndClick('금고')
    # imageFinder.waitAndClick('모험단금고')
    # imageFinder.waitAndClick('자동보관')
    # imageFinder.waitAndClick('확인', threshold=0.91, error=False)
    # # robot.pressKey('ESC')
    # # pyautogui.sleep(2)
    # waitToHomeWithKey('ESC')

def 수리및보관2():
    do(Presser('i', fallbackSkip=True))
    do(Clicker('장비수리'))
    do(Clicker('장비수리확인'), canSkip=True)
    do(Presser('ESC'))

    # 해체
    장비해체2()

    # 판매
    do(Clicker('판매'))
    for i in range(2):
        if(do(Clicker('판매확인'), canSkip=True)):
            do(Clicker('확인'), canSkip=True)
    do(Presser('ESC'))

    # 보관
    do(Clicker('금고'))
    do(Clicker('모험단금고'))
    do(Clicker('자동보관'))
    do(Clicker('확인'), canSkip=True)
    do(Presser('ESC'))
    # waitToHomeWithKey('ESC')

# 수리및보관2()

def 길드활동(char: Unit):
    # 길드 출석
    robot.pressKey(';')
    imageFinder.waitAndClick('길드기부', maxWait=3, error=False)
    imageFinder.waitAndClick('길드기부_상자클릭', maxWait=3, error=False)
    imageFinder.waitAndClick('x', maxWait=3, error=False)
    # robot.pressKey('ESC')
    waitToHomeWithKey('ESC')

def 캐릭터선택(char:Unit):
    imageFinder.waitAndClick('캐릭_선택', threshold=0.97)
    # imageFinder.waitAndClick('캐릭_보리뚜')

    imageFinder.clickDirect(1352, 522)

    pyautogui.sleep(1)
    for i in range(100):
        if(imageFinder.isFound('캐릭_' + char.name, threshold=0.86, sleep=0) != None):
            imageFinder.findAndClick('캐릭_' + char.name, threshold=0.86, sleep=0, error=False)
            break
        pyautogui.scroll(30000)
        # pyautogui.scroll(-25000)
        # pyautogui.scroll(-10000)
        pyautogui.sleep(0.5)
    pyautogui.sleep(1)
    imageFinder.waitAndClick('캐릭_게임시작')
    # waitToHome()
    # FIXME 아래 두개가 더 필요할수도 있음 (상황나오면 그때 확인해보자)
    pyautogui.sleep(2)
    # imageFinder.findAndClick('확인', error=False)

    # loop until found image
    i = 0
    maxWait = 15
    while True:
        i += 1 
        imageFinder.findAndClick('확인', error=False, printLog=False, sleep=0.1)
        pt = imageFinder.isFound('스케쥴러', threshold = 0.92, sleep=0.5, printLog=False)
        if (pt != None or i > maxWait * 2):
            break
    if(pt == None):
        imageFinder.errorf('스케쥴러 이미지를 찾을 수 없습니다. (캐릭터 선택)')
    
    pyautogui.sleep(3)

# action(Clicker('캐릭_소울뚜', threshold=0.70), onlyOneTime=True) 
# Clicker('캐릭_소울뚜', threshold=0.82).action(printFail=True) 

def 캐릭터선택2():
    imgPathBackup = image_finder.imgPath
    image_finder.imgPath = 'Images/'

    char = unit.selected

    do(Clicker('캐릭_선택', threshold=0.94))
    time.sleep(3)
    do(Founder('캐릭_선택확인'))
    imageFinder.clickDirect(1352, 522)
    # pyautogui.sleep(1)
    for i in range(100):
        # if imageFinder.findAndClick('캐릭_' + char.name, threshold=0.86, sleep=0, error=False) :
        # if action(Clicker('캐릭_' + char.name, threshold=0.82), onlyOneTime=True) :
        if Clicker('캐릭_' + char.name, threshold=0.75).action(printFail=True) :
            break
        pyautogui.sleep(0.5)
        pyautogui.scroll(70000)
        # pyautogui.scroll(40000)
        # pyautogui.scroll(-25000)
        # pyautogui.scroll(-10000)
    
    if(do(Founder('게임시작_이미접속중', threshold=0.77), onlyOneTime=True, canSkip=True)):
        keyboard2.pressKey('ESC')
    else:
        do(Clicker('캐릭_게임시작', threshold=0.80))
        pyautogui.sleep(1)

    do(Founder('스케쥴러'))

    image_finder.imgPath = imgPathBackup

def 산등최초입장():
    imageFinder.waitAndClick('입장_최초맵선택', threshold=0.97)
    imageFinder.waitAndClick('입장_설산')
    imageFinder.waitAndClick('모험난이도', threshold=0.9, maxWait=15)
    imageFinder.waitAndClick('산등성이')
    imageFinder.waitAndClick('전투시작', threshold=0.9, maxWait=20)

def 산등최초입장2():
    do(Clicker('입장_최초맵선택'))
    do(Clicker('입장_설산'))
    do(Clicker('모험난이도'))
    do(Clicker('산등성이', threshold=0.97))
    do(Clicker('전투시작'))

def 산등지옥재도전(): 
    pyautogui.press("ESC")
    imageFinder.waitAndClick('재도전확인')
    #imageFinder.waitAndClick('확인', threshold=0.9)
    robot.pressKey('left', duration=4)
    robot.pressKey('left', duration=4)
    imageFinder.waitAndClick('모험난이도', threshold=0.9)
    imageFinder.waitAndClick('산등성이')
    imageFinder.waitAndClick('전투시작', threshold=0.9)

# def 산등지옥재도전2(): 
#     action(Presser('ESC'))
#     time.sleep(1)
#     action(Clicker('재도전확인'))
#     action(Presser('left'))
#     action(Clicker('모험난이도'))
#     action(Clicker('산등성이', threshold=0.99))
#     action(Clicker('전투시작'))

# 산등지옥재도전2()

def 산등노가다(char:Unit):

    loopCount = char.loopCount
    print(loopCount)
    if(loopCount == 0):
        return

    j = char.loop
    while(True):
    # for j in range(loopCount):
        j+=1
        uprint(char, "산등 노가다 진행중 : " + str(j) + "/" + str(loopCount))
        pyautogui.sleep(2)
        imageFinder.waitAndClick('산등맵', threshold= 0.97, delay=0.8)
        robot.pressKey(str(char.buffIndex), sleep=0.2)

        if(imageFinder.isFound('지옥파티', sleep=0.2) != None): 
            j-=1
            if(j == loopCount):
                pyautogui.press("ESC")
                imageFinder.waitAndClick('재도전확인')
                return
            산등지옥재도전()
            continue

        unit.loopDone()

        findClock=False
        for i in range(200):
            # uprint(char, f'{i} ({j}/{loopCount-1})')
            printf('산등재도전중', f'{i}', f'{j}/{loopCount}', '')

            # if multip 30
            if(i%45 == 0 and i != 0):

                switcher = {
                    0: 'right',
                    1: 'left',
                    2: 'up',
                }
                # random move with switcher
                robot.pressKey(switcher.get(random.randint(0,2)), duration=2)
                imageFinder.findAndClick('부활', 1, 0.75, error=False)

            pyautogui.sleep(0.01)
            pyautogui.keyDown('x')
            pyautogui.sleep(3)
            imageFinder.findAndClick('산등_골카', sleep=0, error=False, printLog=False)
            if(imageFinder.isFound('재도전', threshold=0.6, printLog=False) != None):
                pyautogui.sleep(2.5)
                pyautogui.keyUp('x')
                if(imageFinder.isFound('재도전_초과', threshold=0.97) != None):
                    imageFinder.waitAndClick('재도전_초과')
                    imageFinder.waitAndClick('판매')
                    imageFinder.waitAndClick('판매확인', maxWait=10, error=False)
                    imageFinder.waitAndClick('확인', maxWait=3, threshold=0.91, error=False)
                    imageFinder.waitAndClick('확인', maxWait=3, threshold=0.91, error=False)
                    robot.pressKey('ESC', sleep=4)
                    robot.pressKey('ESC', sleep=4)
                if(imageFinder.isFound('재도전_수리', threshold=0.75) != None):
                    imageFinder.waitAndClick('재도전_수리', threshold=0.7)
                    imageFinder.waitAndClick('장비수리확인', maxWait=3, error=False)
                    robot.pressKey('ESC', sleep=4)
                break

            pyautogui.keyUp('x')

        pyautogui.sleep(3)
        if(j == loopCount):
            robot.pressKey('F8', sleep=2)
            imageFinder.findAndClick('확인', error=False)
            pyautogui.sleep(4)
            return
        if(i == 199):
            robot.pressKey('ESC', sleep=4)
            robot.pressKey('ESC', sleep=4)
            return
        robot.pressKey('F6')
        if(imageFinder.isFound('피로도부족', sleep=4) != None):
            break 
    imageFinder.waitAndClick('확인')
    # robot.pressKey('F8', sleep=4)
    waitToHomeWithKey('F8')

def 산등노가다2():
    char = unit.selected
    loopCount = char.loopCount
    print(loopCount)
    if(loopCount == 0):
        return

    j = char.loop
    while(True):
        j+=1
        uprint(char, "산등 노가다 진행중 : " + str(j) + "/" + str(loopCount))
        do(Founder('산등', threshold=0.93))
        robot.pressKey(str(char.buffIndex), sleep=0.1, duration=0.1)
        do(Direct(1887, 467))
        #time.sleep(0.15)
        bossFounder=Founder('맵_보스')
        do(bossFounder)
        # time.sleep(0.2)
        pyautogui.keyUp('x')
        time.sleep(0.1)
        pyautogui.keyDown('x')

        if(Founder('지옥파티', screenShot=bossFounder.screenShot).action()): 
            pyautogui.keyUp('x')
            j-=1
            if(j == loopCount):
                pyautogui.press("ESC")
                imageFinder.waitAndClick('재도전확인')
                return
            산등지옥재도전()
            continue

        unit.loopDone()
        useFinalSkill = False
        findGoldCard = False

        for i in range(550):
            printf('산등재도전중', f'{i}', f'{j}/{loopCount}', '')
            screenShot = image_finder.getScreenShotToGray("loop")

            if(i%45 == 0 and i != 0):
                switcher = {
                    0: 'right',
                    1: 'left',
                    2: 'up',
                }
                robot.pressKey(switcher.get(random.randint(0,2)), duration=0.5)
                Clicker('부활', screenShot=screenShot, threshold=0.75).action()
                pyautogui.keyUp('x')
                time.sleep(0.1)
                pyautogui.keyDown('x')

            if(findGoldCard == False and Clicker('산등_골카', screenShot=screenShot).action()):
                time.sleep(0.5)
                Presser('1').action()
                Clicker('산등_결과', screenShot=screenShot, threshold=0.985).action()
                Clicker('산등_결과', screenShot=screenShot, threshold=0.985).action()
                findGoldCard=True

            if (Founder('down', screenShot=screenShot).action()):
                time.sleep(1)
                pyautogui.keyUp('x')
                time.sleep(0.1)
                pyautogui.keyDown('x')

            if (Founder('down_stand', screenShot=screenShot, threshold=0.85).action()):
                time.sleep(1)
                pyautogui.keyUp('x')
                time.sleep(0.1)
                pyautogui.keyDown('x')

            # pyautogui.sleep(0.05)
            # if(useFinalSkill is False and action(Clicker('BOSS', screenShot=screenShot), onlyOneTime=True)):
            #     robot.pressKey(char.finalIndex)
            #     useFinalSkill = True

            if(Founder('재도전', screenShot=screenShot, threshold=0.75).action()):

                robot.pressKey('right', duration=0.05, sleep=0)
                pyautogui.keyUp('x')
                time.sleep(0.1)
                pyautogui.keyDown('x')
                time.sleep(3.5)
                pyautogui.keyUp('x')

                if(do(Clicker('재도전_수리', screenShot=screenShot, threshold=0.75), onlyOneTime=True)):
                    imageFinder.waitAndClick('장비수리확인', maxWait=3, error=False)
                    robot.pressKey('ESC', sleep=4)

                if(do(Clicker('재도전_초과', screenShot=screenShot, threshold=0.93), onlyOneTime=True)):
                    do(Clicker('판매'))
                    imageFinder.waitAndClick('판매확인', maxWait=10, error=False)
                    imageFinder.waitAndClick('확인', maxWait=3, threshold=0.91, error=False)
                    imageFinder.waitAndClick('확인', maxWait=3, threshold=0.91, error=False)
                    robot.pressKey('ESC', sleep=4)
                    robot.pressKey('ESC', sleep=4)
                break

        pyautogui.keyUp('x')
        if(j == loopCount):
            robot.pressKey('F8', sleep=2)
            imageFinder.findAndClick('확인', error=False)
            pyautogui.sleep(4)
            return
        if(i == 450):
            robot.pressKey('ESC', sleep=4)
            robot.pressKey('ESC', sleep=4)
            return

        robot.pressKey('F6')
        if(do(Founder('피로도부족'), canSkip=True)):
            pyautogui.keyUp('x')
            waitToHomeWithKey('F8')
            break 

# unit.select(char.name)
# 산등노가다2()

def 우편함():
    do(Clicker('우편함'))
    do(Clicker('우편함_일괄수령'), canSkip=True)
    do(Clicker('확인'), onlyOneTime=True, canSkip=True)
    do(Clicker('뒤로가기'))

def 즐찾구매():
    # # 즐찾상점
    # robot.pressKey('s', sleep=4)
    # imageFinder.findAndClick('구매하기_오늘그만보기', error=False)   
    # imageFinder.waitAndClick('상점_관심상품')
    # imageFinder.waitAndClick('구매하기', maxWait=3, threshold=0.91, error= False)
    # imageFinder.waitAndClick('확인', maxWait=3, threshold=0.91, error=False)
    # imageFinder.waitAndClick('확인', maxWait=2, threshold=0.91, error=False)
    # # robot.pressKey('ESC', sleep=8)
    # # robot.pressKey('ESC')
    # # waitToHome()
    # # imageFinder.pressAndWait('ESC', '스케쥴러')
    # waitToHomeWithKey('ESC')
    do(Clicker('상점', threshold=0.78))
    do(Clicker('상점_상점'))

    # 자질구리한 팝업 스킵
    screenshot = image_finder.getScreenShotToGray()
    Clicker('구매하기_오늘그만보기', screenShot=screenshot).action(printFail=True)

    do(Clicker('상점_관심상품'), canSkip=True)
    if do(Clicker('구매하기')):
        do(Clicker('확인'), canSkip=True)
    do(Clicker('뒤로가기'))
    do(Founder('스케쥴러'))

def 신비상점구매2():
    do(Clicker('상점', threshold=0.78))
    do(Clicker('상점_신비'))
    # action(Clicker('신비상점입장'))

    pyautogui.sleep(4) 
    buyList = []
    # buyList.append('상점_신비천')
    # buyList.append('상점_신비뼈')
    # buyList.append('상점_신비철')
    # buyList.append('상점_신비')
    # buyList.append('상점_신비연석')
    # buyList.append('상점_신비가죽')
    buyList.append('상점_열쇠')
    # buyList.append('상점_신비라코')
    buyList.append('상점_신비라코2')
    buyList.append('상점_신비원소')
    buyList.append('상점_신비경화제')
    buyList.append('상점_신비다이야')

    if(unit.selected.신비전체구매 == True):
        buyList.append('상점_신비칼박')
        buyList.append('상점_신비칼박2')
        buyList.append('상점_신비칼박3')
    # else:
        # buyList.append('상점_신비테라')
        # buyList.append('상점_신비테라2')
    
    imageFinderBulk.findAndClick('신비로그_' + char.name, buyList)

    if do(Clicker('구매하기', threshold=0.8), canSkip=True):
        do(Clicker('구입', threshold=0.8), canSkip=True)
        # action(Clicker('확인'))

    if do(Founder('신비상점_소지금액부족'), canSkip=True, onlyOneTime=True):
        do(Presser('ESC'))
        time.sleep(1)

    # if(Founder('신비_소지금액부족').action()):
        # action(Clicker('확인'))
        # action(Presser('ESC'))
    
    # time.sleep(2)
    do(Clicker('뒤로가기', threshold=0.98))
    # time.sleep(2)
    do(Founder('스케쥴러'))
    # time.sleep(2)

# 신비상점구매2()

def 신비상점구매(char:Unit):
    # 신비상점
    imageFinder.waitAndClick('상점')
    imageFinder.waitAndClick('상점_신비')

    imageFinder.wait('신비상점입장')
    pyautogui.sleep(3) 

    buyList = []
    buyList.append('상점_신비천')
    buyList.append('상점_신비뼈')
    buyList.append('상점_신비철')
    buyList.append('상점_신비')
    buyList.append('상점_신비연석')
    buyList.append('상점_신비라코')
    buyList.append('상점_신비가죽')
    buyList.append('상점_신비원소')
    buyList.append('상점_신비경화제')
    buyList.append('상점_신비다이야')

    if(char.신비전체구매 == True):
        buyList.append('상점_신비칼박')
    # else:
        # buyList.append('상점_신비테라')
        # buyList.append('상점_신비테라2')
    
    imageFinderBulk.findAndClick('신비로그_' + char.name, buyList)

    if(imageFinder.waitAndClick('구매하기', maxWait=2, threshold=0.85, error=False) == True) :
        imageFinder.waitAndClick('구입', maxWait=3, threshold=0.85, error=False)
        imageFinder.waitAndClick('확인', maxWait=3, threshold=0.91, error=False)

    if(imageFinder.isFound('신비_소지금액부족') != None):
        robot.pressKey('ESC')
    # robot.pressKey('ESC')
    waitToHomeWithKey('ESC')

def 서조(char:Unit):
    imageFinder.waitAndClick('스케쥴러')
    imageFinder.waitAndClick('서조의계곡3', threshold=0.75)
    imageFinder.waitAndClick('입장')
    for j in range(3):
        isBossFound = False
        # imageFinder_bk.waitAndClick('서조입장', threshold=0.95)
        for i in range(200):
            # print(i)
            imageFinder.findAndClick('확인', sleep=0, threshold=0.81, error=False)
            # when first i
            if(i == 0):
                keyboard2.pressKey(str(char.buffIndex), sleep=0, duration=0.2)

            if(i%30 == 0 and i != 0):
                # random move with seed
                random.seed(i)
                robot.pressKey('right', duration=2)
                imageFinder.findAndClick('부활', 1, 0.75, error=False)

            if(isBossFound == False and imageFinder.isFound('서조_보스', threshold=0.95, printLog=False) != None):
                # pyautogui.press(char.finalIndex)
                keyboard2.pressKey(char.finalIndex, sleep=0, duration=0.1)
                isBossFound = True

            # swtich case with random value
            switcher = {
                0: 'q',
                1: 'w',
                2: 'e',
                3: 'r',
            }
            keyboard2.pressKey(switcher.get(random.randint(0,3)), sleep=0, duration=0.1, printLog=False)

            pyautogui.keyDown('x')
            pyautogui.sleep(1.5)
            if(imageFinder.isFound('다른긴급의뢰선택', threshold=0.88, printLog=False) != None):
                pyautogui.keyUp('x')
                # for loop 3 times
                for i in range(4):
                    pyautogui.keyDown('x')
                    pyautogui.sleep(3)
                    pyautogui.keyUp('x')
                break
            pyautogui.keyUp('x')
        robot.pressKey('f6', sleep=2)

    robot.pressKey('f8', sleep=2)
    imageFinder.wait('스케쥴러입장')
    # robot.pressKey('esc')
    waitToHomeWithKey('ESC')

def 서조2():
    char = unit.selected
    do(Clicker('스케쥴러'))
    do(Clicker('서조의계곡3', threshold=0.75))
    do(Clicker('입장', threshold=0.85))
    do(Founder('서조입장확인'))

    for j in range(3):
        isBossFound = False
        for i in range(200):
            # when first i
            if(i == 0):
                do(Presser(str(char.buffIndex)))
                # keyboard2.pressKey(str(char.buffIndex), sleep=0, duration=0.2)

            if(i%30 == 0 and i != 0):
                # random move with seed
                random.seed(i)
                robot.pressKey('right', duration=2)
                imageFinder.findAndClick('부활', 1, 0.75, error=False)

            if(isBossFound == False and imageFinder.isFound('서조_보스', threshold=0.95, printLog=False) != None):
                # pyautogui.press(char.finalIndex)
                keyboard2.pressKey(char.finalIndex, sleep=0, duration=0.1)
                isBossFound = True

            # swtich case with random value
            switcher = {
                0: 'q',
                1: 'w',
                2: 'e',
                3: 'r',
            }
            keyboard2.pressKey(switcher.get(random.randint(0,3)), sleep=0, duration=0.1, printLog=False)

            pyautogui.keyDown('x')
            pyautogui.sleep(1.5)
            if(imageFinder.isFound('다른긴급의뢰선택', threshold=0.88, printLog=False) != None):
                pyautogui.keyUp('x')
                # for loop 3 times
                for i in range(4):
                    pyautogui.keyDown('x')
                    pyautogui.sleep(3)
                    pyautogui.keyUp('x')
                break
            pyautogui.keyUp('x')
        robot.pressKey('f6', sleep=2)

    robot.pressKey('f8', sleep=2)
    imageFinder.wait('스케쥴러입장')
    # robot.pressKey('esc')
    waitToHomeWithKey('ESC')

def 아티팩트판매():
    imageFinder.pressAndWaitAndClick('ESC', '크리처')
    imageFinder.waitAndClick('크리처_아티팩트')
    imageFinder.waitAndClick('장비해체', maxWait=3, error=False)
    imageFinder.waitAndClick('크리처_장비해체클릭', maxWait=3, error=False)
    if(imageFinder.isFound('확인', sleep=4) != None):
        imageFinder.waitAndClick('확인', maxWait=3, error=False)
        imageFinder.waitAndClick('확인', maxWait=3, error=False)
    robot.pressKey('ESC') 
    # robot.pressKey('ESC', sleep=5) # 최초분해 따아앙뜨는거 5초
    # robot.pressKey('ESC') # 최초분해 따아앙뜨는거 5초 안기다려도 가짐
    waitToHomeWithKey('ESC')

# 크리처()
# sampleUnit = Unit("보리핏", 3, 'w', False)
# 신비상점구매(sampleUnit)
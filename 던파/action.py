from unit import Unit
import pyautogui
import robot
import imageFinder
import threading


def 장비해체():
    imageFinder.waitAndClick('장비해체')
    imageFinder.waitAndClick('장비해체클릭', maxWait=2, error=False)
    imageFinder.waitAndClick('확인', maxWait=2, error=False)
    imageFinder.waitAndClick('확인', maxWait=2, error=False)
    robot.pressKey('ESC')

def 수리및보관():
    # 수리
    robot.pressKey('i')
    imageFinder.waitAndClick('장비수리')
    imageFinder.waitAndClick('장비수리확인',maxWait=3, error=False)
    robot.pressKey('ESC', sleep=8)

    # 해체
    장비해체()

    # 판매
    imageFinder.waitAndClick('판매')
    for i in range(3):
        imageFinder.findAndClick('판매확인', sleep=1, error=False)
        imageFinder.findAndClick('확인', sleep=1, threshold=0.91, error=False)
        imageFinder.findAndClick('확인', sleep=1, threshold=0.91, error=False)
    robot.pressKey('ESC', sleep=4)

    # 보관
    imageFinder.waitAndClick('금고')
    imageFinder.waitAndClick('모험단금고')
    imageFinder.waitAndClick('자동보관')
    imageFinder.waitAndClick('확인', threshold=0.91)
    robot.pressKey('ESC')

def 길드활동(char: Unit):
    # 길드 출석
    robot.pressKey(';')
    if(char.길드기부):
        imageFinder.waitAndClick('길드기부', maxWait=3, error=False)
        imageFinder.waitAndClick('기부하기', maxWait=3, error=False)
        imageFinder.waitAndClick('확인', maxWait=3, error=False)
        imageFinder.waitAndClick('길드기부_상자클릭', maxWait=3, error=False)
        robot.pressKey('ESC')
        robot.pressKey('ESC')
    imageFinder.waitAndClick('길드출석', maxWait=3, error=False)
    imageFinder.waitAndClick('길드출석10000', maxWait=3, error=False)
    imageFinder.waitAndClick('확인', maxWait=3, error=False)
    imageFinder.waitAndClick('확인', maxWait=3, error=False)
    imageFinder.waitAndClick('길드출석상자', threshold=0.70, error=False)
    imageFinder.waitAndClick('확인', maxWait=3, error=False)
    #imageFinder.waitAndClick('확인', error=False)
    robot.pressKey('ESC', sleep=4)
    robot.pressKey('ESC', sleep=7)

def 친구포인트():
    robot.pressKey('l')
    imageFinder.waitAndClick('친구일괄보내기', error=False)
    imageFinder.waitAndClick('확인', error=False)
    imageFinder.waitAndClick('친구일괄받기', error=False)
    robot.pressKey('ESC')

def 캐릭터선택(char:Unit):
    imageFinder.waitAndClick('캐릭_선택')
    imageFinder.waitAndClick('캐릭_보리뚜')
    for i in range(100):
        if(imageFinder.isFound('캐릭_' + char.name, threshold=0.85, sleep=0) != None):
            imageFinder.findAndClick('캐릭_' + char.name, threshold=0.80, sleep=0, error=False)
            break
        pyautogui.scroll(-60000)
        pyautogui.sleep(0.2)
    pyautogui.sleep(2)
    imageFinder.waitAndClick('캐릭_게임시작')
    pyautogui.sleep(3)

def 산등최초입장():
    imageFinder.waitAndClick('확인', threshold=0.7, maxWait=5, error=False)
    imageFinder.waitAndClick('입장_최초맵선택', threshold=0.85)
    imageFinder.waitAndClick('입장_설산')
    imageFinder.waitAndClick('모험난이도', threshold=0.9, maxWait=15)
    imageFinder.waitAndClick('산등성이')
    imageFinder.waitAndClick('전투시작', threshold=0.9)

def 산등노가다(char:Unit):

    for j in range(40):
        imageFinder.waitAndClick('산등맵', threshold= 0.75, error=False)
        pyautogui.press(str(char.buffIndex))
        if(imageFinder.isFound('지옥파티', sleep=1) != None):
            산등지옥재도전()
            continue

        findClock=False
        for i in range(300):
            print(i)
            # if multip 30
            if(i%30 == 0 and i != 0):
                robot.pressKey('right', duration=2)
                imageFinder.findAndClick('부활', 1, 0.75, error=False)

            pyautogui.sleep(0.01)
            pyautogui.keyDown('x')
            pyautogui.sleep(3)
            if(imageFinder.isFound('재도전', threshold=0.6) != None):
                pyautogui.keyUp('x')
                pyautogui.keyDown('x')
                pyautogui.sleep(2)
                if(imageFinder.isFound('재도전_초과') != None):
                    imageFinder.waitAndClick('재도전_초과')
                    imageFinder.waitAndClick('판매')
                    imageFinder.waitAndClick('판매확인', maxWait=10, error=False)
                    imageFinder.waitAndClick('확인', maxWait=3, threshold=0.91, error=False)
                    imageFinder.waitAndClick('확인', maxWait=3, threshold=0.91, error=False)
                    robot.pressKey('ESC', sleep=4)
                    robot.pressKey('ESC', sleep=4)
                if(imageFinder.isFound('재도전_수리', threshold=0.7) != None):
                    imageFinder.waitAndClick('재도전_수리', threshold=0.7)
                    imageFinder.waitAndClick('장비수리확인', maxWait=3, error=False)
                    robot.pressKey('ESC', sleep=4)
                pyautogui.keyUp('x')
                break

            pyautogui.keyUp('x')

        pyautogui.sleep(3)
        pyautogui.press('F6')
        if(imageFinder.isFound('피로도부족', sleep=4) != None):
            break 
    imageFinder.waitAndClick('확인')
    robot.pressKey('F8', sleep=2)
    pyautogui.sleep(4)

def 산등지옥재도전(): 
    pyautogui.press("ESC")
    imageFinder.waitAndClick('재도전확인')
    robot.pressKey('left', 9)
    imageFinder.waitAndClick('모험난이도', threshold=0.9)
    imageFinder.waitAndClick('산등성이')
    imageFinder.waitAndClick('전투시작', threshold=0.9)

def 즐찾구매():
    # 즐찾상점
    robot.pressKey('s', sleep=4)
    imageFinder.waitAndClick('상점_관심상품')
    imageFinder.waitAndClick('구매하기', maxWait=3, threshold=0.91, error= False)
    imageFinder.waitAndClick('확인', maxWait=3, threshold=0.91, error=False)
    imageFinder.waitAndClick('확인', maxWait=2, threshold=0.91, error=False)
    robot.pressKey('ESC', sleep=8)

def 신비상점구매(char:Unit):
    # 신비상점
    imageFinder.waitAndClick('상점')
    imageFinder.waitAndClick('상점_신비')
    # imageFinder.findAndClick('상점_신비천', threshold=0.95, error=False)
    imageFinder.findAndClick('상점_신비연석', sleep=3, threshold=0.95, error=False)
    imageFinder.findAndClick('상점_신비라코', sleep=0.5, threshold=0.95, error=False)
    imageFinder.findAndClick('상점_신비가죽', sleep=0.5, threshold=0.95, error=False)
    imageFinder.findAndClick('상점_신비뼈', sleep=0.5, threshold=0.95, error=False)
    imageFinder.findAndClick('상점_신비경화제', sleep=0.5, threshold=0.95, error=False)
    imageFinder.findAndClick('상점_신비원소', sleep=0.5, threshold=0.9, error=False)
    if(char.신비전체구매 == True):
        # imageFinder.findAndClick('상점_신비다이야', threshold=1, error=False)
        imageFinder.findAndClick('상점_신비칼박', sleep=0.5, threshold=0.95, error=False)
    imageFinder.waitAndClick('구매하기', maxWait=3, threshold=0.85, error=False)
    imageFinder.waitAndClick('구입', maxWait=3, threshold=0.85, error=False)
    imageFinder.waitAndClick('확인', maxWait=3, threshold=0.91, error=False)
    if(imageFinder.isFound('신비_소지금액부족') != None):
        robot.pressKey('ESC')
    robot.pressKey('ESC')

def 크리처_OLD():
    robot.pressKey('ESC', sleep=5)
    imageFinder.findAndClick('크리처')

    imageFinder.findAndClick('크리처_심부름')
    if(imageFinder.isFound('크리처_보상받기', sleep=4) != None):
        imageFinder.findAndClick('크리처_보상받기')
        imageFinder.findAndClick('확인')
    if(imageFinder.isFound('크리처_빠른심부름', sleep=7) != None):
        imageFinder.findAndClick('크리처_빠른심부름', sleep=0)
        imageFinder.findAndClick('크리처_자동배치')
        imageFinder.findAndClick('크리처_보내기')
        if(imageFinder.isFound('확인', sleep=4) == None):
            robot.pressKey('ESC')
        else:
            imageFinder.findAndClick('확인')
    robot.pressKey('ESC')

def 크리처():
    robot.pressKey('ESC')
    imageFinder.waitAndClick('크리처')
    imageFinder.waitAndClick('크리처_심부름')
    if(imageFinder.isFound('크리처_보상받기', sleep=4) != None):
        imageFinder.waitAndClick('크리처_보상받기')
        imageFinder.waitAndClick('확인')
    if(imageFinder.isFound('크리처_빠른심부름', sleep=7) != None):
        imageFinder.waitAndClick('크리처_빠른심부름')
        imageFinder.waitAndClick('크리처_자동배치')
        imageFinder.waitAndClick('크리처_보내기')
        if(imageFinder.isFound('확인', sleep=4) == None):
            robot.pressKey('ESC')
        else:
            imageFinder.waitAndClick('확인')
    robot.pressKey('ESC')


def 아티팩트판매():
    robot.pressKey('ESC')
    imageFinder.waitAndClick('크리처')
    imageFinder.waitAndClick('크리처_아티팩트')
    imageFinder.waitAndClick('장비해체', maxWait=3, error=False)
    imageFinder.waitAndClick('크리처_장비해체클릭', maxWait=3, error=False)
    if(imageFinder.isFound('확인', sleep=4) != None):
        imageFinder.waitAndClick('확인', maxWait=3, error=False)
        imageFinder.waitAndClick('확인', maxWait=3, error=False)
    robot.pressKey('ESC') 
    robot.pressKey('ESC', sleep=5) # 최초분해 따아앙뜨는거 5초

# 크리처()
# sampleUnit = Unit("보리핏", 3, 'w', False)
# 신비상점구매(sampleUnit)
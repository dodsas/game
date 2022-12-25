from unit import Unit
import pyautogui
import robot
import imageFinder
import threading


def 장비해체():
    imageFinder.findAndClick('장비해체')
    imageFinder.findAndClick('장비해체클릭', error=False)
    imageFinder.findAndClick('확인', error=False)
    imageFinder.findAndClick('확인', error=False)
    robot.pressKey('ESC')

def 수리및보관():
    # 수리
    robot.pressKey('i', sleep=4)
    imageFinder.findAndClick('장비수리')
    imageFinder.findAndClick('장비수리확인', error=False)
    robot.pressKey('ESC', sleep=4)
    pyautogui.sleep(6)
    # 해체
    장비해체()

    # 판매
    imageFinder.findAndClick('판매', sleep=10)
    for i in range(3):
        imageFinder.findAndClick('판매확인', error=False)
        imageFinder.findAndClick('확인', threshold=0.91, error=False)
        imageFinder.findAndClick('확인', threshold=0.91, error=False)
    robot.pressKey('ESC', sleep=4)

    # 보관
    imageFinder.findAndClick('금고', sleep=10)
    imageFinder.findAndClick('모험단금고')
    imageFinder.findAndClick('자동보관')
    imageFinder.findAndClick('확인', threshold=0.91)
    robot.pressKey('ESC', sleep=4)

def 길드활동(char: Unit):
    # 길드 출석
    robot.pressKey(';', sleep=4)
    if(char.길드기부):
        imageFinder.findAndClick('길드기부', error=False)
        imageFinder.findAndClick('기부하기', error=False)
        imageFinder.findAndClick('확인', sleep=5, error=False)
        imageFinder.findAndClick('길드기부_상자클릭')
        robot.pressKey('ESC')
        robot.pressKey('ESC')
    imageFinder.findAndClick('길드출석', sleep=5)
    imageFinder.findAndClick('길드출석10000')
    imageFinder.findAndClick('확인', threshold=0.91)
    imageFinder.findAndClick('확인', threshold=0.91)
    imageFinder.findAndClick('길드출석상자', threshold=0.70, error=False)
    imageFinder.findAndClick('확인', threshold=0.91, error=False)
    imageFinder.findAndClick('확인', threshold=0.91, error=False)
    robot.pressKey('ESC', sleep=5)
    robot.pressKey('ESC', sleep=10)

def 친구포인트():
    robot.pressKey('l', sleep=4)
    imageFinder.findAndClick('친구일괄보내기')
    imageFinder.findAndClick('확인', threshold=0.91)
    imageFinder.findAndClick('친구일괄받기', sleep=5)
    robot.pressKey('ESC')

def 캐릭터선택(char:Unit):
    imageFinder.findAndClick('캐릭_선택')
    imageFinder.findAndClick('캐릭_보리뚜')
    for i in range(100):

        pt = imageFinder.isFound('캐릭_' + char.name, threshold=0.85, sleep=0)
        if(pt != None):
            imageFinder.findAndClick('캐릭_' + char.name, threshold=0.80, sleep=0, error=False)
            break
        pyautogui.scroll(-1000)
        pyautogui.sleep(0.1)
    imageFinder.findAndClick('캐릭_게임시작')

def 산등최초입장():
    imageFinder.findAndClick('확인', sleep=9, error=False)
    imageFinder.findAndClick('입장_최초맵선택', threshold=0.7, sleep=9)
    imageFinder.findAndClick('입장_설산')
    imageFinder.findAndClick('모험난이도', threshold=0.9, sleep=15)
    imageFinder.findAndClick('산등성이')
    imageFinder.findAndClick('전투시작', threshold=0.9)

def 산등노가다(char:Unit):

    for j in range(20):
        pyautogui.sleep(3)
        pyautogui.press(str(char.buffIndex))
        imageFinder.findAndClick('산등맵', 1, 0.75, error=False)
        if(imageFinder.isFound('지옥파티', 0.5) != None):
            산등지옥재도전()
            continue

        for i in range(300):
            print(i)
            # if multip 30
            if(i%30 == 0):
                robot.pressKey('right', duration=2)
                imageFinder.findAndClick('부활', 1, 0.75, error=False)

            pyautogui.sleep(0.01)
            pyautogui.keyDown('x')
            pyautogui.sleep(3)
            if(imageFinder.isFound('재도전', threshold=0.6) != None):
                pyautogui.keyUp('x')
                pyautogui.keyDown('x')
                pyautogui.sleep(4)
                pyautogui.keyUp('x')
                break
            # if(imageFinder.isFound('산등_시계방갈림길') != None):
                # robot.pressKey('right', duration=5)
            pyautogui.keyUp('x')

        pyautogui.sleep(3)
        pyautogui.press('F6')
        if(imageFinder.isFound('피로도부족', sleep=4) != None):
            break 
    imageFinder.findAndClick('확인')
    robot.pressKey('F8', 5)

def 산등지옥재도전(): 
    pyautogui.press("ESC")
    imageFinder.findAndClick('재도전확인')
    robot.pressKey('left', 10)
    imageFinder.findAndClick('모험난이도', threshold=0.9)
    imageFinder.findAndClick('산등성이')
    imageFinder.findAndClick('전투시작', threshold=0.9)

def 즐찾구매():
    # 즐찾상점
    robot.pressKey('s', sleep=4)
    imageFinder.findAndClick('상점_관심상품', 4)
    imageFinder.findAndClick('구매하기', threshold=0.91, error= False)
    imageFinder.findAndClick('확인', threshold=0.91, error=False)
    imageFinder.findAndClick('확인', threshold=0.91, error=False)
    robot.pressKey('ESC', 10)

def 신비상점구매(char:Unit):
    # 신비상점
    imageFinder.findAndClick('상점', sleep=4)
    imageFinder.findAndClick('상점_신비')
    # imageFinder.findAndClick('상점_신비천', threshold=0.95, error=False)
    imageFinder.findAndClick('상점_신비연석', threshold=0.95, error=False)
    imageFinder.findAndClick('상점_신비라코', threshold=0.95, error=False)
    imageFinder.findAndClick('상점_신비가죽', threshold=0.95, error=False)
    imageFinder.findAndClick('상점_신비뼈', threshold=0.95, error=False)
    if(char.신비전체구매 == True):
        imageFinder.findAndClick('상점_신비원소', threshold=0.9, error=False)
        # imageFinder.findAndClick('상점_신비다이야', threshold=1, error=False)
        imageFinder.findAndClick('상점_신비경화제', threshold=0.95, error=False)
        imageFinder.findAndClick('상점_신비칼박', threshold=0.95, error=False)
    imageFinder.findAndClick('구매하기', threshold=0.85, error=False)
    imageFinder.findAndClick('구입', threshold=0.85, error=False)
    imageFinder.findAndClick('확인', threshold=0.91, error=False)
    if(imageFinder.isFound('신비_소지금액부족') != None):
        robot.pressKey('ESC')
    robot.pressKey('ESC')

def 크리처():
    robot.pressKey('ESC', sleep=7)
    imageFinder.findAndClick('크리처')

    imageFinder.findAndClick('크리처_심부름')
    if(imageFinder.isFound('크리처_보상받기', sleep=4) != None):
        imageFinder.findAndClick('크리처_보상받기')
        imageFinder.findAndClick('확인')
    imageFinder.findAndClick('크리처_빠른심부름', sleep=7)
    imageFinder.findAndClick('크리처_자동배치')
    imageFinder.findAndClick('크리처_보내기')
    if(imageFinder.isFound('확인', sleep=4) == None):
        robot.pressKey('ESC')
    else:
        imageFinder.findAndClick('확인')
    robot.pressKey('ESC')

def 아티팩트판매():
    robot.pressKey('ESC', sleep=7)
    imageFinder.findAndClick('크리처')
    imageFinder.findAndClick('크리처_아티팩트')
    imageFinder.findAndClick('장비해체', error=False)
    imageFinder.findAndClick('크리처_장비해체클릭', error=False)
    if(imageFinder.isFound('확인', sleep=4) != None):
        imageFinder.findAndClick('확인', error=False)
        pyautogui.sleep(4)
        imageFinder.findAndClick('확인', error=False)
    robot.pressKey('ESC') 
    robot.pressKey('ESC')

# 크리처()
# sampleUnit = Unit("보리핏", 3, 'w', False)
# 신비상점구매(sampleUnit)
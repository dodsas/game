import pyautogui
import robot
import imageFinder
import unit

def 사냥종료():
    imageFinder.findAndClick('확인')
    robot.pressKey('F8', 6)

    # 아이템 보관
    robot.pressKey('i', 4)
    imageFinder.findAndClick('장비수리')
    imageFinder.findAndClick('장비수리확인')
    robot.pressKey('ESC')
    imageFinder.findAndClick('판매', sleep=4)
    for i in range(3):
        imageFinder.findAndClick('판매확인', error=False)
        imageFinder.findAndClick('확인', threshold=0.91, error=False)
        imageFinder.findAndClick('확인', threshold=0.91, error=False)
    robot.pressKey('ESC')
    imageFinder.findAndClick('금고')
    imageFinder.findAndClick('모험단금고')
    imageFinder.findAndClick('자동보관')
    imageFinder.findAndClick('확인', threshold=0.91)
    robot.pressKey('ESC')

    # 길드 출석
    robot.pressKey(';', sleep=3)
    imageFinder.findAndClick('길드출석', sleep=5)
    imageFinder.findAndClick('길드출석10000')
    imageFinder.findAndClick('확인', threshold=0.91)
    imageFinder.findAndClick('확인', threshold=0.91)
    imageFinder.findAndClick('길드출석상자', threshold=0.70, error=False)
    imageFinder.findAndClick('확인', threshold=0.91, error=False)
    robot.pressKey('ESC', sleep=5)
    robot.pressKey('ESC', sleep=10)

    # 친구포인트
    robot.pressKey('l', sleep=3)
    imageFinder.findAndClick('친구일괄보내기')
    imageFinder.findAndClick('확인', threshold=0.91)
    imageFinder.findAndClick('친구일괄받기', sleep=5)
    robot.pressKey('ESC')

def retry(): 
    pyautogui.press("ESC")
    imageFinder.findAndClick('재도전확인')
    robot.pressKey('left', 4)
    imageFinder.findAndClick('모험난이도', 0.9)
    imageFinder.findAndClick('산등성이')
    imageFinder.findAndClick('전투시작', 0.9)

def 캐릭터선택(name:str):
    imageFinder.findAndClick('캐릭_선택')
    imageFinder.findAndClick('캐릭_보리뚜')
    for i in range(100):

        pt = imageFinder.isFound('캐릭_' + name, threshold=0.85, sleep=0)
        if(pt != None):
            imageFinder.findAndClick('캐릭_' + name, threshold=0.80, sleep=0, error=False)
            break
        pyautogui.scroll(-1000)
        pyautogui.sleep(0.1)
    imageFinder.findAndClick('캐릭_게임시작')
    imageFinder.findAndClick('입장_최초맵선택', sleep=10)
    imageFinder.findAndClick('입장_설산')
    imageFinder.findAndClick('모험난이도', threshold=0.9, sleep=13)
    imageFinder.findAndClick('산등성이')
    imageFinder.findAndClick('전투시작', threshold=0.9)

def 상점물품구매(unit:unit.Unit):
    # 즐찾상점
    robot.pressKey('s')
    imageFinder.findAndClick('상점_관심상품', 4)
    imageFinder.findAndClick('구매하기', threshold=0.91, error= False)
    imageFinder.findAndClick('확인', threshold=0.91, error=False)
    imageFinder.findAndClick('확인', threshold=0.91, error=False)
    robot.pressKey('ESC', 10)

    # 신비상점
    imageFinder.findAndClick('상점')
    imageFinder.findAndClick('상점_신비')
    imageFinder.findAndClick('상점_신비라코', error=False)
    imageFinder.findAndClick('상점_신비천', error=False)
    imageFinder.findAndClick('상점_신비연석', error=False)
    if(unit.고급부캐 == True):
        imageFinder.findAndClick('상점_신비칼박', error=False)
        imageFinder.findAndClick('상점_신비원소', error=False)
    imageFinder.findAndClick('구매하기', threshold=0.85, error=False)
    imageFinder.findAndClick('구입', threshold=0.85, error=False)
    imageFinder.findAndClick('확인', threshold=0.91, error=False)
    robot.pressKey('ESC')
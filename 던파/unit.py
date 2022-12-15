import pyautogui
import robot
import imageFinder

def 사냥종료():
    robot.pressKey('F8', 6)
    # 아이템 보관
    robot.pressKey('i', 4)
    imageFinder.findAndClick('장비수리', sleep=1)
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
    imageFinder.findAndClick('길드출석상자', threshold=0.75)
    imageFinder.findAndClick('확인', threshold=0.91)
    robot.pressKey('ESC')
    robot.pressKey('ESC')

    # 친구포인트
    robot.pressKey('l')
    imageFinder.findAndClick('친구일괄보내기')
    imageFinder.findAndClick('확인', threshold=0.91)
    imageFinder.findAndClick('친구일괄받기', sleep=5)
    robot.pressKey('ESC')

def retry(): 
    pyautogui.press("ESC")
    imageFinder.findAndClick('재도전확인')
    robot.pressKey('left', 2)
    imageFinder.findAndClick('모험난이도', 0.9)
    imageFinder.findAndClick('산등성이')
    imageFinder.findAndClick('전투시작', 0.9)

사냥종료()
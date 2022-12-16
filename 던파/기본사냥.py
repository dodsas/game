# pyautogui is a module that allows you to control the mouse and keyboard
import pyautogui
import imageFinder
import robot
import action
import unit 

# map of Unit objects
map = {
    "윈드꾸꾸": unit.Unit("윈드꾸꾸", 6, False),
    "보리뚜킥": unit.Unit("보리뚜킥", 3, False),
    "보리커": unit.Unit("보리커", 3, False),
    "보리뚜비": unit.Unit("보리뚜비", 3, False),
    "웨펀꾸꾸": unit.Unit("웨펀꾸꾸", 3, False),
    "보리꾸꾸": unit.Unit("보리꾸꾸", 6, True),
    "런처꾸꾸": unit.Unit("런처꾸꾸", 6, True),
    "보리템플러": unit.Unit("보리템플러", 3, True),
    "보리술사": unit.Unit("보리술사", 3, True),
    "소울뚜": unit.Unit("소울뚜", 5, True),
    "보리뚜뚜": unit.Unit("보리뚜뚜", 6, True),
}

# map iterator
for key in map:
    char = map[key]
    # unit.캐릭터선택(char.name)

    # loop 20 times
    for j in range(20):
        pyautogui.sleep(4)
        pyautogui.press(str(char.buffIndex))
        imageFinder.findAndClick('산등맵', 2, 0.75)
        if(imageFinder.isFound('지옥파티', 0.5) != None):
            action.retry()
            continue

        for i in range(50):
            # print(i)
            for j in range(5):
                pyautogui.keyDown('x')
                pyautogui.sleep(1)
            if(imageFinder.isFound('재도전') != None):
                pyautogui.keyUp('x')
                pyautogui.keyDown('x')
                pyautogui.sleep(4)
                pyautogui.keyUp('x')
                break
            if(imageFinder.isFound('산등_시계방갈림길') != None):
                robot.pressKey('right', duration=5)
            pyautogui.keyUp('x')

        pyautogui.sleep(3)
        pyautogui.press('F6')
        if(imageFinder.isFound('피로도부족', sleep=4) != None):
            break 

    action.사냥종료()
    action.상점물품구매(char)


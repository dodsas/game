from dataclasses import dataclass 

# pyautogui is a module that allows you to control the mouse and keyboard
import pyautogui
import imageFinder
import robot
import unit

@dataclass
class Module:
    name: str
    buffIndex: int 
    # constructor
    def __init__(self, name, buffIndex):
        self.name = name
        self.buffIndex = buffIndex

# map of Module objects
map = {
    "보리꾸꾸": Module("보리꾸꾸", 6),
    "보리런처": Module("보리런처", 6),
    "보리템플러": Module("보리템플러", 3),
    "보리술사": Module("보리술사", 3),
    "소울뚜": Module("소울뚜", 5),
    "보리뚜뚜": Module("보리뚜뚜", 6),
}

# loop 20 times
char = map["소울뚜"]
for j in range(20):
    pyautogui.sleep(5)
    # int to string
    pyautogui.press(str(char.buffIndex))
    imageFinder.findAndClick('산등맵', 0.95, sleep=2)
    if(imageFinder.isFound('지옥파티', sleep=0.5) != None):
        unit.retry()
        continue

    for i in range(50):
        # print the value of i
        print(i)
        # hold key down for 2 seconds
        pyautogui.keyDown('x')
        pyautogui.sleep(5)
        if(imageFinder.isFound('재도전') != None):
            pyautogui.keyUp('x')
            break
        pyautogui.keyUp('x')

    pyautogui.press('F6')
    if(imageFinder.isFound('피로도부족', sleep=2) != None):
       break 

unit.사냥종료()


import pyautogui

def pressKey(key: str, sleep: float = 2, duration: float = 1):
    pyautogui.sleep(sleep)
    print('pressKey: ' + key)
    pyautogui.keyDown(key)
    pyautogui.sleep(duration)
    pyautogui.keyUp(key)

def printf(p1, p2, p3, p4):
    print(f'[ {p1:13} ][ {p2:9} ][ {p3:6} ] {p4:15}')
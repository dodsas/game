import pyautogui

def pressKey(key: str, sleep: float = 2, duration: float = 1):
    pyautogui.sleep(sleep)
    print('pressKey: ' + key)
    pyautogui.keyDown(key)
    pyautogui.sleep(duration)
    pyautogui.keyUp(key)
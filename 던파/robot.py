import pyautogui

def pressKey(key: str, sleep: float = 1):
    pyautogui.sleep(sleep)
    print('pressKey: ' + key)
    pyautogui.keyDown(key)
    pyautogui.sleep(sleep)
    pyautogui.keyUp(key)
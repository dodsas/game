import keyboard

# while(True):
    # robot.pressKey('f', sleep=0, duration=0.1)
    # robot.pressKey('e', sleep=0, duration=0.1)
    # robot.pressKey('r', sleep=0, duration=0.1)
    # robot.pressKey('w', sleep=0, duration=0.1)
    # robot.pressKey('q', sleep=0, duration=0.1)
    
    # robot.pressKey('f6', sleep=0, duration=0.1)
    # pyautogui.press('f')
    # pyautogui.press('f6')

# keyboard.send('f')

keyboard.hook(print)
# input()

while(True):
    keyboard.press_and_release(3) # f
    keyboard.press_and_release('f6') # q
    pyautogui.sleep(2)
    print('aaa')

# keyboard.press_and_release(3) # f
# keyboard.press_and_release(12) # q
# keyboard.press_and_release(13) # w
# keyboard.press_and_release(14) # e
# keyboard.press_and_release(15) # r


# show all keymap for keybarod module

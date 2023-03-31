import keyboard
import time
# import robot

def press(key: str, sleep: float = 2, duration: float = 1):
    time.sleep(sleep)
    # if(printLog == True):
    #    robot.printf('pressKey', key, '', '')

    keyMap = {
        'f': 3,
        'q': 12,
        'w': 13,
        'e': 14,
        'r': 15,
        '1': 18,
        '2': 19,
        '3': 20,
        '4': 21,
        '5': 23,
        '6': 22,
        '7': 26,
        '8': 28,
    }

    # check keyMap contain key
    modifiedKey = None
    if key in keyMap:
        modifiedKey = keyMap[key]

    if modifiedKey == None:
        # print('pressKey: key not found in keyMap ' + key)
        modifiedKey = key
    
    keyboard.press(modifiedKey)
    time.sleep(duration)
    keyboard.release(modifiedKey)

# pressKey('f6')
# show all keymap for keybarod module
# print('키보드후킹중')
# keyboard.hook(print)
# input()

# while(True):
#     # keyboard.press_and_release('f6') # q
#     pressKey('f', 2, 1)    # sleep 2 seconds
#     time.sleep(2)
#     print('aaa')
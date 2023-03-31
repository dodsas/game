# pip3 install pyautogui

import image_finder
import pyautogui 

# x, y = 100, 100
# current_x, current_y = pyautogui.position()
# pyautogui.moveTo(x, y)
# pyautogui.click()
# pyautogui.moveTo(current_x, current_y)

def click(pt):
    pyautogui.sleep(0.5)
    if (pt == None):
        raise Exception(f"Click Pointer is null")
        # errorf(name)
    pyautogui.click(x=pt[0], y=pt[1])

def clickDirect(x, y):
    pyautogui.sleep(0.5)
    pyautogui.click(x, y)

# click(image_finder.find("test")[0])

# # method to isFount and click
# def findAndClick(imageName: str, sleep = 3, threshold: float = 0.80, error: bool = True, printLog: bool = True):
#     pyautogui.sleep(sleep)
#     pt = isFound(imageName, threshold=threshold, sleep=sleep, printLog=printLog)
#     # if error is true and pt is null, exit
#     if (error == False and pt == None):
#         return
#     click(pt, imageName)

# def pressAndWaitAndClick(key: str, imageName: str, threshold: float = 0.80, maxWait=10, error: bool = True, delay: float=0.0):    

#     if (key == 'esc' or key == 'ESC'): 
#         sleep = 3

#     i = 0
#     while True:
#         i += 1 
#         robot.pressKey(key, sleep=0.0)
#         pyautogui.sleep(sleep)
#         pt = isFound(imageName, threshold = threshold, sleep=0.5, printLog=False)
#         if(error == False and i > maxWait * 2):
#             isFound(imageName, threshold = threshold, sleep=0.0, printLog=True)
#             robot.printf(imageName, 'NOT_FOUND', '', 'waitAndClick')
#             return False
#         if (pt != None or i > maxWait * 2):
#             break
    
#     pyautogui.sleep(delay)
#     click(pt, imageName)
#     return True

# def pressAndWait(key: str, imageName: str, threshold: float = 0.92, maxWait=10, error: bool = True):    
#     i = 0
#     while True:
#         i += 1 
#         robot.pressKey(key, sleep=0)
#         findAndClick('확인', threshold=0.9, error=False, printLog=False)
#         pt = isFound(imageName, threshold = threshold, sleep=0.5, printLog=False)
#         if(error == False and i > maxWait * 2):
#             isFound(imageName, threshold = threshold, sleep=0.0, printLog=True)
#             robot.printf(imageName, 'NOT_FOUND', '', 'waitAndClick')
#             return False
#         if (pt != None or i > maxWait * 2):
#             break

#     if(pt == None):
#         isFound(imageName, threshold = threshold, sleep=0.0, printLog=True)
#         robot.printf(imageName, 'NOT_FOUND', '', 'waitAndClick')
#         errorf(imageName)

#     return True

# def waitAndClick(imageName: str, threshold: float = 0.80, maxWait=10, error: bool = True, delay: float=0.0):
#     # loop until found image
#     i = 0
#     while True:
#         i += 1 
#         pt = isFound(imageName, threshold = threshold, sleep=0.5, printLog=False)
#         if(error == False and i > maxWait * 2):
#             isFound(imageName, threshold = threshold, sleep=0.0, printLog=True)
#             robot.printf(imageName, 'NOT_FOUND', '', 'waitAndClick')
#             return False
#         if (pt != None or i > maxWait * 2):
#             break
    
#     pyautogui.sleep(delay)
#     click(pt, imageName)
#     return True

# def wait(imageName: str, threshold: float = 0.92, maxWait=10, error: bool = True):
#     # loop until found image
#     i = 0
#     while True:
#         i += 1 
#         pt = isFound(imageName, threshold = threshold, sleep=0.5, printLog=False)
#         if(error == False and i > maxWait * 2):
#             isFound(imageName, threshold = threshold, sleep=0.0, printLog=True)
#             robot.printf(imageName, 'NOT_FOUND', '', 'waitToFind')
#             return False
#         if (pt != None or i > maxWait * 2):
#             break

#     if(pt == None):
#         errorf(imageName)
    
#     return True

# # findAndClick('재도전_초과')
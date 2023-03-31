# pip3 install pyautogui
# pip3 install opencv-python
# pip3 install opencv-contrib-python
# pip3 install numpy
# pip3 install matplotlib

import pyautogui
import cv2
import numpy as np
# import matplotlib.pyplot as plt

imgPath = 'Images/'
imgLogPath = 'ImagesLog/'

# 1920 x 1080 해상도기준
removeX=1280
removeY=300

width=640
heigth=700

pyautogui.FAILSAFE = False

def getScreenShotToGray():
    # payutogui half screenshot
    img = pyautogui.screenshot(region=(removeX, removeY, width, heigth))
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(imgLogPath+'바탕화면.png', gray)
    return gray

def find(imageName: str, screenShot: cv2.Mat=None, threshold: float = 0.9):
 
    if screenShot is None:
        screenShot = getScreenShotToGray()

    template = cv2.imread(imgPath+imageName+'.jpg', 0)
    templateRGB = cv2.cvtColor(template, cv2.COLOR_BGR2RGB)
    templateGray = cv2.cvtColor(templateRGB, cv2.COLOR_BGR2GRAY)

    cv2.imwrite(imgLogPath+imageName+'_gray.png', templateGray)

    h, w = template.shape

    res = cv2.matchTemplate(screenShot, templateGray, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # dedect
    for pt in zip(*loc[::-1]):
        cv2.rectangle(screenShot, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        cv2.imwrite(imgLogPath+imageName+'_detect.png', screenShot)
        # print(imageName + ' is found ')
        # print(f'[x:{pt[0]+removeX:4} y:{pt[1]+removeY:4}][FOUND!!! ][{max_val:.4f}] {imageName:15}')
        # robot.printf(imageName, 'FOUND', f'{max_val:.4f}', f'x:{pt[0]+removeX:4} y:{pt[1]+removeY:4}')        
        print(pt)
        print(w, h)

        return (pt[0] + w/2 + removeX, pt[1] + h/2 + removeY), max_val

    # if (printLog == True):
    #     robot.printf(imageName, 'NOT_FOUND', f'{max_val:.4f}', '')
    return None, max_val

def isFound(imageName: str, screenShot: cv2.Mat=None, threshold: float = 0.9):
    pt, maxVal = find(imageName, screenShot, threshold)
    if pt is None:
        return False 
    else:
        return True 

# pt, maxVal = find("test")
# print(pt, maxVal)

# method to click on pt
# def click(pt, name):
#     pyautogui.sleep(0.5)
#     if (pt == None):
#         errorf(name)
#     pyautogui.click(x=pt[0]+5+removeX, y=pt[1]+5+removeY)
#     # print x y
#     # print(f'[x:{pt[0]+removeX:4} y:{pt[1]+removeY:4}][CLICKED!!! ] {name:15}')

# def clickDirect(x, y):
#     pyautogui.sleep(0.5)
#     pyautogui.click(x, y)

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
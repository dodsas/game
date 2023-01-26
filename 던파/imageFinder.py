# image dedect in current screen
# pip3 install pyautogui
# pip3 install opencv-python
# pip3 install opencv-contrib-python
# pip3 install numpy
# pip3 install matplotlib

import pyautogui
import cv2
import numpy as np
import matplotlib.pyplot as plt
from robot import printf

imgPath = 'Images/'
imgLogPath = 'ImagesLog/'

removeX=1280
removeY=300

# def method to return wether or not the image is found
def isFound(imageName: str, sleep: float = 0.0, threshold: float = 0.8, printLog: bool = True):
    if(sleep != 0.0):
        pyautogui.sleep(sleep)

    # osx 에서는 아래 코드를 추가해야 한다
    pyautogui.FAILSAFE = False

    # payutogui half screenshot
    img = pyautogui.screenshot(region=(removeX, removeY, 1920, 700))
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    # 이미지를 흑백으로 변환
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2GRAY)

    # 이미지 출력
    # cv2.imshow('image', gray)
    # cv2.waitKey(0)

    # 이미지 저장
    cv2.imwrite(imgLogPath+imageName+'_바탕화면.png', gray)

    # 이미지 검색
    template = cv2.imread(imgPath+imageName+'.jpg', 0)
    # template to gray
    templateRGB = cv2.cvtColor(template, cv2.COLOR_BGR2RGB)
    templateGray = cv2.cvtColor(templateRGB, cv2.COLOR_BGR2GRAY)

    cv2.imwrite(imgLogPath+imageName+'_gray.png', templateGray)

    w, h = template.shape[::-1]

    res = cv2.matchTemplate(gray, templateGray, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # dedect
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        cv2.imwrite(imgLogPath+imageName+'_detect.png', img)
        # print(imageName + ' is found ')
        # print(f'[x:{pt[0]+removeX:4} y:{pt[1]+removeY:4}][FOUND!!! ][{max_val:.4f}] {imageName:15}')
        printf(imageName, 'FOUND', f'{max_val:.4f}', f'x:{pt[0]+removeX:4} y:{pt[1]+removeY:4}')        
        return pt
    # return null

    if (printLog == True):
        # print(imageName + ' is not found')
        # print(f'[             ][NOT FOUND][{max_val:.4f}] {imageName:15}')
        printf(imageName, 'NOT_FOUND', f'{max_val:.4f}', '')
    
    return None

# method to click on pt
def click(pt, name):
    pyautogui.sleep(0.5)
    if (pt == None):
        print('Error At ' + name)
        exit()
    pyautogui.click(x=pt[0]+5+removeX, y=pt[1]+5+removeY)

# method to isFount and click
def findAndClick(imageName: str, sleep = 3, threshold: float = 0.80, error: bool = True, printLog: bool = True):
    pyautogui.sleep(sleep)
    pt = isFound(imageName, threshold=threshold, sleep=sleep, printLog=printLog)
    # if error is true and pt is null, exit
    if (error == False and pt == None):
        return
    click(pt, imageName)

def waitAndClick(imageName: str, threshold: float = 0.80, maxWait=10, error: bool = True, delay: float=0.0):
    # loop until found image
    i = 0
    while True:
        i += 1 
        pt = isFound(imageName, threshold = threshold, sleep=0.5, printLog=False)
        if(error == False and i > maxWait * 2):
            isFound(imageName, threshold = threshold, sleep=0.0, printLog=True)
            printf('waitAndClick', 'NOT_FOUND', imageName)
            return False
        if (pt != None or i > maxWait * 2):
            break
    
    pyautogui.sleep(delay)
    click(pt, imageName)
    return True

def waitToFind(imageName: str, threshold: float = 0.92, maxWait=10, error: bool = True):
    # loop until found image
    i = 0
    while True:
        i += 1 
        pt = isFound(imageName, threshold = threshold, sleep=0.5, printLog=False)
        if(error == False and i > maxWait * 2):
            isFound(imageName, threshold = threshold, sleep=0.0, printLog=True)
            printf('wiatToFind', 'NOT_FOUND', imageName)
            return False
        if (pt != None or i > maxWait * 2):
            break
    
    return True

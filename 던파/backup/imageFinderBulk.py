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
imgGrayPath = 'ImagesGray/'
imgLogPath = 'ImagesLog/'

removeX=1280
removeY=300

# osx 에서는 아래 코드를 추가해야 한다
pyautogui.FAILSAFE = False

def convertToGray():
    import os
    import glob

    os.system('rm -rf imagesGray/*')

    os.chdir(imgPath)
    for file in glob.glob("*.jpg"):
        # remove .jpg string
        imageName = file[:-4]
        print(imageName)

        template = cv2.imread(imageName+'.jpg', 0)
        templateRGB = cv2.cvtColor(template, cv2.COLOR_BGR2RGB)
        templateGray = cv2.cvtColor(templateRGB, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('../'+imgGrayPath+imageName+'.png', templateGray)

    os.chdir('../')

convertToGray()

def extractBackgroundImage():
    img = pyautogui.screenshot(region=(removeX, removeY, 1920, 700))
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    # imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # gray = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2GRAY)
    #cv2.imwrite(imgLogPath+'_바탕화면.png', gray)
    return img


# return type is list
def isFound(bg: cv2.Mat, imageName: str, threshold: float = 0.95, printLog: bool = True):  

    bgRGB = cv2.cvtColor(bg, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(bgRGB, cv2.COLOR_BGR2GRAY)

    # 이미지 검색
    template = cv2.imread(imgGrayPath+imageName+'.png', 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
 
    # dedect
    ptList = []
    for pt in zip(*loc[::-1]):
        # rectangle fill color
        cv2.rectangle(bg, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), -1)
        # print(f'[x:{pt[0]+removeX:4} y:{pt[1]+removeY:4}][FOUND!!! ][{max_val:.4f}] {imageName:15}')
        printf(imageName, 'FOUND', f'{max_val:.4f}', f'x:{pt[0]+removeX:4} y:{pt[1]+removeY:4}')
        ptList.append(pt)

    # if ptList is empty, return None
    if (len(ptList) == 0):
        if (printLog == True):
            # print(f'[             ][NOT FOUND][{max_val:.4f}] {imageName:15}')
            printf(imageName, 'NOT_FOUND', f'{max_val:.4f}', '')
        return None

    return ptList

def saveDebugImage(name: str, img: cv2.Mat):
    cv2.imwrite(imgLogPath+name+'.png', img)

def findBulk(name: str, imageNmaeList: list):
    foundList = []

    bg = extractBackgroundImage()
    saveDebugImage(f'{name}', bg)
    # for imageNameList
    for imageName in imageNmaeList:
        found = isFound(bg, imageName, threshold=0.93)
        if(found != None):
            foundList.extend(found)

    #remove none value in foundList
    foundList = [x for x in foundList if x is not None]
    # print(foundList)
    saveDebugImage(f'{name}_detected', bg)
    return foundList

def click(ptList):
    for pt in ptList:
        pyautogui.sleep(0.2)
        pyautogui.click(pt[0]+removeX, pt[1]+removeY)

def findAndClick(name: str, imageNmaeList: list):
    foundList = findBulk(name, imageNmaeList)
    click(foundList)

# buyList = []
# buyList.append('상점_신비천')
# buyList.append('상점_신비뼈')
# buyList.append('상점_신비철')
# buyList.append('상점_신비연석')
# buyList.append('상점_신비라코')
# buyList.append('상점_신비가죽')
# buyList.append('상점_신비원소')
# buyList.append('상점_신비경화제')
# buyList.append('상점_신비다이야')

# buyList.append('상점_신비칼박')

# buyList.append('상점_신비테라')
# buyList.append('상점_신비테라2')

# findAndClick('신비', buyList)
# af  = ''
# af.l


# findAndClick('신비', ['상점_신비가죽', '상점_신비라코', '상점_신비2라코100', '상점_신비2라코110', '상점_신비2칼박1'])
# image dedect library
# pip3 install opencv-python
# pip3 install opencv-contrib-python
# pip3 install numpy
# pip3 install matplotlib

import cv2
import numpy as np
import matplotlib.pyplot as plt

imgPath = 'Images'

# 이미지 읽기
img = cv2.imread(imgPath + '/산등맵.jpg', cv2.IMREAD_COLOR)

# 이미지를 흑백으로 변환
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2GRAY)

# 이미지 출력
# cv2.imshow('image', gray)
# cv2.waitKey(0)

# 이미지를 블러처리
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# 이미지를 이진화
ret, thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY_INV)

# 이미지 출력
# cv2.imshow('image', thresh)
# cv2.waitKey(0)

# 이미지의 외곽선을 찾는다
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 이미지에 외곽선을 그린다
img2 = imgRGB.copy()
cv2.drawContours(img2, contours, -1, (0, 255, 0), 3)

# 이미지 출력
cv2.imshow('image', img2)
cv2.waitKey(0)



# def find(imageName):

#     # osx 에서는 아래 코드를 추가해야 한다
#     pyautogui.FAILSAFE = False

#     # 이미지 읽기
#     img = pyautogui.screenshot()
#     img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

#     # 이미지를 흑백으로 변환
#     imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     gray = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2GRAY)

#     # 이미지 출력
#     # cv2.imshow('image', gray)
#     # cv2.waitKey(0)

#     # 이미지 저장
#     cv2.imwrite(imgLogPath+imageName+'_바탕화면.png', gray)

#     # 이미지 검색
#     template = cv2.imread(imgPath+imageName+'.jpg', 0)
#     # template to gray
#     templateRGB = cv2.cvtColor(template, cv2.COLOR_BGR2RGB)
#     templateGray = cv2.cvtColor(templateRGB, cv2.COLOR_BGR2GRAY)

#     cv2.imwrite(imgLogPath+imageName+'_gray.png', templateGray)

#     w, h = template.shape[::-1]

#     res = cv2.matchTemplate(gray, templateGray, cv2.TM_CCOEFF_NORMED)
#     loc = np.where(res >= threshold)
#     print(loc)

#     # dedect
#     for pt in zip(*loc[::-1]):
#         cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
#         pyautogui.click(x=pt[0] + w/2, y=pt[1] + h/2)
#         break

#     cv2.imwrite(imgLogPath+imageName+'_detected.png', img)
#     # cv2.imshow('Detected', img)
#     # cv2.waitKey(0)

# pyautogui is a module that allows you to control the mouse and keyboard
import pyautogui
import robot
import time
import action
from unit import Unit
import os
from datetime import datetime
import imageFinderBulk

# map of Unit objects
loop = 14 # 피로도남기 13 / 풀피로도 14
# loop = 13
map = {
   # "보리성": Unit("보리성", 4, 'w', 신비전체구매=True, 산등노가다=True, 길드기부=True),
    #"보리뚜": Unit("보리뚜", 3, 'q', 신비전체구매=True, 산등노가다=True, 길드기부=True),
   # "보리세이더": Unit("보리세이더", 3, 'w', 신비전체구매=True, 산등노가다=True, 길드기부=True, loopCount=loop),
    # "보리빵떡": Unit("보리빵떡", 3, 'w', 신비전체구매=True, 산등노가다=False, 길드기부=True),
 #   "윈드꾸꾸": Unit("윈드꾸꾸", 6, 'w', 신비전체구매=False, loopCount=14),
    # "보리뚜킥": Unit("보리뚜킥", 3, 'w', 신비전체구매=False, loopCount=14), 
#    "보리커": Unit("보리커", 3, 'w', 신비전체구매=True, 길드기부=True),
#    "보리꾸꾸": Unit("보리꾸꾸", 3, 'w', 신비전체구매=True, loopCount=14), 
#    "보리뚜비": Unit("보리뚜비", 3, 'w', 신비전체구매=False, loopCount=14), !@#!@#
   "런처꾸꾸": Unit("런처꾸꾸", 3, 'w', 신비전체구매=True, loopCount=14),
   "보리템플러": Unit("보리템플러", 3, 'w', 신비전체구매=False),
   "보리술사": Unit("보리술사", 3, 'w', 신비전체구매=False, loopCount=14),
   "소울뚜": Unit("소울뚜", 3, 'w', 신비전체구매=False, loopCount=14),
   "보리뚜뚜": Unit("보리뚜뚜", 6, 'w', 신비전체구매=True, loopCount=14),
   "웨펀꾸꾸": Unit("웨펀꾸꾸", 3, 'w', 신비전체구매=False, loopCount=14), 
   "베인뚜": Unit("베인뚜", 6, 'w', 신비전체구매=True, 길드기부=True, loopCount=14),
   "보리핏": Unit("보리핏", 3, 'w', 신비전체구매=True, 길드기부=True, loopCount=14),
 #  "무녀뚜": Unit("무녀뚜", 3, 'w', 신비전체구매=True, 길드기부=True, loopCount=14),
  #  "보리파": Unit("보리파", 3, 'w', 신비전체구매=True, 길드기부=True, loopCount=14),
   "서큐버뚜": Unit("서큐버뚜", 3, 'w', 신비전체구매=True, 길드기부=True, loopCount=14),
    "보리심판관": Unit("보리심판관", 3, 'w', 신비전체구매=True, 길드기부=True, loopCount=14),
}

# romove all files in imagesLog folder on osx
os.system('rm -rf imagesLog/*')

# remove result.txt
os.system('rm -rf result.txt')

# action.일최초시작("0700")
for key in map:

    startTime = time.time()

    char = map[key]

    action.캐릭터선택(char)
    if (char.산등노가다):
        action.산등최초입장()
        action.산등노가다(char)
    action.수리및보관()

    # action.크리처()
    action.길드활동(char)
    action.친구포인트()
    action.즐찾구매()
    #action.신비상점구매(char)
    action.아티팩트판매()

    # save startTime as minutes
    duration = round((time.time() - startTime) / 60, 2)
    f = open("result.txt", "a")
    f.write(f'{char.name.ljust(10)} : {str(duration)}\n')
    f.close()
    print("*********** END OF " + char.name)
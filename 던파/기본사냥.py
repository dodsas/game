# pyautogui is a module that allows you to control the mouse and keyboard
import pyautogui
import imageFinder
import robot
import action
from unit import Unit
import os

# map of Unit objects
map = {
   "보리뚜": Unit("보리뚜", 3, 'q', 신비전체구매=True, 산등노가다=True, 길드기부=True),
   "보리성": Unit("보리성", 3, 'w', 신비전체구매=True, 산등노가다=True, 길드기부=True),
   "보리세이더": Unit("보리세이더", 3, 'w', 신비전체구매=True, 산등노가다=True, 길드기부=True),
   "보리빵떡": Unit("보리빵떡", 3, 'w', 신비전체구매=True, 산등노가다=True, 길드기부=True),
   "윈드꾸꾸": Unit("윈드꾸꾸", 6, 'w', False),
   "보리뚜킥": Unit("보리뚜킥", 3, 'w', False),
   "보리커": Unit("보리커", 3, 'w', False),
   "보리뚜비": Unit("보리뚜비", 3, 'w', False),
   "보리꾸꾸": Unit("보리꾸꾸", 6, 'w', True),
   "런처꾸꾸": Unit("런처꾸꾸", 6, 'w', True),
   "보리템플러": Unit("보리템플러", 3, 'w', True),
   "보리술사": Unit("보리술사", 3, 'w', True),
   "소울뚜": Unit("소울뚜", 3, 'w', True),
   "보리뚜뚜": Unit("보리뚜뚜", 6, 'w', True),
   "웨펀꾸꾸": Unit("웨펀꾸꾸", 3, 'w', False),
    "베인뚜": Unit("베인뚜", 6, 'w', True),
    "보리핏": Unit("보리핏", 3, 'w', False),
}

# romove all files in imagesLog folder on osx
os.system('rm -rf imagesLog/*')

# map iterator
for key in map:
    char = map[key]
    action.캐릭터선택(char)
    action.크리처()

    if(char.산등노가다):
        action.산등최초입장()
        action.산등노가다(char)
        action.수리및보관()

    action.길드활동(char)
    action.친구포인트()
    action.즐찾구매()
    action.신비상점구매(char)
    action.아티팩트판매()
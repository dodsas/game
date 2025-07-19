# pyautogui is a module that allows you to control the mouse and keyboard
import pyautogui
import robot
import time
import action
import unit
import os
from datetime import datetime
import imageFinderBulk
import imageFinder
import mailSender
from unit import Unit
from tobe import *

# import 신비크리처 
# import 서조

os.system('rm -rf imagesLog/*')
# action.일최초시작("0700")
f = open(f'result/result_{datetime.now().strftime("%Y%m%d")}.txt', "a")

map = unit.map
# map = {  "보리성": unit.Unit("보리성", s='안톤무기바지벨트목걸이반지', buffIndex=4), }
map = {
   "베인뚜": Unit("베인뚜", s='master'),
   "보리성": Unit("보리성", buffIndex=4, s='master'),
  "보리빵떡": Unit("보리빵떡", s='master'),
   "지짱보": Unit("지짱보", s='master'),
  "강한보리": Unit("강한보리", s='master'),
   "보리뚜": Unit("보리뚜", s='master'),
  "보리세이더": Unit("보리세이더", s='master'),
   "보리템플러": Unit("보리템플러", b='제국'),
   "보리뚜뚜": Unit("보리뚜뚜", b='제국'),
  "인챈뚜": Unit("인챈뚜"), 
  "무녀뚜": Unit("무녀뚜", b='제국'),
   "소울뚜": Unit("소울뚜"),

   "런처꾸꾸": Unit("런처꾸꾸"), #--
   "보리꾸꾸": Unit("보리꾸꾸"), #--
   "웨펀꾸꾸": Unit("웨펀꾸꾸"), #--

#    "보리뚜킥": Unit("보리뚜킥"),
#    "보리술사": Unit("보리술사"),
#     "보리메이지": Unit("보리메이지"),
#     "보리핏": Unit("보리핏"),
#     "건꾸꾸": Unit("건꾸꾸"),
}
for key in map:

    char = map[key]
    unit.select(key)
    robot.charName = char.name

    if(unit.selected.workingDone):
        continue

    startTime = time.time()

    action.캐릭터선택2()


    do(Clicker('모험', threshold=0.8))
    # time.sleep(3)
    # robot.pressKey('i')
    # imageFinder.waitAndClick('장비수리')
    # imageFinder.waitAndClick('장비수리확인',maxWait=3, error=False)
    # else:

   # action.즐찾구매()
    action.우편함()
    # action.아티팩트판매()
    time.sleep(2)
    do(Clicker('인벤토리', threshold=0.70))
    do(Clicker('장비수리'))
    do(Clicker('장비수리확인'), onlyOneTime=True)
    time.sleep(1)
    do(Clicker('x', threshold=0.83))

    # 추출
    # do(Clicker('추출'))
    # do(Clicker('추출에픽해제'), onlyOneTime=True)
    # do(Clicker('추출2'), onlyOneTime=True)
    # do(Clicker('확인', 0.81), onlyOneTime=True)
    # do(Clicker('x', threshold=0.83))

    # 판매
    do(Clicker('판매'))
    # do(Clicker('판매유니크해제'), onlyOneTime=True)
    do(Clicker('판매2'))
    if(do(Founder('알림', threshold=0.76), onlyOneTime=True, okSkip=True)):
        do(Clicker('알림취소', threshold=0.86))
    do(Clicker('확인', 0.81), onlyOneTime=True, okSkip=True)
    time.sleep(1)
    do(Clicker('x', threshold=0.83), fallbackSkip=True)

    do(Clicker('판매'))
    do(Clicker('판매2'))
    if(do(Founder('알림', threshold=0.76), onlyOneTime=True, okSkip=True)):
        do(Clicker('알림취소', threshold=0.86))
    do(Clicker('확인', 0.81), onlyOneTime=True, okSkip=True)
    time.sleep(1)
    do(Clicker('x', threshold=0.83), fallbackSkip=True)

    do(Clicker('해체', threshold=0.85))
    do(Clicker('해체체크'), onlyOneTime=True)
    do(Clicker('해체2', 0.83))
    # do(Clicker('확인', 0.81), onlyOneTime=True)
    do(Clicker('확인', 0.81), onlyOneTime=True, okSkip=True)
    do(Clicker('x', threshold=0.83))

    # 금고보관
    do(Clicker('금고', 0.81))
    do(Clicker('모험단금고'))
    do(Clicker('자동보관'))
    do(Clicker('확인', 0.81), onlyOneTime=True)

    do(Clicker('뒤로가기'))

    # event
    #do(Clicker('이벤트'))
    #do(Clicker('보상받기'), canSkip=True)
    #do(Clicker('뒤로가기'))

    unit.workingDone()


    # save startTime as minutes
    duration = round((time.time() - startTime) / 60, 2)
    f.write(f'{char.name.ljust(10)} : {str(duration)}\n')

    print("*********** END OF " + char.name)

do(Clicker('menu'))
do(Clicker('캐릭터선택'))
mailSender.sendMail("[DNF] 기본사냥 완료", "-")
f.close()

os.system('rm -rf ..*screenshot*png*')

# unit.select('보리메이지')
# action.산등최초입장2()
# action.산등노가다2()
# unit.workingDone()
# action.수리및보관()

# # action.즐찾구매()
# action.아티팩트판매()
# action.우편함()
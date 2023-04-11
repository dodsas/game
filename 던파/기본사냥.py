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

# import 신비크리처 
# import 서조

os.system('rm -rf imagesLog/*')
# action.일최초시작("0700")
f = open(f'result/result_{datetime.now().strftime("%Y%m%d")}.txt', "a")

map = unit.map
for key in map:

    char = map[key]
    unit.select(key)
    robot.charName = char.name

    if(unit.selected.workingDone):
        continue

    startTime = time.time()

    action.캐릭터선택(char)
    if (char.산등노가다 and char.loopCount != 0):
        action.산등최초입장2()
        # action.산등노가다(char)
        action.산등노가다2()
        action.수리및보관()

    # action.크리처()
    # action.길드활동(char)
    # action.친구포인트()
    action.즐찾구매()
    # action.신비상점구매(char)
    action.아티팩트판매()

    # save startTime as minutes
    duration = round((time.time() - startTime) / 60, 2)
    f.write(f'{char.name.ljust(10)} : {str(duration)}\n')

    unit.workingDone()
    print("*********** END OF " + char.name)

mailSender.sendMail("[DNF] 기본사냥 완료", "-")
f.close()

os.system('rm -rf ..*screenshot*png*')

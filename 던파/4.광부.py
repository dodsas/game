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

# for 20 times
for i in range(99):
    while True:
        for j in range(20):
            robot.pressKey('left', sleep=0, duration=0)
            robot.pressKey('right', sleep=0, duration=0)

        # robot.pressKey('left', sleep=0, duration=0.5)
        # robot.pressKey('right', sleep=0, duration=0.5)
        # for j in range(40):
        #     robot.pressKey('left', sleep=0, duration=0)
        #     robot.pressKey('right', sleep=0, duration=0)
        if(imageFinder.isFound('광산_다시하기')):
            imageFinder.findAndClick('광산_다시하기', sleep=0, error=False)
            # imageFinder.waitAndClick('광산_채광시작', error=False)
            break

mailSender.sendMail("[DNF] Mining 완료", "-")
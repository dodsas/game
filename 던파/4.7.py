import logging
import pyautogui
import robot
import time
import action
import action2
from unit import Unit
from unit import select
import unit
import os
from datetime import datetime
import mailSender
import random
import imageFinder
import keyboard2
import sys

from tobe import * 

select('보리뚜')

def find():
    time.sleep(0.2)
    found, pos = do(Founder('7book', threshold=0.95), onlyOneTime=True, returnPosition=True)
    if found and pos is not None:
        do(Direct(1852, pos[1]))
        do(Clicker('7buy'))
        do(Founder('7refresh'))
        time.sleep(0.5)

    found, pos = do(Founder('7book2', threshold=0.95), onlyOneTime=True, returnPosition=True, delay=0)
    if found and pos is not None:
        do(Direct(1852, pos[1]))
        do(Clicker('7buy'))
        do(Founder('7refresh'))
        time.sleep(0.5)

    found, pos = do(Founder('7medal', threshold=0.95), onlyOneTime=True, returnPosition=True, delay=0)
    if found and pos is not None:
        do(Direct(1852, pos[1]))
        do(Clicker('7buy'))
        do(Founder('7refresh'))
        time.sleep(0.5)
    found, pos = do(Founder('7medal2', threshold=0.95), onlyOneTime=True, returnPosition=True, delay=0)
    if found and pos is not None:
        do(Direct(1852, pos[1]))
        do(Clicker('7buy'))
        do(Founder('7refresh'))
        time.sleep(0.5)
os.system('rm -rf imagesLog/*')

do(Direct(1663, 655))
while True:
    do(Founder('7refresh'), delay=0.1)
    find()
    do(Direct(1663, 655))
    pyautogui.scroll(-20000)
    find()
    do(Clicker('7refresh'), delay=0)
    do(Clicker('7ok'), delay=0.1)

# mailSender.sendMail("[DNF] 비밀작전 완료" , "-")



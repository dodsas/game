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

os.system('rm -rf imagesLog/*')

def back() :
    do(Presser('esc'))
    time.sleep(1)

def checkHome() :
    do(Founder('n_home'))

def soloRaid() :
    do(Direct(1300, 600), delay=3)
    time.sleep(3)
    for i in range(3) : 
        do(Direct(1648, 709), delay=1)
        do(Direct(1648, 709), delay=1)
        back()
    back()
    checkHome()

def benner(name: str) :
    do(Clicker(name))
    do(Direct(1649, 543), delay=1)
    do(Direct(1592, 765), delay=1)
    do(Direct(1592, 765), delay=1)
    do(Direct(1592, 765), delay=1)
    back()
    checkHome()

# get hunting point
def getHuntingPoint() :
    print("[*] Getting hunting points...")
    do(Direct(1464, 731), delay=3)
    do(Direct(1565, 743), delay=1)
    do(Direct(1647, 710), delay=1)
    do(Direct(1647, 710), delay=1)
    do(Direct(1544, 710), delay=1)
    do(Direct(1651, 740), delay=1)
    do(Direct(1651, 740), delay=1)
    checkHome()

# get cache shop
def getCacheShop() :
    print("[*] Getting cache shop...")
    do(Direct(1480, 658), delay=1)
    do(Direct(1310, 508), delay=5)
    do(Direct(1365, 536), delay=2)
    do(Direct(1319, 594), delay=1)
    do(Direct(1336, 775), delay=1)
    back()
    checkHome()

# battle ground
def battleGround() :
    print("[*] Battle ground...")
    do(Direct(1481, 711), delay=1)
    do(Direct(1613, 775), delay=6)
    do(Direct(1657, 733), delay=1)
    do(Direct(1657, 733), delay=1)
    do(Direct(1605, 733), delay=3)
    do(Direct(1635, 733), delay=1)
    back()
    back()
    checkHome()

# battle
def battle() :
    print("[*] Battle...")
    do(Direct(1731, 678), delay=3)
    do(Direct(1540, 599), delay=3)
    do(Clicker('n_simulation'), delay=2)
    do(Clicker('n_simulation_ok'))
    do(Clicker('n_simulation_close'))
    time.sleep(3)
    back()
    do(Direct(1656, 643), delay=2)
    do(Direct(1656, 643), delay=3)
    if(do(Founder('n_special_arena'), canSkip=True)) :
        do(Direct(1600, 516), delay=2)
        do(Direct(1643, 754), delay=2)
        do(Direct(1643, 754), delay=2)
        back()
    back()
    do(Direct(1561, 699), delay=3)
    do(Direct(1597, 727), delay=5)
    for i in range(3) :
        do(Clicker('n_eg'))
        time.sleep(2)
        back()
    back()
    back()
    checkHome()

# friendship
def friendship() :
    print("[*] Friendship...")
    do(Direct(1900, 522), delay=1)
    do(Direct(1644, 740), delay=1)
    do(Direct(1644, 740), delay=1)
    back()

# present to nikke
def presentToNikke() :
    print("[*] Present to nikke...")
    do(Direct(1527, 765), delay=1)
    do(Direct(1833, 476), delay=4)
    do(Direct(1432, 558), delay=1)
    for i in range(10):
        do(Founder('n_present_check'))
        do(Direct(1642, 704), delay=1)
        if do(Founder('n_present_is_full'), onlyOneTime=True) == True :
            mailSender.sendMail('nikke present full', 'full')
            sys.exit(1)
        do(Direct(1645, 658), delay=1)
        do(Direct(1778, 542), delay=1)
        do(Direct(1891, 587), delay=1)
    back()
    back()
    back()
    checkHome()

# get reward
def getReward() :
    print("[*] Get reward...")
    do(Direct(1836, 468), delay=1)
    do(Direct(1663, 758), delay=1)
    do(Direct(1663, 758), delay=1)
    do(Direct(1663, 758), delay=1)
    back()
    do(Direct(1893, 445), delay=1)
    do(Direct(1655, 740), delay=1)
    do(Direct(1655, 740), delay=1)
    back()
    checkHome()

# def event():


battleGround()
getHuntingPoint()
friendship()
presentToNikke()
battle()
getReward()
getCacheShop()
# benner('n_benner1')

# benner('n_benner2')
# event()
# soloRaid()
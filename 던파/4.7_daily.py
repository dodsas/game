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

def wakeUp():
    do(Direct(1594, 630))
    do(Direct(1594, 630))

def back():
    do(Direct(1300, 448))
    time.sleep(1)

def guild():
    wakeUp()
    do(Clicker('7_guild'))
    do(Clicker('7_touch'), canSkip=True)

    do(Clicker('7_guild_daliy'))
    do(Clicker('7_touch', threshold=0.88))
    
    # world
    do(Clicker('7_guild_attack'))
    do(Clicker('7_guild_touch_2', threshold=0.88), canSkip=True)
    do(Clicker('7_guild_world'))
    for i in range(2):
        do(Clicker('7_guild_ready'))
        do(Clicker('7_guild_team_select'))
        do(Clicker('7_guild_team_select_2'))
        do(Clicker('7_guild_team_select_4'))
        do(Clicker('7_guild_team_select_3'))
        # todo skip
        do(Clicker('7_guild_world_open'), customFallbackCount=300)
        do(Clicker('7_guild_world_open_ok'))
        do(Clicker('7_guild_world_open_ok_2'))

    do(Clicker('7_guild_world_back'))

    # donation
    do(Clicker('7_guild_donation'))
    do(Clicker('7_guild_donation_do_1'))
    do(Clicker('7_guild_donation_do_2'))

    # support
    do(Clicker('7_guild_support'))
    do(Clicker('7_guild_support_request'))
    do(Clicker('7_guild_support_request_flower'))
    do(Clicker('7_guild_support_request_do'))

    for i in range(4):
        if do(Clicker('7_guild_support_supply'), canSkip=True) == True : 
            do(Clicker('7_touch', threshold=0.88))


    do(Clicker('7_guild_donation_back'))

def area():
    wakeUp()
    do(Direct(1873, 630), delay=1)
    do(Direct(1455, 637), delay=1)

    do(Clicker('7_area_npc'))

    for i in range(7):
        time.sleep(5)
        do(Direct(1520, 550), delay=1)
        do(Clicker('7_area_try'))
        do(Direct(1318, 554), delay=3)
        do(Clicker('7_area_start'))
        do(Clicker('7_area_ok'), canSkip=True)

        do(Founder('7_area_ready'))
        time.sleep(2)
        do(Direct(1846, 451), delay=1)
            
        do(Clicker('7_area_ok2'), customFallbackCount=100, fallbackSkip=True)
        do(Founder('7_area_check'))

    do(Clicker('7_back'), delay=1.5)

    time.sleep(3)
    
def shop():
    wakeUp()
    do(Clicker('7_shop'))
    do(Clicker('7_shop_free'))
    do(Clicker('7_shop_free_ok'))
    do(Clicker('7_touch'))

    do(Clicker('7_shop_normal'))
    do(Direct(1591, 641))
    pyautogui.scroll(120000)

    for i in range(2) : 
        do(Direct(1766, 636), delay=1)
        do(Clicker('7_shop_normal_buy', threshold=0.80), delay=1)

    do(Clicker('7_shop_next'))
    do(Clicker('7_shop_friend'))
    do(Clicker('7_shop_friend_buy_1', threshold=0.8))
    do(Clicker('7_shop_buy', threshold=0.8))
    do(Clicker('7_shop_friend_buy_2', threshold=0.8))
    do(Clicker('7_shop_buy', threshold=0.8))
    
    do(Clicker('7_shop_arena'))
    do(Clicker('7_shop_arena_buy_1', threshold=0.90))
    do(Clicker('7_buy_max', threshold=0.83))
    do(Clicker('7_buy', threshold=0.7))
    
    if do(Clicker('7_shop_arena_buy_2', threshold=0.90), canSkip=True) == True : # muragora
        do(Clicker('7_buy', threshold=0.7))

    back()

def holy():
    wakeUp()
    do(Clicker('7_holy'))
    do(Clicker('7_holy_forest'))

    do(Direct(1844, 559))
    do(Clicker('7_touch'), canSkip=True)

    do(Direct(1844, 618))
    do(Clicker('7_touch'), canSkip=True)

    do(Direct(1844, 677))
    do(Clicker('7_touch'), canSkip=True)

    back()
    back()

def battle():
    wakeUp()
    do(Direct(1844, 677))
    do(Clicker('7_battle'))
    do(Clicker('7_battle_hunting'))
    
    # for i in range(2):
    #     time.sleep(2)
    #     # do(Direct(1576, 450), delay=1)
    #     do(Clicker('7_battle_hunting_buy_eg'))
    #     do(Clicker('7_battle_hunting_buy'))
    #     time.sleep(1.5)

    do(Clicker('7_battle_hunting_wyvern_eg'))

    # if do(Founder('7_battle_hunting_wyvern_auto_already', threshold=0.88), canSkip=True) == False :
    # if do(Founder('7_battle_hunting_wyvern_auto_3times_already', threshold=0.88), canSkip=True) == False :
        # do(Clicker('7_battle_hunting_wyvern_auto'))
    # if do(Founder('7_battle_hunting_wyvern_auto_already', threshold=0.9), canSkip=True) == False :
    #     do(Clicker('7_battle_hunting_wyvern_auto_3times', threshold=0.83))
    do(Direct(1572, 712), delay=2)

    # do(Clicker('7_battle_hunting_wyvern_eg_go', threshold=0.88))
    do(Direct(1828, 766))
    do(Clicker('7_battle_hunting_wyvern_eg_go_dontshow'), canSkip=True, fallbackSkip=True)
    do(Clicker('7_battle_hunting_wyvern_out'), fallbackSkip=True)
    do(Clicker('7_battle_hunting_wyvern_out_ok'))

def pet():
    wakeUp()
    do(Clicker('7_pet'))
    do(Clicker('7_pet_get'))
    do(Clicker('7_pet_get_2'))
    do(Clicker('7_pet_get_out'))
    do(Clicker('7_pet_get_out_2'))
    back()

def reward():
    wakeUp()
    do(Clicker('7_reward'))
    do(Clicker('7_reward_get'))
    do(Clicker('7_reward_get_close'))
    do(Clicker('7_reward_get_close_2'))

def event():
    wakeUp()
    do(Clicker('7_event'))

    do(Clicker('7_event_1'), canSkip=True) # dreaming clear something
    do(Clicker('7_event_1_get'))
    do(Clicker('7_touch'))
    do(Clicker('7_event_1_get'))
    do(Clicker('7_touch'))
    back()

# event()
# shop()
# battle()
# holy()
area()
guild()
pet()
reward()

mailSender.sendMail("[7] Deily Practice Done" , "-")



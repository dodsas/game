import sys
sys.path.append('tobe')
from image_robot import * 

from dataclasses import dataclass
import json
from datetime import datetime
import os

@dataclass
class Unit:
    name: str = 'None'
    # 짧은스킬 = 'q'
    finalIndex: int = '6'
    buffIndex: int = 3
    신비전체구매: bool = False
    산등노가다 = True
    loopCount:int = 13
    loop:int = 0
    workingDone: bool = False
    jsonString: str = None
    sunganDone: bool = False
    epicDone: bool = False

    def __post_init__(self):
        if (self.jsonString != None):
            self.__dict__ = json.loads(self.jsonString)
            if self.sunganDone and self.loopCount == 12:
                self.loopCount = 13

            if self.epicDone and self.loopCount == 11:
                self.loopCount = 13

    def to_json(self):
        return json.dumps(self, indent=4, default=lambda o: o.__dict__)

def load():
    print("load")

    # if no file, create one
    if not os.path.exists(fileName):
        update()

    with open(fileName, 'r') as f:
        global map
        list = []
        for jsonString in json.load(f):
            list.append(Unit(jsonString=jsonString))
        map = {}
        for char in list:
            print(char)
            map[char.name] = char
        # print(mapLoad)

def update():
    global map
    list = []
    for key, value in map.items():
        list.append(value.to_json())
    with open(fileName, 'w') as f:
        json.dump(list, f)

def select(name):
    print("=== select " + name)
    global selected
    selected = map[name]
    dun_print.g_charName = name
    print(selected)

def loopDone():
    global selected
    selected.loop += 1
    print("=== loopDone " + selected.name + " " + str(selected.loop))
    print(selected)
    update()

def workingDone():
    global selected
    print("=== workingDone " + selected.name)
    print(selected)
    selected.workingDone = True
    update()

def workingDone2(name):
    select(name)
    global selected
    print("=== workingDone " + selected.name)
    selected.workingDone = True
    print(selected)
    update()
#
selected: Unit = None
fileName = f'result/char_{datetime.now().strftime("%Y%m%d")}.json'

loop=11

mapInit = {
    "보리성": Unit("보리성", 신비전체구매=True, buffIndex=4, loopCount=loop, epicDone=True),
    "보리뚜": Unit("보리뚜", 신비전체구매=True, loopCount=loop, sunganDone=True, epicDone=True),
    "보리세이더": Unit("보리세이더", 신비전체구매=True, loopCount=loop, sunganDone=True, epicDone=True),
    "베인뚜": Unit("베인뚜", 신비전체구매=True, loopCount=4, finalIndex='f', epicDone=True),

    "보리빵떡": Unit("보리빵떡", 신비전체구매=True, loopCount=loop, sunganDone=True, epicDone=True),
    "보리템플러": Unit("보리템플러", 신비전체구매=True, loopCount=loop, epicDone=True),
    "보리뚜뚜": Unit("보리뚜뚜", 신비전체구매=True, buffIndex=2, loopCount=loop, epicDone=True),
    "무녀뚜": Unit("무녀뚜", 신비전체구매=False, loopCount=loop, epicDone=True),

    "보리뚜킥": Unit("보리뚜킥", loopCount=loop, epicDone=True),
    "보리핏": Unit("보리핏", 신비전체구매=False, loopCount=loop, sunganDone=True, epicDone=True),
    "윈드꾸꾸": Unit("윈드꾸꾸", 신비전체구매=False, finalIndex='f', loopCount=loop, sunganDone=True, epicDone=True),
    "보리심판관": Unit("보리심판관", 신비전체구매=False, loopCount=loop, epicDone=True),

    "보리커": Unit("보리커", 신비전체구매=True, loopCount=loop),
    "보리파": Unit("보리파", 신비전체구매=False, loopCount=loop, sunganDone=True),
    "런처꾸꾸": Unit("런처꾸꾸", 신비전체구매=True, loopCount=loop),
    "보리꾸꾸": Unit("보리꾸꾸", 신비전체구매=True, buffIndex=6, loopCount=loop),
    "보리술사": Unit("보리술사", loopCount=loop),
    "소울뚜": Unit("소울뚜", loopCount=loop, sunganDone=True),
    "보리뚜비": Unit("보리뚜비", loopCount=loop),
    "웨펀꾸꾸": Unit("웨펀꾸꾸", loopCount=loop),
    "서큐버뚜": Unit("서큐버뚜", 신비전체구매=False, loopCount=loop, finalIndex='3'),
    "지짱보": Unit("지짱보", 신비전체구매=False, loopCount=loop),
    "건꾸꾸": Unit("건꾸꾸", 신비전체구매=False, loopCount=loop),
    "보리닉": Unit("보리닉", 신비전체구매=False, loopCount=0),
}
map = mapInit
# update()
load()

workingDone2("보리성")
workingDone2("보리뚜")
workingDone2("베인뚜")
workingDone2("보리세이더")
workingDone2("보리빵떡")
workingDone2("보리템플러")
workingDone2("보리뚜뚜")
workingDone2("무녀뚜")
workingDone2("보리핏")
workingDone2("보리뚜킥")
workingDone2("보리심판관")
workingDone2("윈드꾸꾸")

workingDone2("보리커")
workingDone2("보리파")
workingDone2("런처꾸꾸")
workingDone2("보리꾸꾸")
workingDone2("보리술사")
workingDone2("소울뚜")
workingDone2("보리뚜비")
# workingDone2("웨펀꾸꾸")
# workingDone2("서큐버뚜")
workingDone2("지짱보")
# print(selected.workingDone)



# select("보리템플러")
# selected.loopCount=10
# selected.workingDone = False 
# print(selected)
# update()
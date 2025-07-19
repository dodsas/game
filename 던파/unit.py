from tobe import * 

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
    s: str = 'expert'
    s10: str = '무기목걸이어깨신발'
    s30: str = '무기목걸이어깨신발30'
    b: str = '노이'

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
        print(f'fileName: {fileName}')
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

loop=13

mapInit = {
    "베인뚜": Unit("베인뚜", s='안톤상의어깨신발팔찌보장'),
    "보리성": Unit("보리성", s='안톤상의어깨신발팔찌보장', buffIndex=4),
    "보리빵떡": Unit("보리빵떡", s='안톤상의어깨신발팔찌보장'),
    "지짱보": Unit("지짱보", s='안톤상의어깨신발팔찌보장'),
    "강한보리": Unit("강한보리", s='안톤상의어깨신발팔찌보장'),
    "보리뚜": Unit("보리뚜", s='안톤상의어깨신발팔찌보장'),
    "보리세이더": Unit("보리세이더", s='안톤상의어깨신발팔찌보장'),
    "보리뚜뚜": Unit("보리뚜뚜", s='안톤상의어깨신발팔찌보장'),
    "보리템플러": Unit("보리템플러", s='안톤상의어깨신발팔찌보장'),
    "인챈뚜": Unit("인챈뚜", s='반지상의하의보장팔찌벨트2'),

    "무녀뚜": Unit("무녀뚜", s='안톤상의어깨신발팔찌보장'),
    "소울뚜": Unit("소울뚜", s='반지상의하의보장팔찌벨트2'),

    "런처꾸꾸": Unit("런처꾸꾸", s='안톤상의어깨신발팔찌보장'),
    "보리꾸꾸": Unit("보리꾸꾸", s='안톤상의어깨신발팔찌보장'),
    "웨펀꾸꾸": Unit("웨펀꾸꾸", s='안톤상의어깨신발팔찌보장'),
    "보리뚜킥": Unit("보리뚜킥", s='안톤상의어깨신발팔찌보장'),
    "보리술사": Unit("보리술사", s='안톤상의어깨신발팔찌보장'),
    "보리메이지": Unit("보리메이지", s='안톤상의어깨신발팔찌보장'),
    "보리핏": Unit("보리핏", s='안톤상의어깨신발팔찌보장'),
    "건꾸꾸": Unit("건꾸꾸", s='안톤상의어깨신발팔찌보장'),
    "서큐버뚜": Unit("서큐버뚜", s='안톤상의어깨신발팔찌보장'),
    "보리커": Unit("보리커", s='안톤상의어깨신발팔찌보장'),
    "보리파": Unit("보리파", s='안톤상의어깨신발팔찌보장'),
    "보리심판관": Unit("보리심판관", s='안톤상의어깨신발팔찌보장'),
    "보리뚜비": Unit("보리뚜비", s='안톤상의어깨신발팔찌보장'),
    "윈드꾸꾸": Unit("윈드꾸꾸"),
    "보리닉": Unit("보리닉"),
    "보리뱅": Unit("보리뱅"),

    "보리왕": Unit("보리왕"),
    "보리샷": Unit("보리샷"),
    "보리치료사": Unit("보리치료사"),
}
map = mapInit
# update()
load()

# workingDone2("보리성")
# workingDone2("보리뚜")
# workingDone2("베인뚜")
# workingDone2("보리세이더")
# workingDone2("보리빵떡")
# workingDone2("보리템플러")
# workingDone2("보리뚜뚜")
# workingDone2("무녀뚜")
# workingDone2("런처꾸꾸")
# workingDone2("보리술사")
# workingDone2("보리꾸꾸")
# workingDone2("보리뚜킥")
# workingDone2("건꾸꾸")
# workingDone2("지짱보")
# workingDone2("보리핏")
# workingDone2("보리심판관")
# workingDone2("윈드꾸꾸")
# workingDone2("보리커")
# workingDone2("소울뚜")
# workingDone2("보리뚜비")
# workingDone2("보리파")
# workingDone2("웨펀꾸꾸")
# workingDone2("서큐버뚜")
# workingDone2("보리닉")
# print(selected.workingDone)


# select("보리템플러")
# selected.loopCount=10
# selected.workingDone = False 
# print(selected)
# update()
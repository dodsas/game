from dataclasses import dataclass
import json

@dataclass
class Unit:
    name: str = 'None'
    # 짧은스킬 = 'q'
    finalIndex: int = '6'
    buffIndex: int = 3
    신비전체구매: bool = False
    산등노가다 = True
    loopCount:int = 13
    workingDone: bool = False
    jsonString: str = None

    def __post_init__(self):
        if (self.jsonString != None):
            self.__dict__ = json.loads(self.jsonString)

    def to_json(self):
        return json.dumps(self, indent=4, default=lambda o: o.__dict__)


def load():
    print("load")
    with open(fileName, 'r') as f:
        global map
        list = []
        for jsonString in json.load(f):
            list.append(Unit(jsonString=jsonString))
        map = {}
        for char in list:
            print(char)
            map[char.name] = char

def update():
    global map
    list = []
    for key, value in map.items():
        list.append(value.to_json())
    with open(fileName, 'w') as f:
        json.dump(list, f)

def select(name):
    global selected
    selected = map[name]
    print(selected)

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

selected: Unit = None
fileName = 'result/char.json'
loop=11
mapInit = {
    "보리성": Unit(name="보리성", 신비전체구매=True, buffIndex=4),
    "보리뚜": Unit("보리뚜", 신비전체구매=True),
    "보리세이더": Unit("보리세이더", 신비전체구매=True, loopCount=2),
    "보리빵떡": Unit("보리빵떡", 신비전체구매=True, loopCount=2),
    "보리뚜뚜": Unit("보리뚜뚜", 신비전체구매=True, buffIndex=2),

    "보리템플러": Unit("보리템플러", 신비전체구매=True),
    "보리뚜킥": Unit("보리뚜킥", loopCount=loop),
    "보리핏": Unit("보리핏", 신비전체구매=False, loopCount=loop),
    "베인뚜": Unit("베인뚜", 신비전체구매=False, loopCount=loop, finalIndex='f'),

    "보리뚜비": Unit("보리뚜비", loopCount=loop),
    "보리커": Unit("보리커", 신비전체구매=True, loopCount=loop),
    "런처꾸꾸": Unit("런처꾸꾸", 신비전체구매=True, loopCount=loop),
    "보리꾸꾸": Unit("보리꾸꾸", 신비전체구매=True, buffIndex=6, loopCount=loop),
    "보리술사": Unit("보리술사", loopCount=loop),
    "소울뚜": Unit("소울뚜", loopCount=loop),
    "보리파": Unit("보리파", 신비전체구매=False, loopCount=loop),
    "윈드꾸꾸": Unit("윈드꾸꾸", 신비전체구매=False, finalIndex='f', loopCount=loop),
    "무녀뚜": Unit("무녀뚜", 신비전체구매=False, loopCount=loop),

    "웨펀꾸꾸": Unit("웨펀꾸꾸", loopCount=0),
    "서큐버뚜": Unit("서큐버뚜", 신비전체구매=False, loopCount=0, finalIndex='3'),
    "보리심판관": Unit("보리심판관", 신비전체구매=False, loopCount=0),
}
# map = mapInit
# update()

load()

# select("보리세이더")
# workingDone()
# workingDone2("보리성")
# workingDone2("보리뚜")
# workingDone2("보리세이더")
# workingDone2("보리빵떡")
# workingDone2("보리템플러")
# workingDone2("보리뚜뚜")
# workingDone2("보리뚜킥")
# workingDone2("보리핏")
# workingDone2("베인뚜")
# workingDone2("보리뚜비")
# workingDone2("보리커")
# workingDone2("런처꾸꾸")
# workingDone2("보리꾸꾸")
# workingDone2("보리술사")
# workingDone2("소울뚜")
# workingDone2("웨펀꾸꾸")
# workingDone2("무녀뚜")
# workingDone2("보리파")
# workingDone2("서큐버뚜")
# workingDone2("윈드꾸꾸")
# workingDone2("보리심판관")
# print(selected.workingDone)




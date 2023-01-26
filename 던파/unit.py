from dataclasses import dataclass 

@dataclass
class Unit:
    name: str
    짧은스킬: str
    finalIndex: str 
    buffIndex: int 
    신비전체구매: bool = False
    산등노가다: bool = True
    길드기부: bool = False 
    loopCount: int = 14
    
    def __init__(self, name, buffIndex, 짧은스킬, 신비전체구매=False, 산등노가다=True, 길드기부=False, loopCount=13,
    finalIndex='6'):
        self.name = name
        self.짧은스킬 = 짧은스킬
        self.buffIndex = buffIndex
        self.신비전체구매 = 신비전체구매
        self.산등노가다 = 산등노가다
        self.길드기부 = 길드기부
        self.loopCount = loopCount
        self.finalIndex = finalIndex
from dataclasses import dataclass 

@dataclass
class Unit:
    name: str
    buffIndex: int 
    고급부캐: bool = False
    # constructor
    def __init__(self, name, buffIndex, 고급부캐):
        self.name = name
        self.buffIndex = buffIndex
        self.고급부캐 = 고급부캐
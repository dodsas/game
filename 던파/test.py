# import Unit
from unit import Unit

# import json
import json

map = {
    "보리세이더": Unit("보리세이더", 3, 'w', 신비전체구매=True, 산등노가다=True, 길드기부=True),
    "보리뚜": Unit("보리뚜", 3, 'q', 신비전체구매=True, 산등노가다=True, 길드기부=True),
    "보리성": Unit("보리성", 4, 'w', 신비전체구매=True, 산등노가다=True, 길드기부=13),
    "보리빵떡": Unit("보리빵떡", 3, 'w', 신비전체구매=True, 산등노가다=False, 길드기부=True),
}

# print(map)

# save map as file
with open('map.json', 'w') as f:
    map['보리세이더'].buffIndex = 4
    # dump dict to fils
    json.dump(map, f)

# load map from file
with open('map.json', 'r') as f:
    map2 = json.load(f)

# print map
print(map2)
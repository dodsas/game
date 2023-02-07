# import Unit
from unit import Unit

# import json
import json

# cc = Unit("보리세이더", 3, 'w', 신비전체구매=True, 산등노가다=True, 길드기부=True)
cc = Unit()

# save map as file
with open('map2.json', 'w') as f:
    # dump dict to fils
    json.dump(cc, f, cls = Unit)

# load map from file
with open('map.json', 'r') as f:
    map2 = json.load(f, cls = Unit)

# print map
print(map2)
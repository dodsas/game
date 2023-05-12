import json 
import requests

apiKey = 'PMt9Td4PPMxB2WpdMRshXQwqjylCzWNB'

def getItemInfo(itemName: str):
    params = {
        'itemName': itemName,
        'apikey': apiKey 
    }
    response = requests.get('https://api.neople.co.kr/df/auction-sold', params=params)
    return response.text

def showAuctionHistory(auctionHistory: bytearray):
    dict_data = json.loads(auctionHistory)
    firstItme = dict_data['rows'][0]
    print(f'Item Name: {firstItme["itemName"]}')
    print(f'Sold Date: {firstItme["soldDate"]} UnitPirce: {firstItme["unitPrice"]}')

    # for item in dict_data['rows']:
    #     print(f'Sold Date: {item["soldDate"]} UnitPirce: {item["unitPrice"]}')

    # # print average print
    # sum = 0
    # for item in dict_data['rows']:
    #     sum += item['unitPrice']
    # print(f'Average: {sum / len(dict_data["rows"])}')

showAuctionHistory(getItemInfo('최상급 힘의 비약'))

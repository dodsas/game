import json 
import requests
from ljustk import * 

apiKey = 'PMt9Td4PPMxB2WpdMRshXQwqjylCzWNB'
apiCallCount = 0
apiCaches = []

def getItemInfo(itemName: str):
    global apiCallCount
    global apiCaches

    # if there is cache, return it
    for cache in apiCaches:
        if cache['itemName'] == itemName:
            return cache['info']

    params = {
        'itemName': itemName,
        'apikey': apiKey,
        'sort' : 'unitPrice:asc'
    }
    response = requests.get('https://api.neople.co.kr/df/auction-sold', params=params)
    # response = requests.get('https://api.neople.co.kr/df/auction', params=params)
    # save cache
    apiCaches.append({
        'itemName': itemName,
        'info': response.text
    })
    apiCallCount += 1
    # print (f'apiCallCount: {apiCallCount} itemName : {itemName}')
    return response.text


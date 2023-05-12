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
    # response = requests.get('https://api.neople.co.kr/df/auction-sold', params=params)
    response = requests.get('https://api.neople.co.kr/df/auction', params=params)
    # save cache
    apiCaches.append({
        'itemName': itemName,
        'info': response.text
    })
    apiCallCount += 1
    # print (f'apiCallCount: {apiCallCount} itemName : {itemName}')
    return response.text

def getItemPriceDirect(itemName: str):
    info = getItemInfo(itemName)
    return getItemPrice(info)

def getItemPrice(info):
    dict_data = json.loads(info)
    firstItme = dict_data['rows'][0]
    return firstItme['unitPrice']

def getItemSoldDate(info):
    dict_data = json.loads(info)
    firstItme = dict_data['rows'][0]
    return firstItme['soldDate']

def getItemDetails(info, columnName):
    dict_data = json.loads(info)
    firstItme = dict_data['rows'][0]
    return firstItme[columnName]

def showAuctionHistory(auctionHistory: bytearray):
    dict_data = json.loads(auctionHistory)
    firstItme = dict_data['rows'][0]
    print(f'[{ljustk(firstItme["itemName"],18)}][{firstItme["soldDate"]}] UnitPirce: {firstItme["unitPrice"]}')

makeCount = 50
def calcProfit(item:str, condtionList, printDetail=False):
    itemInfo = getItemInfo(item)
    itemPrice = getItemPrice(itemInfo)
    # itemSoldDate = getItemSoldDate(itemInfo)
    itemSoldDate = '' 
    itemSoldCount = getItemDetails(itemInfo, 'count')
    totalPrice = 0
    totalConditionPrice = 0
    for condition in condtionList:
        conditionPrice = getItemPriceDirect(condition[0])
        conditionCount = condition[1]
        conditionPriceTotal = conditionPrice * conditionCount
        totalPrice += conditionPriceTotal
        totalConditionPrice += conditionPriceTotal*makeCount
        if printDetail:
            print(f'({ljustk(condition[0],18)}) {ljustk(str(condition[1]*makeCount),4)} 개 총 {rjustk(conditionPriceTotal*makeCount,8)}원 (개당 {conditionPrice}원)')

    if printDetail: 
        print(f'총 재료비 : {totalConditionPrice}')

    profit = round((itemPrice - totalPrice) * 0.97)
    # profit = round((itemPrice - totalPrice) * 1.05 * 0.97)
    print(f'[{ljustk(item,20)}] 원가 {rjustk(itemPrice, 5)}원 수익 {rjustk(profit, 5)}원 (총 수익 {rjustk(profit*makeCount, 8)}원, 재료비 {rjustk(totalConditionPrice,8)}원) 마지막거래시간:{itemSoldDate} 수량:{itemSoldCount}')



# calcProfit('1', [('생명의 숨결',20),('적색 마력의 산물',1),('노련한 영혼의 정수', 1)])

# 8레벨
# 극상 HP 회복 포션: 생명의 숨결 4개, 황금 가루 4개
# 최상급 생명력의 비약: 생명의 숨결 3개, 황금 가루 5개
# 최상급 마나의 비약: 생명의 숨결 3개, 용의 심장 5개

# 고농축 힘의 비약: 생명의 숨결 5개, 황금 가루 7개
# 고농축 생명력의 비약: 생명의 숨결 5개, 황금 가루 7개
# 스태미너 회복 포션: 생명의 숨결 10개, 황금 큐브 조각 1개

# 11레벨
# calcProfit('고농축 힘의 비약', [('생명의 숨결',5),('황금 가루',7)])
# calcProfit('고농축 생명력의 비약', [('생명의 숨결',5),('황금 가루',7)])
calcProfit('스태미너 회복 포션', [('생명의 숨결',10),('황금 큐브 조각',1)])

# 7레벨
calcProfit('신의 가호', [('생명의 숨결',10),('흰색 마력의 산물',10),('강인한 영혼의 정수', 1)])
calcProfit('순간이동 포션', [('생명의 숨결',1),('무색 마력의 산물',1)])
calcProfit('피로 회복의 영약', [('생명의 숨결',20),('무색 마력의 산물',1),('노련한 영혼의 정수',3),('황금 큐브 조각',3)])
calcProfit('강화의 비밀', [('생명의 숨결',20),('황금 큐브 조각',10),('강인한 영혼의 정수', 5)], printDetail=True)

# 이득이긴 하나 거래물량이 적음
# calcProfit('천상의 HP 포션', [('생명의 숨결',20),('적색 마력의 산물',1),('노련한 영혼의 정수', 1)]) # 이득, 거래물량 적음

# 핵적자
# calcProfit('로톤의 극상 HP 포션', [('생명의 숨결',4),('황금 가루', 4)])
# calcProfit('최상급 생명력의 비약', [('생명의 숨결',3),('황금 가루', 5)])
# calcProfit('최상급 마나의 비약', [('생명의 숨결',3),('용의 심장', 5)])
# calcProfit('천상의 MP 포션', [('생명의 숨결',20),('청색 마력의 산물',1),('노련한 영혼의 정수', 1)])
# calcProfit('슈퍼 아머 포션', [('생명의 숨결',10),('무색 마력의 산물',2)])
# calcProfit('에픽 추적 물약 - 지혜의 인도', [('생명의 숨결',25),('무색 큐브 조각',100), ('황금 가루', 20), ('상급 원소결정', 20)])

# showAuctionHistory(getItemInfo('순간이동 포션'))
# showAuctionHistory(getItemInfo('생명의 숨결'))
# showAuctionHistory(getItemInfo('무색 마력의 산물'))

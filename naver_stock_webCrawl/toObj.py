#from DB import StockInfoStorage as si
from DB.StockInfoStorage import StockPastInfoStorage
import pastInfo as pi
#import getHref as gh
import datetime
'''import getHref as gh'''

"""
global d_final

d_final = pi.fullInfo("096530")
"""


'''
Grab all of the code for kospi & kosdaq
'''

'''
def kospi_code():
    codeArr = gh.getKospiCode()
    return codeArr

def kosdaq_code():
    codeArr = gh.getKosdaqCode()
    return codeArr
'''


def kospi_dict():
    return



def make_kospi_obj(code):
    dict = pi.fullInfo(code)
    objects = []
    for k,v in dict.items():
        """
                code: 주식 코드    (ex. 000660)
                marketType: 증권 시장 종류 (ex. KOSPI)
                highPrice: 고가      lowPrice: 저가       startingPrice: 시가     closingPrice: 종가
                increasingRate: 전일비(%)      tradingVolume: 거래량      datetime: 날짜 (ex. 2019.01.01)
            """
        obj = StockPastInfoStorage(code, "KOSPI", v[3], v[4], v[2], v[0], v[1], v[5], pi.strToDate(k))
        objects.append(obj)


    return objects

def make_kosdaq_obj(code):
    dict = pi.fullInfo(code)
    objects = []
    for k,v in dict.items():
        """
                code: 주식 코드    (ex. 000660)
                marketType: 증권 시장 종류 (ex. KOSPI)
                highPrice: 고가      lowPrice: 저가       startingPrice: 시가     closingPrice: 종가
                increasingRate: 전일비(%)      tradingVolume: 거래량      datetime: 날짜 (ex. 2019.01.01)
            """
        obj = StockPastInfoStorage(code, "KOSDAQ", v[3], v[4], v[2], v[0], v[1], v[5], pi.strToDate(k))
        objects.append(obj)



    return objects











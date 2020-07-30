from DB.StockInfoStorage import StockPastInfoStorage
import past_stock_crawler as crawler


def make_kospi_obj(code):
    dict = crawler.fullInfo(code)
    objects = []
    for k,v in dict.items():
        """
                code: 주식 코드    (ex. 000660)
                marketType: 증권 시장 종류 (ex. KOSPI)
                highPrice: 고가      lowPrice: 저가       startingPrice: 시가     closingPrice: 종가
                increasingRate: 전일비(%)      tradingVolume: 거래량      datetime: 날짜 (ex. 2019.01.01)
            """
        obj = StockPastInfoStorage(code, "KOSPI", v[3], v[4], v[2], v[0], v[1], v[5], crawler.strToDate(k))
        objects.append(obj)

    return objects


def make_kosdaq_obj(code):
    dict = crawler.fullInfo(code)
    objects = []
    for k,v in dict.items():
        """
                code: 주식 코드    (ex. 000660)
                marketType: 증권 시장 종류 (ex. KOSPI)
                highPrice: 고가      lowPrice: 저가       startingPrice: 시가     closingPrice: 종가
                increasingRate: 전일비(%)      tradingVolume: 거래량      datetime: 날짜 (ex. 2019.01.01)
            """
        obj = StockPastInfoStorage(code, "KOSDAQ", v[3], v[4], v[2], v[0], v[1], v[5], crawler.strToDate(k))
        objects.append(obj)

    return objects


def intoDict(objects):

    dicts = []

    for i in range (0,len(objects)):
       dicts.append({"dates": objects[i].getDatetime(), "code": objects[i].getCode(), "closing_price":objects[i].getClosingPrice() ,
                       "increasing_rate": objects[i].getIncreasingRate(), "string_price":objects[i].getStartingPrice() ,
                        "high_price": objects[i].getHighPrice(), "low_price":objects[i].getLowPrice() ,
                       "trading_volume": objects[i].getTradingVolume() , "market_type": objects[i].getMarketType()
                     })

    return dicts







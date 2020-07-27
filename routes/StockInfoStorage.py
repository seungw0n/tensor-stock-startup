#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 13:44:52 2020

@author: stevenjoeng
"""


# Stock information storage _ Version 0.0.1
from datetime import datetime as dt


class StockPastInfoStorage:
    """
        name: 주식 이름    (ex. SK하이닉스)
        code: 주식 코드    (ex. 000660)
        marketType: 증권 시장 종류 (ex. KOSPI)
        highPrice: 고가      lowPrice: 저가       startingPrice: 시가     closingPrice: 종가
        increasingRate: 전일비(%)      tradingVolume: 거래량      datetime: 날짜 (ex. 2019.01.01)
    """
    def __init__(self, code: str, marketType: str,
                 highPrice: float, lowPrice: float, startingPrice: float, closingPrice: float, increasingRate: float,
                 tradingVolume: float, datetime: dt):
        self.__code = code
        self.__marketType = marketType
        self.__highPrice = highPrice
        self.__lowPrice = lowPrice
        self.__startingPrice = startingPrice
        self.__closingPrice = closingPrice
        self.__increasingRate = increasingRate
        self.__tradingVolume = tradingVolume
        self.__datetime = datetime

    # Codes below here are get/set functions
    def getName(self):
        return self.__name
    def setName(self, n):
        self.__name = n

    def getCode(self):
        return self.__code
    def setCode(self, c):
        self.__code = c

    def getMarketType(self):
        return self.__marketType
    def setMarketType(self, t):
        self.__marketType = t

    def getHighPrice(self):
        return self.__highPrice
    def setHighPrice(self, hp):
        self.__highPrice = hp

    def getLowPrice(self):
        return self.__lowPrice
    def setLowPrice(self, lp):
        self.__lowPrice = lp

    def getStartingPrice(self):
        return self.__startingPrice
    def setStartingPrice(self, sp):
        self.__startingPrice = sp

    def getClosingPrice(self):
        return self.__closingPrice
    def setClosingPrice(self, cp):
        self.__closingPrice = cp

    def getIncreasingRate(self):
        return self.__increasingRate
    def setIncreasingRate(self, ir):
        self.__increasingRate = ir

    def getTradingVolume(self):
        return self.__tradingVolume
    def setTradingVolume(self, t_vol):
        self.__tradingVolume = t_vol

    def getDateTime(self):
        return self.__datetime
    def setDateTime(self, dt):
        self.__datetime = dt
    # Codes above here are get/set functions

class StockCurrentInfoStorage:
    """
        name: 주식 이름    (ex. SK하이닉스)
        code: 주식 코드    (ex. 000660)
        marketType: 증권 시장 종류 (ex. KOSPI)
        buyingPrice: 매수 호가      buyingVolume: 매수 물량
        sellingPrice: 매도 호가     sellingVolume: 매도 물량
        highPrice: 고가      lowPrice: 저가       startingPrice: 시가     closingPrice: 종가
        increasingRate: 전일비(%)      tradingVolume: 거래량      datetime: 날짜 (ex. 2019.01.01)
    """
    def __init__(self, code: str, marketType: str,
                 buyingPrice: list, buyingVolume: list, sellingPrice: list, sellingVolume: list,
                 highPrice: float, lowPrice: float, startingPrice: float, closingPrice: float, increasingRate: float,
                 tradingVolume: float, tradingValue: float, tradingTrends: list, datetime: dt):
        self.__code = code
        self.__marketType = marketType
        self.__buyingPrice = buyingPrice
        self.__buyingVolume = buyingVolume
        self.__sellingPrice = sellingPrice
        self.__sellingVolume = sellingVolume
        self.__highPrice = highPrice
        self.__lowPrice = lowPrice
        self.__startingPrice = startingPrice
        self.__closingPrice = closingPrice
        self.__increasingRate = increasingRate
        self.__tradingVolume = tradingVolume
        self.__tradingValue = tradingValue
        self.__tradingTrends = tradingTrends
        self.__datetime = datetime

    '''
    def __init__(self, b_price, s_price, high_price, low_price, trading_volume, trading_value, closing_price, starting_price, inc_price, trading_trends):
        self.__bPrice = b_price
        self.__sPrice = s_price
        self.__highPrice = high_price
        self.__lowPrice = low_price
        self.__tradingVol = trading_volume
        self.__tradingVal = trading_value
        self.__closingPrice = closing_price
        self.__startingPrcie = starting_price
        self.__tradingTrends = trading_trends
    '''
    # Codes below here are get/set functions
    def getName(self):
        return self.__name
    def setName(self, n):
        self.__name = n

    def getCode(self):
        return self.__code
    def setCode(self, c):
        self.__code = c

    def getMarketType(self):
        return self.__marketType
    def setMarketType(self, t):
        self.__marketType = t

    def getBuyingPrice(self):
        return self.__buyingPrice
    def setBuyingPrice(self, bp):
        self.__buyingPrice = bp

    def getBuyingVolume(self):
        return self.__buyingVolume
    def setBuyingVolume(self, bv):
        self.__buyingVolume = bv

    def getSellingPrice(self):
        return self.__sellingPrice
    def setSellingPrice(self, sp):
        self.__sellingPrice = sp

    def getSellingVolume(self):
        return self.__sellingVolume
    def setSellingVolume(self, sv):
        self.__sellingVolume = sv

    def getHighPrice(self):
        return self.__highPrice
    def setHighPrice(self, hp):
        self.__highPrice = hp

    def getLowPrice(self):
        return self.__lowPrice
    def setLowPrice(self, lp):
        self.__lowPrice = lp

    def getStartingPrice(self):
        return self.__startingPrice
    def setStartingPrice(self, sp):
        self.__startingPrice = sp

    def getClosingPrice(self):
        return self.__closingPrice
    def setClosingPrice(self, cp):
        self.__closingPrice = cp

    def getIncreasingRate(self):
        return self.__increasingRate
    def setIncreasingRate(self, ir):
        self.__increasingRate = ir

    def getTradingVolume(self):
        return self.__tradingVolume
    def setTradingVolume(self, t_vol):
        self.__tradingVolume = t_vol

    def getTradingValue(self):
        return self.__tradingValue
    def setTradingValue(self, t_val):
        self.__tradingValue = t_val

    def getTradingTrends(self):
        return self.__tradingTrends
    def setTradingTrends(self, tt):
        self.__tradingTrends = tt

    def getDateTime(self):
        return self.__datetime
    def setDateTime(self, dt):
        self.__datetime = dt
    # Codes above here are get/set functions
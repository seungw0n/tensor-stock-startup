#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 13:44:52 2020

@author: stevenjoeng
"""


# Stock information storage _ Version 0.0.1

class StockInfoStorage:

    def __init__(self, s_type, name, b_price, s_price, high_price, low_price, trading_volume, trading_value, closing_price, starting_price, inc_rate, trading_trends):
        self.__sType = s_type
        self.__name = name
        self.__bPrice = b_price
        self.__sPrice = s_price
        self.__highPrice = high_price
        self.__lowPrice = low_price
        self.__tradingVol = trading_volume
        self.__tradingVal = trading_value
        self.__closingPrice = closing_price
        self.__startingPrcie = starting_price
        self.__tradingTrends = trading_trends
        self.__increasingRate = inc_rate

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

    def getType(self):
        return self.__sType
    def setType(self, t):
        self.__sType = t
    
    def getName(self):
        return self.__name
    def setName(self, n):
        self.__name = n
    
    def getBuyingPrice(self):
        return self.__bPrice
    def setBuyingPrice(self, bp):
        self.__bPrice = bp
    
    def getSellingPrice(self):
        return self.__sPrice
    def setSellingPrice(self, sp):
        self.__sPrice = sp
    
    def getHighPrice(self):
        return self.__highPrice
    def setHighPrice(self, hp):
        self.__highPrice = hp
    
    def getLowPrice(self):
        return self.__lowPrice
    def setLowPrice(self, lp):
        self.__lowPrice = lp
    
    def getTradingVolume(self):
        return self.__tradingVol
    def setTradingVolume(self, t_vol):
        self.__tradingVol = t_vol
    
    def getTradingValue(self):
        return self.__tradingVal
    def setTradingValue(self, t_val):
        self.__tradingVal = t_val
    
    def getClosingPrice(self):
        return self.__closingPrice
    def setClosingPrice(self, cp):
        self.__closingPrice = cp
    
    def getStartingPrice(self):
        return self.__startingPrcie
    def setStartingPrice(self, sp):
        self.__startingPrice = sp
    
    def getTradingTrends(self):
        return self.__tradingTrends
    def setTradingTrends(self, tt):
        self.__tradingTrends = tt
        
    def getIncreasingRate(self):
        return self.__increasingRate
    def setIncreasingRate(self, ir):
        self.__increasingRate = ir
    
    # Codes above here are get/set functions
    
    '''
    Function getMA(n) returns n-day moving average
    MA(Moving Average): 이동평균선
    '''

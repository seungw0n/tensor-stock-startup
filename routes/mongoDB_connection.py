#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 13:13:40 2020

@author: stevenjoeng
"""

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

import importlib.util
from .StockInfoStorage import StockCurrentInfoStorage
from .StockInfoStorage import StockPastInfoStorage

"""
operation types:
    create

ex) 
obj = StockPastInfoStorage(....)
connect(create, obj)
or
connect(delete_all)
"""

def connect(self, operation: str, obj = None):

    spec = importlib.util.spec_from_file_location("accounts", "../config/accounts.py")
    accounts = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(accounts)
    _username = accounts.mongoAccount['username']
    _password = accounts.mongoAccount['password']

    # Connect to Cluster0-Tester
    global client
    global db
    global collection

    try:
        client = MongoClient(host='mongodb+srv://' + self.__USERNAME + ':' + self.__PASSWORD + '@cluster0-tester.cwbjo.mongodb.net/<Cluster0-Tester>?retryWrites=true&w=majority',
                                  maxPoolSize=100, socketTimeoutMS=20000, connectTimeoutMS=20000, serverSelectionTimeoutMS=20000)
        print(self.client)
    except ConnectionFailure:
        print("Connection Error")


    '''
    # Create a database object referencing a new database, called "test"
    db = client.test
    '''
    if obj is not None:
        if isinstance(obj, StockPastInfoStorage):
            db = client["Past"]
            collection = db[obj.getCode()]
            if operation == "create":
                create_past_info(obj)


        if isinstance(obj, StockCurrentInfoStorage):
            db = client["Current"]
            collection = db[obj.getCode()]
            if operation == "create":
                create_past_info(obj)




    db = client["test"]
    collection = db["test"]

    """
    if operation == "deleteAll":
        deleteAll()


    if obj is not None:
        if operation == "create":
            create(obj)
        else:
            print("Invalid Operation, Try again - DB connection is automatically closed.")
            client.close()
        '''
        elif operation == "read":
            read(obj)
        elif operation == "update":
            update(obj)
        elif operation == "delete":
            delete(obj)
        '''
    """

def closeConnection(self):
    client.close()
    print("Connection closed")


# Need to be added trading_trends later.
def create_past_info(self, obj):
    """
            name: 주식 이름    (ex. SK하이닉스)
            code: 주식 코드    (ex. 000660)
            marketType: 증권 시장 종류 (ex. KOSPI)
            highPrice: 고가      lowPrice: 저가       startingPrice: 시가     closingPrice: 종가
            increasingRate: 전일비(%)      tradingVolume: 거래량      datetime: 날짜 (ex. 2019.01.01)
        """
    tmp = {"code": obj.getCode(), "marketType": obj.getMarketType(),
           "highPrice": obj.getHighPrice(), "lowPrice": obj.getLowPrice(),
           "startingPrice": obj.getStartingPrice(), "closingPrice": obj.getClosingPrice(),
           "increasingRate": obj.getIncreasingRate(), "tradingVolume": obj.getTradingVolume(),
           "datetime": obj.getDatetime()
           }

    result = collection.insert_one(tmp)

    if result != "":
        print("Success: " + str(result.inserted_id) + " - Create")
    else:
        print("Failure - Create")


def create_cur_info(self, obj):
    tmp = {"code": obj.getCode(), "marketType": obj.getMarketType(),
           "buyingPrice": obj.getBuyingPrice(), "buyingVolume": obj.getBuyingVolume(),
           "sellingPrice": obj.getSellingPrice(), "sellingVolume": obj.getSellingVolume(),
           "highPrice": obj.getHighPrice(), "lowPrice": obj.getLowPrice(),
           "startingPrice": obj.getStartingPrice(), "closingPrice": obj.getClosingPrice(),
           "increasingRate": obj.getIncreasingRate(), "tradingVolume": obj.getTradingVolume(),
           "tradingValue": obj.getTradingValue(), "tradingTrends": obj.getTradingTrends(),
           "datetime": obj.getDatetime()
           }
    result = collection.insert_one(tmp)

    if result != "":
        print("Success: " + str(result.inserted_id) + " - Create")
    else:
        print("Failure - Create")


"""
def delete_all(self, col):
    x = col.delete_many({})
    print(x.deleted_count, " documents successfully deleted")

"""


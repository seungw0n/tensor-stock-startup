#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 13:13:40 2020

@author: stevenjoeng
"""

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
# import datetime

import importlib.util
from StockInfoStorage import StockCurrentInfoStorage
from StockInfoStorage import StockPastInfoStorage

"""
operation types:
    create
"""

def connect(operation: str, obj = None):

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
        client = MongoClient(host='mongodb+srv://' + _username + ':' + _password + '@cluster0-tester.cwbjo.mongodb.net/<Cluster0-Tester>?retryWrites=true&w=majority',
                                  maxPoolSize=100, socketTimeoutMS=30000, connectTimeoutMS=30000, serverSelectionTimeoutMS=30000)
        print(client)
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

def closeConnection():
    client.close()
    print("Connection closed")


# Need to be added trading_trends later.
def create_past_info(obj):

    tmp = {"code": obj.getCode(), "marketType": obj.getMarketType(),
           "highPrice": obj.getHighPrice(), "lowPrice": obj.getLowPrice(),
           "startingPrice": obj.getStartingPrice(), "closingPrice": obj.getClosingPrice(),
           "increasingRate": obj.getIncreasingRate(), "tradingVolume": obj.getTradingVolume(),
           "date": obj.getDatetime()
           }

    result = collection.insert_one(tmp)

    if result != "":
        print("Success: " + str(result.inserted_id) + " - Create")
    else:
        print("Failure - Create")


def create_cur_info(obj):
    tmp = {"code": obj.getCode(), "marketType": obj.getMarketType(),
           "buyingPrice": obj.getBuyingPrice(), "buyingVolume": obj.getBuyingVolume(),
           "sellingPrice": obj.getSellingPrice(), "sellingVolume": obj.getSellingVolume(),
           "highPrice": obj.getHighPrice(), "lowPrice": obj.getLowPrice(),
           "startingPrice": obj.getStartingPrice(), "closingPrice": obj.getClosingPrice(),
           "increasingRate": obj.getIncreasingRate(), "tradingVolume": obj.getTradingVolume(),
           "tradingValue": obj.getTradingValue(), "tradingTrends": obj.getTradingTrends(),
           "date": obj.getDatetime()
           }
    result = collection.insert_one(tmp)

    if result != "":
        print("Success: " + str(result.inserted_id) + " - Create")
    else:
        print("Failure - Create")


"""
def delete_all(col):
    x = col.delete_many({})
    print(x.deleted_count, " documents successfully deleted")

"""
"""
d = datetime.datetime(2019, 12, 11)
obj = StockPastInfoStorage(
    "12345", "KOSPI", 12.11, 12.11, 12.12, 12.12, 12.12, 12.12, d
)

connect("create", obj)
"""
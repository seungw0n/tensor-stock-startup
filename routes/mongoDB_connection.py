#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 13:13:40 2020

@author: stevenjoeng
"""

import pymongo
from pymongo import MongoClient
import importlib.util
from StockInfoStorage import StockInfoStorage

spec = importlib.util.spec_from_file_location("accounts", "../config/accounts.py")
accounts = importlib.util.module_from_spec(spec)
spec.loader.exec_module(accounts)


USERNAME = accounts.mongoAccount['username']
PASSWORD = accounts.mongoAccount['password']


def connect(operation, obj: StockInfoStorage):
    
    # Connect to Cluster0-Tester
    global client
    global db
    global collection
    
    client = MongoClient('mongodb+srv://' + USERNAME + ':' + PASSWORD + 
                         '@cluster0-tester.cwbjo.mongodb.net/<Cluster0-Tester>?retryWrites=true&w=majority')
    
    '''
    # Create a database object referencing a new database, called "test"
    db = client.test
    '''
    
    
    db = client["test"]
    collection = db["test"]
    

    
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
    client.close()

# Need to be added trading_trends later.
def create(obj: StockInfoStorage):
    tmp = {"name": obj.getName(), "buying_price": obj.getBuyingPrice(), "selling_price": obj.getSellingPrice(),
           "high_price": obj.getHighPrice(), "low_price": obj.getLowPrice(), "starting_price": obj.getStartingPrice(),
           "closing_price": obj.getClosingPrice(), "trading_volume": obj.getTradingVolume(),
           "trading_value": obj.getTradingValue()}
    
    result = collection.insert_one(tmp)
    
    if result != "":
        print("Success: " + str(result.inserted_id) + " - Create")
    else:
        print("Failure - Create")



if __name__ == "__main__":
    print("Start")
    obj = StockInfoStorage("blue_chip", "Samsung", 123.23, 112.99, 145.12, 110.14, 123456, 123456, 123.11, 123.11, 123.11, 123.11)
    
    
    
    connect("create", obj)
    print("End")



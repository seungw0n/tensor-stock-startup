#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 13:13:40 2020

@author: stevenjoeng
"""

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import importlib.util
from StockInfoStorage import StockInfoStorage

class MongoDB_Connection:

    def __init__(self):
        spec = importlib.util.spec_from_file_location("accounts", "../config/accounts.py")
        accounts = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(accounts)

        self.__USERNAME = accounts.mongoAccount['username']
        self.__PASSWORD = accounts.mongoAccount['password']


    def connect(self, obj: StockInfoStorage = None):

        # Connect to Cluster0-Tester
        global db
        global collection

        try:
            self.client = MongoClient(host='mongodb+srv://' + self.__USERNAME + ':' + self.__PASSWORD + '@cluster0-tester.cwbjo.mongodb.net/<Cluster0-Tester>?retryWrites=true&w=majority',
                                      maxPoolSize=100, socketTimeoutMS=1000, connectTimeoutMS=20000, serverSelectionTimeoutMS = 3000
                                      )
            print(self.client)
        except ConnectionFailure:
            print("Connection Error")



        '''
        # Create a database object referencing a new database, called "test"
        db = client.test
        '''


        db = self.client["test"]
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
        #self.client.close()

    def closeConnection(self):
        self.client.close()
        print("Connection closed")


    # Need to be added trading_trends later.
    def create(self, obj: StockInfoStorage):
        tmp = {"name": obj.getName(), "code": obj.getCode(), "marketType": obj.getMarketType(),
               "buyingPrice": obj.getBuyingPrice(), "buyingVolume": obj.getBuyingVolume(),
               "sellingPrice": obj.getSellingPrice(), "sellingVolume": obj.getSellingVolume(),
               "highPrice": obj.getHighPrice(), "lowPrice": obj.getLowPrice(),
               "startingPrice": obj.getStartingPrice(), "closingPrice": obj.getClosingPrice(),
               "increasingRate": obj.getIncreasingRate(), "tradingVolume": obj.getTradingVolume(),
               "tradingValue": obj.getTradingValue(), "tradingTrends": obj.getTradingTrends()
               }
        result = collection.insert_one(tmp)

        if result != "":
            print("Success: " + str(result.inserted_id) + " - Create")
        else:
            print("Failure - Create")

    def deleteAll(self):
        x = collection.delete_many({})
        print(x.deleted_count, " documents successfully deleted")





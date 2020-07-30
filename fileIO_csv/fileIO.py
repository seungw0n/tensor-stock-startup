#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29

@author: stevenjoeng
"""

import csv
import os
from DB.StockInfoStorage import *

path = os.path.join(os.pardir, "resources/records")
csv_columns = ["CODE", "DATES", "HIGH_PRICE", "LOW_PRICE", "STARTING_PRICE", "CLOSING_PRICE", "INCREASING_PRICE", "TRADING_VOLUME"]


"""
function convert_to_dictionaries for multiple objects
@ Parameter:
    A list of StockPastInfoStorage objects
@ Post:
    Return a dictionary list
"""
def convert_to_dictionaries(objects : list):
    dict_list = []

    for obj in objects:
        dict_list.append({
            "CODE": obj.getCode(), "DATES": obj.getDatetime(), "HIGH_PRICE": obj.getHighPrice(), "LOW_PRICE": obj.getLowPrice(),
            "STARTING_PRICE": obj.getStartingPrice(), "CLOSING_PRICE": obj.getClosingPrice(), "INCREASING_PRICE": obj.getIncreasingRate(),
            "TRADING_VOLUME": obj.getTradingVolume()
        })

    return dict_list

"""
function convert_to_dictionary for a single object
@ Parameter:
    A StockPastInfoStorage object
@ Post:
    Return a dictionary
"""
def convert_to_dictionary(obj: StockPastInfoStorage):
    dict = {"CODE": obj.getCode(), "DATES": obj.getDatetime(), "HIGH_PRICE": obj.getHighPrice(), "LOW_PRICE": obj.getLowPrice(),
             "STARTING_PRICE": obj.getStartingPrice(), "CLOSING_PRICE": obj.getClosingPrice(),
             "INCREASING_PRICE": obj.getIncreasingRate(), "TRADING_VOLUME": obj.getTradingVolume()
             }

    return dict

"""
function create_csv
@ Parameter:
    A list of StockPastInfoStorage objects
@ Post:
    Create and write csv file: ./resources/records/_CODE_.csv
    
"""
def create_csv(objects):
    dicts = convert_to_dictionaries(objects)

    filename = dicts[0].get('CODE') + ".csv"
    full_path = os.path.join(path, filename)

    try:
        with open(full_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=csv_columns)
            writer.writeheader()
            for data in dicts:
                writer.writerow(data)
        print("Success")
    except IOError:
        print("File not founded: " + full_path)


"""
function add_datum for a single object
@ Parameter:
    A StockPastInfoStorage object
@ Post:
    Update a csv file: ./resources/records/_CODE_.csv
"""
def add_datum(obj):
    dict = convert_to_dictionary(obj)

    filename = dict.get("CODE") + ".csv"
    full_path = os.path.join(path, filename)

    try:
        with open(full_path, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=csv_columns)
            writer.writerow(dict)
        print("Success")
    except IOError:
        print("File not found: " + full_path)


"""
function add_data for multiple objects
@ Parameter:
    A list of StockPastInfoStorage objects
@ Post:
    Update a csv file: ./resources/records/_CODE_.csv
"""
def add_data(objects):
    dicts = convert_to_dictionaries(objects)

    filename = dicts[0].get("CODE") + ".csv"
    full_path = os.path.join(path, filename)

    try:
        with open(full_path, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=csv_columns)
            writer.writerows(dicts)
        print("Success")
    except IOError:
        print("File not found: " + full_path)
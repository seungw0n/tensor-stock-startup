from StockInfoStorage import StockInfoStorage
from mongoDB_connection import MongoDB_Connection
import time


print("Start")

'''
def __init__(self, name, code, marketType,
             buyingPrice, buyingVolume, sellingPrice, sellingVolume,
             highPrice, lowPrice, startingPrice, closingPrice, increasingRate,
             tradingVolume, tradingValue, tradingTrends):
'''
conn = MongoDB_Connection()
storageOne = StockInfoStorage("LG", "123456", "KOSPI",
                              [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5],
                              123.12, 123.12, 123.12, 123.12, 123.12,
                              123.12, 123.12, 123.12)
start = time.time()
conn.connect()
print(time.time() - start)



print("Finish")

'''
print("Start to check deleteAll()")
connect("deleteAll")
print("Finish")
'''
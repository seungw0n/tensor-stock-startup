import toObj

def intoDict (objArr):

    dictArr = []

    for i in range (0,len(objArr)):
       dictArr.append({"dates": objArr[i].getDatetime(), "code": objArr[i].getCode(), "closing_price":objArr[i].getClosingPrice() ,
                       "increasing_rate": objArr[i].getIncreasingRate(), "string_price":objArr[i].getStartingPrice() ,
                        "high_price": objArr[i].getHighPrice(), "low_price":objArr[i].getLowPrice() ,
                       "trading_volume": objArr[i].getTradingVolume() , "market_type": objArr[i].getMarketType(),

        })

    return dictArr



objArr = toObj.make_kospi_obj("096530")

print (intoDict(objArr))




"""
Created on Sat Jul 25 23:00:52 2020

@author: kwanyeobjung
"""
import time
import requests
from bs4 import BeautifulSoup


def kospiAndDaq(s, p):
    url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok={}&page={}".format(s, p)
    request = requests.get(url)
    bs_obj = BeautifulSoup(request.content, "html.parser")
    return bs_obj


def getHrefs(bs_obj):
    table = bs_obj.find("table", {"class": "type_2"})
    trs = table.findAll("tr")
    '''
    After find all tr, we need to fliter tds (bevasuse the hrefs are inside <td> tags)
    '''

    stringTr = []
    for i in range(2, len(trs)):
        stringTr.append(trs[i].findAll("td"))

    '''
    After collecting all tds, we need to sort out the error. Because some of tds do not have
    info that we want. 

    As catching the error for not having info we can only have the td that we want 
    '''

    tmp = []

    for i in range(0, len(stringTr)):

        try:
            tmp.append(stringTr[i][1])

        except Exception as e:
            pass
    '''
    Then, we transform the href into string and cut into a proper range. 
    '''

    res = []
    for i in range(0, len(tmp)):
        strArr = str(tmp[i])
        res.append(strArr[27:53])




    return res


def getCode(bs_obj):
    table = bs_obj.find("table", {"class": "type_2"})
    trs = table.findAll("tr")

    '''
    After find all tr, we need to fliter tds (bevasuse the hrefs are inside <td> tags)
    '''

    stringTr = []
    for i in range(2, len(trs)):
        stringTr.append(trs[i].findAll("td"))

    '''
    After collecting all tds, we need to sort out the error. Because some of tds do not have
    info that we want. 

    As catching the error for not having info we can only have the td that we want 
    '''

    tmp = []

    for i in range(0, len(stringTr)):

        try:
            tmp.append(stringTr[i][1])

        except Exception as e:
            pass
    '''
    Then, we transform the href into string and cut into a proper range. 
    '''

    res = []
    for i in range(0, len(tmp)):
        strArr = str(tmp[i])
        res.append(strArr[47:53])

    return res


'''
Getting all of the href url for kospi and kosdaq and the corresponding codes 
'''


def getKospi():
    result = []
    for i in range(1, 33):
        obj = kospiAndDaq(0, i)
        result.append(getHrefs(obj))
    return result


def getKosdaq():
    result = []
    for i in range(1, 29):
        obj = kospiAndDaq(1, i)
        result.append(getHrefs(obj))
    return result


def getKospiCode():
    result = []
    for i in range(1, 33):
        obj = kospiAndDaq(0, i)
        result.append(getCode(obj))
    return result


def getKosdaqCode():
    result = []
    for i in range(1, 30):
        obj = kospiAndDaq(1, i)
        result.append(getCode(obj))



    return result


startingTime = time.time()
'''
print(len(getKospi()))
print("---------------------------------------")

print (len(getKospi()))
print("---------------------------------------")

print (getKosdaq())
print(len(getKosdaq))
print("---------------------------------------")

print(getKospiCode())
print(len(getKospiCode()))
print("---------------------------------------")
'''
print(getKosdaqCode())

print("---------------------------------------")

print("-----%d-----" % (time.time() - startingTime))

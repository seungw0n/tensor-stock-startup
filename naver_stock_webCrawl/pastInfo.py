"""
Created on Fri Jul 24 14:37:37 2020

@author: kwanyeobjung
"""

import time
import requests
import datetime
from bs4 import BeautifulSoup


global final

def controlPage(code, page):
    url = "https://finance.naver.com/item/sise_day.nhn?code={}&page={}".format(code, page)
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

def strToDate (str):
    tmp = str.split(".") # 2019.01.01 --> tmp = {"2019", "01", "01"}
    date = datetime.datetime(int(tmp[0]), int(tmp[1]), int(tmp[2]))
    return date



def byDayFirstHalf(bs_obj):
    table = bs_obj.find("table", {"class": "type2"})
    trs = table.findAll("tr")

    '''
    Initialize all the data structures that I need.
    '''

    tds = []
    result = []
    dates = []

    ''' 
    This for loop is accessing all the boxes from top to bottom. 
    One box contains all the info that we want such as inc rate, highest price, lowest price etc.
    '''
    for i in range(2, 7):
        trsFirstHalf = trs[i]
        tds.append(trsFirstHalf.findAll("td"))

    '''
    This forloop is just to grab dates ONLY. 
    I want the dates to be the key and the rest to be the values. 
    That is why I made a seperate for loop to initialize the dates as keys 
    '''
    for i in range(0, 5):
        # Changed
        dates.append(tds[i][0].text)
        #dates.append(strToDate(tds[i][0].text))

    '''
    Initialize the keys
    '''


    d = {key: [] for key in dates}

    '''
    This for loop is just for values. I store all of the values in an array. 
    Result contains all the info EXCEPT for the dates 

    '''
    for i in range(0, 5):
        for j in range(1, 7):
            result.append(nospaceToInt(tds[i][j].text))

    '''
    Now initialize the values to a key. 6 different infos regarding the dates must be 
    initialized as values. 
    After looping 6 times, move on to the next key and store the next 6 info. 


    The logic between this part is simple but in terms of coding, it might be confusing.
    I have a result array which is the array of all the info that I need to initalize to
    the right key. 

    Also to assign the values to a key, I need to know the key. So I brought dates array 
    which is the array of keys and specifies which key that I am pointing. 

    A key has to have 6 infos. So while the for loop is running, I made a counter variable 
    to count when it reaches the 6th element. Then I increment index by 1 and multiply variable
    by 1. 

    So that the key will be the second element of the key array(dates) and counter will be 
    updated to 12 which will make only store 6 elements to the next key.   
    '''
    counter = 0
    index = 0
    multiply = 1
    for i in range(0, len(result)):
        counter += 1
        d[dates[index]].append(result[i])

        if counter == 6 * multiply:
            index += 1
            multiply += 1
        if counter == len(result):
            break

    return d


def byDaySecondHalf(bs_obj):
        table = bs_obj.find("table", {"class": "type2"})
        trs = table.findAll("tr")

        '''
        Initialize all the data structures that I need.
        '''

        tds = []
        result = []
        dates = []
        ''' Dictionary should be accessed anywhere'''


        ''' 
        This for loop is accessing all the boxes from top to bottom. 
        One box contains all the info that we want such as inc rate, highest price, lowest price etc.
        '''
        for i in range(10, 15):
            trsFirstHalf = trs[i]
            tds.append(trsFirstHalf.findAll("td"))

        '''
        This forloop is just to grab dates ONLY. 
        I want the dates to be the key and the rest to be the values. 
        That is why I made a seperate for loop to initialize the dates as keys 
        '''
        for i in range(0, 5):
            # Changed
            dates.append(tds[i][0].text)
            #dates.append(strToDate(tds[i][0].text))

        '''
        Initialize the keys
        '''

        d1 = {key: [] for key in dates}

        '''
        This for loop is just for values. I store all of the values in an array. 
        Result contains all the info EXCEPT for the dates 
    
        '''
        for i in range(0, 5):
            for j in range(1, 7):
                result.append(nospaceToInt(tds[i][j].text))

        '''
        Now initialize the values to a key. 6 different infos regarding the dates must be 
        initialized as values. 
        After looping 6 times, move on to the next key and store the next 6 info. 
    
    
        The logic between this part is simple but in terms of coding, it might be confusing 
        so I have a result array which is the array of all the info that I need to initalize to
        the right key. 
    
        Also to assign the values to a key, I need to know the key. So I brought dates array 
        which is the array of keys and specifies which key that I am pointing. 
    
        A key has to have 6 infos. So while the for loop is running, I made a counter variable 
        to count when it reaches the 6th element. Then I increment index by 1 and multiply variable
        by 1. 
    
        So that the key will be the second element of the key array(dates) and counter will be 
        updated to 12 which will make only store 6 elements to the next key.   
        '''
        counter = 0
        index = 0
        multiply = 1
        for i in range(0, len(result)):
            counter += 1
            d1[dates[index]].append(result[i])

            if counter == 6 * multiply:
                index += 1
                multiply += 1
            if counter == len(result):
                break

        return d1


def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res


def find (dates):
    return final.get(dates)


def nospaceToInt(txt):
    txt = txt.replace("\n", '')
    txt = txt.replace("\t", '')
    txt = txt.replace(",", '')
    txt = txt.replace(".", '')
    tmp = float(txt)
    result = int(tmp)
    return result


def getTheLastPage(code):
    url = "https://finance.naver.com/item/sise_day.nhn?code={}".format(code)
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    table = bs_obj.find("table", {"class":"Nnavi"})
    tds = table.findAll("td")

    '''
    Find all the tds and store in an array. The last element of td it has the number of the last page.
    Need to extract the number. 
    So excess the last element and extract <a> tag. 
    Convert into String and cut within the range that I have set up. And switch the string (number) into integer
    
    However some of the page has three digit. So catch an error and shorten the range in order to extract smaller 
    digit of the number. 
    
    '''
    length = len(tds)-1
    tmp = tds[length]
    a = tmp.find("a")
    stringA = str(a)
    cut = stringA[49:52]

    try:
        intCut = int(cut)
        
    except Exception as e:
        intCut = int(stringA[49:51])
        pass

    return intCut


def lastPageFirstHalf(code):
    page = getTheLastPage(code)
    url = "https://finance.naver.com/item/sise_day.nhn?code={}&page={}".format(code,page)
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    table = bs_obj.find("table", {"class": "type2"})
    trs = table.findAll("tr")
    tds = []
    dates = []
    result = []
    for i in range(2, 7):
        trsFirstHalf = trs[i]
        tds.append(trsFirstHalf.findAll("td"))

    for i in range(0, 5):

        if tds[i][0].text != '\xa0':
            # changed
            tmp = tds[i][0].text
            # tmp = strToDate(tds[i][0].text)
            dates.append(tmp)

    d1 = {key: [] for key in dates}

    length = len(dates)

    for i in range(0, length):
        for j in range(1, 7):
            result.append(nospaceToInt(tds[i][j].text))
    counter = 0
    index = 0
    multiply = 1
    for i in range(0, len(result)):
        counter += 1
        d1[dates[index]].append(result[i])

        if counter == 6 * multiply:
            index += 1
            multiply += 1
        if counter == len(result):
            break


    return d1

'''
The second half of the last page has a lot of retrictions. I have to handle if second half is not filled at all, 
second half is filled but not fully. 
Therefore, I have if statements to make sure I elimate the not filled up part. 
'''

def lastPageSecondHalf(code):
    page = getTheLastPage(code)
    url = "https://finance.naver.com/item/sise_day.nhn?code={}&page={}".format(code, page)
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    table = bs_obj.find("table", {"class": "type2"})
    trs = table.findAll("tr")
    tds = []
    dates = []
    result = []

    for i in range(10, 15):
        trsFirstHalf = trs[i]
        tds.append(trsFirstHalf.findAll("td"))

    for i in range(0, 5):
        if tds[i][0].text != '\xa0':
            dates.append(tds[i][0].text)

    if len(dates) == 0:
        return {}
    else:
        d0 = {key: [] for key in dates}

        length = len(dates)

        for i in range(0, length):
            for j in range(1, 7):
                result.append(nospaceToInt(tds[i][j].text))
        counter = 0
        index = 0
        multiply = 1
        for i in range(0, len(result)):
            counter += 1
            d0[dates[index]].append(result[i])

            if counter == 6 * multiply:
                index += 1
                multiply += 1
            if counter == len(result):
                break



    return d0



def getLastPageFull(code):
    d1 = lastPageFirstHalf(code)
    d2= lastPageSecondHalf(code)

    d = Merge(d1,d2)

    return d


'''
This is the dictionary formation of the info without the last page.

'''

def lastPageMissing (code):

    lastPage = getTheLastPage(code)

    finalFinal = {}
    for i in range (1,lastPage):
        obj = controlPage(code, i)
        diction = byDayFirstHalf(obj)
        diction1 = byDaySecondHalf(obj)
        res = Merge(diction,diction1)
        finalFinal.update(res)

    return finalFinal

'''
Combine all the info together 
'''
def fullInfo (code):

    d1 = lastPageMissing(code)
    d2 = getLastPageFull(code)
    final = Merge(d1,d2)

    return final



'''
startingTime = time.time()
print(fullInfo("096530"))
print("-----%d-----" % (time.time() - startingTime))
'''



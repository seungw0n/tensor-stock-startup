"""
@author: steven joeng
Description:
    Downloading files from Yahoo Finance
"""

from pandas_datareader import data as pdr
import pandas as pd
import numpy as np
import yfinance as yf
import os


yf.pdr_override()

def save_data_from_yf(saving_path, code, ticker_name, start, end):
    df = pdr.get_data_yahoo(ticker_name, start=start, end=end)
    df.values[1:].astype(np.float)
    path = os.path.join(saving_path, (code + '.csv'))
    df.to_csv(path)


def modify_csv_file(path):
    # return pd.read_csv(path)
    # Date,Open,High,Low,Close,Adj Close,Volume
    df = pd.read_csv(path,
                     names=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'],
                     encoding='euc-kr',
                     header=0
                     )
    del df['Adj Close']

    df.columns.values[0] = "DATE"
    df.columns.values[1] = "STARTING_PRICE"
    df.columns.values[2] = "HIGH_PRICE"
    df.columns.values[3] = "LOW_PRICE"
    df.columns.values[4] = "CLOSING_PRICE"
    df.columns.values[5] = "TRADING_VOLUME"

    dates = df['DATE']
    for i in range(0, len(dates)):
        dates[i] = dates[i].replace('-','')

    df.to_csv(path, index=False)



"""
-------------------------------------EXAMPLE---------------------------------------
"""
csv_list = [
    '005490', '005930', '011170', '012330', '035720', '036570',
    '051900', '051910', '207940', '316140'
]


for l in csv_list:
    saving_path = os.path.join('..', 'records')
    save_data_from_yf(saving_path, l, l+'.KS', '2020-08-03', '2020-09-05')
    path = os.path.join(saving_path, l + '.csv')
    modify_csv_file(path)


# save_data_from_yf(csv_list[0], csv_list[0]+'.KS', '2020-08-03', '2020-09-01')
# path = os.path.join('..', csv_list[0] + '.csv')
# modify_csv_file(path)

"""
-------------------------------------EXAMPLE---------------------------------------
"""
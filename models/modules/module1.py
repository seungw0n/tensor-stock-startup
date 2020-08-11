import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

from sklearn.preprocessing import MinMaxScaler
from keras import Sequential, backend
from keras.layers import LSTM, Dropout, Dense, Activation
import datetime as dt

def divisor():
    print('=' * 100)

def read_csv(directory_name,code):
    path = os.path.join(os.pardir, 'resources/records/day_records', directory_name, code + '.csv')
    return pd.read_csv(path)

def min_max_scaler(data):
    try:
        return (np.asarray(data)-np.asarray(data).min()) / (np.asarray(data).max() - np.asarray(data).min())
    except ZeroDivisionError:
        return (np.asarray(data)-np.asarray(data).min()) / (np.asarray(data).max() - np.asarray(data).min() + 1e-7)

def setup_date(data):
    data['DATE'] = pd.to_datetime(data['DATE'], format='%Y%m%d')
    data['YEAR'] = data['DATE'].dt.year
    data['MONTH'] = data['DATE'].dt.month
    data['DAY'] = data['DATE'].dt.day
    df_data = data.loc[data['YEAR'] >= 1980]
    return df_data

"""
ex) x_axis = 'DATE', y_axis = 'CLOSING_PRICE'
"""
def pre_graph(df, x_axis: str, y_axis: str):
    plt.figure(figsize=(16, 9))
    sns.lineplot(y=df[y_axis], x=df[x_axis])
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.show()

def scale_columns():
    return ['STARTING_PRICE', 'HIGH_PRICE', 'LOW_PRICE', 'CLOSING_PRICE', 'TRADING_VOLUME']

def get_scaled_data(df, scale_cols):
    scaler = MinMaxScaler()
    df_scaled = scaler.fit_transform(df[scale_cols])
    return df_scaled


"""
HOW TO USE THEM ?
CODE EXAMPLE


"""
# EXAMPLE CODE
raw_data = read_csv("COSMETIC", "002790")
df_data = setup_date(raw_data)

pre_graph(df_data, 'DATE', 'CLOSING_PRICE')
divisor()
df_scaled = get_scaled_data(df_data, scale_columns())
# Below code is to test this function
df_scaled = pd.DataFrame(df_scaled)
df_scaled.columns = scale_columns()
print(df_scaled)
# Above code is to test this function
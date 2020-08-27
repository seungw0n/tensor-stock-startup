"""
Created on Sun Aug  2 21:14:12 2020

@author: stevenjoeng
"""

import pandas as pd
import numpy as np
import os


def divisor():
    print('=' * 100)

def window_sizes():
    return [i for i in range(1, 91) if i % 5 == 0]

def read_csv(directory_name,code):
    p = os.path.join('..', os.pardir)
    path = os.path.join(p, 'resources/records/day_records', directory_name, code + '.csv')
    #return pd.read_csv(path)
    return pd.read_csv(path,
                       names=['DATE','STARTING_PRICE','HIGH_PRICE','LOW_PRICE','CLOSING_PRICE','TRADING_VOLUME'],
                       encoding='euc-kr'
                       )

def read_target_csv(directory_name, code):
    p = os.path.join('..', os.pardir)
    path = os.path.join(p, 'resources/records/target_records', directory_name, code + '.csv')

    return pd.read_csv(path,
                       names=['DATE','STARTING_PRICE','HIGH_PRICE','LOW_PRICE','CLOSING_PRICE','TRADING_VOLUME'],
                       encoding='euc-kr'
                       )

def data_vectorization(raw_data):
    del raw_data['DATE'] #delete DATE
    return raw_data.values[1:].astype(np.float)

def data_reverse_order(vectorized_data):
    return vectorized_data[::-1]

def min_max_scaling(x):
    xnp = np.asarray(x)
    return (xnp - xnp.min()) / (xnp.max() - xnp.min() + 1e-7)

def data_normalization(vectorized_data):
    # 'STARTING_PRICE','HIGH_PRICE','LOW_PRICE','CLOSING_PRICE'
    prices = vectorized_data[:, :-1]
    scaled_prices = min_max_scaling(prices)
    #print("Normalized price: ", scaled_prices[0])

    # 'TRADING_VOLUME'
    volumes = vectorized_data[:,-1:]
    scaled_volumes = min_max_scaling(volumes)
    #print("Normalized volume: ", scaled_volumes[0])

    # Concatenate two metrics based on y-axis
    return np.concatenate((scaled_prices, scaled_volumes), axis=1)

def reverse_min_max_scaling(original, x):
    onp = np.asarray(original)
    xnp = np.asarray(x)
    return (xnp * (onp.max() - onp.min() + 1e-7)) + onp.min()

def get_target_data(scaled_data):
    return scaled_data[:, [-2]]

def make_dataset(x_data, y_data, window_size):
    result_x = []
    result_y = []
    for i in range(0, len(y_data) - window_size):
        _input = x_data[i: i + window_size]
        _output = y_data[i + window_size]

        result_x.append(_input)
        result_y.append(_output)
    return result_x, result_y

def divide_dataset(data_x, data_y, train_size, validation_size):
    train_size = int(len(data_y) * train_size)
    validation_size = int(len(data_y) * validation_size)

    train_x = np.array(data_x[0: train_size])
    train_y = np.array(data_y[0: train_size])
    validation_x = np.array(data_x[train_size: train_size + validation_size])
    validation_y = np.array(data_y[train_size: train_size + validation_size])
    test_x = np.array(data_x[train_size + validation_size: len(data_x)])
    test_y = np.array(data_y[train_size + validation_size: len(data_y)])

    return train_x, train_y, validation_x, validation_y, test_x, test_y


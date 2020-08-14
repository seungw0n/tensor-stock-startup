"""
@author: stevenjoeng
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 21:14:12 2020

@author: stevenjoeng
"""
from modules import module1

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import os
import random
import datetime

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

import tensorflow as tf
from keras import Sequential
from keras.layers import LSTM, Dropout, Dense, Activation
from keras.callbacks import EarlyStopping, ModelCheckpoint


""" PRE-SET
Set random seed to get reproducible results in Keras
1) PYTHONHASHSEED environment variable at a fixed value
2) python built-in pseudo-random generator at a fixed value
3) numpy pseudo-random generator at a fixed value
4) tensorflow pseudo-random generator at a fixed value
5) Configure a new global tensorflow session if we handle tesorflow directly.
- https://stackoverflow.com/questions/32419510/how-to-get-reproducible-results-in-keras
I recommend comment out below codes when it is released.
"""
seed_value = 123
os.environ['PYTHONHASHSEED'] = str(seed_value)
seed_value = 234
random.seed(seed_value)
seed_value = 345
np.random.seed(seed_value)
seed_value = 456
tf.random.set_seed(seed_value)

"""
SET HYPER-PARAMETERS 
"""
window_size = 20


def divisor():
    print('=' * 100)

def read_csv(directory_name,code):
    path = os.path.join(os.pardir, 'resources/records/day_records', directory_name, code + '.csv')
    #return pd.read_csv(path)
    return pd.read_csv(path,
                       names=['DATE','STARTING_PRICE','HIGH_PRICE','LOW_PRICE','CLOSING_PRICE','TRADING_VOLUME'],
                       encoding='euc-kr'
                       )

def create_graph(dataset, x: str, y: str):
    fig = px.line(dataset, x=x, y=y)
    fig.show()


def data_vectorization(raw_data):
    del raw_data['DATE'] # delete DATE
    return raw_data.values[1:].astype(np.float)

def data_reverse_order(raw_data):
    return raw_data[::-1]

def min_max_scaling(x):
    xnp = np.asarray(x)
    return (xnp - xnp.min()) / (xnp.max() - xnp.min() + 1e-7)

def data_normalization(raw_data):
    # 'STARTING_PRICE','HIGH_PRICE','LOW_PRICE','CLOSING_PRICE'
    prices = raw_data[:, :-1]
    scaled_prices = min_max_scaling(prices)
    #print("Normalized price: ", scaled_prices[0])

    # 'TRADING_VOLUME'
    volumes = raw_data[:,-1:]
    scaled_volumes = min_max_scaling(volumes)
    #print("Normalized volume: ", scaled_volumes[0])

    # Concatenate two metrics based on y-axis
    return np.concatenate((scaled_prices, scaled_volumes), axis=1)

def get_target_data(scaled_data):
    return scaled_data[:, [-2]]


# Read csv file
raw_data = read_csv("KOSPI 100", "005490")


# Data vectorization and delete Date column
vectorized_data = data_vectorization(raw_data)
# Reverse the data since our data is in order current from past
vectorized_data = data_reverse_order(vectorized_data)

#print("Shape: ", raw_data.shape)
# ['STARTING_PRICE','HIGH_PRICE','LOW_PRICE','CLOSING_PRICE','TRADING_VOLUME']
#print("index: ", raw_data[0])

# Normalize data as a min max scaling [0,1]
scaled_data = data_normalization(vectorized_data)
divisor()
print(scaled_data[-1])
divisor()
target_data = get_target_data(scaled_data)
print(target_data[-1])
divisor()

data_input = []
data_output = []
for i in range(0, len(target_data) - window_size):
    _input = scaled_data[i: i + window_size]
    _output = target_data[i + window_size]

    data_input.append(_input)
    data_output.append(_output)

train_size = int(len(data_output) * 0.5)
validation_size = int(len(data_output) * 0.25)
test_size = len(data_output) - train_size - validation_size

train_input = np.array(data_input[0: train_size])
train_output = np.array(data_output[0: train_size])
print("train_input.shape() : ", train_input.shape)
print("train_output.shape() : ", train_output.shape)
divisor()

validation_input = np.array(data_input[train_size: train_size + validation_size])
validation_output = np.array(data_output[train_size: train_size + validation_size])

test_input = np.array(data_input[train_size: len(data_input)])
test_output = np.array(data_output[train_size: len(data_output)])
print("test_input.shape() : ", test_input.shape)
print("test_output.shape() : ", test_output.shape)
divisor()

start = datetime.datetime.now()
model = Sequential()
model.add(LSTM(16,
               input_shape=(train_input.shape[1], train_input.shape[2]),
               activation='relu',
               return_sequences=False
               )
          )
model.add(Dense(1))


model.compile(loss='mse', optimizer='rmsprop')
history = model.fit(train_input, train_output,
                    epochs=200,
                    batch_size=16,
                    validation_data=(validation_input, validation_output),
                    )

divisor()
end = datetime.datetime.now()
elapsed = end - start
print("Time elapsed: ", elapsed)
divisor()

loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(loss)+1)
plt.figure()
plt.plot(epochs, loss, 'bo', label='Training_loss')
plt.plot(epochs, val_loss, 'b', label='Validation_loss')
plt.title('Training and validation loss')
plt.legend()
plt.show()

pred = model.predict(test_input)
plt.figure(figsize=(12,9))
plt.plot(test_output, label='ACTUAL')
plt.plot(pred, label='PREDICTION')
plt.legend()
plt.show()

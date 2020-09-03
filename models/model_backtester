
"""
@author: kwanyeob Jung
"""

import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import LSTM
import random
from keras.callbacks import EarlyStopping
from keras.layers.core import Dense, Dropout
from numpy.random import seed
from keras.models import load_model
import csv
import matplotlib.pyplot as plt



#seed setting

seed_value = 123
os.environ['PYTHONHASHSEED'] = str(seed_value)
seed_value = 234
random.seed(seed_value)
seed_value = 345
np.random.seed(seed_value)
seed_value = 456
tf.random.set_seed(seed_value)


# read the desired data from github. Path is a global variable that has been declared in the main method.
def read():
    # data is bringing all data. Like staringprice, closingprice, high ,low etc.
    data = pd.read_csv(path)
    # raw_data is just bringing closing price data
    del data['DATE']
    return data

# Reversing the entire order of the data.
def data_reverse_order(raw_data):
    return raw_data[::-1]

# Normalize the data 0-1
def normalize(data):
    global scaler
    scaler = MinMaxScaler()
    x = scaler.fit_transform(data)
    return x

# Reverse the normalize. Back the nomral data
def rev_normalize(original):
    x = scaler.inverse_transform(original)
    return x

#Make the data(integer) to float and extract input data and output data then normalize.
def data_process(data):

    flt = data.values[0:].astype(np.float)
    flt_data = data_reverse_order(flt)


    # eliminate the trading volume due to less corrlation between other features.
    no_rest_data = flt_data[:, :-1]
    no_rest_data = data_reverse_order(no_rest_data)

    # Extract high price which is our output data.
    no_norm_high_price = no_rest_data[:,[1]]

    #Normalize the data
    norm_rest_data = normalize(no_rest_data)
    norm_high_data = normalize(no_norm_high_price)

    return norm_rest_data, norm_high_data


def divide_datas_for_Train(norm_rest_data, norm_high_data, window):
    wind_size = window
    input = []
    output = []

    for i in range (len(norm_rest_data)-wind_size):
        input.append(norm_rest_data[i:i+wind_size])
        output.append(norm_high_data[i+wind_size])

    # now input and output array are set. input shape is (8390, 20, 4) and output shape is (8390,1)
    output = np.array(output)
    input = np.array(input)

    # Now divide the input and output into train, test data sets
    # since I am not going to do the testing with the data, therefore use the entire data for train
    # There is a seperate testing data.
    train_size = int(len(norm_rest_data)*1)

    train_input = np.array(input[0: train_size])
    train_output = np.array(output[0: train_size])

    test_input = np.array(input[train_size: len(input)])
    test_output = np.array(output[train_size: len(output)])

    return train_input,train_output,test_input,test_output

# train the model and save it in order to use the trained model later on.
def train_model(train_input,train_output):

    # hyperparameters need to be tuned.
    model = Sequential()
    model.add(LSTM(32, return_sequences=False, activation='softsign', input_shape=(train_input.shape[1], train_input.shape[2])))
    model.add(Dropout(0.4, seed= 123))
    model.add(Dense(1))

    callback_list = [
    EarlyStopping(monitor='loss', patience=5)
    ]

    model.compile(loss='mse', optimizer='rmsprop', metrics=['accuracy'])

    history = model.fit(train_input, train_output,
                    epochs=100,
                    batch_size=26,
                    callbacks=callback_list,
                    validation_split=0.2,
                    )

    model.save('LSTM_highprice_predict_model.h5')



#extract last 19 data and concatenate with the new data to make it 20 like the normal window size
def new_slicing_for_new_data(norm_new_wind_data):
    window = norm_new_wind_data[:20]
    return window

# Invoke the train model and run it with the new window set which is an input (testing data) and see the output.
def new_predict (new_wind_input, actual,starting_price):

    model = load_model('LSTM_highprice_predict_model.h5')
    pred = model.predict(new_wind_input)
    rev_pred = rev_normalize(pred)
    error = ((actual - int(rev_pred)) / actual) * 100
    hit_range = 0.1
    hit_ratio = 1
    no_hit = 0
    print("prediction 8/3:" + str(rev_pred))
    print ("Actual data: " + str (actual))
    print("percent Error: " + str(error))
    print("starting price: " + str(starting_price))

    if actual * (1-hit_range) <= rev_pred <= actual:
        print("hit ratio: " + str(hit_ratio))
    else:
        print("hit ratio: " + str(no_hit))

    if rev_pred > starting_price and error > 0:
        profit =((rev_pred / starting_price) - 1)*100
        print("profit percentage: " + str(profit))

    print('================================================================')


#main method

if __name__ == '__main__':
    global path
    path = os.path.join(os.pardir, 'resources/records/day_records/KOSPI 100/316140.csv')

    # store the updated data by calling read() function
    updated_data = read()
    norm_data = data_process(updated_data)

    #norm_data is
    new_wind_input = new_slicing_for_new_data(norm_data[0])
    new_wind_input = np.array(new_wind_input).reshape(1, 20, 4)

    new_wind_output = new_slicing_for_new_data(norm_data[1])

    norm_rest_data = norm_data[0]
    norm_high_data = norm_data[1]

    train_input = divide_datas_for_Train(norm_rest_data, norm_high_data,20)[0]
    train_output = divide_datas_for_Train(norm_rest_data, norm_high_data,20)[1]

    train_no_norm_input = data_process(updated_data)[0]
    train_no_norm_output = data_process(updated_data)[1]

    lists = [[20200803,8490,8510,8390,8390,1485135],
            [20200804,8380,8570,8380,8570,1390921],
            [20200805,8570,8610,8500,8560,1170169],
            [20200806,8550,8790,8550,8670,2423276],
            [20200807,8680,8710,8530,8640,1753193],
            [20200810,8650,8890,8600,8890,2647901],
            [20200811,8990,9100,8900,9050,3535877],
            [20200812,9150,9300,8980,9240,3014579],
            [20200813,9200,9300,9110,9210,2968102],
            [20200814,9210,9210,9040,9100,1551834],
            [20200818,9000,9070,8760,8760,2145369],
            [20200819,8750,8860,8750,8760,1080761],
            [20200820,8710,8760,8450,8450,1834558],
            [20200821,8480,8690,8480,8590,1172932],
            [20200824,8640,8700,8500,8680,1293520],
            [20200825,8760,8850,8700,8810,1499954],
            [20200826,8760,8800,8610,8800,1590558],
            [20200827,8720,8750,8610,8610,1028686]]


    actual_list = np.array(lists)[:, 2]
    starting_list = np.array(lists)[:,1]
    #--------------------------- Initialize the all the datas that I need -------------------------

    #------------------Train my model, save it and compare with the new datas ----------------------

    train_model(train_input, train_output)

    for x in range(len(lists)):
        with open(path, "r") as infile:
            reader = list(csv.reader(infile))
            reader.insert(1, lists[x])


        with open(path, "w") as outfile:
            writer = csv.writer(outfile)
            for line in reader:
                writer.writerow(line)

        new_predict(new_wind_input,actual_list[x],starting_list[x])




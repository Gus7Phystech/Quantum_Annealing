from datetime import datetime
import pandas_datareader as pdr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

def open_csv(path):
    return pd.read_csv(path, delimiter=',')


def get_value(data, index):
    return data.iloc[index]['Close']


def collect_predictions(data, start, stop):
    predictions = {}
    for i in range(start, stop+1):
        percent = (data.iloc[i]['Close'] / data.iloc[i-1]['Close'] - 1)*100
        if percent in predictions:
            predictions[percent] += 1/(stop - start + 1)
        else:
            predictions[percent] = 1/(stop - start + 1)
    return predictions


data = open_csv('Stocks/TSLA.csv')

prediction = collect_predictions(data, len(data)-60, len(data)-1)
percent = 0
check = 0
for key in prediction.keys():
    percent += prediction[key]*key
    check += prediction[key]

print(prediction)
print(percent)
print(check)

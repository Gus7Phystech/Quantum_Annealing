from datetime import datetime
import pandas_datareader as pdr
import numpy as np
import pandas as pd

def open_csv(path):
    return pd.read_csv(path, delimiter=',')


def get_value(data, index):
    return data.iloc[index]['Close'] / data.iloc[index-60+1]['Close']


def get_avg_value(data, start, stop):
    #print(data.iloc[start:stop+1]['Close'].values.tolist())
    #print([data.iloc[0]['Close']] * (stop - start + 1))
    return np.mean(np.divide(data.iloc[start:stop+1]['Close'].values.tolist(),
                             [data.iloc[0]['Close']]*(stop-start+1)))


def covariance(n, averages_1, values_1, averages_2, values_2):
    s = 0
    for i in range(n):
        s += (values_1[i] - averages_1[i])*(values_2[i] - averages_2[i])
    return s/n

MATR_COV = [[0 for i in range(6)] for j in range(6)]

stock_names = ['GAZP.ME', 'TSLA', 'BP', 'AAPL', 'GOOG', 'SBER.ME']
for d_1 in enumerate(stock_names):
    for d_2 in enumerate(stock_names):


        data_1 = open_csv('Stocks/{}.csv'.format(d_1[1]))
        data_2 = open_csv('Stocks/{}.csv'.format(d_2[1]))
        l = min(len(data_1), len(data_2))

        avg_1 = []
        val_1 = []
        avg_2 = []
        val_2 = []
        for i in range(l//30-1):
            val_1.append(get_value(data_1, len(data_1) - l + 30*(i+2) - 1))
            avg_1.append(get_avg_value(data_1, len(data_1) - l + 30*i, len(data_1) - l + 30*(i+2) - 1))

            val_2.append(get_value(data_2, len(data_2) - l + 30*(i+2) - 1))
            avg_2.append(get_avg_value(data_2, len(data_2) - l + 30*i, len(data_2) - l + 30*(i+2) - 1))

#print(val_2)
#print(avg_2)

        cov = covariance(l//30-1, avg_1, val_1, avg_2, val_2)

        MATR_COV[d_1[0]][d_2[0]] = cov


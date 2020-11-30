from datetime import datetime
import pandas_datareader as pdr
import numpy as np
import pandas as pd

stock_names = ['GAZP.ME', 'TSLA', 'BP', 'AAPL', 'GOOG', 'SBER.ME']

for stock_name in stock_names:
    data = pdr.get_data_yahoo(symbols='{}'.format(stock_name), start=datetime(2019, 1, 1))
    data.to_csv('Stocks\\{}.csv'.format(stock_name), columns=['Close'])






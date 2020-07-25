import datetime as dt
import pandas as pd
import numpy as np
import pandas_datareader as pdr
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters 
register_matplotlib_converters()

class Analyze:
    default_date = dt.date.isoformat(dt.date.today() - dt.timedelta(365))
    
    def get_data(symbol, date=default_date):
        data = pdr.get_data_yahoo(symbol, start=date)
        return data
    
    def moving_average(df, fast=5, slow=20):
        df[str(fast)+'_day'] = df.Close.rolling(fast).mean()
        df[str(slow)+'_day'] = df.Close.rolling(slow).mean()
        
        
    def plot_MA(df):
        df['tradeSingal']=np.where(df['5_day'] > df['20_day'], 'Buy', 'Sell')
        plt.plot(df['Close'])
        plt.plot(df.filter(regex='day'))
        plt.grid(True)
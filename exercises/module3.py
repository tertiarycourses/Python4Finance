# Code guide for Python Pandas for Finance
# Copyright: Tertiary Infotech Pte Ltd
# Author: Dr Alfred Ang
# Date: 13 Jan 2017

# Module 3 Time Series

import pandas as pd 

# Time Range
# date = pd.to_datetime('2017-1-13')
# print(date)
# print(pd.to_datetime("4th of July"))
# print(pd.to_datetime("13.01.2000"))
# print(pd.to_datetime("7/8/2000"))
# print(pd.to_datetime("7/8/2000", dayfirst=True))
# print(issubclass(pd.Timestamp, datetime.datetime))

# date = pd.date_range('2017-1-1',periods=30)
# date = pd.date_range('2017-1-1',periods=12,freq='M')
# print(pd.date_range(start="2000-01-01", periods=3, freq='H'))
# print(pd.date_range(start="2000-01-01", periods=3, freq='T'))
# print(pd.date_range(start="2000-01-01", periods=3, freq='S'))
# print(pd.date_range(start="2000-01-01", periods=3, freq='B'))
# print(pd.date_range(start="2000-01-01", periods=5, freq='1D1h1min10s'))
# print(pd.date_range(start="2000-01-01", periods=5, freq='12BH'))

# print(date)

# Time Series
aapl = pd.read_csv('data/aapl.csv',index_col='Date',usecols=['Date','Volume','Close'])

# Rolling Window
ts = aapl.rolling(window=3).sum()
ts = aapl.rolling(window=3).sum()


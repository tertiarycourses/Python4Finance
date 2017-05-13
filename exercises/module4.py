# Code guide for Python Pandas for Finance
# Copyright: Tertiary Infotech Pte Ltd
# Author: Dr Alfred Ang
# Date: 13 Jan 2017

# Module 4 Time Series

#import datetime

# date = datetime.datetime(2017,1,13)
# print(date)

# import pandas as pd 

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

# import numpy as np
# import matplotlib.pyplot as plt

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

# ts = pd.Series(np.random.randn(1000), index = pd.date_range('2016-1-1',periods=1000))

# ts = ts.cumsum()
# ts.plot()
# ts2 = ts.rolling(window=60)
# ts2.mean().plot()
# plt.show()

df = pd.DataFrame(np.random.randn(1000,4),index = pd.date_range('2016-1-1',periods=1000),columns=['A','B','C','D'])

df = df.cumsum()
df2 = df.rolling(window=60)
df2.mean().plot(subplots=True)
plt.show()

# # Time series plotting
# # ====================

# rng = pd.date_range(start='2000', periods=120, freq='MS')
# ts = pd.Series(np.random.randint(-10, 10, size=len(rng)), rng).cumsum()

# print(ts.head())

# plt.clf()
# ts.plot(c='k', title='Example time series')
# plt.savefig('time_series_1.png')

# ts.resample('2A').plot(c='0.75', ls='--')
# ts.resample('5A').plot(c='0.25', ls='-.')

# plt.clf()

# tsx = ts.resample('1A')
# ax = tsx.plot(kind='bar', color='k')
# plt.savefig('time_series_2.png')

# ax.set_xticklabels(tsx.index.year)
# plt.clf()
# ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
# df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=['A', 'B', 'C', 'D'])
# df = df.cumsum()
# df.plot(color=['k', '0.75', '0.5', '0.25'], ls='--')
# plt.savefig('time_series_3.png')

mport pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

ts = pd.Series(np.random.randn(1000), index = pd.date_range('2016-1-1',periods=1000))

ts = ts.cumsum()
ts2 = ts.rolling(window=60)
print(ts2.mean()[61:120])
# ts.plot()
# plt.show()

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import mpl_finance as fin
from matplotlib.dates import date2num
import tushare as ts
from pandas import Series,DataFrame
plt.plot([1,2,3,4],[2,4,5,3],color = 'red',label = 'line A') #折线图
plt.plot([1,2,3,4],[4,3,2,4],color = 'green',marker = 'o',label = 'line B')
plt.title('Marplotlib Test Plot')
plt.xlabel('time')
plt.ylabel('speed')
plt.legend()
#plt.show()
df = pd.read_csv(r'E:\data\601318.csv',parse_dates=['date'],index_col='date')[['open','close','high','low']]
print(df)
df.plot()
plt.show()
x = np.linspace(-100,100,10000)
y1 = x.copy()
y2 = x ** 2
y3 = x**3+5*x**2+2*x+1
plt.plot(x,y1,color = 'red',label = 'y=x')
plt.plot(x,y2,color = 'blue',label = 'y=x^2')
plt.plot(x,y3,color = 'green',label = 'y=x^3+5x^2+2x+1')
plt.ylim(-1000,1000)
plt.legend()
plt.show()
data = [24,56,73,33]
labels = ['Jan','Feb','Mar','Apr']
plt.bar(np.arange(len(data)),data)
plt.xticks(np.arange(len(data)),labels = labels)
plt.show()
plt.pie([20,30,25,25],labels = labels,autopct = '%.0f%%',explode=(0,0,0.1,0))
plt.axis('equal')
plt.show()
df['time'] = date2num(df.index.to_pydatetime())
print(df)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
arr = df[['time','open','close','high','low']].values
fin.candlestick_ochl(ax,arr)
plt.show()
print(ts.get_k_data("601318"))
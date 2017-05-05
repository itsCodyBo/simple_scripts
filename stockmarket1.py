#Beginning of stock market analysis via python 1.0

import pandas
import pandas_datareader.data as web
import datetime

#We will look at stock prices over the past year, starting 1/1/16
start = datetime.datetime(2016,1,1)
end = datetime.date.today()

#Let's get Apple stock data; Apples ticker is AAPL
#First argument is the series we want, second is source, third is start, fourth is end
apple = web.DataReader("AAPL", "yahoo",start, end)

print type(apple)

print apple.head()

import matplotlib.pyplot as plt #import matplotlib as plt to visualize data
import IPython 
#import ipython and set as inline

get_ipython().magic('matplotlib inline')
'''
#control the default size of figures in this jupyter notebook
%pylab.rcParams['figure.figsize'] = (15,9) #change the sizze of plots

apple['Adj Close'].plot(grid= True) #Plot adjusted closing price of AAPL
'''



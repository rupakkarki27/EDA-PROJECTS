#!/usr/bin/env python
# coding: utf-8

# # Tesla stock data from 2010 to 2020
# ## How did TSLA do since its inception?

# Dataset from https://www.kaggle.com/timoboz/tesla-stock-data-from-2010-to-2020

# In[1]:


# import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# ### 1. Loading the Dataset

# In[3]:


tesla = pd.read_csv('tesla_stock_data.csv')


# #### Data Description
# * Date      -  Date of trading
# * Open      -  Opening price of the stock on that particular day
# * High      -  Highest trading price on the day
# * Low       -  Lowest trading price on the day
# * Adj Close -  Adjusted closing price, taking splits etc into account
# * Volume    -  Number of trades on that day

# ### 2. Some pre-processing before we move on to the fun part

# In[4]:


# See the first 5 rows of the data
tesla.head()


# In[5]:


# See the last 5 rows of the data
tesla.tail()


# In[6]:


tesla.shape


# The dataset has 2416 observations and 7 features from 2010-06-29 to 2020-02-03.

# In[7]:


tesla.dtypes


# In[8]:


# checking null values
tesla.isnull().sum()


# Here, we can infer from the above cell that the dataset contains no null values and therefore we don't need to impute any missing values.

# In[9]:


# converting Date feature to datetime feature
tesla.Date = pd.to_datetime(tesla.Date)
tesla.dtypes


# ## 3. Exploratory Data Analysis

# #### 3.1 - Trend Analysis

# In[10]:


# Date vs opening price
plt.figure(figsize=(16, 8))
plt.plot(tesla.Date, tesla.Open, lw=2, label='Opening Price')
plt.title('Opening price of stock')
plt.xlabel('Date')
plt.ylabel('Opening price of Stock')
plt.xticks(rotation=90)
plt.legend()
plt.show()


# Tesla's stock price from 2010 to the Q1 of 2013 were mostly stationary but after 2013 the stock price has mostly increased and it reached its peak in 2020.
# During 2011 and 2012, their revenues were around $ 30-$40 million per quarter. Then in the last quarter of 2012 they exploded and reached USD 306 million, and went to USD 560 million in the first quarter of 2013. So that’s almost a 20-fold increase in revenues in a very short period of time. Even though Wall Street was very bullish on the stock back then, even they didn’t anticipate such demand for their cars. The stock price responded promptly and went from USD 40 in April to USD 190 by September 2013.

# In[11]:


# comparing highest and lowest trading price
plt.figure(figsize=(16, 8))
plt.plot(tesla.Date, tesla.High, lw=2, label='High')
plt.plot(tesla.Date, tesla.Low, lw=2, label='Low')
plt.title('Comparison of High and Low price of stock')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.xticks(rotation=90)
plt.legend()
plt.show()


# The lowest and highest trading prices are rather close to each other for this data and we can see that this trend continues through the data.

# In[12]:


# Analyzing Volume of trades
plt.figure(figsize=(16, 8))
plt.plot(tesla.Date, tesla.Volume, lw=2, label='Trade volume')
plt.title('Volume trend')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.xticks(rotation=90)
plt.legend()
plt.show()


# In[13]:


tesla['Year'] = tesla['Date'].dt.year
volume = pd.DataFrame(tesla.groupby('Year').sum()['Volume'])

plt.figure(figsize=(10,6))
plt.plot(volume)
plt.xlabel('Year')
plt.xticks(volume.index)
plt.ticklabel_format(style='plain')


# The number of trading of the TSLA stock has also increased gradually and also the most volume of sales were done in the year 2019 which the table below clearly shows. *2020 is lower because it contains only data upto February.*

# In[14]:


# checking number of sales
volume.sort_values(by='Volume', ascending=False)


# In[15]:


# Looking at monthly volumes
by_month = pd.DataFrame(tesla.groupby(tesla['Date'].dt.month).sum()['Volume'])
print(by_month.sort_values(by='Volume', ascending=False))
plt.figure(figsize=(10, 6))
plt.plot(by_month)
plt.xticks(by_month.index)
plt.xlabel('Month')
plt.ylabel('Total monthly Volume of all years')
plt.ticklabel_format(style='plain')


# So, we get the insight that May is the month where most of the trades happened. (For reasons I don't know)

# In[16]:


# The mean opening and Closing price every year for the stock
mean_price = pd.DataFrame(tesla.groupby('Year').mean()[['Open', 'Close']])


# In[17]:


plt.figure(figsize=(10, 6))
plt.plot(mean_price, lw=3, ls='--')
plt.plot(tesla.groupby('Year').mean()['High'], lw=3)


# The value of Tesla stock prices has also gone up significantly.

# #### 3.2 - Creating Columns (Daily Return)

# We will create the daily lag column to help us calculate the daily returns in % for the stock prices after the sales close for the day before.

# In[18]:


tesla['daily_lag'] = tesla['Close'].shift(1)
tesla.head()


# In[19]:


tesla['daily_returns'] = (tesla['daily_lag'] / tesla['Close']) - 1
tesla.head()


# In[20]:


mean = tesla['daily_returns'].mean()
std = tesla['daily_returns'].std()
print("Mean % returns: {:.4f}".format(mean))
print("Std of % returns: {:.2f}".format(std))


# In[21]:


tesla['daily_returns'].hist(bins=20)
plt.axvline(mean, color='red')
plt.axvline(std, color='green')
plt.axvline(-std, color='green')


# In[118]:


plt.figure(figsize=(16,8))
plt.plot(tesla.Date, tesla.daily_returns)


# ### 3.3 - Interactive Plots (plotly)

# In[27]:


# Setting up plotly
import cufflinks as cf
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
cf.go_offline()


# In[31]:


fig = px.line(tesla, x='Date', y='Open', title='Date v/s Open price w/o Slider')
fig.show()


# In[29]:


# Date vs Opening Price
fig = px.line(tesla, x='Date', y='Open', title='Date v/s Open price with Slider')
fig.update_xaxes(rangeslider_visible=True)
fig.show()


# In[32]:


# Date and Volume 
fig = px.line(tesla, x='Date', y='Volume', title='Date v/s Volume w/o Slider')
fig.show()


# In[33]:


# Date and Daily Returns 
fig = px.line(tesla, x='Date', y='daily_returns', title='Date v/s Volume w/o Slider')
fig.show()


# In[ ]:





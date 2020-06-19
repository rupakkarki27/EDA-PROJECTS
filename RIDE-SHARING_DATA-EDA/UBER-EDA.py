#!/usr/bin/env python
# coding: utf-8

# # NewYork Uber Jan 2015 to June 2015 data

# This dataset is courtesy of FiveThirtyEight from Kaggle. Since the data size is large, this folder doesnot contain any data but the link is provided below.
# https://www.kaggle.com/fivethirtyeight/uber-pickups-in-new-york-city

# In[1]:


# import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import matplotlib
matplotlib.rcParams['figure.figsize'] = (15.0, 6.0)


# In[3]:


# Loading te dataset
uber = pd.read_csv('/home/rupakkarki/Desktop/datasets/uber-data/ride_data/uber-raw-data-janjune-15.csv')


# ## 1 - Data Exploration

# In[4]:


uber.shape


# This dataset is huge, the original csv file is over 500MB and we can see that there is data for more than 14 million uber pickups in just 6 months in NewYork alone.

# In[5]:


# Explore Head
uber.head()


# In[6]:


uber.tail()


# #### Let's check for null values.

# In[7]:


uber.isnull().sum()


# In[8]:


# Unique values
uber.nunique()


# In[9]:


uber.dtypes


# There are no missing values for the pickup date columns and that's preety much what we need for this dataset. We have to perform any data preprocessing for the pickup date column.

# #### Making separate columns for month, day and hour

# In[10]:


# rename pickup date to Date
uber.rename(columns={'Pickup_date': 'Date'}, inplace=True)


# In[11]:


# convert to datetime field.
uber['Date'] = pd.to_datetime(uber['Date'])


# In[12]:


uber.dtypes


# The date column is converted to datetime

# In[13]:


# Let's extract the month, day and hour
uber['month'] = uber['Date'].dt.month
uber['day'] = uber['Date'].dt.day
uber['hour'] = uber['Date'].dt.hour


# In[14]:


# Just checking
uber.head()


# Let's map the month to its name 

# In[15]:


month_names = {1: 'January',2: 'February',3: 'March',4: 'April',5: 'May',6: 'June'}
uber['month_name'] = uber['month'].map(month_names)


# ## 2 - Data Visualization and Analysis

# Let's visualize the data from the modified dataset.

# #### Number of pickups each month

# In[34]:


ax = sns.countplot(x='month', data=uber)
plt.ticklabel_format(style='plain', axis='y', useOffset=False)
plt.title("Number of Pickups each month from Jan - Jun 2015")
for p in ax.patches:
        ax.annotate('{}'.format(p.get_height()), (p.get_x()+0.1, p.get_height()+50))


# We can see the trend here that in 2015, the pickup numbers have been increasing throughout the first half. Though the numbers were fairly similar from February through April, in may and June the numbers increased significantly.

# #### No. of pickups each day

# In[35]:


ax = sns.countplot(x='day', data=uber)
plt.title("No. of pickups each day of the month")
plt.ticklabel_format(style='plain', axis='y', useOffset=False)


# The number of pickus are more during the mid of any month and the lowest towards the end of the month during these 6 months.

# #### No. of pickups across different hours of the day

# In[36]:


sns.countplot(x='hour', data=uber)
plt.title("No. of pickups across different hours of the day")
plt.ticklabel_format(style='plain', axis='y', useOffset=False)


# #### According to weekday

# In[27]:


uber['DayOfWeek'] = uber['Date'].dt.dayofweek


# In[29]:


dayOfWeek={0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
uber['DayOfWeek'] = uber['DayOfWeek'].map(dayOfWeek)


# In[37]:


sns.countplot(x='DayOfWeek', data=uber)
plt.title(" Number of pickups according to weekday")
plt.ticklabel_format(style='plain', axis='y', useOffset=False)


# Monday sees the least number of pickups may be because people are busy on their jobs during the first day of the week and the weekends sees large pickups because people tend to travel a lot during holidays.

# In[42]:


plt.figure(figsize=(15, 8))
sns.countplot(x='month', data=uber, hue='DayOfWeek')
plt.ticklabel_format(style='plain', axis='y', useOffset=False)
plt.legend(loc='best')
plt.title("Number of Pickups each month from Jan - Jun 2015 according to day of week")
plt.show()


# In[ ]:





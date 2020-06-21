#!/usr/bin/env python
# coding: utf-8

# # Olympic Medal Data Analysis (1896-2014)
# This dataset is available in Kaggle: <br>
# https://www.kaggle.com/the-guardian/olympic-games/

# In[1]:


# import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls


# # SUMMER OLYMPICS DATA ANALYSIS

# ## 1 - Loading and Exploring the Data

# In[185]:


summer = pd.read_csv('/home/rupakkarki/Desktop/EDA-PROJECTS/OLYMPICS/data/summer.csv')


# In[128]:


countries = pd.read_csv('/home/rupakkarki/Desktop/EDA-PROJECTS/OLYMPICS/data/dictionary.csv')


# In[5]:


summer.shape


# In[6]:


summer.head()


# In[7]:


summer.tail()


# This dataset contains the record of olympic medals from 1896 to 2012. There are 31165 rows and 9 columns that have data about the year of olypic, City, Sport, Discipline, Athlete Name, Country, Gender, Event and The medal they obtained.

# In[8]:


summer.info()


# In[9]:


summer.isnull().sum()


# No missing values, that's great for us!

# #### Let's clean up our data

# In[186]:


# Cleanup the Athlete name
summer['Athlete'] = summer['Athlete'].str.split(', ').str[::-1].str.join(' ')
summer['Athlete'] = summer['Athlete'].str.title()
summer.head(1)


# In[115]:


countries.head()


# In[187]:


summer=summer.merge(countries,left_on='Country',right_on='Code',how='left')
summer = summer[['Year','City','Sport','Discipline','Athlete','Country_x','Gender','Event','Medal','Country_y']]
summer = summer.rename({'Country_x':'Code',
                       'Country_y':'Country'}, axis=1)


# In[188]:


summer.head()


# ### Players with the most medals

# In[189]:


male_most_medals = summer[summer['Gender'] == 'Men']['Athlete'].value_counts()[:1].index[0]
print("The Male player with the most medals is {} of {}.".format(
    male_most_medals, 
    summer[summer['Athlete'] == male_most_medals]['Country'].values[0]))
print("No.of Medals: {}".format(
    summer[summer['Gender'] == 'Men']['Athlete'].value_counts()[:1].values[0]))


# In[191]:


female_most_medals = summer[summer['Gender'] == 'Women']['Athlete'].value_counts()[:1].index[0]
print("The Male player with the most medals is {} of {}.".format(
    female_most_medals, 
    summer[summer['Athlete'] == female_most_medals]['Code'].values[0]))
print("No.of Medals: {}".format(
    summer[summer['Gender'] == 'Women']['Athlete'].value_counts()[:1].values[0]))


# Had to use the Country Code for female player because URS has now been renamed RUS for RUSSIA.

# ### Athletes with highest number of medals according to medal type

# In[210]:


medal_types = summer.groupby(by=['Athlete', 'Medal'])['Sport'].count().reset_index().sort_values(
    ascending=False, by='Sport')
medal_types = medal_types.drop_duplicates(subset='Medal', keep='first')
medal_types.columns = [['Athlete', 'Medal Type', 'Count']]
medal_types


# ## No. of medals according to country

# In[211]:


medal_country = summer.groupby(['Country', 'Code'])['Medal'].count().reset_index()


# In[214]:


# making map
fig = go.Figure(data=go.Choropleth(
    locations = medal_country['Code'],
    z = medal_country['Medal'],
    text = medal_country['Country'],
    colorscale = 'Blues',
    autocolorscale=False,
    reversescale=True,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_title = 'No. of Medals',
))

fig.update_layout(
    title_text='No. of medals according to country',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    )
)

fig.show()


# ### Medals distribution of top 10 countries

# In[252]:


top_ten = summer.groupby(['Country','Medal'])['Gender'].count().reset_index().sort_values(
    by='Gender', ascending=False)
top_ten = top_ten.pivot('Country', 'Medal', 'Gender').fillna(0)
top_ten = top_ten.sort_values(ascending=False, by='Gold')[:11]
top_ten.plot.barh(width=0.8)
fig = plt.gcf()
fig.set_size_inches(9,9)
plt.title('Medals Distribution Of Top 10 Countries (Summer Olympics)')
plt.show()


# ### Medals distribution of last 10 countries

# In[253]:


low_ten = summer.groupby(['Country','Medal'])['Gender'].count().reset_index().sort_values(
    by='Gender',ascending=False)
low_ten = low_ten.pivot('Country','Medal','Gender').fillna(0)
low_ten = low_ten.sort_values(by='Gold',ascending=True)[:11]
low_ten.plot.barh(width=0.8)
fig = plt.gcf()
fig.set_size_inches(9,9)
plt.title('Medals Distribution Of Top 10 Countries (Summer Olympics)')
plt.show()


# ### Medals by top countries by sport

# In[270]:


test=summer[summer['Country'].isin(summer['Country'].value_counts()[:11].index)]
test=test[test['Discipline'].isin(summer['Discipline'].value_counts()[:11].index)]
test=test.groupby(['Country','Discipline'])['Sport'].count().reset_index()
test=test.pivot('Discipline','Country','Sport')
sns.heatmap(test, annot=True, fmt='2.0f')
fig=plt.gcf()
fig.set_size_inches(8,6)
plt.show()


# In[273]:


medals_year = summer.groupby(['Country','Year'])['Medal'].count().reset_index()
medals_year = medals_year[medals_year['Country'].isin(summer['Country'].value_counts()[:5].index)]
medals_year = medals_year.pivot('Year','Country','Medal')
medals_year.plot()
fig=plt.gcf()
fig.set_size_inches(18,8)
plt.title('Medals By Years By Country (top 5)')
plt.show()


# In[ ]:





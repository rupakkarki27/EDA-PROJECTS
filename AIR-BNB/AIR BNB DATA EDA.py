#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis of Air BnB Data

# ### Context
# 
# Since 2008, guests and hosts have used Airbnb to expand on traveling possibilities and present more unique, personalized way of experiencing the world. This dataset describes the listing activity and metrics in NYC, NY for 2019.
# 
# ### Content
# This data file includes all needed information to find out more about hosts, geographical availability, necessary metrics to make predictions and draw conclusions.
# 
# ### Acknowledgements
# This public dataset is part of Airbnb, and the original source can be found on http://insideairbnb.com/ 
# 

# In[31]:


# Let's import some basic libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[2]:


# Loading the dataset
air_bnb = pd.read_csv('air_bnb.csv')


# ## 1 - Data Preprocessing
# Let's get familiar with the data and process it if required.

# In[4]:


# Checking the head and tail
air_bnb.head()


# In[5]:


air_bnb.tail()


# In[9]:


# check datatypes
air_bnb.dtypes


# In[10]:


# checking info
air_bnb.info()


# In[11]:


# null values
air_bnb.isnull().sum()


# Let's remove the data where there are null values.

# In[12]:


# removing null values
air_bnb = air_bnb.dropna(how='any', axis=0)


# In[13]:


# let's check again for null values
air_bnb.isnull().sum()


# In[14]:


air_bnb.info()


# After removing the null values the shape of the data has also changed. We remove the data for simplicity's sake and not impute of fill with any other data.

# In[23]:


air_bnb.nunique()


# In[16]:


# check the shape of the data
air_bnb.shape


# There are 38, 821 observations and total of 16 features.

# ## 2 - Exploratory Data Analysis

# In[32]:


# No. of unique values
sns.set_style('darkgrid')
palettes=['inferno','plasma','magma','cividis','Oranges','Greens','YlOrBr', 
          'YlOrRd', 'OrRd','Greys', 'Purples', 'Blues']
def plot_unique_num(df):
    
    column=[]
    unique_values=[]
    for col in df.columns:
        column.append(col)
        unique_values.append(df[col].nunique())

    fig, ax = plt.subplots(figsize=(8,8))
    sns.barplot(x = unique_values, y = column, ax = ax, palette =palettes[np.random.randint(0,12)])

    for i,p in enumerate(ax.patches):
        ax.annotate('{}'.format(unique_values[i]),(p.get_width(),p.get_y()+0.4),fontsize=12)
        
    
    plt.xlabel('No. of unique values')
    plt.ylabel('Columns')
    plt.show()


# In[33]:


categorical_features = air_bnb.select_dtypes(include='object')
plot_unique_num(categorical_features)


# In[34]:


# unique  numerical values
numeric_features = air_bnb.select_dtypes(include=['float', 'integer'])
plot_unique_num(numeric_features)


# Neighborhood groups and counts of rooms

# In[43]:


plt.figure(figsize=(15,6))
ax = sns.countplot(x='neighbourhood_group', data=air_bnb)
plt.title('Count according to neighborhood group')

for p in ax.patches:
        ax.annotate('{}'.format(p.get_height()), (p.get_x()+0.1, p.get_height()+50))


# As the data suggests, most of the rooms in rent are in the Brooklyn/Manhattan area. Fewer rooms are available in the Staten Island than other neighborhood. 

# #### Price Variation across neighborhood groups according to room type

# In[45]:


# Between groups and room type
plt.figure(figsize=(15,6))
plt.title('Distribution of Price according to neighborhood and room type')

sns.boxenplot(x='neighbourhood_group', y='price', data=air_bnb, hue='room_type')


# Since, the most popular Neighbourhood groups are Brooklyn and Manhattan, the prices are also in the high side of the spectrum. We can also infer that the prices are lower in less popular neighbourhood groups.

# In[60]:


# Average minimum nights according to room type across different groups
plt.figure(figsize=(15,6))
plt.title('Average minimum nights according to room type across different groups')

sns.barplot(x='neighbourhood_group', y='minimum_nights', hue='room_type', data=air_bnb)


# Across all the Neighbourhood groups, we can see the trend that if you wish to rent an entire home or apartment, you need to rent for an average 4 nights. In manhattan, it goes up to more than 8 nights in average.

# In[66]:


# Average price according to room type across different groups
plt.figure(figsize=(15,6))
plt.title('Average price according to room type across different groups')

sns.barplot(x='neighbourhood_group', y='price', hue='room_type', data=air_bnb, palette='Greys')


# In[67]:


# Calculated host listing count to room type across different groups
plt.figure(figsize=(15,6))
plt.title('Calculated host listing count to room type across different groups')

sns.barplot(x='neighbourhood_group', y='calculated_host_listings_count', 
            hue='room_type', data=air_bnb, palette='Blues')


# In[70]:


# variation in avalibiity across different  groups
plt.figure(figsize=(15,6))
plt.title('variation in avalibiity across different  groups')

sns.barplot(x='neighbourhood_group', y='availability_365', 
            hue='room_type', data=air_bnb, palette='Greens')


# In[73]:


# No. of rooms in different grouptypes
plt.figure(figsize=(15,6))
plt.title('No. of rooms')

ax = sns.countplot(x='neighbourhood_group', hue='room_type', data=air_bnb)
for p in ax.patches:
        ax.annotate('{}'.format(p.get_height()), (p.get_x()+0.1, p.get_height()+50))


# Manhattan offers the most number of entire home or apartment options but if you are looking for private rooms, Brooklyn may offer more choices. In Queens, Staten Island and Bronx the numbers are relatively low.

# In[78]:


# Average number of reviews per month count acc to room_type
plt.figure(figsize=(15,6))
plt.title('Average reviews per month')

sns.barplot(x='neighbourhood_group', y='reviews_per_month', hue='room_type', data=air_bnb)


# In[74]:


# Most Polpuar Neighbourhood
data = air_bnb.neighbourhood.value_counts()[:20]
plt.figure(figsize=(12, 8))
x = list(data.index)
y = list(data.values)
x.reverse()
y.reverse()

plt.title("Most Popular Neighbourhood")
plt.ylabel("Neighbourhood Area")
plt.xlabel("Number of guest Who host in this Area")

plt.barh(x, y)


# #### I've heard there are some free houses/rooms, let's find out

# In[80]:


print(f"Average of price per night : ${air_bnb.price.mean():.2f}")
print(f"Maximum price per night : ${air_bnb.price.max()}")
print(f"Minimum price per night : ${air_bnb.price.min()}")


# So, there are some free houses!! hmmmm....

# In[83]:


free = air_bnb[air_bnb['price'] == 0]


# Let's visualize the free houses data

# In[84]:


free.shape


# There are only 10 free houses. Let's see which neighbourhood group they come from.

# In[88]:


plt.figure(figsize=(10, 6))
sns.countplot(x='neighbourhood_group', hue='room_type', data=free)


# Which particular neighbourhood do they belong to???

# In[89]:


plt.figure(figsize=(10, 6))
sns.countplot(x='neighbourhood', hue='room_type', data=free)


# 
# # Correlation matrix

# In[93]:


sns.set(font_scale=3)
plt.figure(figsize=(30, 20))
sns.heatmap(air_bnb.corr(), annot=True)


# # Thanks for checking out.
# There is no model building or feature engineering involved because the sole purpose of this notebook is to perform exploratory data analysis and visualize and analyze the data.

# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis on Toy Facebook Dataset
# This is only for analysis and practice purposes and in no way represents real data from facebook.<br>
# The dataset can be found in https://www.kaggle.com/sheenabatra/facebook-data 

# In[1]:


# Let's import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


import matplotlib
matplotlib.rcParams['figure.figsize'] = (15.0, 6.0)


# ## 1 - Loading and Exploring the data

# In[4]:


fb = pd.read_csv('fb.csv')


# In[5]:


fb.head()


# In[6]:


fb.tail()


# In[7]:


fb.shape


# The dataset contains 15 columns that dedscribe about a certain account such as date of birth, gender, friend count, likes received, likes given, etc. 
# We may need to engineer some features.

# ### Engineering Features

# 1. Let's make a new column that contains groups for age and year of birth.

# In[43]:


fb['age_group'] = pd.cut(fb['age'], bins=10, precision=0)
fb['dob_year_group'] = pd.cut(fb['dob_year'], bins=10, precision=0)


# # 2 - Visualization

# - Compare the number of males and females

# In[23]:


sns.countplot(x='gender', data=fb)


# The data contains more males and less females.

#  - There's always been an argument that boys don't get their posts liked as much as girls. We can see it everyday but let's confirm it using our data.

# In[94]:


gender_like_count = fb.groupby(['gender'])['likes_received'].sum().reset_index()
sns.barplot(x='gender', y='likes_received', data=gender_like_count)
plt.ticklabel_format(style='plain', axis='y', useOffset=False)


# It's true! THE GIRLS DO GET THE MOST LIKES. Even when the data has significantly higher number of males.

# - Let's see the distribution of users of a given age group.

# In[37]:


sns.countplot(x='age_group', data=fb, hue='gender', color='blue')
plt.title("No of users across different age groups")
plt.show()


# The most number of users are in the teenage to mid 20's group (as would anyone expect) and this number falls gradually as the age increases. We can aslo see that the users number rise when they enter into their 90's (maybe because being 90 above is an achievement and people want to share that with the world, you can do things even when you're old.)

# - Let's see the distribution of users across birth years.

# In[39]:


fb.columns


# In[46]:


sns.countplot(x='dob_year_group', data=fb, hue='gender', color='red')
plt.title("No of users across different birth year groups")
plt.xticks(rotation=45)
plt.show()


# - Total number of friends according to age group

# In[63]:


age_friends = fb.groupby(['age_group','gender'])['friend_count'].sum().reset_index()
sns.barplot(x='age_group', y='friend_count', data=age_friends, hue='gender', palette='bright')
plt.xticks(rotation=45)
plt.ticklabel_format(style='plain', axis='y', useOffset=False)


# - Who initiated more friendships (Men or Women)?

# In[66]:


gender_initiation = fb.groupby(['gender'])['friendships_initiated'].sum().reset_index()
sns.barplot(x='gender', y='friendships_initiated', data=gender_initiation)
plt.ticklabel_format(style='plain', axis='y', useOffset=False)


# Males initiated the most number of friendships.

# In[88]:


device_likes = [fb['mobile_likes'].sum(), fb['www_likes'].sum()]
device = ['Mobile', 'Web']
plt.figure(figsize=(8,6))
sns.barplot(x=device, y=device_likes)
plt.title("Total likes obtained from different platforms")
plt.ticklabel_format(style='plain', axis='y', useOffset=False)


# - Who gave the most likes??

# In[97]:


likes_given = fb.groupby(['gender'])['likes'].sum().reset_index()
sns.barplot(x='gender', y='likes', data=likes_given)
plt.title("Comparison of likes given according to gender")
plt.ticklabel_format(style='plain', axis='y', useOffset=False)


# - Which age group spends the most average time on facebook?

# In[115]:


age_tenure = fb.groupby(['age_group'])['tenure'].mean().reset_index()
sns.barplot(y='age_group', x='tenure',data=age_tenure)
plt.title("Average time spent on Facebook according to age group")
plt.show()


# It is clear that even though the younger age group are more active in giving and receiving likes, the older age are often the ones who spend most time on facebook. It is obvious because after retirement you have a lot of free time on your hand and you probably spend a lot of that time on social media. If facebook wants to be more competent, it should offer more features to the senior citizens.

# 

# 

# 

# # Thank You for Checking out this notebook.

# Check out my portfolio:<br>
# https://rupakkarki27.github.io

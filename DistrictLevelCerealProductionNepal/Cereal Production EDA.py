#!/usr/bin/env python
# coding: utf-8

# # **District Level Cereal Production Data of Nepal**

# This is an exploratory data analysis of the cereal production data of Nepal from 1979/80 to 2013/14. This dataset was obatined from [ICIMOD](https://www.icimod.org/) Nepal. <br>
# [Link to Dataset](http://rds.icimod.org/Home/DataDetail?metadataId=17200)

# In this exploration, we will be trying to explore and analyze the cereal productions over the years.

# Data Description:<br>
# * Product --> ProductCode --> StatsType --> StatsDescription<br>
# * Paddy --> PD -->--> P, A, Y -->--> Production(mt), Area(ha), Yield(kg/ha)<br>
# * Wheat --> WT -->--> P, A, Y -->--> Production(mt), Area(ha), Yield(kg/ha)<br>
# * Maize --> MZ -->--> P, A, Y -->--> Production(mt), Area(ha), Yield(kg/ha)<br>
# * Millet --> ML -->--> P, A, Y -->--> Production(mt), Area(ha), Yield(kg/ha)<br>
# * Barley --> B -->--> P, A, Y -->--> Production(mt), Area(ha), Yield(kg/ha)<br>
# 
# e.g. PD_P_201213: Paddy production in fiscal year 2012/13.<br>

# The main visualization library we will use in this analysis is the **plotly** library.

# In[1]:


# import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# setup plotly to work offline
import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
cf.go_offline()


# In[114]:


# setting default renderer as notebook, to load plots when exported to HTML
import plotly.io as pio
pio.renderers.default = "notebook"


# In[3]:


# setting default plot size
plt.rcParams["figure.figsize"] = (18, 10)


# In[4]:


# loading the csv data from source
data = pd.read_csv("/home/rupakkarki/Desktop/RUPAK/datasets/District level cereal crop production in Nepal/data/nepal_crop.csv")


# In[5]:


# first 5 rows
data.head()


# In[6]:


# Shape of the data
data.shape


# This dataset contains information about 75 districts and crop production for them.

# ## **Creating new DataFrames**

# We will generate 5 different datasets for five cereal crops and visualize them differently.

# ### 1. Paddy

# In[127]:


paddy = pd.concat([pd.Series(data["DISTRICT_NAME"]),
                   data[data.columns[data.columns.str.contains("PD_")]]], axis=1)

wheat = pd.concat([pd.Series(data["DISTRICT_NAME"]),
                   data[data.columns[data.columns.str.contains("WT_")]]], axis=1)

maize = pd.concat([pd.Series(data["DISTRICT_NAME"]),
                   data[data.columns[data.columns.str.contains("MZ_")]]], axis=1)

millet = pd.concat([pd.Series(data["DISTRICT_NAME"]),
                    data[data.columns[data.columns.str.contains("ML_")]]], axis=1)

barley = pd.concat([pd.Series(data["DISTRICT_NAME"]),
                    data[data.columns[data.columns.str.contains("BL_")]]], axis=1)


# # **Data Visualization**

# This is the part where we start to explore our data. We have an old data but we can still see the trend and the production of these cereal crops.<br>
# We try to explore each cereal crops separately and will also try to analyze them together for comparison.

# # **1. Paddy**

# In[12]:


paddy.head()


# ## Paddy production over time

# In[298]:


paddy_prod = paddy[paddy.columns[paddy.columns.str.contains("PD_P")]].sum()
paddy_prod.iplot(title="Production of Paddy over time",
                 xTitle="Fiscal Year", yTitle="Production (in million tons)", mode="lines+markers", size=10)


# ## Cultivation Area over time

# In[162]:


paddy_area = paddy[paddy.columns[paddy.columns.str.contains("PD_A")]].sum()
paddy_area.iplot(title="Area of Paddy Cultivation over time",
                 xTitle="Fiscal Year", yTitle="Area (in hectars)", mode="lines+markers", size=10)


# ## Paddy Yield (kg/ha) over time

# In[192]:


paddy_yield = paddy[paddy.columns[paddy.columns.str.contains("PD_Y")]].sum()
paddy_yield.iplot(title="Paddy Yield over time",
                 xTitle="Fiscal Year", yTitle="Yield (kg/hecter)", mode="lines+markers", size=10)


# ## Top 10 most and least paddy producing districs till FS 2013/14

# In[105]:


# sum of all productions over the years in descending order
paddy_top = paddy.sum(axis=1)
paddy_top = pd.concat([pd.Series(data["DISTRICT_NAME"]),paddy_top], axis=1)
paddy_top = paddy_top.sort_values(by=0, ascending=False)
paddy_top.set_index("DISTRICT_NAME", inplace=True)


# In[140]:


paddy_top[:10].iplot(kind="bar", title="Top 10 most paddy producers till FY 2013/14",
                    xTitle="Name of District", yTitle="Production  (Metric Tons)")


# ### Production status of top 5 districts over time

# In[185]:


top_dist_paddy = ["Jhapa", "Morang", "Rupandehi", "Bara", "Kapilbastu"]
jhapa = paddy[paddy["DISTRICT_NAME"] == top_dist_paddy[0]].transpose()
morang = paddy[paddy["DISTRICT_NAME"] == top_dist_paddy[1]].transpose()
rupandehi = paddy[paddy["DISTRICT_NAME"] == top_dist_paddy[2]].transpose()
bara = paddy[paddy["DISTRICT_NAME"] == top_dist_paddy[3]].transpose()
kapilbastu = paddy[paddy["DISTRICT_NAME"] == top_dist_paddy[4]].transpose()


# In[139]:


paddy_top[-10:].iplot(kind="bar",title="Top 10 Least paddy producers till FY 2013/14",
                    xTitle="Name of District", yTitle="Production  (Metric Tons)")


# # 2. Wheat

# ## Production of wheat over time

# In[276]:


wheat_prod = wheat[wheat.columns[wheat.columns.str.contains("WT_P")]].sum()
wheat_prod.iplot(title="Production of Wheat over time",
                 xTitle="Fiscal Year", yTitle="Production (in million tons)", mode="lines+markers", size=10)


# ## Total wheat cultivation area

# In[194]:


wheat_area = wheat[wheat.columns[wheat.columns.str.contains("WT_A")]].sum()
wheat_area.iplot(title="Area of Wheat Cultivation over time",
                 xTitle="Fiscal Year", yTitle="Area (in hectars)", mode="lines+markers", size=10)


# ## Wheat Yield over time

# In[195]:


wheat_yield = wheat[wheat.columns[wheat.columns.str.contains("WT_Y")]].sum()
wheat_yield.iplot(title="Wheat Yield over time",
                 xTitle="Fiscal Year", yTitle="Yield (kg/hecter)", mode="lines+markers", size=10)


# ## Top 10 most and least wheat producers

# In[134]:


# sum of all productions over the years in descending order
wheat_top = wheat.sum(axis=1)
wheat_top = pd.concat([pd.Series(data["DISTRICT_NAME"]),wheat_top], axis=1)
wheat_top = wheat_top.sort_values(by=0, ascending=False)
wheat_top.set_index("DISTRICT_NAME", inplace=True)


# In[199]:


wheat_top[:10].iplot(kind="bar", title="Top 10 most wheat producers till FY 2013/14",
                    xTitle="Name of District", yTitle="Production  (Metric Tons)")


# In[198]:


wheat_top[-10:].iplot(kind="bar",title="Top 10 Least wheat producers till FY 2013/14",
                    xTitle="Name of District", yTitle="Production  (Metric Tons)")


# # 3. Maize

# In[200]:


maize_prod = maize[maize.columns[maize.columns.str.contains("MZ_P")]].sum()
maize_prod.iplot(title="Production of Maize over time",
                 xTitle="Fiscal Year", yTitle="Production (in million tons)", mode="lines+markers", size=10)


# In[201]:


maize_area = maize[maize.columns[maize.columns.str.contains("MZ_A")]].sum()
maize_area.iplot(title="Area of Maize Cultivation over time",
                 xTitle="Fiscal Year", yTitle="Area (in hectars)", mode="lines+markers", size=10)


# In[202]:


maize_yield = maize[maize.columns[maize.columns.str.contains("MZ_Y")]].sum()
maize_yield.iplot(title="Maize Yield over time",
                 xTitle="Fiscal Year", yTitle="Yield (kg/hecter)", mode="lines+markers", size=10)


# In[144]:


# sum of all productions over the years in descending order
maize_top = maize.sum(axis=1)
maize_top = pd.concat([pd.Series(data["DISTRICT_NAME"]),maize_top], axis=1)
maize_top = maize_top.sort_values(by=0, ascending=False)
maize_top.set_index("DISTRICT_NAME", inplace=True)


# In[145]:


maize_top[:10].iplot(kind="bar", title="Top 10 most wheat producers till FY 2013/14",
                    xTitle="Name of District", yTitle="Production  (Metric Tons)")


# In[146]:


maize_top[-10:].iplot(kind="bar", title="Top 10 least wheat producers till FY 2013/14",
                    xTitle="Name of District", yTitle="Production  (Metric Tons)")


# # 4. Millet

# In[203]:


millet_prod = millet[millet.columns[millet.columns.str.contains("ML_P")]].sum()
millet_prod.iplot(title="Production of Millet over time",
                 xTitle="Fiscal Year", yTitle="Production (in million tons)", mode="lines+markers", size=10)


# In[204]:


millet_area = millet[millet.columns[millet.columns.str.contains("ML_A")]].sum()
millet_area.iplot(title="Area of Millet Cultivation over time",
                 xTitle="Fiscal Year", yTitle="Area (in hectars)", mode="lines+markers", size=10)


# In[205]:


millet_yield = millet[millet.columns[millet.columns.str.contains("ML_Y")]].sum()
millet_yield.iplot(title="Millet Yield over time",
                 xTitle="Fiscal Year", yTitle="Yield (kg/hectar)", mode="lines+markers", size=10)


# In[150]:


# sum of all productions over the years in descending order
millet_top = millet.sum(axis=1)
millet_top = pd.concat([pd.Series(data["DISTRICT_NAME"]),millet_top], axis=1)
millet_top = millet_top.sort_values(by=0, ascending=False)
millet_top.set_index("DISTRICT_NAME", inplace=True)


# In[152]:


millet_top[:10].iplot(kind="bar", title="Top 10 most Millet producers till FY 2013/14",
                    xTitle="Name of District", yTitle="Production  (Metric Tons)")


# In[151]:


millet_top[-10:].iplot(kind="bar",title="Top 10 least Millet producers till FY 2013/14",
                    xTitle="Name of District", yTitle="Production  (Metric Tons)")


# # 5. Barley

# In[206]:


barley_prod = barley[barley.columns[barley.columns.str.contains("BL_P")]].sum()
barley_prod.iplot(title="Production of Barley over time",
                 xTitle="Fiscal Year", yTitle="Production (in million tons)", mode="lines+markers", size=10)


# In[207]:


barley_area = barley[barley.columns[barley.columns.str.contains("BL_A")]].sum()
barley_area.iplot(title="Area of Barley Cultivation over time",
                 xTitle="Fiscal Year", yTitle="Area (in hectars)", mode="lines+markers", size=10)


# In[208]:


barley_yield = barley[barley.columns[barley.columns.str.contains("BL_Y")]].sum()
barley_yield.iplot(title="Barley Yield over time",
                 xTitle="Fiscal Year", yTitle="Yield (kg/hectar)", mode="lines+markers", size=10)


# In[157]:


# sum of all productions over the years in descending order
barley_top = barley.sum(axis=1)
barley_top = pd.concat([pd.Series(data["DISTRICT_NAME"]),barley_top], axis=1)
barley_top = barley_top.sort_values(by=0, ascending=False)
barley_top.set_index("DISTRICT_NAME", inplace=True)


# In[210]:


barley_top[:10].iplot(kind="bar", title="Top 10 most Barley producers till FY 2013/14",
                    xTitle="Name of District", yTitle="Production  (Metric Tons)")


# In[159]:


barley_top[-10:].iplot(kind="bar",title="Top 10 least Barley producers till FY 2013/14",
                    xTitle="Name of District", yTitle="Production  (Metric Tons)")


# # Comparing cereal crops

# In[320]:


import plotly.graph_objects as go
fig = go.Figure()

fy = list(paddy_prod.index)
fy = [year[3:].replace("P_", "FY ") for year in fy]

fig.add_trace(go.Scatter(x=fy, y=paddy_prod.values, name="Paddy", mode="lines+markers"))
fig.add_trace(go.Scatter(x=fy, y=wheat_prod.values, name="Wheat", mode="lines+markers"))
fig.add_trace(go.Scatter(x=fy, y=millet_prod.values, name="Millet", mode="lines+markers"))
fig.add_trace(go.Scatter(x=fy, y=maize_prod.values, name="Maize", mode="lines+markers"))
fig.add_trace(go.Scatter(x=fy, y=barley_prod.values, name="Barley", mode="lines+markers"))

fig.show()


# We can see from this plot that **Paddy** *(Dhaan)* is the most produced cereal crop in nepal. Then comes **Maize** *(Makai)*, **Wheat** *(Gahu)*, **Millet** *(Kodo)*. The least produced of them is **Barley** *(Jau).*

# # Conclusion

# Production of all the cereal crops per year risen significantly from the FY 1979/80 up to 2013/14. This might be due to the reason that over the years, cultivation area has increased definitely as seen from the next plot. But also the fact that fertilizers became prominently available and advancement in agriculture tools and techniques has significantly improved.<br>
# There have been some years where the production has drastically reduced, there may be many many factors that contribute to it, main being the weather. If the weather that year was not suitable for these crops, their production will decrease.<br>
# <hr>
# Also, the cultivation land increased over the years. Population rise and the need for more cultivable land to meet the demands has driven this increase.
# <hr>
# The most producing districts for many cereal crops are in the terai region and the least are from either hilly and mostly from himalayan regions where it is extremly cold and there is least production of any crops.

# <hr>

# 
# **Rupak Karki**<br>
# [GitHub](https://www.github.com/rupakkarki27)<br>
# [Website](https://www.rupakkarki.com.np)

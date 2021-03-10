#!/usr/bin/env python
# coding: utf-8

# In[44]:


import os 
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# In[33]:


hoteldata = pd.read_csv("D:\KAGGLE DATASET\Zomato Chennai Listing 2020.csv")


# In[34]:


hoteldata.shape


# In[6]:


hoteldata = hoteldata.drop('Zomato URL',axis=1)


# In[7]:


hoteldata.head() 


# In[6]:


pallavaram_data = hoteldata[hoteldata['Location']=='pallavaram']
pallavaram_data.head(50)


# In[23]:


sort_pallavaram = hoteldata.sort_values(by='Price for 2',ascending=True).head(20)
sort_pallavaram


# In[24]:


sns.relplot(x='Price for 2',y='Dining Rating',hue='Location',data=hoteldata)


# In[26]:


hoteldata.isnull().sum()


# In[28]:


hoteldata.dtypes


# In[7]:


hoteldata.loc[34:40,['Address','Location']]
# Code used to find information from a certain columns only, it prints only the column you required  


# In[8]:


hoteldata.iloc[44]
# iloc code is used to print a certain detail of the column


# In[36]:


hoteldata.iloc[44:50]


# In[44]:


# iloc can also be used to print certain colums by using this code
hoteldata.iloc[44:50,0:4]


# In[43]:


# renmaing a colum
#code = row df = df.rename(columns={'$a':'a'})
hoteldata.rename(columns={'Price for 2':'price per head'}).head(2)


# In[45]:


hoteldata.iloc[[1,10,30,44],[0,5,6,9]]
# First list bracket indicates the index values (i.e - index columns 1,2,3,4,5)
# second list bracket indicates the columns required to print (i.e - Name of Restaurant	Price for 2	Dining Rating)


# In[52]:


# GroupBY


# In[53]:


hoteldata.groupby(['Dining Rating','Delivery Rating']).sum()


# In[57]:


hoteldata[hoteldata['Price for 2']>700.0].head(3)
# finding the pricing rate greater or less 


# In[61]:


hoteldata.iloc[8,2]


# In[9]:


hoteldata['Delivery Rating'].value_counts().head(10).plot.bar()


# In[16]:


hoteldata['Price for 2'].value_counts().head(20).sort_index().plot.bar()


# In[19]:


hoteldata['Price for 2'].value_counts().head(20).sort_index().plot.line()
plt.title('Graph')
plt.xlabel('no of Prices')
plt.ylabel('quantity')


# In[22]:


hoteldata[hoteldata['Price for 2']>500].head(20).plot.hist()


# In[1]:


# sns.relplot(x='total_bill',y='tip',hue='smoker',col='size',col_wrap=3,height=4,data=tips)


# In[9]:


hoteldata.head(1)


# In[10]:


sns.relplot(x='Price for 2',y='Dining Rating Count',data=hoteldata,hue='Delivery Rating',col='Dining Rating',col_wrap=3,height=4)


# In[ ]:





# In[ ]:





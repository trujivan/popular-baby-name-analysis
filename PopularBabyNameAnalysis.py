#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install numpy
#!pip install matplotlib
#!pip install pandas
#!pip install sklearn
#!pip install Seaborn


# In[35]:


# Importing neccessary libraries
import numpy as np
import pandas as pd
import re 
from sklearn.linear_model import LinearRegression
from pandas import Series, DataFrame

#For histograns, boxplots, and scatter plots
from pandas.tools.plotting import scatter_matrix

from numpy.random import randn
#plt is for object orinated graphing
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb

#Scipy
import scipy
from scipy.stats.stats import pearsonr


# In[36]:


# This tells matplotlib to print data visualization within the python notebook
get_ipython().magic(u'matplotlib inline')
# Setting figure sizes - figure.fixsize
from matplotlib.pyplot import figure
rcParams['figure.figsize'] = 5, 4
sb.set_style('whitegrid')


# In[4]:


BabyNames = pd.read_csv("Popular_Baby_Names.csv")
BabyNames.columns = ['Birth', 'Gender', 'Ethnicity', "FirstName", 'Count', 'Rank']
BabyNames.index = BabyNames.FirstName



# In[5]:


#Taking care of duplicates
BabyNames.duplicated()
BabyNames.dropna()
BabyNames.drop_duplicates()


# In[6]:


BabyNames.sort_values(by="Birth", ascending=True)


# In[7]:


Birth = BabyNames['Birth']

Birth.plot(kind = 'hist')


# In[8]:


Count = BabyNames['Count']
Count.plot(kind = 'hist')


# In[9]:


Rank = BabyNames['Rank']
Rank.plot(kind = 'hist')


# In[10]:


sb.distplot(Birth)


# In[11]:


sb.distplot(Count)


# In[12]:


sb.distplot(Rank)


# In[13]:


BabyNames.plot(kind='scatter', x='Birth', y='Rank', s=300)


# In[14]:


sb.regplot(x='Birth', y='Rank', data=BabyNames, scatter=True)


# In[15]:


sb.pairplot(BabyNames)


# In[16]:


BabyNames.boxplot(column = 'Rank', by = 'Birth')


# In[17]:


BabyNames.boxplot(column = 'Rank', by = 'Count')


# In[18]:


sb.boxplot(x='Rank', y='Birth', data = BabyNames, palette = 'hls')


# In[19]:


#Summary stat
BabyNames.sum()


# In[20]:


BabyNames.median()


# In[21]:


BabyNames.mode()


# In[22]:


BabyNames.mean()


# In[23]:


BabyNames.max()


# In[24]:


#Looking at summary stats that descirbe variables - Returned values is the index value (Here it is FirstNames) the max value for that category
Count = BabyNames.Count
Count.idxmax()


# In[25]:


Birth = BabyNames.Birth
Birth.idxmax()


# In[26]:


#Standard deviation summary stat of the whole DataFrame
BabyNames.std()


# In[27]:


# Calculates the variant (Varience) of the whole DataFrame
BabyNames.var()


# In[28]:


#How often a variable occurs in the data set
FirstNames = BabyNames.FirstName
FirstNames.value_counts()


# In[30]:


#General summary stat :)
#Returns a full statisitcal description of each variable
BabyNames.describe()


# In[38]:


#Addng correlation using scripy
Births = BabyNames['Birth']
Counts = BabyNames['Count']
Ranks = BabyNames['Rank']

pearsonr_coefficient, p_value = pearsonr(Ranks, Births)
print 'PearsonR correlation coefficent %0.3f' % (pearsonr_coefficient)


# In[40]:


#Pearson correlation coefficient using pandas
corr = BabyNames.corr()
corr


# In[41]:


#Visualize the Pearson correlation coefficient using Seaborn
sb.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values)


# In[ ]:





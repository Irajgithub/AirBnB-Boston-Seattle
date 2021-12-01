#!/usr/bin/env python
# coding: utf-8

# In[10]:


# import libraries
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[35]:


# read the files
df_B = pd.read_csv(r'D:\udacity data science\project 1\Boston_Seattle_airbnb\working data\Boston_Airbnb_calendar.csv')
df_S = pd.read_csv(r'D:\udacity data science\project 1\Boston_Seattle_airbnb\working data\Seattle_Airbnb_calendar.csv')


# In[36]:


# information about data set
print('Boston', df_B.shape)
print('Seattle', df_S.shape, end='\n\n**\n\n')

print('Boston',df_B.columns)
print('Seattle', df_S.columns, end='\n\n**\n\n')

print('Boston', df_B.describe())
print('Seattle', df_S.describe(), end='\n\n**\n\n')

print('Boston info', df_B.info())
print('Seattle info', df_S.info(), end='\n\n**\n\n')


# # Block 1
# preprocessing the data

# In[37]:


# dealing with null values
print('Boston_before\n',pd.isnull(df_B).sum())
print('Seattle_before\n',pd.isnull(df_S).sum(), end='\n\n**\n\n')

df_B = df_B.dropna(axis=0, how='any', subset=['price'])
df_S = df_S.dropna(axis=0, how='any', subset=['price'])

print('Boston_after\n',pd.isnull(df_B).sum())
print('Seattle_after\n',pd.isnull(df_S).sum())


# In[38]:


# removing available column because of having just value
print('Boston\n',df_B.available.unique())
print('Seattle\n',df_S.available.unique(), end='\n\n**\n\n')

df_B = df_B.drop('available', axis=1)
df_S = df_S.drop('available', axis=1)

print('Boston\n',df_B.shape)
print('Seattle\n',df_S.shape, end='\n\n**\n\n')

print('Boston\n',df_B.columns)
print('Seattle\n', df_S.columns)


# In[39]:


# preprocessing the data
df_B['date'] = pd.to_datetime(df_B.date)
df_S['date'] = pd.to_datetime(df_S.date)

df_B['price'] = df_B['price'].str.replace('$', '').str.replace(',', '').astype(float)
df_S['price'] = df_S['price'].str.replace('$', '').str.replace(',', '').astype(float)

print('Boston\n',df_B.info())
print('Seattle\n',df_S.info(), end='\n\n**\n\n')

print('Boston\n',df_B.listing_id.unique().size)
print('Seattle\n',df_S.listing_id.unique().size)


# # Block 2
# AirBnB pricing comparison between Boston and Seattle

# In[40]:


# grouping the data over month by average price
print('Boston\n',df_B.shape)
df_B_group_M = df_B.groupby(df_B['date'].dt.strftime('%B')).agg(
    {'listing_id': 'first', 'price': ['mean', 'std', 'min', 'max']})
print('Boston\n',df_B_group_M.shape)
print('Boston\n',df_B_group_M, end='\n\n**\n\n')

print('Seattle\n',df_S.shape)
df_S_group_M = df_S.groupby(df_S['date'].dt.strftime('%B')).agg(
    {'listing_id': 'first', 'price': ['mean', 'std', 'min', 'max']})
print('Seattle\n',df_S_group_M.shape)
print('Seattle\n',df_S_group_M)


# In[41]:


# cleaning the grouped data and sort them by month
month_order = ['January', "February", 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
               'November', 'December']

df_B_group_M.index = pd.CategoricalIndex(df_B_group_M.index, categories=month_order, ordered=True)
df_B_group_M = df_B_group_M.sort_index().reset_index()

df_B_group_M.rename(columns={'date': '', '': 'date', 'listing_id': '', 'first': 'listing_id_first',                              'price': '', 'mean': 'price_mean', 'std': 'price_std', 'min': 'price_min',
                             'max': 'price_max'}, inplace=True, )
df_B_group_M.columns = df_B_group_M.columns.droplevel()
print('Boston\n',df_B_group_M)

df_S_group_M.index = pd.CategoricalIndex(df_S_group_M.index, categories=month_order, ordered=True)
df_S_group_M = df_S_group_M.sort_index().reset_index()

df_S_group_M.rename(columns={'date': '', '': 'date', 'listing_id': '', 'first': 'listing_id_first',                              'price': '', 'mean': 'price_mean', 'std': 'price_std', 'min': 'price_min',
                             'max': 'price_max'}, inplace=True, )
df_S_group_M.columns = df_S_group_M.columns.droplevel()
print('Seattle\n',df_S_group_M)


# In[42]:


# data visualization: monthly comparison by bar plot
plt.figure()
w = 0.4
plt.bar(df_B_group_M.index, df_B_group_M['price_mean'], w, color='blue', yerr=df_B_group_M['price_std'], label='Boston')
plt.bar(df_B_group_M.index + w, df_S_group_M['price_mean'], w, color='red', yerr=df_S_group_M['price_std'],
        label='Seattle')
plt.xlabel('month')
plt.ylabel('average price')
plt.title('monthly average price of Airbnb over a year "2016-2017"')
plt.grid(axis='y', linestyle='--')
plt.xticks(df_B_group_M.index + w / 2, df_B_group_M['date'], rotation='vertical')
plt.legend()
plt.show()


# # block 3
# monthly price distribution using box plot

# In[43]:


# two level grouping of the data over month and listing_id by average price and count over listing_id
print('Boston\n',df_B.shape)
df_B_group_M_id = df_B.groupby([df_B['date'].dt.strftime('%B'), 'listing_id']).agg(
    {'listing_id': 'count', 'price': ['mean', 'std', 'min', 'max']})
print('Boston\n',df_B_group_M_id.shape)
print('Boston\n',df_B_group_M_id, end='\n\n**\n\n')

print('Seattle\n',df_S.shape)
df_S_group_M_id = df_S.groupby([df_S['date'].dt.strftime('%B'), 'listing_id']).agg(
    {'listing_id': 'count', 'price': ['mean', 'std', 'min', 'max']})
print('Seattle\n',df_S_group_M_id.shape)
print('Seattle\n',df_S_group_M_id)


# In[44]:


# cleaning the grouped data and sort them by month
month_order = ['January', "February", 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
               'November', 'December']


df_B_group_M_id.rename(columns={'date': '', '': 'month','listing_id':'','count': 'number_days', 'price': '',                                'mean': 'price_mean','std': 'price_std','min': 'price_min', 'max': 'price_max'}                       , inplace=True, )

df_B_group_M_id.columns = df_B_group_M_id.columns.droplevel()
df_B_group_M_id = df_B_group_M_id.reset_index()

df_B_group_M_id.index = pd.CategoricalIndex(df_B_group_M_id['date'], categories=month_order, ordered=True)
df_B_group_M_id = df_B_group_M_id.sort_index().reset_index(drop=True)

print('Boston\n',df_B_group_M_id, end='\n\n**\n\n')


df_S_group_M_id.rename(columns={'date': '', '': 'month','listing_id':'','count': 'number_days', 'price': '',                                'mean': 'price_mean','std': 'price_std','min': 'price_min', 'max': 'price_max'}                       , inplace=True, )

df_S_group_M_id.columns = df_S_group_M_id.columns.droplevel()
df_S_group_M_id = df_S_group_M_id.reset_index()

df_S_group_M_id.index = pd.CategoricalIndex(df_S_group_M_id['date'], categories=month_order, ordered=True)
df_S_group_M_id = df_S_group_M_id.sort_index().reset_index(drop=True)

print('Seattle\n',df_S_group_M_id)


# In[45]:


# Box plot for Boston data
plt.figure(figsize = (15,8))
BP_B=sns.boxplot(x='date', y='price_mean',data=df_B_group_M_id, showmeans=True,                 meanprops={"marker":"o","markerfacecolor":"black", "markeredgecolor":"black"})
plt.xlabel('month')
plt.ylabel('average price')
plt.title('monthly price distribution of Airbnb over a year for Boston "2016-2017"')
plt.grid(axis='y', linestyle='--')
BP_B.set_xticklabels(BP_B.get_xticklabels(),rotation = 90)
plt.show()


# In[46]:


# Box plot for Seattle data
plt.figure(figsize = (15,8))
BP_S=sns.boxplot(x='date', y='price_mean',data=df_S_group_M_id, showmeans=True,                 meanprops={"marker":"o","markerfacecolor":"black", "markeredgecolor":"black"})
plt.xlabel('month')
plt.ylabel('average price')
plt.title('monthly price distribution of Airbnb over a year for Seattle "2016-2017"')
plt.grid(axis='y', linestyle='--')
BP_S.set_xticklabels(BP_S.get_xticklabels(),rotation = 90)
plt.show()


# In[47]:


# removing outliers higher than $1000
df_B_group_M_id_outlier=df_B_group_M_id[df_B_group_M_id['price_mean']<1000]
df_S_group_M_id_outlier=df_S_group_M_id[df_S_group_M_id['price_mean']<1000]

print('Boston\n',df_B.listing_id.unique().size)
print('Boston outlier removed\n',df_B_group_M_id_outlier.listing_id.unique().size, end='\n\n**\n\n')

print('Seattle\n',df_S.listing_id.unique().size)
print('Seattle outlier removed\n',df_S_group_M_id_outlier.listing_id.unique().size, end='\n\n**\n\n')


# In[48]:


# Box plot for Boston data outliers removed
plt.figure(figsize = (15,8))
BP_B=sns.boxplot(x='date', y='price_mean',data=df_B_group_M_id_outlier, showmeans=True,                 meanprops={"marker":"o","markerfacecolor":"black", "markeredgecolor":"black"})
plt.xlabel('month')
plt.ylabel('average price')
plt.title('monthly price distribution of Airbnb over a year for Boston "2016-2017"')
plt.grid(axis='y', linestyle='--')
BP_B.set_xticklabels(BP_B.get_xticklabels(),rotation = 90)
plt.yticks([100,200,300,400,500,600,700,800,900,1000])
plt.show()


# In[49]:


# Box plot for Seattle data outliers removed
plt.figure(figsize = (15,8))
BP_S=sns.boxplot(x='date', y='price_mean',data=df_S_group_M_id_outlier, showmeans=True,                 meanprops={"marker":"o","markerfacecolor":"black", "markeredgecolor":"black"})
plt.xlabel('month')
plt.ylabel('average price')
plt.title('monthly price distribution of Airbnb over a year for Seattle "2016-2017"')
plt.grid(axis='y', linestyle='--')
BP_S.set_xticklabels(BP_S.get_xticklabels(),rotation = 90)
plt.yticks([100,200,300,400,500,600,700,800,900,1000])
plt.show()


# # Block 4
# the code attempts to answer the question, "What proportion of location providers changes their prices over the course of a year?"

# In[53]:


# two level grouping of the data over listing_id and week by averaging the price
print(df_B.shape)
df_B_group = df_B.groupby(['listing_id', df_B['date'].dt.strftime('%W').astype(int)]).mean()
print(df_B_group.shape)
print(df_B_group, end='\n\n**\n\n')

print(df_S.shape)
df_S_group = df_S.groupby(['listing_id', df_S['date'].dt.strftime('%W').astype(int)]).mean()
print(df_S_group.shape)
print(df_S_group)


# In[54]:


# counting the listing_id that includes change of price over ayear
B_price_change_number = 0
seen_B = set()
for i, v in enumerate(df_B_group.index):
    try:
        if v[0] == df_B_group.index[i - 1][0]:
            if df_B_group.loc[v, 'price'] != df_B_group.loc[(v[0], v[1] - 1), 'price']:
                if v[0] not in seen_B:
                    B_price_change_number += 1
                    seen_B.add(v[0])
    except:
        continue


S_price_change_number = 0
seen_S = set()
df_S_group_vary = pd.DataFrame
for i, v in enumerate(df_S_group.index):
    try:
        if v[0] == df_S_group.index[i - 1][0]:
            if df_S_group.loc[v, 'price'] != df_S_group.loc[(v[0], v[1] - 1), 'price']:
                if v[0] not in seen_S:
                    S_price_change_number += 1
                    seen_S.add(v[0])
    except:
        continue

print('Boston\n',df_B.shape)
print('Boston change\n',B_price_change_number, end='\n\n**\n\n')
print('Seattle\n',df_S.shape)
print('Seattle change\n',S_price_change_number)


# In[55]:


# data visualization pie plot: what ratio of prices changes over a year
plt.figure()
plt.pie([B_price_change_number, df_B.listing_id.unique().size - B_price_change_number], labels=['change', 'constant'],        shadow=True, wedgeprops={'edgecolor': 'black'}, autopct='%1.1f%%', pctdistance=0.3, labeldistance=0.6,         colors=['r', 'g'])
plt.title('ratio of price changing among {} data in Boston'.format(df_B.listing_id.unique().size))
plt.show()

plt.figure()
plt.pie([S_price_change_number, df_S.listing_id.unique().size - S_price_change_number], labels=['change', 'constant'],        shadow=True, wedgeprops={'edgecolor': 'black'}, autopct='%1.1f%%', pctdistance=0.3, labeldistance=0.6,         colors=['r', 'g'])
plt.title('ratio of price changing among {} data in Seattle'.format(df_S.listing_id.unique().size))
plt.show()


#!/usr/bin/env python
# coding: utf-8

# # Problem 1: Tweet Analysis

# In[2]:


import numpy as np
import pandas as pd


# In[4]:


df_tweets = pd.read_json('AOC_recent_tweets.txt') #this is JSON data type
display(df_tweets['id']) #just extracting the id column data
#df_tweet.loc[:,'id']


# In[5]:


display(df_tweets)


# In[6]:


from datetime import datetime
def time_in_hours():
    df_tweets['hours'] = df_tweets['created_at'].dt.hour + (df_tweets['created_at'].dt.minute / 60) + (df_tweets['created_at'].dt.second / 60**2)
    return df_tweets['hours']
print(time_in_hours())


# In[15]:


#df_tweets.insert(1, column='hours', value=df_tweets['hours'])
#df_tweets.columns.tolist()
df_tweets[['created_at', 'hours',
 'id','id_str',
 'full_text',
 'truncated',
 'display_text_range',
 'entities',
 'source',
 'in_reply_to_status_id',
 'in_reply_to_status_id_str',
 'in_reply_to_user_id',
 'in_reply_to_user_id_str',
 'in_reply_to_screen_name',
 'user',
 'geo',
 'coordinates',
 'place',
 'contributors',
 'retweeted_status',
 'is_quote_status',
 'retweet_count',
 'favorite_count',
 'favorited',
 'retweeted',
 'lang',
 'possibly_sensitive',
 'extended_entities',
 'quoted_status_id',
 'quoted_status_id_str',
 'quoted_status_permalink',
 'quoted_status']]


# In[16]:


df_tweets_edited = df_tweets[['created_at','hours','full_text']]
display(df_tweets_edited)
df_tweets_edited.to_csv('df_tweets_edited.csv')
print(type(df_tweets_edited))


# # Problem 2: Planets Planets Planets!

# In[24]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
exoplanets = sns.load_dataset('planets')
exoplanets


# In[76]:


sns.scatterplot(data=exoplanets, x="orbital_period", y="mass", hue="method")
plt.title("Mass VS. Orbital Period")
plt.yscale('log')
plt.xscale('log')


# In[83]:


exoplanets.dropna()
sns.histplot(data=exoplanets, x="year", hue="method")
plt.title("How Many Exoplanets Were Discovered by Year")
plt.ylabel('number')


# In[ ]:





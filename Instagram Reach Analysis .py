#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from sklearn.model_selection import train_test_split
from sklearn.linear_model import PassiveAggressiveRegressor


# In[13]:


data=pd.read_csv('C:/Users/Rakesh/Datasets/Instagram.csv', encoding='latin1')
data.head()


# In[14]:


data.isnull().sum()


# In[15]:


data=data.dropna()


# In[16]:


data.info()


# ## Analyzing Instagram Reach

# In[17]:


plt.figure(figsize=(10,8))
plt.style.use('fivethirtyeight')
plt.title('Distribution of Impressions From Home')
sns.distplot(data['From Home'])
plt.show()


# In[18]:


plt.figure(figsize=(10, 8))
plt.title("Distribution of Impressions From Hashtags")
sns.distplot(data['From Hashtags'])
plt.show()


# In[10]:


plt.figure(figsize=(10, 8))
plt.title("Distribution of Impressions From Hashtags")
sns.distplot(data['From Hashtags'])
plt.show()


# In[19]:


plt.figure(figsize=(10, 8))
plt.title("Distribution of Impressions From Explore")
sns.distplot(data['From Explore'])
plt.show()


# In[22]:


home = data['From Home'].sum()
hashtags = data['From Hashtags'].sum()
explore = data['From Explore'].sum()
other = data['From Other'].sum()

labels = ['From Home', 'From Hashtags', 'From Explore', 'Other']
values = [home, hashtags, explore, other]
fig = px.pie(data,values=values, names=labels,
            title='Impressions on Instagram Posts From Various Sources', hole=0.5)
fig.show()


# In[23]:


text = " ".join(i for i in data.Caption)
stopwords = set(STOPWORDS)
wordcloud=WordCloud(stopwords=stopwords, background_color='white').generate(text)
plt.style.use('classic')
plt.figure(figsize=(12,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()


# In[24]:


text = " ".join(i for i in data.Hashtags)
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
plt.style.use('classic')
plt.figure( figsize=(12,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


# ## Relationship Analysis

# In[25]:


figure = px.scatter(data_frame = data, x='Impressions', y='Likes', size='Likes', trendline='ols', title = "Relationship Between Likes and Impressions")
figure.show()


# In[26]:


figure = px.scatter(data_frame = data, x="Impressions",
                    y="Comments", size="Comments", trendline="ols", 
                    title = "Relationship Between Comments and Impressions")
figure.show()


# In[27]:


figure = px.scatter(data_frame = data, x="Impressions",
                    y="Shares", size="Shares", trendline="ols", 
                    title = "Relationship Between Shares and Impressions")
figure.show()


# In[28]:


figure = px.scatter(data_frame = data, x="Impressions",
                    y="Saves", size="Saves", trendline="ols", 
                    title = "Relationship Between Saves and Impressions")
figure.show()


# In[29]:


conversion_rate = (data['Follows'].sum() / data['Profile Visits'].sum()) * 100
print(conversion_rate)


# In[31]:


figure = px.scatter(data_frame = data, x="Profile Visits",
                    y="Follows", size="Follows", trendline="ols", 
                    title = "Relationship Between Saves and Impressions")
figure.show()


# In[32]:


x = np.array(data[['Likes','Saves','Comments','Shares', 'Profile Visits','Follows']])
y = np.array(data['Impressions'])
xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.2,random_state=42)


# In[33]:


model = PassiveAggressiveRegressor()
model.fit(xtrain, ytrain)
model.score(xtest, ytest)


# In[34]:


features = np.array([[282.0, 233.0,4.0, 9.0, 165.0, 54.0]])
model.predict(features)


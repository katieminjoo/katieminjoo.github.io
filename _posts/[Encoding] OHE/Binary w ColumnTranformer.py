#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


headers = ["symboling", "normalized_losses", "make", "fuel_type", "aspiration",
           "num_doors", "body_style", "drive_wheels", "engine_location",
           "wheel_base", "length", "width", "height", "curb_weight",
           "engine_type", "num_cylinders", "engine_size", "fuel_system",
           "bore", "stroke", "compression_ratio", "horsepower", "peak_rpm",
           "city_mpg", "highway_mpg", "price"]

# Read in the CSV file and convert "?" to NaN
df = pd.read_csv("http://mlr.cs.umass.edu/ml/machine-learning-databases/autos/imports-85.data",
                  header=None, names=headers, na_values="?" )
df.head()


# In[3]:


ag = df.agg(["size", "count", "nunique"]).T
ag.T


# > 편의상 None 값이 있는 컬럼은 모두 제거해주고 시작하자.

# In[4]:


col = ag[ag['count'].values == 205].index
df = df[col]
df.shape


# In[5]:


df.head(3)


# In[6]:


df.agg(['nunique'])


# 예제를 들어 살펴보기 간편한 임의의 칼럼들을 골랐습니다.

# In[7]:


data = df[['curb_weight', 'make', 'body_style', 'drive_wheels']]
data.shape


# `make`와 `body_style`은 22개, 5개의 피쳐를 가지므로 2진법으로 표현해줄 것입니다. : 22 -> 5자리, 5 -> 3자리 : 총 8자리로 축소

# `drive_wheels`는 OneHotEncoding을 사용할 것입니다.

# `curb_weight` 변수는 MinMaxScaler를 해줄겁니다.

# In[8]:


from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from category_encoders import *


# In[21]:


preprocess = make_column_transformer(
    (MinMaxScaler(), ['curb_weight']),
    (BinaryEncoder(drop_invariant=True), ['make', 'body_style']),
    (OneHotEncoder(), ['drive_wheels']),
    verbose = True, remainder='drop')


# In[22]:


res = preprocess.fit_transform(data)
res = pd.DataFrame(res)
res.shape


# In[23]:


res.head(3)


# 예상대로 12자리 숫자가 나왔음을 확인할 수 있습니다.

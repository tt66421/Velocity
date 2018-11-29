
# coding: utf-8

# In[1]:

import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

# 別のフォルダから読み込む場合は、パスを通す必要がある
#import sys
#sys.path.append('ファイルがあるフォルダ')
from Velocity import Velocity


# In[2]:

# データの読み込み
df = pd.read_excel('data.xlsx')
df.head()


# In[6]:

# 速度のデータを元のデータフレームに追加
dfV = Velocity(df, 't', 'x', 'y', 0, 1)
dfV.tail()


# In[7]:

# 速度のグラフ
plt.plot(dfV['t'], dfV['vx'])
plt.plot(dfV['t'], dfV['vy'])
plt.plot(dfV['t'], dfV['v'])


# In[8]:

# 速度のデータを元のデータフレームに追加
dfV = Velocity(df, 't', 'x', 'y', 2, 2)
dfV.tail()


# In[9]:

# 速度のグラフ
plt.plot(dfV['t'], dfV['vx'])
plt.plot(dfV['t'], dfV['vy'])
plt.plot(dfV['t'], dfV['v'])


# In[ ]:




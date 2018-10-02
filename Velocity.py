
# coding: utf-8

# In[ ]:

import pandas as pd
import numpy as np

def Velocity(df):
    # 速度を格納する空のリスト
    v = []
    # 速度を格納していく
    for i in range(len(df)-1):
        v.append( (df['x'].iloc[i+1] - df['x'].iloc[i]) / (df['t'].iloc[i+1] - df['t'].iloc[i]) )
    # 最後の時刻は速度を定義できないので、NaN を入れる
    v.append(np.nan)
    # 空のデータフレームを作成して、速度データを代入し、それを返す
    dfV = pd.DataFrame()
    dfV['v'] = v
    return dfV


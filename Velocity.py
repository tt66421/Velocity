
# coding: utf-8

# In[23]:

import pandas as pd
import numpy as np

def Velocity(df, tname, xname, yname):
    # 速度を格納する空のリスト
    vx = []
    vy = []
    v = []
    # 速度を格納していく
    for i in range(len(df)-1):
        dt = df[tname].iloc[i+1] - df[tname].iloc[i]
        dx = df[xname].iloc[i+1] - df[xname].iloc[i]
        dy = df[yname].iloc[i+1] - df[yname].iloc[i]
        vx.append(dx/dt)
        vy.append(dy/dt)
        v.append( ((dx**2 + dy**2)**0.5) / dt )
    # 最後の時刻は速度を定義できないので、NaN を入れる
    vx.append(np.nan)
    vy.append(np.nan)
    v.append(np.nan)
    # 空のデータフレームを作成して、速度データを代入し、それを返す
    dfVx = pd.DataFrame({'vx': vx})
    dfVy = pd.DataFrame({'vy': vy})
    dfV = pd.DataFrame({'v': v})
    return dfVx, dfVy, dfV



# coding: utf-8

# In[27]:

import pandas as pd
import numpy as np

def Velocity(df, tname, xname, yname, before, after):
    # 速度を格納する空のリスト
    vx = []
    vy = []
    v = []
    # 最初の方は速度を定義できないので、NaN を入れる
    for i in range(before):
        vx.append(np.nan)
        vy.append(np.nan)
        v.append(np.nan)
    # 速度を格納していく
    for i in range(len(df)-before-after):
        dt = df[tname].iloc[i+before+after] - df[tname].iloc[i]
        dx = df[xname].iloc[i+before+after] - df[xname].iloc[i]
        dy = df[yname].iloc[i+before+after] - df[yname].iloc[i]
        vx.append(dx/dt)
        vy.append(dy/dt)
        v.append( ((dx**2 + dy**2)**0.5) / dt )
    # 最後の時刻は速度を定義できないので、NaN を入れる
    for i in range(after):
        vx.append(np.nan)
        vy.append(np.nan)
        v.append(np.nan)
    # 空のデータフレームを作成して、速度データを代入し、それを返す
    dfOutput = df.copy()
    dfOutput['vx'] = vx
    dfOutput['vy'] = vy
    dfOutput['v'] = v
    return dfOutput


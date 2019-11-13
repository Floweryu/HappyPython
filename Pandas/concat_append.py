# -*- coding:utf-8 -*-
# Time: 2019-07-12 17:14:36
# Auther: ZhangJunFeng

import pandas as pd
import numpy as np


def make_df(cols, ind):
    data = {c: [str(c) + str(i) for i in ind] for c in cols}
    return pd.DataFrame(data, ind)


print(make_df('ABC', range(3)))

x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
print(np.concatenate([x, y, z]))

df1 = make_df('AB', [1, 2])
print(df1)
df2 = make_df('AB', [3, 4])
print(df2)
print(pd.concat([df1, df2]))

df3 = make_df('AB', [0, 1])
df4 = make_df('CD', [0, 1])
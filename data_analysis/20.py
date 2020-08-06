import pandas as pd
import numpy as np
data = pd.DataFrame(np.arange(0, 25).reshape(5, 5), columns=list('abcde'))
print('原始数据\n', data)
print('\n.ix 取数据')
print(data.ix[0:3, data.columns != 'b'])  # 注意：index名称 0:3 可以取到名称3

print('\n.loc 取数据')
print(data.loc[0:3, data.columns != 'b'])  # 注意：index名称 0:3 可以取到名称3

print('\n.iloc 取数据')
print(data.iloc[0:3, data.columns != 'b'])  # 下标 0:3 取不到3

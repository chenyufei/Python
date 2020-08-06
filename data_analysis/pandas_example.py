#!/usr/bin/env python3

import numpy as np
import pandas as pd
data = pd.DataFrame(np.arange(0, 60, 2).reshape(5, 6), index=list('abcde'), columns=list('ABCDEF'))
print("输出所有数据项:")
print(data)
print("输出A所在的列:")
print(data['A'])
print("输出a所在的行:")
print(data.loc['a'])
print("输出第0行数据:")
print(data.iloc[0])

print(data.loc[:, ['A', 'B']])  # 取'A'列所有行，多取几列格式为 data.loc[:,['A','B']]
print(data.iloc[:, [0]])  # 取第0列所有行，多取几列格式为 data.iloc[:,[0,1]],data.iloc[0:5,[0,1]],0到5行，0-1列
print(data.loc[['a', 'b'], ['A', 'B']])  # 提取index为'a','b',列名为'A','B'中的数据

print(data.iloc[[0, 1], [0, 1]])  # 提取第0、1行，第0、1列中的数据
print(data.loc[:, :])  # 取A,B,C,D列的所有行
print(data.iloc[:, :])  # 取第0,1,2,3列的所有行

print(data.loc[data['A'] == 0])  # 提取data数据(筛选条件: A列中数字为0所在的行数据)

print(data.loc[(data['A'] == 0) & (data['B'] == 2)])  # 提取data数据(多个筛选条件)

print(data[data['A'] == 0])  # dataframe用法
print(data[data['A'].isin([0])])  # isin函数
print(data[(data['A'] == 0)&(data['B'] == 2)])  # dataframe用法
print(data[(data['A'].isin([0]))&(data['B'].isin([2]))])  # isin函数


data = pd.DataFrame(np.arange(15).reshape(5,3), columns=list('ABC'), index=list('abcde'))
print(data)
print(data.at['a', 'A'])  # 取data中行名为a，列名为A的值

print(data.iat[0, 0])  # 取 data中第1行，第1列的值（注意，第一行，第一列均从0计数）
data.at['a', 'A'] = 666  # 等价于 data.iat[0,0]=666,利用at、iat赋值给某行某列
print(data)

data = data.drop(index='a')  # 删除index='a'的行
print(data)

data = data.drop(labels='b', axis=0)  # 删除 "行号为b" 的行
print(data)

data = data.drop(index=data[data['A'].isin([6])].index[0])  # 删除包含6的行
print(data)
data = data.drop(index=data[data['A'] == 9].index[0])  # 删除包含9的行
print(data)

data = data.drop(columns='A')  # 删除columns为A的列
print(data)

data = data.drop(labels='B', axis=1)  # 删除 "列名为A" 的列
print(data)

data = data.drop(labels='e')
print(data)

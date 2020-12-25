#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/24
# @Author : AlexZ33
# @Site :  https://blog.csdn.net/error404404/article/details/81669929
# https://blog.csdn.net/error404404/article/details/81669929
# @Reference: https://www.kaggle.com/tanmayunhale/titanic-top-4-hyperparameter-tuning
# @File : tatanic.py
# @Software: PyCharm
# 忽略警告提示
import warnings
warnings.filterwarnings('ignore')

# 导入处理数据包
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 导入训练数据和测试数据,并将它们合并方便对两个数据清洗
train_data = pd.read_csv('./data/train.csv')
# print(train_data)
train_data.info()
print(train_data.info())

test_data = pd.read_csv('./data/train.csv')
train = train_data.copy()
test = test_data.copy()
full = train.append(test, ignore_index=True)
# print(train.head(5))

# 获取full数据集中数据类型列的统计描述信息
# full.describe()
# print(full.describe())

# 由于describe只能查询到数据类型列的信息，使用info查看时间数据、字符串数据的列
# full.info()
# print(full.info())

# 丢弃PassengerId这列数据
train.drop(['PassengerId'], axis=1, inplace=True)
# print(train.head(5))

test.drop(['PassengerId'],axis=1,inplace=True)
pred = train_data['Survived']
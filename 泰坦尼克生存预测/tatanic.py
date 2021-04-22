#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/24
# @Author : AlexZ33
# @Site :  https://blog.csdn.net/error404404/article/details/81669929
# https://blog.csdn.net/error404404/article/details/81669929
# https://blog.csdn.net/aicanghai_smile/article/details/79234172
# https://zhuanlan.zhihu.com/p/31743196
# https://zhuanlan.zhihu.com/p/27424282
# https://zhuanlan.zhihu.com/p/26440212
# https://zhuanlan.zhihu.com/p/30538352
# https://www.kaggle.com/omarelgabry/a-journey-through-titanic
# https://www.kaggle.com/arthurtok/introduction-to-ensembling-stacking-in-python
# http://mars.run/2015/11/Machine%20learning%20kaggle%20titanic-0.8/
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
import matplotlib
import seaborn as sns

# fname 为 你下载的字体库路径，注意 SourceHanSansSC-Bold.otf 字体的路径
zhfont1 = matplotlib.font_manager.FontProperties(fname="./font/SourceHanSansSC-Bold.otf")

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


# 绘制存活的比例：
train_data['Survived'].value_counts().plot.pie(autopct = '%1.2f%%')

# 丢弃PassengerId这列数据
train.drop(['PassengerId'], axis=1, inplace=True)
# print(train.head(5))

test.drop(['PassengerId'],axis=1,inplace=True)
pred = train_data['Survived']

fig = plt.figure()
fig.set(alpha = 0.2)  # 设定图表颜色alpha参数

# 2行３列的图标, [0,0]位置
plt.subplot2grid((2,3), (0,0)) # 在一张大图里分列几个小图
train.Survived.value_counts().plot(kind="bar") # 柱状图
plt.title(u"获救情况 (1为获救)", fontproperties=zhfont1) # 标题
plt.ylabel(u"人数", fontproperties=zhfont1)


plt.subplot2grid((2,3),(0,1))
train.Pclass.value_counts().plot(kind="bar")
plt.ylabel(u"人数", fontproperties=zhfont1)
plt.title(u"乘客等级分布", fontproperties=zhfont1)

plt.subplot2grid((2,3),(0,2))
plt.scatter(train.Survived, train.Age)
plt.ylabel(u"年龄", fontproperties=zhfont1)                         # 设定纵坐标名称
plt.grid(b=True, which='major', axis='y')
plt.title(u"按年龄看获救分布 (1为获救)", fontproperties=zhfont1)

plt.subplot2grid((2,3),(1,0), colspan=2)
train.Age[train.Pclass == 1].plot(kind='kde')
train.Age[train.Pclass == 2].plot(kind='kde')
train.Age[train.Pclass == 3].plot(kind='kde')
plt.xlabel(u"年龄", fontproperties=zhfont1)# plots an axis lable
plt.ylabel(u"密度", fontproperties=zhfont1)
plt.title(u"各等级的乘客年龄分布", fontproperties=zhfont1)
plt.legend((u'头等舱', u'2等舱',u'3等舱'),loc='best', prop=zhfont1) # sets our legend for our graph.

plt.subplot2grid((2,3),(1,2))
train.Embarked.value_counts().plot(kind='bar')
plt.title(u"各登船口岸上船人数", fontproperties=zhfont1)
plt.ylabel(u"人数", fontproperties=zhfont1)

plt.show()


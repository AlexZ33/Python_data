"""
Cohort群组分析图表
同期群组分析

群组分析Cohort Analysis：提高用户留存率的关键

"""

import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import datetime as dt  # for date and time processing
import os

# For Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns

path = os.getcwd()

data_csv = path + '/data/2019-Oct.csv'

# 导入数据
raw_data = pd.read_csv(data_csv)
raw_data.head()
# print(raw_data.head())

"""
第一步：数据清洗

数据清洗前看一眼数据情况，明显价格不应该有负值，在清洗过程中需要将负值的价格剔掉
数据清洗，删除重复项、遗失项和价格的负值对应的行
"""

# data cleaning 数据清洗，删除重复项、遗失项和价格的负值对应的行
# 去掉空缺值
cohort_df = raw_data.dropna(subset=["user_id"])
# 去除完全重复的行数据
cohort_df.drop_duplicates()
cohort_df = cohort_df[cohort_df["price"] > 0]

# print(cohort_df.describe())

"""
第二步：整理和汇总数据

因为这次群组分析是按照首次访问的时间，和下一次访问的间隔来计算留存情况。这就需要记录下来每一条会话对应用户的首次访问时间，和这次会话与首次访问的时间间隔。

定义留存不能简单按照有没有登陆，一定要落实到用户的关键行为。什么是关键行为可以用历史会话数据筛选，再补充定性调研结果定位出来。

这个数据集中的会话只有阅览商品，购物车和购买这些重要的用户行为，所以不需要再更换指标。

计算与首次访问的时间间隔，分组的周期需要参照用户一般的使用周期，这个使用周期可以通过统计历史会话的频率得到。因为这里是电商数据，所以方便起见把拆分的周期设置为3天。
"""


def get_day(DateTime_UTC):
    DateTime_UTC = DateTime_UTC.strip(" UTC")
    DateTime_UTC = dt.datetime.fromisoformat(DateTime_UTC)
    y = dt.date(DateTime_UTC.year, DateTime_UTC.month, DateTime_UTC.day)
    return y


cohort_df["session_day"] = cohort_df["event_time"].apply(get_day)
# 记录这个用户本月内最早登陆时间
grouping = cohort_df.groupby("user_id")["session_day"]
print(grouping)
cohort_df["min_day"] = grouping.transform("min")
# 对同一最早登陆日期的客户按照下一次访问日期进行分组
cohort_df["cohort_index"] = (((cohort_df["session_day"] - cohort_df["min_day"]) // 3) + dt.timedelta(days=1)).apply(
    lambda x: x.days)
cohort_df.head()
print(cohort_df.head())

# 按照首次访问的时间，和下一次访问的间隔，统计用户数
grouping = cohort_df.groupby(["min_day","cohort_index"])
# 按照用户ID去重计数每一个分组的用户数
cohort_data = grouping["user_id"].apply(pd.Series.nunique)
# 创建区分最早登陆日期和下一次访问日期的用户数量的数据表
cohort_data = cohort_data.reset_index()
cohort_data.head()
print(cohort_data.head())

"""
第三步：结果输出和可视化
"""
# 数据透视表
cohort_counts = cohort_data.pivot(index="min_day",columns="cohort_index",values="user_id")
print(cohort_counts)

# 用百分位展示, 调整日期格式

cohort_size = cohort_counts.iloc[:,0]
retention_table = cohort_counts.divide(cohort_size,axis=0)
retention_table.round(3) * 100
retention_table.index = retention_table.index.date
retention_table.head()

# 绘制群组分析留存热力图
plt.figure(figsize=(15,8))
plt.title("Cohort Analysis")
sns.heatmap(data=retention_table,annot = True,fmt = '.0%',vmin = 0.0,vmax = 0.2,cmap="BuPu_r")
plt.show()

"""
可以从同期群分析结果判断用户留存情况这个月没有好转。下一步应该拆分获客渠道，和用户激活后用户的行为，分开比较用户留存情况，积累新一轮增长实验的思路。
"""
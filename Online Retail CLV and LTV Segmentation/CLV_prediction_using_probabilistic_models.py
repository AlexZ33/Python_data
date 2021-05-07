import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import openpyxl
import pandas as pd
import datetime
import lifetimes
from lifetimes import BetaGeoFitter
from lifetimes.plotting import plot_frequency_recency_matrix
from lifetimes.plotting import plot_probability_alive_matrix
from lifetimes.plotting import plot_period_transactions
from lifetimes.utils import calibration_and_holdout_data
from lifetimes.plotting import *
from sklearn.metrics import mean_squared_error
from math import sqrt
from lifetimes import ParetoNBDFitter
from lifetimes.plotting import plot_history_alive
import pickle
from lifetimes import ModifiedBetaGeoFitter
import warnings
import os

path = os.getcwd()

warnings.filterwarnings("ignore")
sns.set_theme(style="darkgrid")

input_file = path + '/data/online_retail_II.xlsx'


df = pd.read_excel(input_file,
                   sheet_name=["Year 2009-2010", "Year 2010-2011"])  # reading the excel file

df1 = df["Year 2009-2010"]
df2 = df["Year 2010-2011"]

# 返回一个表示DataFrame维数的元组
df1.shape, df2.shape #checking for the shape of data
print(df1.shape)

total = sum([df1.shape[0], df2.shape[0]])

print(total)

data = df1.append(df2)  #combing the data

dh = df1.head(5)

print(dh)

data.shape

print(data.isnull().sum())


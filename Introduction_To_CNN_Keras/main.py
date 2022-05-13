'''
Author: zhaokang zhaokang1@xiaomi.com
Date: 2022-05-07 17:56:20
LastEditors: zhaokang zhaokang1@xiaomi.com
LastEditTime: 2022-05-11 19:47:27
FilePath: /Python_data/Introduction_To_CNN_Keras/main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# Question
# Reference : https://www.kaggle.com/code/yassineghouzam/introduction-to-cnn-keras-0-997-top-6/notebook
# Keras API Reference/ Utilities : https://keras.io/api/utils/python_utils/
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
# %matplotlib inline
# 用于生成指定随机数。
# https://zhuanlan.zhihu.com/p/266472620
np.random.seed()
# Split arrays or matrices into random train and test subsets.将数组或矩阵拆分为随机训练和测试子集。
from sklearn.model_selection import train_test_split

# Compute confusion matrix to evaluate the accuracy of classification 计算混淆矩阵以评估分类的准确性
# Confusion Matrix : https://www.sciencedirect.com/topics/engineering/confusion-matrix
from sklearn.metrics import confusion_matrix
# https://www.geeksforgeeks.org/python-itertools/
import itertools

# Converts a class vector(integers) to binary class matrix 将类向量（整数）转换为二进制类矩阵。
from keras.utils.np_utils import to_categorical # convert to one-hot-encoding

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
# Python项目如何生成requirements.txt文件 https://www.jianshu.com/p/acb3205aea54

# Alias for set_theme(), which is the preferred interface.
# https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme
sns.set(style='white', context='notebook', palette='deep')


##############################
#     Data preparation       #
##############################

# 1. Load data
train = pd.read_csv("./input/train.csv")
test = pd.read_csv("./input/test.csv")

Y_train = train["label"]


# Drop 'Label' column
X_train = train.drop(labels=["label"], axis=1)

# free some space
del train

# 展示label的计数图
g = sns.countplot(Y_train)
Y_train.value_counts()
# plt.show()


# 2.  check for null and missing values 检查空值和缺失值
# 我检查损坏的图像（内部缺失值）
# 训练和测试数据集中没有缺失值。所以我们可以安全地继续前进。

# check the data
des1 = X_train.isnull().any().describe()
print(des1)
des2 = test.isnull().any().describe()
print(des2)


# 3．　Normalization　归一化
# 我们执行灰度归一化以减少照明差异的影响。
# 此外，CNN 在 [0..1] 数据上的收敛速度比在 [0..255] 上的收敛速度更快。
# Normalize the data
X_train = X_train / 255.0
test = test / 255.0


# 4.Reshape 重塑
# 训练和测试图像 (28px x 28px) 已作为 784 个值的一维向量存入 pandas.Dataframe。我们将所有数据重塑为 28x28x1 3D 矩阵。
# Reshape image in 3 dimensions (height = 28px, width = 28px , canal = 1)
X_train = X_train.values.reshape(-1,28,28,1)
test = test.values.reshape(-1,28,28,1)

# 5. Label encoding 标签编码
# 标签是从 0 到 9 的 10 位数字。我们需要将这些标签编码为一个热向量（例如：2 -> [0,0,1,0,0,0,0,0,0,0]）。
# Encode labels to one hot vectors (ex : 2 -> [0,0,1,0,0,0,0,0,0,0])
Y_train = to_categorical(Y_train, num_classes = 10)

# 6. Split training and valdiation set 拆分训练和验证集
# Set the random seed
random_seed = 2
# Split the train and the validation set for the fitting
# 拆分训练集和验证集以进行拟合
# 我选择将训练集分成两部分：一小部分 (10%) 成为评估模型的验证集，其余部分 (90%) 用于训练模型。
X_train, X_val, Y_train, Y_val = train_test_split(X_train, Y_train, test_size = 0.1, random_state=rand

# 由于我们有 42000 张平衡标签的训练图像（参见 2.1 加载数据），训练集的随机拆分不会导致某些标签在验证集中过度表示。 小心一些不平衡的数据集，简单的随机拆分可能会导致验证期间的评估不准确。
# 为避免这种情况，您可以在 train_test_split 函数中使用 stratify = True 选项（仅适用于 >=0.17 sklearn 版本）。

# 通过可视化图像并查看标签，我们可以更好地理解这些示例之一。
# some example
g = plt.imshow(X_train[0][:,:,0])


# 7. Build the model 构建模型 #######################################################   




"""
曲线拟合
http://lijin-thu.github.io/04.%20scipy/04.04%20curve%20fitting.html
"""
# 导入基础包
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# 多项式拟合
# 多项式的展开就是　泰勒展开　建议看这篇文章加深理解: https://www.zhihu.com/question/25627482
# 导入线多项式拟合工具：
from numpy import polyfit, poly1d

# 自己模拟数据，　一般是从外部读入
x = np.linspace(-5, 5, 100)  # np.linspace主要用来创建等差数列。
y = 4 * x + 1.5
noise_y = y + np.random.randn(y.shape[-1]) * 2.5
# print(noise_y)

# 画出数据
# %matplotlib inline

p = plt.plot(x, noise_y, 'rx')
p = plt.plot(x, y, 'b:')

# 进行线性拟合, polyfit 是多项式拟合函数, 线性拟合即一阶多项式:
coeff = polyfit(x, noise_y, 1)
print(coeff)

# 画出拟合曲线
p = plt.plot(x, noise_y, 'rx')
p = plt.plot(x, coeff[0] * x + coeff[1], 'k-')
p = plt.plot(x, y, 'b--')
# plt.show()


# 还可以用 poly1d 生成一个以传入的 coeff 为参数的多项式函数：
f = poly1d(coeff)

p = plt.plot(x, noise_y, 'rx')
p = plt.plot(x, f(x))
# plt.show()
print(f)
# ===============================================================
# 多项式拟合正弦函数

x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(x)

# 用一阶到九阶多项式拟合，类似泰勒展开：
y1 = poly1d(polyfit(x, y, 1))
y3 = poly1d(polyfit(x, y, 3))
y5 = poly1d(polyfit(x, y, 5))
y7 = poly1d(polyfit(x, y, 7))
y9 = poly1d(polyfit(x, y, 9))

x = np.linspace(-3 * np.pi,3 * np.pi,100)

p = plt.plot(x, np.sin(x), 'k')
p = plt.plot(x, y1(x))
p = plt.plot(x, y3(x))
p = plt.plot(x, y5(x))
p = plt.plot(x, y7(x))
p = plt.plot(x, y9(x))


a = plt.axis([-3 * np.pi, 3 * np.pi, -1.25, 1.25])

# 黑色为原始的图形，可以看到，随着多项式拟合的阶数的增加，曲线与拟合数据的吻合程度在逐渐增大。
plt.show()



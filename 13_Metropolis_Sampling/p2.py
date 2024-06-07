import datetime
import sys
import math
import random
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use('agg')

#question1中生成随机数的函数
class Schrage:
    def __init__(self):
        self.a=16807
        self.m=2147483647

    def function(self,i_n):             #由I_n得到I_n+1
        a=self.a
        m=self.m
        q=m//a
        r=m%a
        res=a*(i_n%q)-r*(i_n//q)
        if res>=0:
            return res
        else:
            return res+m

    def GetElem(self,i_n):              #得到x_n
        i_n=self.function(i_n)
        elem=self.function(i_n)/self.m
        return elem

def Getseed():          #获取初始i_0
    t = datetime.datetime.now()
    i_0=t.year-2000+70*(t.month+12*(t.day+31*(t.hour+23*(t.minute+59*t.second))))
    return i_0

#调用前面两个函数用来生成N个随机数(i为初始种子值),范围为(0,1)
def GetRandom(N,i):
    data = []  # 用于记录产生的随机数的列表
    test = Schrage()
    for n in range(N):
        data.append(test.GetElem(i))
        i = test.function(i)
    return data

# 定义常数
alpha = 2
beta = 3
# gamma = 18
N = 100000

# p(x)的表达式
def p(x):
    res1 = 1/(beta * math.gamma(alpha))
    res2 = (x/beta)**(alpha-1)
    res3 = np.exp(-x/beta)
    res4 = (x - alpha * beta)**2
    return (res1 * res2 * res3 * res4)

# 主程序
# 记录积分值
res = []

# 记录抽样效率
n = [0] * 30
for gamma in range(1, 31):
    # 储存样本x
    x = [1] * N

    # 产生满足T(x)分布的样本
    t = [-gamma * math.log(elem) for elem in GetRandom(N, Getseed())]

    for i in range(N-1):
        r = p(t[i]) / p(x[i]) * math.exp((t[i] - x[i]) / gamma)
        R = random.random()  # 随机产生[0,1]中的随机数

        if R < min(1, r):
            x[i + 1] = t[i]
            n[gamma-1] += 1
        else:
            x[i + 1] = x[i]

    # 储存每次p(x)/p(x)的值
    I = []

    # 定义两个区间
    intervals = [(1, 5), (10, 20)]
    for interval in intervals:
        start, end = interval
        for i in np.arange(start, end + 0.1, 0.1):
            count = len([elem for elem in x if i < elem <= i+0.1])/0.1
            g = count/N
            if g != 0:
                I.append(p(i+0.05)/g)

    res.append(sum(I)/len(I))


# # 绘制概率直方图
# plt.hist(x, bins=500, density=True, label='Experimental')
#
# x_values = np.linspace(0, max(x), 1000)  # 生成 x 值
# y_values = p(x_values)/18  # 计算 g(x) 对应的 y 值
# plt.plot(x_values, y_values, label='g(x)', color='red')
# # 添加图表标签和标题
# plt.xlabel('x')
# plt.ylabel('Probability')
# plt.title('Histogram of Samples with p(x)')
# plt.legend()
#
# # 显示图表
# plt.savefig(f'figure2/gamma={gamma}.png')


# # 绘制计算精度图
# x_values = np.linspace(0, 30, 30)  # 生成 x 值
# z_values = [18] * 30
# plt.plot(x_values, res, label='Experimental')
# plt.plot(x_values, z_values, label='Theoretical')
#
# plt.xticks(np.arange(0, 31, 2))
# plt.xlabel("gamma")
# plt.ylabel("Integrate")
# plt.legend()
#
# plt.savefig(f"figure2/精度.png")

# 绘制抽样效率图
x_values = np.linspace(0, 30, 30)  # 生成 x 值
y_values = [elem/N for elem in n]
plt.plot(x_values, y_values)

plt.xticks(np.arange(0, 31, 2))
plt.xlabel("gamma")
plt.ylabel("efficiency")
plt.savefig(f"figure2/效率.png")
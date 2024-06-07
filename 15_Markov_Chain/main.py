import datetime
import math
import sys
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

# 定义函数H(x)
def H(x, y):
    res = -(x ** 2 + y ** 2) + 0.5 * (x ** 4 + y ** 4) + 1/3 * (x - y) ** 4
    return res

# 常数
x_0 = -5
y_0 = -5
delta_x = 0.5
delta_y = 0.5
N = 10 ** 6
m = 10 ** 3
beta = 0.2

# 储存x, y序列
x = [-5] * N
y = [-5] * N
xi_x = GetRandom(N, Getseed())
xi_y = GetRandom(N, Getseed())

for i in range(N-1):
    x_t = x[i] + (xi_x[i] - 0.5) * delta_x
    y_t = y[i] + (xi_y[i] - 0.5) * delta_y

    r = math.exp(-beta * (H(x_t, y_t) - H(x[i], y[i])))

    xi = random.random()
    if xi < min(1, r):
        x[i+1] = x_t
        y[i+1] = y_t
    else:
        x[i+1] = x[i]
        y[i+1] = y[i]

x2 = [elem ** 2 for elem in x]
y2 = [elem ** 2 for elem in y]
print(f"β={beta}")
print(f"<x^2>={sum(x2[m:N])/(N-m)}")
print(f"<y^2>={sum(y2[m:N]) / (N - m)}")


# 二维Markov链
plt.plot(x, y, label='Markov')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.savefig(f"β={beta}Markov.png")

input("Press Enter to exit...")
sys.exit()
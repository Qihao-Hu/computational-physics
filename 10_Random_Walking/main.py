import datetime
import pandas as pd
import math
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import random
import sys
matplotlib.use('agg')

# 参数声明
tau = 1
Delta_t = 0.001
T = 10
omega = 2*math.pi
A_max = 0.01
K = 0.01   #弱电场
# K = 1     #强电场

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

# 得到某一时刻的速度
def V(v_x, v_y, i):
    # 得到x方向速度
    res1 = (1 - Delta_t/tau)*v_x + (A_x[i] + K*math.sin(omega*i*Delta_t))*Delta_t
    # 得到y方向速度
    res2 = (1 - Delta_t/tau)*v_y + (A_y[i] + K*math.sin(omega*i*Delta_t))*Delta_t
    return res1, res2

# 储存速度的自相关函数
C = [0] * 10**4

# 每个C取1000个做平均
for num in range(1000):
    # 生成x,y方向随机涨落力(范围均为[-0.01, 0.01])
    A_x = [0.01 * (2 * elem - 1) for elem in GetRandom(10 ** 4, Getseed())]
    A_y = [0.01 * (2 * elem - 1) for elem in GetRandom(10 ** 4, Getseed() + 10)]

    # x = [0] * 10**4
    # y = [0] * 10**4
    v_x = [0] * 10**4
    v_y = [0] * 10**4
    v_x[0] = random.uniform(-1, 1)
    v_y[0] = random.uniform(-1, 1)
    for i in range(10**4-1):
        v_x[i + 1] = V(v_x[i], v_y[i], i)[0]
        v_y[i + 1] = V(v_x[i], v_y[i], i)[1]
        # x[i + 1] = x[i] + v_x[i + 1] * Delta_t
        # y[i + 1] = y[i] + v_y[i + 1] * Delta_t
        C[i] += (0.5 * v_x[0] * v_x[i] + 0.5 * v_y[0] * v_y[i])/1000

# # 画出随机行走图
# plt.plot(x, y, color='r', marker='o', markersize=0.5)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.savefig(f"(K={K})random walk.png")

# 画出实验曲线
x = np.linspace(0, T, 10**4)
plt.plot(x, C, color='b', marker='o',  markersize=1.5, label='experimental')

# 画出理论曲线
x = np.linspace(0, T, 100)
y = C[0]*np.exp(-x/tau)

plt.plot(x, y, color='y', linewidth=2, label='Theoretical')

plt.legend()

plt.xlabel('t(s)')
plt.ylabel('Autocorrelation function')

plt.xlim(0, T)
plt.savefig(f"K={K}.png")
print(f"当K={K}时，速度的自相关函数已画出")


input("Press Enter to exit...")
sys.exit()
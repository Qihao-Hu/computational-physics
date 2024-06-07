import datetime
import sys
import math
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

#定义函数p(x)
def p(x):
    res = math.exp(-2*x**2)/math.sqrt(2*math.pi)
    return res

#定义函数F(x)
def F(x):
    res = 1.2/(math.sqrt(2*math.pi)*(1+4*x**4))
    return res

#定义函数F(x)的原函数G(x):
def G(x):
    res1 = 1.2/(8*math.sqrt(2*math.pi))
    res2 = math.log(2*x**2+2*x+1)-math.log(2*x**2-2*x+1)+2*math.atan(2*x+1)-2*math.atan(1-2*x)
    return res1*res2

#单调递增的函数f(x):
def f(x):
    res = (G(x)-G(-3))/(G(3)-G(-3))
    return res

#利用二分法求f(x)反函数的值,即此函数为f(x)的反函数
def f_1(res):
    #初始范围
    a = -3
    b = 3
    c = (a+b)/2

    #精度为1e-6
    while math.fabs(f(c)-res) > 1e-6:
        if f(c) > res:
            b = c
        elif f(c) == res:
            return c
        else:
            a = c
        c = (a+b)/2
    return c

#设置不同量级的N值
N = [1000, 5000, 10000, 50000, 100000]
num = 1

#不同量级的N值依次得到
for n in N:
    xi_1 = GetRandom(n, Getseed())   #得到范围为(0,1)的随机数,储存到\xi_1里面
    xi_2 = GetRandom(n, Getseed()+100)  #同理,种子值加了100，防止\xi_1与\xi_2初始种子值太近

    #根据舍选法给\xi_x,\xi_y赋值
    xi_x = [f_1(elem) for elem in xi_1]
    xi_y = [elem1*F(elem2) for elem1,elem2 in zip(xi_2, xi_x)]

    #判断\xi_x是否满足要求,若满足,则储存到x里面
    x = []
    for elem1,elem2 in zip(xi_x,xi_y):
        if elem2 < p(elem1):
            x.append(elem1)

    print(f"总点数为N={n},抽样点数为n={len(x)},效率为{len(x)/n}")

    # 作图检验是否满足
    x = np.array(x)

    bins = 101  # 分为101个区间

    # 作概率直方图
    counts, bin_edges = np.histogram(x, bins=bins, range=(-3, 3))
    probabilities = 101/12 *counts / counts.sum()
    plt.bar(bin_edges[:-1], probabilities, width=np.diff(bin_edges), ec="k", label='Experimental')

    # 画p(x)图
    x = np.linspace(-3, 3, 300)
    y = [p(elem) for elem in x]
    plt.plot(x, y, color='r', linewidth=2, label='Theoretical')
    plt.legend()

    plt.xlim(-3, 3)
    plt.ylim(0,1)
    plt.ylabel('Probability')

    plt.savefig(f"figure{num}.png")
    plt.figure()
    num += 1

input("Press Enter to exit...")
sys.exit()
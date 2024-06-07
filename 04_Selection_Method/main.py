import datetime
import math
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use('agg')

#利用question1中的函数产生随机数
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

#一阶阶跃函数H(x)
def H(x):
    if x >= 0:
        return 1
    else:
        return 0

#第三种情形的p(x)
def p(x):
    a = 1 + math.exp(1 / 3) - 3 * math.exp(-1 / 3)
    res = a*H(x)-math.exp(-x/3)+math.exp(1/3)
    return res

#c为0且b不为0
def Situation1():
    i = Getseed()        #获取初始种子i_0
    data = []            #储存产生的随机数
    x = []               #储存产生的样本x
    test = Schrage()
    for n in range(100000):
        data.append(test.GetElem(i))        #随机数储存到data[]里面
        i = test.function(i)
    for elem in data:
        if elem < 0.5 :                     #x的值与data里面的元素大小有关系，需要分类
            x.append(-math.sqrt(1-2*elem))
        else:
            x.append(1-math.sqrt(2-2*elem))

    #作图检验是否满足
    x = np.array(x)

    bins = 101    #分为101个区间

    #作概率直方图
    counts, bin_edges = np.histogram(x, bins=bins, range=(-1, 1))
    probabilities = 50.5 * counts / counts.sum()
    plt.bar(bin_edges[:-1], probabilities, width=np.diff(bin_edges), ec="k", label='Experimental')

    #画p(x)图
    x = np.linspace(-1, 1, 100)
    y = [H(elem)-elem for elem in x]
    plt.plot(x, y, color='r', linewidth=2, label='Theoretical')
    plt.legend()

    plt.xlim(-1, 1)
    plt.ylim(0, 1)
    plt.ylabel('Probability')

    plt.savefig('figure1.png')

#b为0
def Situation2():
    i = Getseed()  # 获取初始种子i_0
    data = []  # 储存产生的随机数
    x = []  # 储存产生的样本x
    test = Schrage()
    for n in range(100000):
        data.append(test.GetElem(i))  # 随机数储存到data[]里面
        i = test.function(i)
    x = data.copy()                     #直接将data的值赋给x

    # 作图检验是否满足
    x = np.array(x)

    bins = 101  # 分为101个区间

    # 作概率直方图
    counts, bin_edges = np.histogram(x, bins=bins, range=(-1, 1))
    probabilities = 50.5 * counts / counts.sum()
    plt.bar(bin_edges[:-1], probabilities, width=np.diff(bin_edges), ec="k", label='Experimental')

    # 画p(x)图
    x = np.linspace(-1, 1, 100)
    y = [H(elem)  for elem in x]
    plt.plot(x, y, color='r', linewidth=2, label='Theoretical')
    plt.legend()

    plt.xlim(-1, 1)
    plt.ylim(0, 1)
    plt.ylabel('Probability')

    plt.savefig('figure2.png')

#b*c不等于0
def Situation3():
    i = Getseed()  # 获取初始种子i_0
    d1 = []  # 储存产生的随机数\xi_1
    d2 = []  # 储存产生的随机数\xi_2
    x = []  # 储存产生的样本x
    M = 2*math.exp(1/3)+1-4*math.exp(-1/3)
    test = Schrage()
    for n in range(2000000):
        if n < 1000000:
            d1.append(test.GetElem(i))          #前1000000个随机数储存到d1里面
        else:
            d2.append(test.GetElem(i))          #后1000000个随机数储存到d2里面
        i = test.function(i)
    for elem1,elem2 in zip(d1,d2):
        if M*elem2 <= p(2*elem1-1):
            x.append(2 * elem1 - 1)

    #作图检验
    data = np.array(x)
    bins = 101

    counts, bin_edges = np.histogram(data, bins=bins, range=(-1, 1))
    probabilities = 50.5 * counts / counts.sum()
    plt.bar(bin_edges[:-1], probabilities, width=np.diff(bin_edges), ec="k")

    # 添加函数曲线
    x = np.linspace(-1, 1, 100)
    y = [p(elem) for elem in x]

    plt.plot(x, y, color='r', linewidth=2)

    plt.xlim(-1, 1)
    plt.ylim(0, 1)
    plt.ylabel('Probability')

    plt.savefig('figure3.png')

#调用函数
Situation1()

#清除上一个图形
plt.figure()

Situation2()

#清除上一个图形
plt.figure()

Situation3()
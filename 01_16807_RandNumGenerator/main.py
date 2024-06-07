import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')

import numpy as np

#利用Schrage方法取模
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

i=Getseed()
data=[]                   #用于记录产生的随机数的列表
I=[]                      #记录前43个I值，为第二题做准备
test=Schrage()
for n in range(10000001):                    #产生N>10^7个随机数(通过改变range里面的值实现不同的N的大小)
    data.append(test.GetElem(i))
    i=test.function(i)                  #迭代一下
    if n<43:                            #获得第二题前43个I值
        I.append(i)
df=pd.DataFrame(data)
df2=pd.DataFrame(I)
df.to_csv("output.csv")                     #写入csv文件
df2.to_csv("I.csv")

#画散点图
x=data[0:10000]
y=data[2:10002]

plt.scatter(x, y, s=1)
plt.title("Scatter Plot with Interval 2")
plt.xlabel("x")
plt.ylabel("y")

plt.savefig('figure.png')

#利用k阶矩检验均匀性
for k in range(3,11):
    sum = 0
    for n in range(10000001):
        sum += data[n]**k
    average = sum/10000001
    expectation = 1/(k+1)
    print(f"当K={k}时, <x^k>={average}, expectation={expectation}")

#统计点数(分别将区间分为2~10个区间，统计每个区间的点数),并使用卡方检验
for bins in range(1,11):   #bins为区间数
    Ka=0    #初始卡方的值
    counts, bin_edges = np.histogram(data, bins=bins)   #counts为区间内的点数，bin_edges为区间边上的点数
    for num in range(1,bins+1):
        m_k=10000001/bins
        n_k=counts[num-1]
        Ka+=((m_k-n_k)**2)/m_k
    print(f"在K={bins}时，卡方值为{Ka}")

#用C(l)进行二维独立性检验
for l in range(2,11):
    x=np.array(data[:-l])
    y=np.array(data[l:])
    d=np.array(data)

    r1=(x*y).mean()             #<(x_n)(x_n+l)>
    r2=(d.mean())**2            #<x_n>^2
    r3=(d*d).mean()             #<x_n^2>

    C_l=(r1-r2)/(r3-r2)

    print(f"l={l}时，C({l})={C_l}")









































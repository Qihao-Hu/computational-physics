import datetime
import sys
import math

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

# I_1中的f(x)
def f(x):
    res = math.sqrt(x**2+2*math.sqrt(x))
    return res

# p(x)
def p(x):
    res = (0.96*x+0.7)/15.5
    return res

#求解I_1
def I_1(N):
    res1 = 0    #储存<y>的值
    res2 = 0    #储存<y^2>的值
    x1 = [(math.sqrt(0.49+29.76*elem)-0.7)/0.96 for elem in GetRandom(N, Getseed())]     #满足p(x)分布的样本储存到x1数组里面
    for n in range(N):
        res1 += f(x1[n])/p(x1[n])
        res2 += (f(x1[n])/p(x1[n]))**2
    return res1/N, res2/N

# 求解I_2
def I_2(N):
    X = [7*elem/10 for elem in GetRandom(N, Getseed())]
    Y = [4*elem/7 for elem in GetRandom(N, Getseed()+100)]
    Z = [9*elem/10 for elem in GetRandom(N, Getseed()+100)]
    U = [2*elem for elem in GetRandom(N, Getseed()+100)]
    V = [13*elem/11 for elem in GetRandom(N, Getseed()+100)]

    res1 = 0    #储存<f>的值
    res2 = 0    #储存<f^2>的值
    for x, y, z, u, v in zip(X,Y,Z,U,V):
        res1 += (5+x**2-y**2+3*x*y-z**2+u**3-v**3)/N
        res2 += ((5+x**2-y**2+3*x*y-z**2+u**3-v**3)**2)/N
    return res1, res2

N = [1000, 5000, 10000, 50000, 100000, 500000, 1000000]
print("第一个积分值:")
for n in N:
    y = I_1(n)[0]
    y2 = I_1(n)[1]
    print(f"总样本数为N={n},I_1={y}, 与标准值的差:{math.fabs(y-15.4390107356)}，标准偏差:{5*math.sqrt(math.fabs(y2-y**2))/math.sqrt(n)}")
print("第二个积分值:")
for n in N:
    f = I_2(n)[0]
    f2 = I_2(n)[1]
    print(f"总样本数为N={n},I_2={234/275*f}, 与标准值的差= {math.fabs(234/275*f-5.6771209204)}，标准偏差:{234/275*math.sqrt(math.fabs(f2-f**2))/math.sqrt(n)}")

input("Press Enter to exit...")
sys.exit()
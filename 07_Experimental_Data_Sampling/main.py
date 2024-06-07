import matplotlib.pyplot as plt
import datetime
import numpy as np
import matplotlib
import sys
from scipy import integrate
from scipy import interpolate
import math
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

#调用前面两个函数用来生成N个随机数(i为初始种子值，由Getseed()函数获得,范围为(0,1)
def GetRandom(N,i):
    data = []  # 用于记录产生的随机数的列表
    test = Schrage()
    for n in range(N):
        data.append(test.GetElem(i))
        i = test.function(i)
    return data

# 得到高斯分布函数
def F(x):
    res = 39000*math.exp(-0.01*(x-3000)**2)
    return res

# \xi_x关于\xi_3的函数
def G(x):
    # 计算分子的积分值
    result_numerator, _ = integrate.quad(F, 2993, x)

    # 计算分母的积分值
    result_denominator, _ = integrate.quad(F, 2993, 3006)

    # 执行除法操作
    res = result_numerator / result_denominator
    return res

# 求G(x)的反函数,利用二分法
def G_1(res):
    # 初始范围
    a = 2993
    b = 3006
    c = (a + b) / 2

    # 精度为1e-6
    while math.fabs(G(c) - res) > 1e-6:
        if G(c) > res:
            b = c
        elif G(c) == res:
            return c
        else:
            a = c
        c = (a + b) / 2
    return c

#获取txt文件里面的数据
def read_txt():
    # 打开文本文件
    with open('data.txt', 'r') as file:
        # 跳过前一行
        next(file)
        # 使用 numpy 读取数据
        data = np.loadtxt(file)

    # 将数据分离为 x 和 y
    x = data[:, 0]  # 第一列作为 x 轴
    y = data[:, 1]  # 第二列作为 y 轴

    return x,y

# 直接抽样法
def Direct_samping():
    energy = read_txt()[0]
    num = read_txt()[1]    #储存每个energy的数量
    p = [elem/sum(num) for elem in num]     #储存每个energy的概率

    xi_1 = GetRandom(10000, Getseed())   #(0,1)的随机数储存到xi_1中
    x = []          #储存满足要求的x

    for xi in xi_1:
        for n in range(2, 115):
            if sum(p[:n-1]) < xi <= sum(p[:n]):
                x.append(energy[n-1])
    return x

# 舍选抽样法
def round_choice_sampling():
    # 样条插值法
    energy = read_txt()[0]
    num = read_txt()[1]  # 储存每个energy的数量
    spline = interpolate.splrep(energy, num, s=0)

    x1 = []         #储存满足舍选法的值
    #第一个区间[2900, 2993]
    xi_1 = GetRandom(100000, Getseed())         #（0，1）的随机数储存到\xi_1
    xi_2 = GetRandom(100000, Getseed()+100)     # （0，1）的随机数储存到\xi_2,防止初始值太近，因此加100

    xi_x1 = [93*elem+2900 for elem in xi_1]
    xi_y1 = [5672*elem for elem in xi_2]

    for elem1, elem2 in zip(xi_x1, xi_y1):
        if elem2 <= interpolate.splev(elem1, spline):
            x1.append(elem1)

    x2 = []
    #第二个区间[2993, 3006]
    xi_3 = GetRandom(10000, Getseed())                #（0，1）的随机数储存到\xi_3
    xi_4 = GetRandom(10000, Getseed()+100)          # （0，1）的随机数储存到\xi_4, 防止初始值太近，因此加100

    xi_x2 = [G_1(elem) for elem in xi_3]
    xi_y2 = [elem1*F(elem2) for elem1, elem2 in zip(xi_4, xi_x2)]

    for elem1, elem2 in zip(xi_x2, xi_y2):
        if elem2 <= interpolate.splev(elem1, spline):
            x2.append(elem1)

    x3 = []
    #第三个区间[3006, 3013]
    xi_5 = GetRandom(10000, Getseed())  # （0，1）的随机数储存到\xi_5
    xi_6 = GetRandom(10000, Getseed() + 100)  # （0，1）的随机数储存到\xi_6, 防止初始值太近，因此加100

    xi_x3 = [7*elem+3006 for elem in xi_5]
    xi_y3 = [800*elem for elem in xi_6]

    for elem1, elem2 in zip(xi_x3, xi_y3):
        if elem2 <= interpolate.splev(elem1, spline):
            x3.append(elem1)

    return x1, x2, x3

# 绘制图表
plt.plot(read_txt()[0], read_txt()[1], color='r', linewidth=2, label='Theoretical')
#
# # 画出包含原始数据的函数
# x = np.linspace(2900, 3013, 1000)
# y = []
# for elem in x:
#     if elem <= 2993:
#         y.append(5672)
#     elif 2993 <= elem <= 3006:
#         y.append(F(elem))
#     else:
#         y.append(800)
# plt.plot(x, y, color='r', linewidth=2)
# plt.xlabel('Energy(eV)')
# plt.ylabel('Intensity (counts)')
# plt.xlim(2900, 3013)
# plt.ylim(0,40000)
#
# plt.savefig('figure1.png')

# 直接抽样法画概率直方图
x = np.array(Direct_samping())
bins = 1001  # 分为1001个区间

# 作概率直方图
counts, bin_edges = np.histogram(x, bins=bins, range=(2900, 3013))
probabilities = counts / counts.sum() *read_txt()[1].sum()
plt.bar(bin_edges[:-1], probabilities, width=np.diff(bin_edges), ec="k", color='black', label='Direct_samping')

plt.xlabel('Energy(eV)')
plt.ylabel('Intensity (counts)')
plt.xlim(2900, 3013)
plt.ylim(0,40000)

plt.legend()
plt.savefig('Direct_samping.png')

#清除
plt.figure()

print("已得到直接抽样概率直方图")

# 绘制图表
plt.plot(read_txt()[0], read_txt()[1], color='r', linewidth=2, label='Theoretical')

# 舍选抽样法画概率直方图
x1 = np.array(round_choice_sampling()[0])
bins = 1001  # 分为1001个区间

# 作概率直方图
counts, bin_edges = np.histogram(x1, bins=bins, range=(2900, 2993))
probabilities = 1001/93*counts / counts.sum() *read_txt()[1][:93].sum()
plt.bar(bin_edges[:-1], probabilities, width=np.diff(bin_edges), ec="k", color='black', label='round_choice_sampling')

x2 = np.array(round_choice_sampling()[1])
counts, bin_edges = np.histogram(x2, bins=bins, range=(2993, 3006))
probabilities = 1001/22*counts / counts.sum() *read_txt()[1][94:106].sum()
plt.bar(bin_edges[:-1], probabilities, width=np.diff(bin_edges), color='black', ec="k")

x3 = np.array(round_choice_sampling()[2])
counts, bin_edges = np.histogram(x3, bins=bins, range=(3006, 3013))
probabilities = 1001/8*counts / counts.sum() *read_txt()[1][106:114].sum()
plt.bar(bin_edges[:-1], probabilities, width=np.diff(bin_edges), color='black', ec="k")

plt.xlabel('Energy(eV)')
plt.ylabel('Intensity (counts)')
plt.xlim(2900, 3013)
plt.ylim(0,40000)

plt.legend()
plt.savefig('round_choice_sampling.png')
plt.figure()

print("已得到舍选抽样概率直方图")
print(f"舍选法区间1点数为N1=100000,抽样样本为n1={len(x1)},效率为{len(x1)/100000}")
print(f"舍选法区间2点数为N2=10000,抽样样本为n2={len(x2)},效率为{len(x2)/10000}")
print(f"舍选法区间3点数为N3=10000,抽样样本为n3={len(x3)},效率为{len(x3)/10000}")
print(f"舍选法总点数为N=120000,抽样样本为n={len(x1)+len(x2)+len(x3)},效率为{(len(x1)+len(x2)+len(x3))/120000}")

input("Press Enter to exit...")
sys.exit()
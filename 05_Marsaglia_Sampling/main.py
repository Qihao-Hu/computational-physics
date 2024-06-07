import datetime
import math
import matplotlib.pyplot as plt
import matplotlib
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

#调用前面两个函数用来生成N个随机数(i为初始种子值)
def GetRandom(N,i):
    data = []  # 用于记录产生的随机数的列表
    test = Schrage()
    for n in range(N):
        data.append(test.GetElem(i))
        i = test.function(i)
    return data

u = []  #储存(0,1)随即数u
v = []  #储存(0,1)随机数v
u1 = []  #将u变换为(-1,1)的随机数
v1 = []  #将v变换为(-1,1)的随机数
u2 = []  #储存满足（u1，v1）在圆内的u1值
v2 = []  #储存满足（u1，v1）在圆内的v1值
x, y, z =[], [], [] #储存球面上点的坐标
u = GetRandom(10000,Getseed())
v = GetRandom(10000,Getseed()+50)   #防止初始值太近

#变换将(0,1)变换到(-1,1)
u1 = [2*elem-1 for elem in u]
v1 = [2*elem-1 for elem in v]

for elem1, elem2 in zip(u1, v1):
    if elem1**2+elem2**2 <= 1:
        u2.append(elem1)
        v2.append(elem2)
num = len(u2)

#根据Marsaglia方法得到x,y,z
x = [2*elem1*math.sqrt(1-elem1**2-elem2**2) for elem1, elem2 in zip(u2,v2)]
y = [2*elem2*math.sqrt(1-elem1**2-elem2**2) for elem1, elem2 in zip(u2,v2)]
z = [1-2*(elem1**2+elem2**2) for elem1, elem2 in zip(u2,v2)]

# 绘制3D图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制散点图
ax.scatter(x, y, z, c='r', marker='o', s=1)

# 设置坐标轴范围
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 添加标题
ax.set_title(f'{num} Random Numbers On the Sphere')

# 储存图形
plt.savefig('figure.png')
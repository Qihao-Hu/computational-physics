import datetime
import math
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')

#调用question1的函数来生成均匀随机数
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

i = Getseed()          #初始种子
test = Schrage()
d1 = []    #用来储存均匀随机数1,此随机数与\theta转化
d2 = []    #用来储存均匀随机数2,此随机数与\varphi转化
theta = []  #用来储存\theta
varphi = [] #用来储存\varphi
x = []      #用来储存x
y = []      #用来储存y
z= []       #用来储存z

for n in range(4000):
    if n < 2000:
        d1.append(test.GetElem(i))          #将前2000个随机数储存到d1
    else:
        d2.append(test.GetElem(i))          #将剩下2000个随机数储存到d2
    i = test.function(i)

#将随机数与球坐标转化
for elem in d1:
    theta.append(math.acos(elem))
for elem in d2:
    varphi.append(elem*2*math.pi)

#将直角坐标与球坐标转化
x = [math.sin(e1)*math.cos(e2) for e1,e2 in zip(theta,varphi)]
y = [math.sin(e1)*math.sin(e2) for e1,e2 in zip(theta,varphi)]
z = [math.cos(e1) for e1 in theta]

# 绘制3D图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制散点图
ax.scatter(x, y, z, c='r', marker='o', s=1)

# 设置z轴范围
ax.set_zlim(0, 1)

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 添加标题
ax.set_title('2000 Random Numbers on a Sphere')

# 储存图形
plt.savefig('figure.png')

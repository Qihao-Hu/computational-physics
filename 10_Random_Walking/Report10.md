# Report10

PB21000235	胡琦浩

### 一、问题

Monte Carlo方法研究二维平面上荷电粒子在正弦外电场（ ~ $sin(\omega t)$）中的随机行走。推导速度自相关函数的表达式，它随时间的变化是怎样的行为？能否模拟得到该自相关函数的曲线？是的话与理论曲线进行比较，否的话讨论理由。

### 二、方法

#### 2.1	数学推导

​	由$Langevin$方程:
$$
m\frac{d\vec{v}}{dt}=-\frac{1}{B}\vec{v}+\vec{F}(t)+q\vec{E}sin(\omega t)\tag{1}
$$

$$
\frac{d\vec{v}}{dt}=-\frac{1}{\tau}\vec{v}+\vec{A}(t)+\vec{K}sin(\omega t)\tag{2}
$$

式中：$\tau=mB,\,\,\,\,\, B=\frac{1}{6\pi\eta a},\,\,\,\,\, \vec{K}=\frac{q\vec{E}}{m}$

$\vec{A}$代表随机涨落力，则$<A(t)>=0$

由式(2)解出$\vec{v}$可得:
$$
\vec{v}(t)=\vec{v}(0)e^{-t/\tau}+e^{-t/\tau}\int_{0}^{t}e^{t'/\tau}(\vec{A}(t')+\vec{K}sin(\omega t'))\,dt' \tag{4}
$$
由定义，二维速度自相关函数为：
$$
C(t)=\frac{1}{2}<\vec{v}(t)\cdot\vec{v}(0)>
	=\frac{1}{2}<\vec{v}^2(0)e^{-t/\tau}>+\frac{1}{2}e^{-t/\tau}\int_{0}^{t}e^{t'/\tau}(<\vec{A}(t')\cdot\vec{v}(0)>+<\vec{K}\cdot\vec{v}(0)sin(\omega t')>\,)dt'\newline
=\frac{1}{2}<\vec{v}^2(0)e^{-t/\tau}>\tag{5}
$$


#### 2.2	算法实现

取时间间隔足够小，则假设:$d\vec{v}\approx\Delta\vec{v}$，$dt\approx\Delta t$，故(2)式可化为：
$$
\Delta\vec{v}=-\frac{\Delta t}{\tau}\vec{v}+(\vec{A}+\vec{K}sin(\omega t))\Delta t
\\\tag{6}
\vec{v}(t+\Delta t)=\vec{v}+\Delta\vec{v}
$$
根据式(6)可以算得每个时间t的速度。

选择参数：

由于$\tau>>\Delta t$，不妨取：$\tau=1s$，$\Delta t=10^{-3}s$

总时间：$T=10s$，此时：$e^{-T/\tau}=e^{-10}\approx4.54\times10^{-5}\rightarrow0$满足要求

由于只需保证总时间$T$内可以观测到足够多的电场震荡周期，故取：$\omega=2\pi \,\,\,rad/s$

涨落力通常不会很大，故取：$A_{max}=0.01m/s^2$

由于不知道电磁力的数量级，则分为两种情况讨论：(1)强电场力，此时假设$K=1m/s^2$		(2)弱电场力，此时假设$K=0.01m/s^2$



<img src="C:\Users\86130\Desktop\Computational Physics\hw4\report10\1.png" style="zoom:50%;" />

​																							图1：算法的具体流程

### 三、实验结果

![](C:\Users\86130\Desktop\Computational Physics\hw4\question10\(K=1)random walk.png)

​																									图2：K=1时的随机行走

<img src="C:\Users\86130\Desktop\Computational Physics\hw4\question10\K=1.png"  />

​																	图3：K=1时(强电场)，速度的自相关函数与理论函数的比较

![](C:\Users\86130\Desktop\Computational Physics\hw4\question10\(K=0.01)random walk.png)

​																							图4：K=0.01时的随机行走

![](C:\Users\86130\Desktop\Computational Physics\hw4\question10\K=0.01.png)

​																图5：K=0.01时(弱电场)，速度的自相关函数与理论函数的比较



由图示结论可以看出，无论电场强度多大，我们的模拟结果都与理论曲线十分接近，也验证了理论$C(t)$与$K$无关的结论。

而图3与图5尾处的波动则是由于$<v(0)>$不精确为0导致的。



### 四、总结

此次实验模拟外加电场下的随机运动，理论上得出速度的自相关函数与外加电场无关的结论，并在实验上验证成功

加深了对随机运动的理解

# Report14

胡琦浩	PB21000235



## 一、问题

以 $x_{n+1}=\lambda sin(\pi x_n)$为迭代方程进行迭代：

(1)画出系统状态随参数$\lambda$的变化图，要求在图中体现出定值状态、倍周期分叉和混沌状态；

(2)列出各个倍周期分叉处的$\lambda$值，求相应的 $Feigenbaum$ 常数。



## 二、方法

### 3.1	系统状态随参数$\lambda$的变化图

主要采用迭代法计算：

![](C:\Users\86130\Desktop\Computational Physics\hw8\report14\未命名文件(2).png)

​																						图1：算法流程图

如图所示，只要计算了$0<\lambda <1$的情况，一共取了400个值，并定义了初始$x=0.5$



### 3.2	求倍周期分叉处的$\lambda$值和 $Feigenbaum$ 常数

求倍周期分叉处的$\lambda$值的算法流程：

(1)	根据得到的倍周期图将$\lambda$分为[0.71, 0.73], [0.83, 0.84], [0.85, 0.87], 每隔$10^{-5}$取值（这些范围是倍周期转变点，由下面得到的图可以清晰看出）

(2)	对应每个$\lambda$值迭代$5000$次，在最后$500$次得到的$x$值储存到$values$列表中（认为迭代多次后结果已经稳定）

(3)	将这$values$列表经过如下操作：

```python
period = len(set(np.round(values, decimals=8)))
```

np.round(values, decimals=4) 是将values中的所有元素四舍五入到小数点后8位，set则是一个集合(其中的元素具有唯一性)，故可以清晰地得到次$\lambda$值对应的周期数为多少

(4)	最后记录period从$1\rightarrow 2, 2\rightarrow 4, 4\rightarrow8$等的$\lambda$值即可



求$\alpha$的算法流程：

(1)	根据画出的图将$\lambda$的范围定为$[0.77,0.87]$，由于图中只能清晰看得到$T\leq8$时的图案，故不求$T=16$及以后的值

(2)	和上面算法类似，当set(np.round(values, decimals=8))集合内出现一个元素值于$0.5$的差值小于$0.001$，则将这个集合储存到字典my_dict中，且key=period

(3)	最后输出my_dict，然后根据图像的相对位置关系得出得出$d_m$即可

## 三、实验结果

### 3.1	系统状态随参数$\lambda$的变化图

<img src="C:\Users\86130\Desktop\Computational Physics\hw8\question14\0_lambda_1.png" style="zoom:72%;" />

​																							图2：定值状态、倍周期分叉和混沌状态

图中可以清晰的可以看出：$0<\lambda<0.318$时，$x$序列都收敛于0；$0.318<\lambda<0.717$时，系统处于定值状态；$0.717<\lambda<1$时，系统处于分别倍周期分叉和混沌状态。

<img src="C:\Users\86130\Desktop\Computational Physics\hw8\question14\0.7_lambda_1.png" style="zoom:72%;" />

​																							图3：放大后的倍周期和混沌状态

图中可以清晰得看到$T=2,4,8$的分叉点，而$T=16$并无法清晰看出



### 3.2	求倍周期分叉处的$\lambda$值和 $Feigenbaum$ 常数

由：$\lambda_{\infty}-\lambda_m=A\delta ^{-m}$，$(m>>1)$

则$\delta = \frac{\lambda_m - \lambda_{m-1}}{\lambda_{m+1}-\lambda_{m}}$

​																							表1：横轴方向倍周期分岔中的标度行为

|  m   |         T          | $\lambda_m$ | $\delta$ |
| :--: | :----------------: | :---------: | :------: |
|  1   |  1$\rightarrow$2   |   0.71909   |          |
|  2   |  2$\rightarrow$4   |   0.83292   |  4.424   |
|  3   |  4$\rightarrow$8   |   0.85865   |  4.721   |
|  4   |  8$\rightarrow$16  |   0.86410   |  4.658   |
|  5   | 16$\rightarrow$32  |   0.86527   |  4.680   |
|  6   | 32$\rightarrow$64  |   0.86552   |  5.000   |
|  7   | 64$\rightarrow$128 |   0.86557   |          |

最后得到的$\delta$值需要舍去，因为我的$\lambda$值精确到$10^{-5}$，而$m=6,7$时，$\lambda$值差就在最后一位，故误差较大需舍去

而由图表可以看出与理论值$\delta=0.669$的值相差不大，在其附近跳动





$\alpha=d_m/d_{m+1}$

​																							表2：纵轴方向倍周期分岔中的标度行为

|  m   |  T   |  $d_m$  | $\alpha$ |
| :--: | :--: | :-----: | :------: |
|  1   |  2   | 0.27943 |          |
|  2   |  4   | 0.10887 | 2.56664  |
|  3   |  8   | 0.04138 | 2.63098  |

可以看出结果较接近于理论值$\alpha=2.502 91$



## 四、总结

利用迭代法得到 $x_{n+1}=\lambda sin(\pi x_n)$得到系统状态随$\lambda$图，清晰地看出了定值态，倍周期分叉态和混沌态

最后还验证了$Feigenbaum$ 常数是一个与迭代方程无关的普适常数

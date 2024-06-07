# Report15

胡琦浩	PB21000235



## 一、问题

设体系能量为  $H(x,y)=-(x^2+y^2)+\frac{1}{2}(x^4+y^4)+\frac{1}{3}(x-y)^4$，取  $\beta=0.2, 1, 5$，采用Metrolopis抽样方法计算$<x^2>,<y^2>,<x^2+y^2>$。抽样时在二维平面上依次标出Markov链点分布，从而形象地理解Markov链。



## 二、方法

#### 2.1	理论计算

该热力学系统满足Boltzmann分布：
$$
p(x,y)=\frac{1}{A}exp(-\beta H(x,y))
$$
式中：$A=\int\int_{-\infty}^{\infty}exp(-\beta H(x,y))\,dxdy$

则应该有：
$$
<x^2>=\int\int_{-\infty}^{\infty}x^2p(x,y)\,dxdy
\\
<y^2>=\int\int_{-\infty}^{\infty}y^2p(x,y)\,dxdy
\\
<x^2+y^2>=\int\int_{-\infty}^{\infty}(x^2+y^2)p(x,y)\,dxdy=<x^2>+<y^2>
$$
由Mathematica计算结果如下：

| $\beta$ | $<x^2>$ | $<y^2>$ | $<x^2+y^2>$ |
| :-----: | :-----: | :-----: | :---------: |
|   0.2   | 1.13138 | 1.13138 |   2.26277   |
|    1    | 0.75789 | 0.75789 |   1.51579   |
|    5    | 0.86552 | 0.86552 |   1.73105   |



#### 2.2	抽样方法

由Metropolis方法：
$$
p_iW_{ij}=p_jW_{ij}
\\
W_{ij}=\begin{cases}T_{ij}\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,if\,\,p_j>p_i
\\
T_{ij}(p_j/p_i)\,\,\,\,\,\,\,if\,\,p_j<p_i
\end{cases}
$$
下标$i$和$j$是不同的，当两者相同时，满足转移概率的归一化：
$$
W_{ii}=1-\sum_{j\neq i}W_{ij}
$$
根据上述方法即可抽样出满足$p(x,y)$的样本

![](C:\Users\86130\Desktop\Computational Physics\hw9\report15\未命名文件(3).png)

​																								图1：抽样流程图

在本题中，不妨取$r_0=(-5,-5),\,\,\Delta r=(0.5,0.5),\,\,N=10^6$

则根据得到的样本值：$<x^2>=\frac{1}{N-m}\sum_{i=m+1}^{N}x_i^2$，舍去前$m$个热化的构型，在本题中取$m=1000$



## 三、实验结果

由Metropolis抽样法得到结果如下：

| $\beta$ | $<x^2>$ | $<y^2>$ | $<x^2+y^2>$ |
| :-----: | :-----: | :-----: | :---------: |
|   0.2   | 1.13002 | 1.13862 |   2.26864   |
|    1    | 0.75627 | 0.76115 |   1.51742   |
|    5    | 0.86251 | 0.86682 |   1.72933   |

可以看出，与Mathematica得到结果相差很小，精度很高

<img src="C:\Users\86130\Desktop\Computational Physics\hw9\question15\β=0.2Markov.png" style="zoom:72%;" />

​																		图2：$\beta=0.2$时的Markov链

<img src="C:\Users\86130\Desktop\Computational Physics\hw9\question15\β=1Markov.png" style="zoom:72%;" />

​																			图3：$\beta=1$时的Markov链

<img src="C:\Users\86130\Desktop\Computational Physics\hw9\question15\β=5Markov.png" style="zoom:72%;" />

​																			图4：$\beta=5$时的Markov链

由图可以看出，经过一段时间的热化过程，Markov链最后会交织在一起，达到平衡状态



## 四、总结

本题中再次运用了Metropolis抽样方法，更加深刻地认识了解了Markov链，以及运用Metropolis方法更加熟练


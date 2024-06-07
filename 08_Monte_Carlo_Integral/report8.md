# Report8

PB21000235	胡琦浩

### 一、问题

用Monte Carlo方法计算如下定积分，并讨论有效数字位数。
$$
\int_{0}^{5}dx\,\sqrt{x^2+2\sqrt{x}}
$$

$$
\int_{0}^{7/10}dx\,\int_{0}^{4/7}dy\,\int_{0}^{9/10}dz\,\int_{0}^{2}du\,\int_{0}^{13/11}dv\,(5+x^2-y^2+3xy-z^2+u^3-v^3)
$$

### 二、方法

### 2.1	$\int_{0}^{5}dx\,\sqrt{x^2+2\sqrt{x}}$

![](C:\Users\86130\Desktop\Computational Physics\hw3\report8\1.png)

采用重要抽样法:

在GeoGebra中选择不同参数的一次函数$g(x)$, 最终选定如图所示的$g(x)=0.96x+0.7$, 可以看出与f(x)吻合的很好。

对$g(x)$归一化处理:	$p(x)=\frac{g(x)}{\int_{0}^{5}g(x')\,dx'}=\frac{g(x)}{15.5}=\frac{0.96x+0.7}{15.5}$

则$I_1=\int_{0}^{5}f(x)\,dx=\int_{0}^{5}\frac{f(x)}{p(x)}p(x)\,dx=\int_{0}^{5}y(x)p(x)\,dx=<y>$,	式中:$y(x)=\frac{f(x)}{p(x)}$

要得到满足$p(x)$分布的样本，利用直接抽样法:	求$p(x)$的累计函数:$P(x)=\frac{0.48x^2+0.7x}{15.5}=\xi\in[0,1]$，则$x=\frac{-0.7+\sqrt{0.49+29.76\xi}}{0.96}$

标准值$I_1=15.4390107356$，误差为:$Error=\abs{<y>-15.4390107356}$

标准偏差: $\sigma_s\simeq \frac{5}{\sqrt{N}}\sqrt{<y^2>-<y>^2}$



### 2.2$\int_{0}^{7/10}dx\,\int_{0}^{4/7}dy\,\int_{0}^{9/10}dz\,\int_{0}^{2}du\,\int_{0}^{13/11}dv\,(5+x^2-y^2+3xy-z^2+u^3-v^3)$

直接利用简单抽样的Monte Carlo方法:

$I_2=\frac{1}{N}[\prod_{j=1}^{5}(b_j-a_j)]\sum_{i=1}^{N}f(x_i,y_i,z_i,u_i,v_i)=\frac{1}{N}\frac{234}{275}\sum_{i=1}^{N}f(x_i,y_i,z_i,u_i,v_i)=\frac{234}{275}<f(x,y,z,u,v)>$

标准值$I_2=5.6771209204$，误差为:$Error=\abs{\frac{234}{275}<f>-5.6771209204}$

标准偏差: $\sigma_s=\frac{234}{275}\frac{\sqrt{<f^2>-<f>^2}}{\sqrt{N}}$



### 三、实验结果

![](C:\Users\86130\Desktop\Computational Physics\hw3\report8\2.png)

可以看出，随着总样本数的提升，与标准值的差越来越小，在$N>5\times10^5$量级后，有效位数可以达到4位，标准偏差也逐渐变小

![](C:\Users\86130\Desktop\Computational Physics\hw3\report8\3.png)

分析同上，特别的$N=5\times10^5$时的误差比$N=10^6$小，可能是由于前者偶然的产生的随机数比后者更好，不过是小概率。有效位数随着N的增大而变多，可以达到4位



### 四、总结

此实验学习了Monte Carlo方法求解积分的具体过程，当N足够大时，积分的值精确度越高


























































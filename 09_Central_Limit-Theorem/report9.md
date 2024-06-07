# Report9

胡琦浩	PB21000235

### 一、问题

考虑泊松分布、指数分布，并再自设若干个随机分布（它们有相同或不同的$\mu$和$\sigma^2$)，通过Monte Carlo模拟，验证中心极限定理成立（*N* =2、5、10）

### 二、方法

中心极限定理:
$$
x=\frac{<X>-\mu}{\sigma/\sqrt{N}}\sim N(0,1)
$$
式中:$<X>=\frac{1}{N}\sum_{k=1}^{N}X_k$，$\sigma=\sqrt{<X^2>-<X>^2}$

因此, 先得到满足$f(x)$分布的N个样本，再利用python库依次算出分布函数$f(x)$的$\mu$与$\sigma$，标准化后画概率直方图验证是否满足标准正态分布

选择的分布有:

$\bullet$	指数分布$f(x)=\lambda e^{-\lambda x}$	$\lambda=\frac{1}{2}$

$\bullet$	泊松分布$P(X=k)=\frac{e^{-\lambda} \cdot \lambda^k}{k!}$	$\lambda=3$

$\bullet$	二项分布$P(X=k)=C_{n}^{k}(1-p)^kp^k$	$p=0.3$

### 三、实验结果

![](C:\Users\86130\Desktop\Computational Physics\hw3\question9\ExpN=10.png)

​																											图1：指数分布

![](C:\Users\86130\Desktop\Computational Physics\hw3\question9\PoiN=10.png)

​																											图2：泊松分布

![](C:\Users\86130\Desktop\Computational Physics\hw3\question9\BinoN=10.png)

​																											图3：二项分布

可以看出，随着N的增大，得到的概率直方图与标准正态分布越吻合，因此可以验证中心极限定理。但泊松分布和二项分布有些部分明显超过标准曲线，可能是样本数太少，得到的直方图并不稳定。



### 四、总结

此实验基本验证了中心极限定理，随着N越大，直方图越吻合标准正态分布

不过，不同参数的$\lambda$和$p$也会影响直方图与标准正态分布的吻合

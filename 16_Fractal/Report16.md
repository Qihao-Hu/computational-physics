# Report16

胡琦浩	PB21000235



## 一、问题

进行单中心DLA模型的模拟(可以用圆形边界，也可以用正方形边界)，并用两种方法计算模拟得到的DLA图形的分形维数，求分形维数时需要作出双对数图。



## 二、方法

#### 2.1	DLA模拟

DLA模拟过程在问题11中已解决，大致算法流程如下：

![](C:\Users\86130\Desktop\Computational Physics\hw5\report11\未命名文件(1).png)

​																				图1：算法流程

在本题中，初始化数据如下：

网格大小：grid_size = 256

释放粒子数目：num_particles = 5000

初始：r_max = 10



#### 2.2	Sandbox法

Sandbox 法（图 3.13）是将一系列尺寸 *r*（>1）不断增大的方框（也可以是圆）覆盖到分形图形（如 DLA 图形）上，计数不同方框（或圆）中象素数 *N*（即以象素为测量单元）在$ln N$~$ln r$图上如有直线部分，则在此范围内存在：$N$~$r^D$，直线部分的斜率即分形维数$D$

<img src="C:\Users\86130\AppData\Roaming\Typora\typora-user-images\image-20231223143826638.png" alt="image-20231223143826638" style="zoom:67%;" />

​																							图2：Sandbox法计算分维示意图

在我的实验中采用的是圆形边框，圆的半径由10~70，统计各半径内像素个数N，然后线性拟合即可



#### 2.3	盒计数法

![image-20231223151522438](C:\Users\86130\AppData\Roaming\Typora\typora-user-images\image-20231223151522438.png)

​																							图3：盒计数法示意图

此方法如图3所示，不断减小网格尺寸$\varepsilon$继续计数含图形象素的网格数$N(\varepsilon)$，直至最小的网格尺寸达到象素为止。

为了减少误差，应该使不同尺寸的网格能覆盖相同大小的图形, 因此在本题中取网格$\varepsilon$大小，并记录相应的$N(\varepsilon)$，作$ln(N(\varepsilon))$~$ln(1/\varepsilon)$图，图中线性部分的斜率即为图形分形维数$D$



## 三、实验结果

<img src="C:\Users\86130\Desktop\Computational Physics\hw10\question16\DLA.png" style="zoom:72%;" />

​																						图4：得到的DLA模型图

#### 3.1	Sandbox法

<img src="C:\Users\86130\AppData\Roaming\Typora\typora-user-images\image-20231223155055298.png" alt="image-20231223155055298" style="zoom: 80%;" />

​																					图5：Sandbox结果





<img src="C:\Users\86130\AppData\Roaming\Typora\typora-user-images\image-20231223155813237.png" alt="image-20231223155813237" style="zoom:80%;" />

​																						图6：$ln N$与$lnr$的关系图

可以看出后面几个点由于靠近整个分形的边缘导致不合理，应该舍取。因此取前9个点进行拟合，结果如下：<img src="C:\Users\86130\AppData\Roaming\Typora\typora-user-images\image-20231223161137344.png" alt="image-20231223161137344" style="zoom: 67%;" />

​																					   图7：$ln N$与$lnr$拟合结果

由拟合结果可以得到：$D=1.7024$与理论值很接近，结果较好



#### 3.2	盒计数法

![image-20231223162143201](C:\Users\86130\AppData\Roaming\Typora\typora-user-images\image-20231223162143201.png)

​																						图8：盒计数法结果



<img src="C:\Users\86130\AppData\Roaming\Typora\typora-user-images\image-20231223163440703.png" alt="image-20231223163440703" style="zoom: 80%;" />

​																							图9：$lnN$与$ln(1/\varepsilon)$的关系图

![image-20231223165848809](C:\Users\86130\AppData\Roaming\Typora\typora-user-images\image-20231223165848809.png)

​																						图10：$lnN$与$ln(1/\varepsilon)$拟合关系图

​		可以看出得到结果较差，$D=1.404$与标准值相差较大，当我尝试多试几组数值数据时，发现改变并不大，得到的结果始终在$1.4$附近，我考虑可能的原因是我盒子的放置范围为图4整个范围，而不是包含分形的最小矩阵范围，因此我将范围改为包含分形的最小矩阵范围。由于每次生成的分形最小矩阵范围都不相同，因此同一设定$\varepsilon=1,5,10,15,20,25,30$，结果如下：

​														<img src="C:\Users\86130\AppData\Roaming\Typora\typora-user-images\image-20231223224626331.png" alt="image-20231223224626331" style="zoom:80%;" />

​																								图11：改进后盒计数法结果



<img src="C:\Users\86130\AppData\Roaming\Typora\typora-user-images\image-20231223225219624.png" alt="image-20231223225219624" style="zoom:80%;" />

​																								图12：改进后$lnN$与$ln(1/\varepsilon)$的关系图

由图像可以看出，前面几个点较线性，因此舍取最后一个点，拟合结果如下：     		   

​                                      <img src="C:\Users\86130\AppData\Roaming\Typora\typora-user-images\image-20231223225700594.png" alt="image-20231223225700594" style="zoom:80%;" />   

​																							图13：改进后$lnN$与$ln(1/\varepsilon)$拟合关系图																														

​		此时可以看出：$D=1.5928$，与标准值在1.6~1.7之间较为符合，考虑到由于最小矩阵大小的不确定性，我没取能整除矩阵边长的$\varepsilon$值，因此有一定的误差可以理解



## 四、总结

​		在本题中采用了两种不同的方法去计算DLA分形的维数。

​		在我的实际实验中，认为Sandbox方法相较于盒计数法更加便捷，它不需要考虑每次生成的分形的不同而采用不同的实验参数，只需要取一系列不完全涵盖分形的圆形边框并记数即可，不过此方法最好需要分形图案有个中心点，本次DLA图形刚好符合。

​		而对于盒计数法，取一个围住分形的最小边框可能让结果精度更高，不过由于每次生成的分形都不相同，因此无法确定一个同一的$\varepsilon$值，但如果计算确定的分形图案应该会更好。














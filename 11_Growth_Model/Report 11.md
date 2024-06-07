# Report 11

胡琦浩	PB21000235

### 一、问题

模拟2维DLA以及介电击穿（DBM）图案并讨论

### 二、方法

#### 2.1	DLA模型

扩散受限聚集模型（DLA—Diffusion Limited Aggregation）

模拟规则：取一个2维的方形点阵，在点阵中央原点处放置一个粒子作为生长的种子，然后从距原点足够远的圆周界处释放一个粒子，让它作 Brown 运动或随机行走，其结果是：该粒子走到种子的最近邻位置与种子相碰，这时让粒子粘结到种子上不再运动；或者粒子走到大于起始圆的更远处（如2-3倍的半径处）或干脆走到点阵边界，这时认为粒子走了一条无用的轨迹，取消该粒子，把它重新放回原点。因此，那些有用的粒子与种子相粘结后形成不断生长的聚集集团。

![](C:\Users\86130\Desktop\Computational Physics\hw5\report11\未命名文件(1).png)

​																								图1：算法流程图

#### 2.2	介质击穿模型

介电击穿模型原来就是用来理解在气体、液体、固体绝缘体中介电击穿中所产生的分枝状击穿图像。

在这个模型中，假定击穿图形的生长速率是电势$\Phi$的梯度的函数，即$v=f(\nabla_n\phi)$，$\vec{n}$垂直于图形界面。

电势服从于Laplace方程：$\nabla\phi=0$，此时的边界条件为：已被占据的格子上$\phi=\phi_0$，而在远处$\phi=0$，我们需要数值求解离散方格点阵上的 Laplace 方程式：$\phi_{i,j}=(\phi_{i-1,j}+\phi_{i,j-1}+\phi_{i+1,j}+\phi_{i,j+1})/4$ 

通常，假设格点扩散的生长速率是：$v_{i,j}=n\left\lvert\phi_0-\phi_{i,j} \right\rvert ^\eta$，$n$是已被占据的格子数目，$\eta$是速率参数，于是环绕已占据格子周界上的一个空格子被占据的几率是：$p_{i,j}=v_{i,j}/\sum v_{i,j}$，其中求和遍历周界上所有可以被占据的空格子，根据该几率随机选择一个格子进行占据，然后重新计算生长速率。

![](C:\Users\86130\Desktop\Computational Physics\hw5\report11\未命名文件(2).png)

​																								图2：算法流程图	

在我的算法中，采用迭代的方法计算Laplace方程的数值解：

```python
def solve_laplace(grid, phi_0):
    potential = np.copy(grid)
    for _ in range(10):  # 迭代次数
        for i in range(1, grid_size-1):
            for j in range(1, grid_size-1):
                if grid[i, j] == 0:
                    potential[i, j] = (potential[i-1, j] + potential[i+1, j] +
                                       potential[i, j-1] + potential[i, j+1]) / 4
    potential[grid == phi_0] = phi_0
    return potential
```

grid记录网格中已占据的粒子，占据的位置记为1，其余为0。将grid复制给potential，用来记录电势分布，粒子已占据的位置电势值设为1，边界处恒为0。在没有粒子的位置上（$grid[i, j] == 0$），此处的电势值为周围4个电势的平均，遍历整个网格，并迭代10次，收敛于精确值。

计算Laplace方程的数值解时，其复杂度达到了$O(10\times grid\_size^2\times n\_steps)$，式中$n\_steps$为模拟步数(即生成的点数)

在我的实验中取：$grid\_size=150,\,n\_steps=300$

### 三、实验数据

#### 3.1	DLA模型

<img src="C:\Users\86130\Desktop\Computational Physics\hw5\question11\DLA(num=1000).png" style="zoom: 80%;" />

​																			        图3：一共释放了1000个粒子生成的DLA模型

<img src="C:\Users\86130\Desktop\Computational Physics\hw5\question11\DLA(num=2000).png" style="zoom:72%;" />

​																						图4：一共释放了2000个粒子生成的DLA模型

<img src="C:\Users\86130\Desktop\Computational Physics\hw5\question11\DLA(num=3000).png" style="zoom:72%;" />

​																						 图5：一共释放了3000个粒子生成的DLA模型

可以看出生成的DLA模型非常好。枝状图形生长的原因在于粒子的随机运动，随机行走或扩散的粒子抵达集团时绝大多数聚集在集团的尖端附近，只有少数粒子进入到沟槽中，这样使集团显示出各种大小尺度的沟槽和触须。当粒子进入一个沟槽之前，很有可能碰上一根在外的触须，因而粒子无法进入沟槽内，形成屏蔽效应。这一结构反映出生长过程的特征，即越是尖端处生长得越快，从而形成枝蔓向外延伸，越是平坦处生长得越慢，从而出现沟槽中的空隙疏松结构。这样的形貌只有当粒子粘结到集团而无任何优先选择的方向时才会出现，但如果要是有优先方向的话，则产生的集团形貌可以是类似于雪花等其它形状。						

#### 3.2	DBM模型

由于算法限制，选择在$150\times150$的网格里面只生成300个点					

​                                            ![](C:\Users\86130\Desktop\Computational Physics\hw5\question11\DBM(eta=10).png)												 

​																								图6：$\eta=10$生成的DBM模型

​                                            ![](C:\Users\86130\Desktop\Computational Physics\hw5\question11\DBM(eta=12).png)

​																							图7：$\eta=12$生成的DBM模型

​                                         ![](C:\Users\86130\Desktop\Computational Physics\hw5\question11\DBM(eta=15).png)

​																								图8：$\eta=15$生成的DBM模型

可以看出随着$\eta$的增大，DBM模型逐渐由二维变为一维，原因是因为$v_{i,j}=n\left\lvert\phi_0-\phi_{i,j} \right\rvert ^\eta$，随着$\eta$的增大，较大势能梯度的点将会优先选择，导致逐渐成为线性。且在$\eta=15$时，击穿了边界。



### 四、总结

在本题中进行了对DLA模型以及DBM模型的模拟，得到了实验结果，不足的是没有用更有效的方法去计算Laplace方程的数值解，导致DBM模型中的粒子数偏少




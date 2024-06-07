import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')

# 将λ的值从0.7到1的区域放大，并重新绘制分叉图

# 参数
lambda_values = np.linspace(0.7, 1, 400)  # λ的取值范围调整为0.7到1
iterations = 5000  # 每个λ值的迭代次数
last = 500  # 要绘制的最后迭代次数，用以展示行为

# 初始化存储x值的数组
x = 0.5 * np.ones_like(lambda_values)

# 创建绘图
plt.figure(figsize=(12, 6))

# 遍历每个λ值
for i in range(iterations):
    x = lambda_values * np.sin(np.pi * x)  # 迭代方程
    # 仅绘制最后'last'次迭代以展示最终行为
    if i >= (iterations - last):
        plt.plot(lambda_values, x, ',k', alpha=1)  # 改变点的颜色和大小

# 设置图形
plt.xlabel("$\lambda$")
plt.ylabel("$x$")
plt.xlim(0.7, 1)
plt.ylim(0, 1)

# 设置刻度线
plt.xticks(np.arange(0.7, 1, 0.05))
plt.yticks(np.arange(0, 1, 0.1))
plt.grid(True)

# 显示图形
plt.savefig("0.7_lambda_1.png")


import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')

# 参数
lambda_values = np.linspace(0, 1, 400)  # lambda的取值范围
iterations = 5000  # 每个lambda值的迭代次数
last = 500  # 要绘制的最后迭代次数，用以展示行为

# 初始化存储x值的数组
x = 0.5 * np.ones_like(lambda_values)

# 创建绘图
plt.figure(figsize=(12, 6))

# 遍历每个lambda值
for i in range(iterations):
    x = lambda_values * np.sin(np.pi * x)  # 迭代方程
    # 仅绘制最后'last'次迭代以展示最终行为
    if i >= (iterations - last):
        plt.plot(lambda_values, x, ',k', alpha=1)

# 设置图形
plt.xlabel("$\lambda$")
plt.ylabel("$x$")
plt.xlim(0, 1)
plt.ylim(0, 1)

# 设置刻度线
plt.xticks(np.arange(0, 1.1, 0.1))
plt.yticks(np.arange(0, 1.1, 0.1))
plt.grid(True)

# 显示图形
plt.savefig("0_lambda_1.png")


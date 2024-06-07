import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')

# 模拟的样本数量
sample_count = 10000

# 指数分布的参数
lambda_param = 0.5

# 不同的样本大小 N
Ns = [2, 5, 10]

# 存储变换后的样本均值的列表
standardized_sample_means = []

# 存储样本均值的列表
sample_means = []

# 进行Monte Carlo模拟
for N in Ns:
    means = []
    for _ in range(sample_count):
        # 生成N个指数分布的样本
        samples = np.random.exponential(scale=1 / lambda_param, size=N)

        # 计算样本均值
        sample_mean = np.mean(samples)

        # 存储样本均值
        means.append(sample_mean)

    sample_means.append(means)

    # 标准化样本均值
    standardized_samples = (means - np.mean(means)) / np.std(means)
    standardized_sample_means.append(standardized_samples)

# 绘制直方图和对比的标准正态分布
plt.figure(figsize=(12, 6))

for i, N in enumerate(Ns):
    plt.subplot(1, len(Ns), i + 1)
    plt.hist(standardized_sample_means[i], bins=30, density=True, alpha=0.7, color='b', label=f'N={N}')

    # 绘制标准正态分布的概率密度函数作为对比
    x = np.linspace(min(standardized_sample_means[i]), max(standardized_sample_means[i]), 100)
    normal_dist = 1 / (np.sqrt(2 * np.pi)) * np.exp(-x ** 2 / 2)
    plt.plot(x, normal_dist, 'k--', label='Standard Normal Distribution')

    plt.title(f'N={N}')
    plt.xlabel('Standardized Sample Mean')
    plt.ylabel('Probability Density')
    plt.legend()

plt.savefig('Exp.png')
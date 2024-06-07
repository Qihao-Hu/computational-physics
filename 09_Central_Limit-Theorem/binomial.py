import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')

# 参数设置
sample_count = 10000  # 模拟样本数量
n_values = [2, 5, 10]  # 样本大小N
p = 0.3  # 二项分布的成功概率

# 存储标准化后的样本均值的列表
standardized_sample_means = []

# 进行Monte Carlo模拟
for n in n_values:
    sample_means = []

    for _ in range(sample_count):
        # 生成二项分布的样本
        samples = np.random.binomial(n, p, size=n)

        # 计算样本均值
        sample_mean = np.mean(samples)

        sample_means.append(sample_mean)

    # 将样本均值列表转换为NumPy数组
    sample_means = np.array(sample_means)

    # 计算均值和标准差
    mean_of_sample_means = np.mean(sample_means)
    std_dev_of_sample_means = np.std(sample_means)

    # 标准化样本均值，使其符合N(0,1)
    standardized_means = (sample_means - mean_of_sample_means) / std_dev_of_sample_means

    # 将标准化后的样本均值存储在列表中
    standardized_sample_means.append(standardized_means)

# 绘制直方图和对比的标准正态分布
plt.figure(figsize=(12, 6))

for i, n in enumerate(n_values):
    plt.subplot(1, len(n_values), i + 1)
    plt.hist(standardized_sample_means[i], bins=30, density=True, alpha=0.7, color='b', label=f'N={n}')

    # 绘制标准正态分布的概率密度函数作为对比
    x = np.linspace(min(standardized_sample_means[i]), max(standardized_sample_means[i]), 100)
    normal_dist = 1 / np.sqrt(2 * np.pi) * np.exp(-x ** 2 / 2)
    plt.plot(x, normal_dist, 'k--', label='Standard Normal Distribution')

    plt.title(f'Standardized N={n}')
    plt.xlabel('Standardized Sample Mean')
    plt.ylabel('Probability Density')
    plt.legend()

plt.savefig('Binomial.png')
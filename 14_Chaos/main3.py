import numpy as np
import sys

iterations = 5000  # 每个λ值的迭代次数
last = 500  # 要绘制的最后迭代次数，用以展示行为

for lambda_value in np.arange(0.71, 0.73, 1e-5):
    x = 0.5
    values = []

    # 先迭代一段时间，让系统达到稳定状态
    for i in range(iterations - last):
        x = lambda_value * np.sin(np.pi * x)

    # 记录最后一段迭代的值，用于判断周期
    for i in range(last):
        x = lambda_value * np.sin(np.pi * x)
        values.append(x)

    # 简单的方法来判断周期 - 查找重复的值
    period = len(set(np.round(values, decimals=8)))
    if period > 1 and period % (2) == 0:
        print(lambda_value)
        break

for lambda_value in np.arange(0.83, 0.84, 1e-5):
    x = 0.5
    values = []

    # 先迭代一段时间，让系统达到稳定状态
    for i in range(iterations - last):
        x = lambda_value * np.sin(np.pi * x)

    # 记录最后一段迭代的值，用于判断周期
    for i in range(last):
        x = lambda_value * np.sin(np.pi * x)
        values.append(x)

    # 简单的方法来判断周期 - 查找重复的值
    period = len(set(np.round(values, decimals=8)))
    if period > 1 and period % (4) == 0:
        print(lambda_value)
        break

n = 0
for lambda_value in np.arange(0.85, 0.87, 1e-5):
    x = 0.5
    values = []

    # 先迭代一段时间，让系统达到稳定状态
    for i in range(iterations - last):
        x = lambda_value * np.sin(np.pi * x)

    # 记录最后一段迭代的值，用于判断周期
    for i in range(last):
        x = lambda_value * np.sin(np.pi * x)
        values.append(x)

    # 简单的方法来判断周期 - 查找重复的值
    period = len(set(np.round(values, decimals=8)))
    if period > 1 and period % (8 * (2**n)) == 0:
        print(lambda_value)
        n = n+1

input("Press Enter to exit...")
sys.exit()
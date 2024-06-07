import numpy as np
import sys

iterations = 5000  # 每个λ值的迭代次数
last = 500  # 要绘制的最后迭代次数，用以展示行为
my_dict = {}    # 储存纵向距离点

for lambda_value in np.arange(0.77, 0.87, 1e-4):
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
    if any(abs(element - 0.5) < 1e-3 for element in set(np.round(values, decimals=8))):
        my_dict[period] = set(np.round(values, decimals=8))
        if period == 8:
            break

print(my_dict)

input("Press Enter to exit...")
sys.exit()
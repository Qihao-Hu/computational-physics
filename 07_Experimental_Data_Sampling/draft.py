import numpy as np
from scipy import interpolate
def read_txt():
    # 打开文本文件
    with open('data.txt', 'r') as file:
        # 跳过前一行
        next(file)
        # 使用 numpy 读取数据
        data = np.loadtxt(file)

    # 将数据分离为 x 和 y
    x = data[:, 0]  # 第一列作为 x 轴
    y = data[:, 1]  # 第二列作为 y 轴

    return x,y

# 示例数据点
energy = read_txt()[0]
num = read_txt()[1]  # 储存每个energy的数量
data = [elem2 / sum(num) for elem2 in num]
spline = interpolate.splrep(energy, data, s=0)

x_new = 3010.5
y_new = interpolate.splev(x_new, spline)

print(f"在 x={x_new} 处的估算值: {y_new}")
import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib
import sys
matplotlib.use('agg')

def initialize_grid(grid_size):
    """ 初始化网格，并在中心处放置初始种子 """
    grid = np.zeros((grid_size, grid_size))
    center = grid_size // 2
    grid[center, center] = 1  # 放置种子
    return grid

def is_adjacent_to_seed(x, y, grid):
    """ 判断是否与种子粘接 """
    neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    for nx, ny in neighbors:
        if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1]:
            if grid[nx, ny] == 1:
                return True
    return False

def simulate_dla(grid, release_distance_func, max_radius_func, num_particles):
    """ 模拟DLA形成过程 """
    grid_size = len(grid)
    center = grid_size // 2
    rmax = 10  # 初始化最大半径

    for _ in range(num_particles):
        rmax = max(
            rmax,
            np.sqrt(((np.argwhere(grid == 1) - center)**2).sum(axis=1)).max()
        )   # 更新最大半径

        release_distance = release_distance_func(rmax)
        max_radius = max_radius_func(rmax)

        # 在释放圆周上随机释放粒子
        angle = random.uniform(0, 2 * np.pi)
        x, y = int(center + release_distance * np.cos(angle)), int(center + release_distance * np.sin(angle))

        while True:
            # 随机行走
            x += random.choice([-1, 0, 1])
            y += random.choice([-1, 0, 1])

            # 判断是否到达边界
            if x < 0 or x >= grid_size or y < 0 or y >= grid_size or np.sqrt((x - center)**2 + (y - center)**2) > max_radius:
                break

            # 判断是否与种子粘接
            if is_adjacent_to_seed(x, y, grid):
                grid[x, y] = 1
                break

    return grid

# 初始化模拟数据
grid_size = 256  # 网格大小
release_distance_func = lambda rmax: rmax + 5  # 释放半径为rmax+5
max_radius_func = lambda rmax: 2 * rmax        # 最远半径为2rmax
num_particles = 5000  # 一共释放粒子数目

# 初始化网格以及模拟DLA
grid = initialize_grid(grid_size)
grid = simulate_dla(grid, release_distance_func, max_radius_func, num_particles)

# 画出图像
plt.figure(figsize=(8, 8))
plt.imshow(grid, cmap='Greys', interpolation='nearest')
plt.title("Diffusion Limited Aggregation Simulation")
# plt.axis('off')
plt.savefig('DLA.png')



# Sandbox方法计算
print("Sandbox法")
def count_elements_within_radius(grid, radius):
    center = np.array(grid.shape) // 2
    y, x = np.ogrid[:grid.shape[0], :grid.shape[1]]
    distances = np.sqrt((x - center[1]) ** 2 + (y - center[0]) ** 2)

    count = np.sum((distances < radius) & (grid == 1))
    return count

# 统计半径小于r的范围内 grid[x, y] = 1 的个数
for radius_limit in range(10, 75, 5):
    count_within_radius = count_elements_within_radius(grid, radius_limit)
    print(f"半径小于{radius_limit}的范围内，grid[x, y] = 1 的个数为: {count_within_radius}")



# 盒计数法
print("盒计数法")
indices = np.argwhere(grid == 1)
def box_counting(grid, size):
    """ 使用不同的盒子尺寸进行盒计数法 """
    count = 0
    # 将网格划分为当前大小的框
    for i in range(np.min(indices, axis=0)[0], np.max(indices, axis=0)[0], size):
        for j in range(np.min(indices, axis=0)[1], np.max(indices, axis=0)[1], size):
            if np.any(grid[i:i+size, j:j+size]):  # 检查盒子里是否有分形的任何部分
                count += 1
    return count

for size in [1, 5, 10, 15, 20, 25, 30]:  # 不同盒子大小
    count = box_counting(grid, size)
    print(f"网格尺寸大小为ε = {size}, 有分形的数目为N = {count}")

input("Press Enter to exit...")
sys.exit()
import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib
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
grid_size = 201  # 网格大小
release_distance_func = lambda rmax: rmax + 5  # 释放半径为rmax+5
max_radius_func = lambda rmax: 3 * rmax       # 最远半径为3rmax
num_particles = 3000  # 一共释放粒子数目

# 初始化网格以及模拟DLA
grid = initialize_grid(grid_size)
grid = simulate_dla(grid, release_distance_func, max_radius_func, num_particles)

# 画出图像
plt.figure(figsize=(8, 8))
plt.imshow(grid, cmap='Greys', interpolation='nearest')
plt.title("Diffusion Limited Aggregation Simulation")
plt.axis('off')
plt.savefig('DLA.png')
import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib
matplotlib.use('agg')

# 初始化参数
grid_size = 150  # 网格大小
phi_0 = 1       # 占据格子的电势
eta = 15       # 速率参数
n_steps = 300   # 模拟步数

# 初始化网格，0表示空格子，1表示已占据的格子
grid = np.zeros((grid_size, grid_size))

# 将网格中心设置为已占据的格子
center = grid_size // 2
grid[center, center] = phi_0

# 函数：求解Laplace方程
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

# 函数：计算生长速率和选择占据的格子
def grow_crystal(grid, potential, phi_0, eta):
    velocities = {}
    for i in range(1, grid_size-1):
        for j in range(1, grid_size-1):
            if grid[i, j] == 0:
                # 计算这个格子四个直接邻居中被占据的格子数目
                n = grid[i - 1, j] + grid[i + 1, j] + grid[i, j - 1] + grid[i, j + 1]
                if n > 0:
                    velocity = n * np.abs(phi_0 - potential[i, j]) ** eta
                    velocities[(i, j)] = velocity
                else:
                    velocities[(i, j)] = 0

    if velocities:
        total_velocity = sum(velocities.values())
        probabilities = {k: v / total_velocity for k, v in velocities.items()}
        chosen_cell = random.choices(list(probabilities.keys()), weights=probabilities.values())[0]
        grid[chosen_cell] = phi_0

# 模拟过程
for _ in range(n_steps):
    potential = solve_laplace(grid, phi_0)
    grow_crystal(grid, potential, phi_0, eta)

# 绘制最终的格子图
plt.imshow(grid, cmap='Greys')
plt.title('Dielectric Breakdown Model Simulation')
plt.axis('off')
plt.savefig('DBM.png')

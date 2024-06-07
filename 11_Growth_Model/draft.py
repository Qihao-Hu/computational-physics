# 使用优化的高斯-塞德尔迭代法求解Laplace方程的函数
def solve_laplace_gauss_seidel_optimized(grid, iterations=50):
    for _ in range(iterations):
        # 使用边界条件
        grid[0, :] = grid[-1, :] = grid[:, 0] = grid[:, -1] = 0
        for i in range(1, grid_size-1):
            for j in range(1, grid_size-1):
                if grid[i, j] == 0:
                    # 直接更新原网格
                    grid[i, j] = (grid[i-1, j] + grid[i+1, j] +
                                  grid[i, j-1] + grid[i, j+1]) / 4
        grid[center, center] = phi_0  # 保持中心格子的电势不变
    return grid

# 重新进行模拟，使用优化后的高斯-塞德尔方法
grid = np.zeros((grid_size, grid_size))  # 重置网格
grid[center, center] = phi_0  # 设置中心点

for _ in range(n_steps):
    potential = solve_laplace_gauss_seidel_optimized(grid)
    grow_crystal(grid, potential, phi_0, eta)

# 绘制最终的格子图
plt.imshow(grid, cmap='hot')
plt.title('Dielectric Breakdown Model Simulation with Optimized Gauss-Seidel')
plt.axis('off')
plt.show()

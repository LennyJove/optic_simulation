import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 参数设置
A0 = 1.0          # 振幅
lmbd = 0.5        # 波长 [单位：空间坐标单位]
L = 2 * lmbd      # 坐标范围 [-L, L]
N = 500           # 采样点数

# 计算波矢k
k = 2 * np.pi / lmbd  # 波数

# 设置源点位置（位于网格中心）
xc, yc = 0 , 0 

# 创建网格
x = np.linspace(-L, L, N)
y = np.linspace(-L, L, N)
X, Y = np.meshgrid(x, y)

# 计算复振幅
R = np.sqrt((X - xc) ** 2 + (Y - yc) ** 2)
E = A0/R * np.exp(1j * k* R)  # 复振幅
intensity = np.abs(E) ** 2
log_in = np.log(1+intensity)
phase = np.angle(E)

# 可视化（绘制强度和相位）
plt.figure(figsize=(12, 6))  # 创建了一个宽12英寸、高6英寸的图形窗口

# 绘制强度图
plt.subplot(1, 2, 1)
plt.imshow(log_in, 
           cmap='viridis',          # 使用viridis颜色映射
           extent=[-L, L, -L, L],
           origin='lower')          # 坐标系原点在左下角
plt.colorbar(label='Intensity')
plt.xlabel('x/um')
plt.ylabel('y/um')
plt.title(f'Intensity Distribution: λ={lmbd:.2e}')

# 绘制相位图
plt.subplot(1, 2, 2)
plt.imshow(phase, 
           cmap='hsv',              # 使用hsv颜色映射表示相位
           extent=[-L, L, -L, L],
           origin='lower')          # 坐标系原点在左下角
plt.colorbar(label='Phase (radians)')
plt.xlabel('x/um')
plt.ylabel('y/um')
plt.title(f'Phase Distribution: λ={lmbd:.2e}')

plt.tight_layout()
plt.show()
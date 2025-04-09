import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 参数设置
A0 = 1.0          # 振幅
lmbd = 632.8e-9   # 波长 [单位：空间坐标单位]
theta = np.pi/4   # 传播方向与x轴夹角 [弧度]
L = 2 * lmbd      # 坐标范围 [-L, L]
N = 500           # 采样点数

# 计算波矢k
k = 2 * np.pi / lmbd  # 波数
kx = k * np.cos(theta)   # x方向波矢分量
ky = k * np.sin(theta)   # y方向波矢分量

# 创建网格
x = np.linspace(-L, L, N)
y = np.linspace(-L, L, N)
X, Y = np.meshgrid(x, y)

# 计算复振幅
phase = kx * X + ky * Y      # 相位项 k·r
E = A0 * np.exp(1j * phase)  # 复振幅
intensity = np.abs(E) ** 2
phase = np.angle(E)

# np.real(E)
# 可视化（绘制实部）
# 可视化（绘制强度和相位）
plt.figure(figsize=(12, 6))

# 绘制强度图
plt.subplot(1, 2, 1)
plt.imshow(intensity, 
           cmap='viridis',          # 使用viridis颜色映射
           extent=[-L, L, -L, L],
           origin='lower')          # 坐标系原点在左下角
plt.colorbar(label='Intensity')     # 在绘图中添加一个颜色条
plt.xlabel('x/m')
plt.ylabel('y/m')
plt.title(f'Intensity Distribution: λ={lmbd:.2e}, θ={np.rad2deg(theta):.1f}°')

# 绘制相位图
plt.subplot(1, 2, 2)
plt.imshow(phase, 
           cmap='hsv',              # 使用hsv颜色映射表示相位
           extent=[-L, L, -L, L],
           origin='lower')          # 坐标系原点在左下角
plt.colorbar(label='Phase (radians)') 
plt.xlabel('x/m')
plt.ylabel('y/m')
plt.title(f'Phase Distribution: λ={lmbd:.2f}, θ={np.rad2deg(theta):.1f}°')

plt.tight_layout()
plt.show()
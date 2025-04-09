import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 参数设置
A0 = 1.0          # 振幅
lmbd = 0.5        # 波长 [um]
theta = 0         # 传播方向与x轴夹角 [弧度]np.pi/4
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

# 创建三维图形
fig = plt.figure(figsize=(18, 12))

# 绘制复振幅的实部
ax1 = fig.add_subplot(221, projection='3d')
ax1.plot_surface(X, Y, np.real(E), cmap='viridis', alpha=0.7)  # 颜色映射，表面透明度
ax1.set_title('Real Part of Complex Amplitude')
ax1.set_xlabel('x/um')
ax1.set_ylabel('y/um')
ax1.set_zlabel('Real(E)')
ax1.view_init(elev=30, azim=45)   # 调整观察角度 仰角30度，方位角45度

# 绘制复振幅的虚部
ax2 = fig.add_subplot(222, projection='3d')
ax2.plot_surface(X, Y, np.imag(E), cmap='viridis', alpha=0.7)
ax2.set_title('Imaginary Part of Complex Amplitude')
ax2.set_xlabel('x/um')
ax2.set_ylabel('y/um')
ax2.set_zlabel('Imag(E)')
ax2.view_init(elev=30, azim=45)

# 绘制强度图
ax3 = fig.add_subplot(223, projection='3d')
ax3.plot_surface(X, Y, intensity, cmap='viridis', alpha=0.7)
ax3.set_title('Intensity Distribution')
ax3.set_xlabel('x/um')
ax3.set_ylabel('y/um')
ax3.set_zlabel('Intensity')
ax3.view_init(elev=30, azim=45)

# 绘制相位图
ax4 = fig.add_subplot(224, projection='3d')
phase_plot = ax4.plot_surface(X, Y, phase, cmap='hsv', alpha=0.7)
fig.colorbar(phase_plot, ax=ax4, label='Phase (radians)')
ax4.set_title('Phase Distribution')
ax4.set_xlabel('x/um')
ax4.set_ylabel('y/um')
ax4.set_zlabel('Phase (radians)')
ax4.view_init(elev=30, azim=45)

plt.tight_layout()
plt.show()
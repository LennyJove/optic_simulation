import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 设置波长
wavelength = 0.5  # 单位：微米
# 计算波数
k = 2 * np.pi / wavelength
# 创建网格
x = np.linspace(-4 * wavelength, 4 * wavelength, 400)
y = np.linspace(-4 * wavelength, 4 * wavelength, 400)
X, Y = np.meshgrid(x, y)

# 设置源点位置（位于网格中心）
xc, yc = 0 * wavelength, 0 * wavelength

# 计算球面波
R = np.sqrt((X - xc) ** 2 + (Y - yc) ** 2)
A = 1.0 / R             # 球面波的振幅随距离增加而减小
P = np.exp(1j * k * R)  # 球面波的相位随距离增加而变化
U = A * P  # 复振幅

# 计算强度和相位
intensity = np.abs(U) ** 2
phase = np.angle(U)

# 创建三维图形
fig = plt.figure(figsize=(18, 12))

# 绘制复振幅的实部
ax1 = fig.add_subplot(221, projection='3d')
surf1 = ax1.plot_surface(X, Y, np.real(U), cmap='viridis', alpha=0.7)
fig.colorbar(surf1, ax=ax1, label='Real(U)')
ax1.set_title('复振幅的实部')
ax1.set_xlabel('x/um')
ax1.set_ylabel('y/um')
ax1.set_zlabel('Real(U)')
ax1.view_init(elev=30, azim=45)

# 绘制复振幅的虚部
ax2 = fig.add_subplot(222, projection='3d')
surf2 = ax2.plot_surface(X, Y, np.imag(U), cmap='viridis', alpha=0.7)
fig.colorbar(surf2, ax=ax2, label='Imag(U)')
ax2.set_title('复振幅的虚部')
ax2.set_xlabel('x/um')
ax2.set_ylabel('y/um')
ax2.set_zlabel('Imag(U)')
ax2.view_init(elev=30, azim=45)

# 绘制强度图（对数尺度）
ax3 = fig.add_subplot(223, projection='3d')
surf3 = ax3.plot_surface(X, Y, np.log(intensity), cmap='viridis', alpha=0.7)
fig.colorbar(surf3, ax=ax3, label='Intensity (log scale)')
ax3.set_title('强度（对数尺度）')
ax3.set_xlabel('x/um')
ax3.set_ylabel('y/um')
ax3.set_zlabel('Intensity (log scale)')
ax3.view_init(elev=30, azim=45)

# 绘制相位图
ax4 = fig.add_subplot(224, projection='3d')
surf4 = ax4.plot_surface(X, Y, phase, cmap='hsv', alpha=0.7)
fig.colorbar(surf4, ax=ax4, label='Phase (radians)')
ax4.set_title('相位')
ax4.set_xlabel('x/um')
ax4.set_ylabel('y/um')
ax4.set_zlabel('Phase (radians)')
ax4.view_init(elev=30, azim=45)

plt.tight_layout()
plt.show()
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 参数设置
wavelength = 0.5e-3       # 波长（单位：毫米）
d = 0.4                   # 两点光源间距（单位：毫米）
L = 1000                  # 观察屏到电源的距离（单位：毫米）1米
H = 12                    # 观察屏的尺寸（单位：毫米）12x12mm
N = 500                   # 采样点数
I1,I2,I0 = 1,1,1

# 创建网格
x = np.linspace(-H/2, H/2, N)
y = np.linspace(-H/2, H/2, N)
X, Y = np.meshgrid(x, y)

# 计算光程差
r1 = np.sqrt((X-d/2)**2+Y**2+L**2)
r2 = np.sqrt((X+d/2)**2+Y**2+L**2)
delta = r2-r1
# 计算相位差
phase_diff = (2 * np.pi / wavelength) * delta

# 计算光强
I = 2*I0*(1+np.cos(phase_diff))

# # 创建一个包含两个子图的窗口
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# # 绘制干涉条纹分布
# im1 = ax1.imshow(I, cmap='gray', extent=[-H/2, H/2, -H/2, H/2], origin='lower')
# fig.colorbar(im1, ax=ax1,orientation='horizontal', label='Intensity')  # 标签
# ax1.set_xlabel('x/mm')
# ax1.set_ylabel('y/mm')
# ax1.set_title('两点光源干涉条纹分布')

# # 截取 y=0 处的光强分布
# y_center = N // 2  # y=0 对应网格的中间行
# intensity_slice = I[y_center, :]
# # 归一化光强
# normalized_intensity = intensity_slice / np.max(intensity_slice)
# # 绘制归一化光强分布曲线
# ax2.plot(x, normalized_intensity)
# ax2.set_xlabel('x/mm')
# ax2.set_ylabel('Normalized Intensity')
# ax2.set_title('y=0 处的光强分布曲线')
# ax2.grid(True)

# plt.tight_layout()
# plt.show()

# 绘制干涉条纹分布
plt.imshow(I, 
           cmap='gray',          # 使用viridis颜色映射
           extent=[-H/2, H/2, -H/2, H/2],
           origin='lower')          # 坐标系原点在左下角
plt.colorbar(label='Intensity')
plt.xlabel('x/mm')
plt.ylabel('y/mm')
plt.title(f'两点光源干涉条纹分布: λ={wavelength*1e6}nm')

plt.tight_layout()
plt.show()
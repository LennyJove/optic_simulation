import numpy as np
# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 参数,单位是米
lmbd = 632.8e-9
K = 2 * np.pi / lmbd
m,n = [16,16]
dx = 1e-4  # 0.1mm
dy = dx
dS = dx * dy
Lx = m * dx / 2
Ly = n * dy / 2
z = 1  # 1米
# 建立网格
x = np.linspace(-Lx, Lx, (m+1))
y = np.linspace(-Ly, Ly, (n+1))
x,y = np.meshgrid(x, y)
# 矩阵到列,列向量
x = x.reshape((m+1)*(n+1), 1)
y = y.reshape((m+1)*(n+1), 1)
#进行拼接
Cd1 = np.hstack((x,y)) # x列，y列
Cd2 = Cd1

## 构建传递函数
h = np.zeros([(m+1)*(n+1),(m+1)*(n+1)],dtype = complex)  # 分配空间
for ii in range(0,(m+1)*(n+1)) :
    for jj in range(0,(m+1)*(n+1)) :
        r = np.sqrt((Cd1[ii,0]-Cd2[jj,0])**2 + (Cd1[ii,1]-Cd2[jj,1])**2 + z**2)
        Cos = z/r
        h[ii,jj] = 1/(1j*lmbd) *np.exp(1j*K*r)/r *Cos *dS
## 计算矩阵的特征值和特征向量
# EqValue 是一个一维数组，包含矩阵 h 的所有特征值。
# Eqvector 是一个二维数组，每一列是一个对应的特征向量。
EqValue,Eqvector = np.linalg.eig(h)  
U1 = Eqvector[: , 0]  # 不同阶数,模式
U1 = U1.reshape((m+1),(n+1))  # 恢复为矩阵

# U1 = np.zeros([(m+1),(n+1)],dtype = complex)
# U1 = U1.reshape((m+1) * (n+1), 1)

plt.pcolormesh(np.abs(U1)**2, cmap ='hot')
plt.title("模式图")
plt.show()

print(1-np.abs(EqValue[0:9]**2))

# print(EqValue[0:3])
# print((U2/U1))
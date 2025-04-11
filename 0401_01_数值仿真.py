import numpy as np
# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 参数-单位是米
lmbd = 632.8e-9
K = 2 * np.pi / lmbd
m,n = [16,16]
dx = 1e-4  # 0.1mm
dy = dx
dS = dx * dy
Lx = m * dx / 2
Ly = n * dy / 2
z = 1  # 传播距离1米

# 建立网格
x = np.linspace(-Lx, Lx, (m+1))
y = np.linspace(-Ly, Ly, (n+1))
x,y  = np.meshgrid(x, y)
# 矩阵转换为列向量，一维数组
x = x.reshape((m+1)*(n+1), 1)
y = y.reshape((m+1)*(n+1), 1)
Cd1 = np.hstack((x,y)) # 将x和y拼接为一个二维数组
Cd2 = Cd1

## 传递函数
h = np.zeros([(m+1)*(n+1),(m+1)*(n+1)],dtype = complex)  # 分配空间，复数类型
for ii in range(0,(m+1)*(n+1)) :
    for jj in range(0,(m+1)*(n+1)) :
        r = np.sqrt((Cd1[ii,0]-Cd2[jj,0])**2 + (Cd1[ii,1]-Cd2[jj,1])**2 + z**2)
        Cos = z/r
        h[ii,jj] = 1/(1j*lmbd) *np.exp(1j*K*r)/r *Cos *dS

## 物平面
U1 = np.zeros([(m+1),(n+1)],dtype = complex) # 给物体，光源，分配空间
# 种子光
U1[8,8] = 1

# U1[0,0] = 1 
# U1[16,16] = -1

# U1[0,0] = 1
# U1[16,0] = -1
# U1[0,16] = -1
# U1[16,16] = 1

U1 = U1.reshape((m+1)*(n+1), 1)  # 将U1转换为一维数组

## 像平面
IterNum = 50  # 传播次数，来回反射
for ii in range(IterNum) :
    U2 = np.dot(h,U1)
    U1 = U2

U2 = np.dot(h,U1)
## 还原为方阵，绘图展示
U2 = U2.reshape((m+1),(n+1))  # 转换为方阵
U1 = U1.reshape((m+1),(n+1))

plt.pcolormesh(np.abs(U2)**2, cmap ='hot')  # 光学系统，看光强，进行取模求平方
plt.title("像面光斑分布")
plt.show()

print((U2/U1))
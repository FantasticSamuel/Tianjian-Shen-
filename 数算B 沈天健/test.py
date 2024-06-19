import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sph_harm, spherical_jn, spherical_yn,lpmv
from mpl_toolkits.mplot3d import Axes3D
from sympy import symbols, diff,cos,lambdify,assoc_legendre
import matplotlib.colors as mcolors

# Constants
n = 1.4500001
l = 10
m = 8
k = 8.86844 -3.05286j
def spherical_h1(l, z):
    return spherical_jn(l, z) + 1j*spherical_yn(l,z)
# Define the spherical harmonics functions
def Ylmtheta(l, m, theta, phi):
    return -1j * m * sph_harm(m, l, phi, theta)/(np.sin(theta)+1e-100)

def Ylmphi(l, m, theta, phi):
    # 定义 theta 为一个符号
    thetaa = symbols('theta')
    # 定义函数
    f = diff(assoc_legendre(l, m, cos(thetaa)),thetaa)
    df_theta_func = lambdify(thetaa, f, "numpy")
    # 计算偏导数
    return df_theta_func(theta) * np.exp(1j*m*phi)

# Vectorize the functions
Ylmphi_vec = np.vectorize(Ylmphi)
Ylmtheta_vec = np.vectorize(Ylmtheta)
N=200
# Define the grid in spherical coordinates
theta, phi = np.linspace(0, np.pi, N), np.linspace(0, 2*np.pi, N)
theta, phi = np.meshgrid(theta, phi)
R = np.linspace(0, 1.2, N)
R = np.meshgrid(R, R)[0]

# Transform spherical to Cartesian coordinates
x = R * np.sin(theta) * np.cos(phi)
y = R * np.sin(theta) * np.sin(phi)
z = R * np.cos(theta)
print('coordinates done')
# Calculate the fields
E1 = spherical_jn(l, n*k*R) / spherical_jn(l, n*k) * ((Ylmphi_vec(l, m, theta, phi)+Ylmphi_vec(l, -m, theta, phi))**2 + (Ylmtheta_vec(l, m, theta, phi)+Ylmtheta_vec(l, -m, theta, phi))**2)**0.5
print('E1 done')
E2 = spherical_h1(l, k*R) / spherical_h1(l, k) * ((Ylmphi_vec(l, m, theta, phi)+Ylmphi_vec(l, -m, theta, phi))**2 + (Ylmtheta_vec(l, m, theta, phi)+Ylmtheta_vec(l, -m, theta, phi))**2)**0.5
print('E2 done')
# Calculate the intensity
intensity = np.where(R < 1, abs(E1)**2, abs(E2)**2)
print('intensity done')
# 计算透明度值
alpha = np.power(intensity / np.max(intensity),1)

intensity_normalized=intensity / np.max(intensity)

# 获取 'viridis' 颜色映射
cmap = plt.get_cmap('viridis')

# 创建一个新的 RGBA 颜色数组
colors = cmap(intensity_normalized.flatten())

# 设置透明度
colors[..., -1] = alpha.flatten()
print('colors done')
# 创建一个 3D 图
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制散点图
sc = ax.scatter(x.flatten(), y.flatten(), z.flatten(), c=colors)
cbar = plt.colorbar(sc)
cbar.set_label('Field Strength')
# 显示图像
plt.show()
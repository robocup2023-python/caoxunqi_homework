import cv2
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

kernel_s=11
sigma=5.0

center=kernel_s//2

kernel =np.zeros((kernel_s,kernel_s))

for i in range(kernel_s):
    for j in range(kernel_s):
        x=i-center
        y=j-center
        kernel[i, j] = (1 / (2 * np.pi * sigma ** 2)) * np.exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2))

kernel=kernel/kernel.sum()

print(kernel)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为SimHei
plt.rcParams['axes.unicode_minus'] = False  # 解决坐标轴负号显示问题

plt.imshow(kernel, cmap='viridis')
plt.colorbar()
plt.title('矩阵可视化')
plt.show()
plt.savefig('kernel3.jpg')
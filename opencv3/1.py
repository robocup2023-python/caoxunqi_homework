import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

# 读取图像并转换为灰度
image = cv2.imread('origin.png', cv2.IMREAD_GRAYSCALE)

# 进行二维傅里叶变换
f_transform = np.fft.fft2(image)
f_transform_shifted = np.fft.fftshift(f_transform)

# 计算振幅谱和相位谱
magnitude_spectrum = np.log(np.abs(f_transform_shifted) + 1)
phase_spectrum = np.angle(f_transform_shifted)

# 显示原始图像和频域谱
plt.figure(figsize=(12, 6))

plt.subplot(231), plt.imshow(image, cmap='gray')
plt.title('Original Image'), plt.axis('off')


plt.subplot(232), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.axis('off')

plt.subplot(233), plt.imshow(phase_spectrum, cmap='gray')
plt.title('Phase Spectrum'), plt.axis('off')

plt.show()


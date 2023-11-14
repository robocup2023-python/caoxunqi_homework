import matplotlib
matplotlib.use('TkAgg')
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像并转换为灰度
image = cv2.imread('origin.png', cv2.IMREAD_GRAYSCALE)

# 进行二维傅里叶变换
f_transform = np.fft.fft2(image)
f_transform_shifted = np.fft.fftshift(f_transform)

# 计算振幅谱和相位谱
magnitude_spectrum = np.abs(f_transform_shifted)

rows, cols = image.shape
center_row, center_col = rows // 2, cols // 2
mask_radius = 500
mask = np.ones((rows, cols), np.uint8)
cv2.circle(mask, (center_col, center_row), mask_radius,(0,0,0), -1)

f_transform_shifted_masked = f_transform_shifted * mask

# 进行反变换
f_inverse_shifted = np.fft.ifftshift(f_transform_shifted_masked)
image_restored = np.fft.ifft2(f_inverse_shifted).real

plt.figure()
plt.subplot(1,3,1)
plt.imshow(image, cmap='gray')
plt.title('Original')
plt.xticks([]), plt.yticks([])

(plt.subplot(1,3,2),
plt.imshow(np.log(1 + magnitude_spectrum), cmap='gray'))
plt.title('Masked')
plt.xticks([]), plt.yticks([])

plt.subplot(133)
plt.imshow(image_restored, cmap='gray')
plt.title('Restored')
plt.xticks([]), plt.yticks([])

plt.show()




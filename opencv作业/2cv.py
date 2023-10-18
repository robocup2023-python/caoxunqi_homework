import cv2
import numpy as np
ksize = (5, 5)
sigma = 1.0
gaussian_kernel = cv2.getGaussianKernel(ksize[0], sigma) @ cv2.getGaussianKernel(ksize[1], sigma).T
print(gaussian_kernel)






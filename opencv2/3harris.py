import cv2
import numpy as np
import math

image=cv2.imread('grayorigin.jpg')
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

image=cv2.GaussianBlur(image,(7,7),1)

sobelx=cv2.Sobel(image,-1,1,0,ksize=3)
sobely=cv2.Sobel(image,-1,1,0,ksize=3)

imageix2=(sobelx*sobelx)
cv2.imwrite('3imageix2.jpg',imageix2)
imageix2=cv2.GaussianBlur(imageix2,(7,7),3)

imageiy2=sobely**2
cv2.imwrite('3imageiy2.jpg',imageiy2)
imageiy2=cv2.GaussianBlur(imageiy2,(7,7),3)

imageixiy=sobelx*sobely
cv2.imwrite('3imageixiy.jpg',imageixiy)
imageixiy=cv2.GaussianBlur(imageixiy,(7,7),3)

k = 0.04  # Harris角点检测参数

Ix = cv2.Sobel(image, -1, 1, 0, ksize=3)
Iy = cv2.Sobel(image, -1, 0, 1, ksize=3)
IxIx = Ix * Ix
IxIy = Ix * Iy
IyIy = Iy * Iy
detM = IxIx * IyIy - IxIy**2
traceM = IxIx + IyIy

R = detM - k * (traceM**2)

block_size = 11
ksize = 3
k = 0.06
harris_corners = cv2.cornerHarris(image, blockSize=block_size, ksize=ksize, k=k)

threshold = 0.01 * harris_corners.max()

for i in range(harris_corners.shape[0]):
    for j in range(harris_corners.shape[1]):
        if harris_corners[i, j] > threshold:
            cv2.circle(image, (j, i), 5, (0, 0, 255), -1)

cv2.imwrite('3HarrisCorners11006.jpg', image)
cv2.waitKey(0)

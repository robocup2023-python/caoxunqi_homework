import cv2
import numpy as np

img =cv2.imread('1.png')
dimensions =img.shape
print(dimensions)
cv2.imshow('',img)
(b,g,r)=img[6,40]
gray_img=cv2.imread('1.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('',gray_img)
cv2.imwrite('1gray.jpg',gray_img)
cv2.waitKey(0)
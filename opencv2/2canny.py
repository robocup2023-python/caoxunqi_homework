import cv2
import numpy as np
import math

image=cv2.imread('grayorigin.jpg')
print(image.shape)
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

image=cv2.GaussianBlur(image,(5,5),3)

sobelx=cv2.Sobel(image,-1,1,0,ksize=3)
sobely=cv2.Sobel(image,-1,1,0,ksize=3)

imagesobel=(sobelx+sobely).astype(np.uint8)

cv2.waitKey(0)
cv2.imwrite('2sobel.jpg',imagesobel)

gradient_magnitude = imagesobel
gradient_direction = np.arctan2(sobely, sobelx)

nms_radius = 3

for i in range(nms_radius, image.shape[0] - nms_radius):
    for j in range(nms_radius, image.shape[1] - nms_radius):
        current_gradient_magnitude = gradient_magnitude[i, j]
        current_direction = gradient_direction[i, j]

        i1, j1 = i + nms_radius, j + nms_radius
        i2, j2 = i - nms_radius, j - nms_radius

        is_maximum = True
        for x in range(i2, i1 + 1):
            for y in range(j2, j1 + 1):
                if gradient_magnitude[x, y] > current_gradient_magnitude:
                    is_maximum = False
                    break
            if not is_maximum:
                break

cv2.imwrite('2NMScanny.jpg', gradient_magnitude.astype(np.uint8))
cv2.waitKey(0)

edges=cv2.Canny(image,threshold1=30,threshold2=70)

cv2.imshow('Original Image', image)
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('1canny.jpg',edges)
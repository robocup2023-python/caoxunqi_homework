import cv2
import numpy as np

image0 = cv2.imread('origin.png')
image = cv2.cvtColor(image0, cv2.COLOR_BGR2GRAY)

cv2.imwrite('grayorigin.jpg',image)

print(image.shape)
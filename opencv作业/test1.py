import cv2
import numpy as np

img1=cv2.imread('2.jpg')
b,g,r =cv2.split(img1)
img_matplotlib=cv2.merge([r,g,b])

from matplotlib import pyplot as plt


img_con=np.concatenate((img1,img_matplotlib),axis=1)
cv2.imshow('',img_con)
cv2.waitKey(0)
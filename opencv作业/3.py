import cv2
import numpy as np

image0 = cv2.imread('1gray.jpg')
image = cv2.cvtColor(image0, cv2.COLOR_BGR2GRAY)

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

def filter(kernel,kernel_s,image,i,j):
    half=kernel_s//2
    sum=0
    for hang in range(kernel_s):
        for lie in range(kernel_s):
            sum=sum+kernel[hang][lie]*image[i-half+hang][j-half+lie]
    return sum

print(image.shape)
hang,lie = image.shape

new_hang=hang-kernel_s+1
new_lie=lie-kernel_s+1
new_image= np.zeros((new_hang,new_lie))
for i in range(new_hang):
    for j in range(new_lie):
        new_image[i][j]=filter(kernel,kernel_s,image,i+center,j+center)
print(new_image)
cv2.imwrite('2gray.jpg',new_image)

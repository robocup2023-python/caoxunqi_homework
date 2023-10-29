import cv2
import numpy as np

image0=cv2.imread('grayorigin.jpg')
image=cv2.cvtColor(image0,cv2.COLOR_BGR2GRAY)

print(image.shape)
height,width=(image.shape)

kernel_s=3
center=kernel_s//2
sobelx=np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
sobely=np.array([[1,2,1],[0,0,0],[-1,-2,-1]])

def filterx(kernel_s,image,i,j):
    kernel=sobelx
    half=kernel_s//2
    sum=0
    for hang in range(kernel_s):
        for lie in range(kernel_s):
            sum=sum+kernel[hang][lie]*image[i-half+hang][j-half+lie]
    return sum

def filtery(kernel_s,image,i,j):
    kernel=sobely
    half=kernel_s//2
    sum=0
    for hang in range(kernel_s):
        for lie in range(kernel_s):
            sum=sum+kernel[hang][lie]*image[i-half+hang][j-half+lie]
    return sum

#可以用于替换image=cv2.filter2D(image,sobelx)

print(image.shape)
hang,lie = image.shape

new_hang=hang-kernel_s+1
new_lie=lie-kernel_s+1
new_image= np.zeros((new_hang,new_lie))
for i in range(new_hang):
    for j in range(new_lie):
        new_image[i][j]=filterx(kernel_s,image,i+center,j+center)
print(new_image)
cv2.imwrite('soblex.jpg',new_image)

for i in range(new_hang):
    for j in range(new_lie):
        new_image[i][j]=filtery(kernel_s,image,i+center,j+center)
print(new_image)
cv2.imwrite('sobley.jpg',new_image)


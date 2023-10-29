import cv2

image = cv2.imread('grayorigin.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.equalizeHist(image)

cv2.imwrite('4equal.jpg', image)

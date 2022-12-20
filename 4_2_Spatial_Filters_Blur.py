import cv2
import numpy as np

image1 = cv2.imread('D:\DHARUN\STUDY\SEM 5\Digital Image Processing\Project\Image1.jpg')
img=cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
kernel = np.identity(5)
conv = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)
blur = cv2.GaussianBlur(img, (11, 11), 0)
bilateral_filter = cv2.bilateralFilter(src=img, d=9, sigmaColor=75, sigmaSpace=75)
median = cv2.medianBlur(src=img, ksize=3)
kernel2 = np.array([[-1, -1, -1],
                    [-1, 8, -1],
                    [-1, -1, -1]])
  
# Applying the filter2D() function
img = cv2.filter2D(src=image1, ddepth=-1, kernel=kernel2)
  
cv2.imshow('conv_ones',conv)
cv2.imshow('MedianBlur',median)
cv2.imshow('GaussianBlur',blur)
cv2.imshow('BilateralBlur',bilateral_filter)
cv2.imshow('Edge detection', img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

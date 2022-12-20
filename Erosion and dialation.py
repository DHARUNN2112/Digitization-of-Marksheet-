import cv2
import numpy as np

image1 = cv2.imread('D:\DHARUN\STUDY\SEM 5\Digital Image Processing\Project\Image1.jpg')
 
img=cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
ath1 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,3)
img_erosion = cv2.erode(ath1, (1,1), iterations=1)
noise = cv2.fastNlMeansDenoising(img_erosion, None, 20, 7, 21) 
img_dilation = cv2.dilate(img_erosion,(1,1), iterations=1)
kernel = np.ones((5, 5), np.uint8)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('adaptive threshing ', ath1)
cv2.imshow('Erosion', img_erosion)
cv2.imshow('dilation',img_dilation)
cv2.imshow('De noise',noise)
cv2.imshow('Morphological',gradient)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

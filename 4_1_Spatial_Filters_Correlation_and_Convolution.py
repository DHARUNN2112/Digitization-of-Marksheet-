import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy import ndimage

image = cv2.imread("D:\DHARUN\STUDY\SEM 5\Digital Image Processing\Project\Image1.jpg")
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
kernel = np.array([[1,1,1],[1,1,0],[1,0,0]])
k=np.rot90(kernel, 2)
CORR = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)
CONV = ndimage.convolve(img, kernel, mode='constant', cval=1.0)

cv2.imshow('Original', img)
cv2.imshow('Convolution', CONV)
cv2.imshow('Correlation', CORR)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

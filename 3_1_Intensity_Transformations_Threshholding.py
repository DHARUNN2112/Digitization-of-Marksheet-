import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image = cv2.imread("D:\DHARUN\STUDY\SEM 5\Digital Image Processing\Project\Image1.jpg")


img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
print(img)           
ret, TH1= cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)
ret, TH2= cv2.threshold(img, 75, 255, cv2.THRESH_BINARY)
ret, TH3= cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
ret, TH4= cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
ret, TH5= cv2.threshold(img, 150, 200, cv2.THRESH_BINARY)
ath1 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow('Binary threshing : 0', TH1)
cv2.imshow('Binary threshing : 75', TH2)
cv2.imshow('Binary threshing : 150', TH3)
cv2.imshow('Binary threshing : 200', TH4)
cv2.imshow('Binary threshing : 150 - 200 ', TH5)
cv2.imshow('adaptive threshing ', ath1)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
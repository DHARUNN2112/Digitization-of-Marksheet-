import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image = cv2.imread("D:\DHARUN\STUDY\SEM 5\Digital Image Processing\Project\Image1.jpg")


img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
print(img)
new_height=2*len(img)
new_width=2*len(img[0])



NN = cv2.resize(image, dsize=(new_height, new_width), 
      interpolation=cv2.INTER_NEAREST)
BL = cv2.resize(image, dsize=(new_height, new_width), 
      interpolation=cv2.INTER_LINEAR)
BC = cv2.resize(image, dsize=(new_height, new_width), 
      interpolation=cv2.INTER_CUBIC)
BLE = cv2.resize(image, dsize=(new_height, new_width), 
      interpolation=cv2.INTER_LINEAR_EXACT)
NNE = cv2.resize(image, dsize=(new_height, new_width), 
      interpolation=cv2.INTER_NEAREST_EXACT)
A = cv2.resize(image, dsize=(new_height, new_width), 
      interpolation=cv2.INTER_AREA)
L = cv2.resize(image, dsize=(new_height, new_width), 
      interpolation=cv2.INTER_LANCZOS4)

cv2.imshow('Nearrest Neighbor ', NN)
cv2.imshow('Bilinear ', BL)
cv2.imshow('Bicubic', BC)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
cv2.imshow('Nearrest Neighbor Exact ', NNE)
cv2.imshow('Bilinear Exact', BLE)
cv2.imshow('Inter Area ', A)
cv2.imshow('Lanczos  ', L)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

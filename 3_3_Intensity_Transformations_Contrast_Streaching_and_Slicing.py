import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image = cv2.imread("D:\DHARUN\STUDY\SEM 5\Digital Image Processing\Project\Image1.jpg")
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
def contrastStreaching(pix, r1, s1, r2, s2):
    if (0 <= pix and pix <= r1):
        return (s1 / r1)*pix
    elif (r1 < pix and pix <= r2):
        return ((s2 - s1)/(r2 - r1)) * (pix - r1) + s1
    else:
        return ((255 - s2)/(255 - r2)) * (pix - r2) + s2
def slice1(img,a,b,c):
    r,c=img.shape
    timg=img.copy()
    for i in range(r):
        for j in range(c):
            if timg[i][j]>=a and timg[i][j]<=b:
                timg[i][j]=c
    return timg

def slice2(img,a,b,c):
    r,c=img.shape
    timg=img.copy()
    for i in range(r):
        for j in range(c):
            if timg[i][j]<=a or timg[i][j]>=b:
                timg[i][j]=c
    return timg

pixelVal_vec = np.vectorize(contrastStreaching)
CS= pixelVal_vec(img, 70, 0, 140, 255)

IS1 = slice1(img,50,100,200)
IS2 = slice2(img,50,100,200)
cv2.imshow('Contrast Streching', CS)
cv2.imshow('Intensity Slicing 1', IS1)
cv2.imshow('Intensity Slicing 2', IS2)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
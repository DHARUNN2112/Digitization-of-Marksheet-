import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image = cv2.imread("D:\DHARUN\STUDY\SEM 5\Digital Image Processing\Project\Image1.jpg")
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
def imgneg(img):
    r,c=img.shape
    nimg=img.copy()
    for i in range(r):
        for j in range(c):
            nimg[i][j]=255-img[i][j]
    return nimg
def logtran(img):
    c = 255/(np.log(1 + np.max(img)))
    log_transformed = c * np.log(1 + img)
    log_image = np.array(log_transformed, dtype = np.uint8)
    return log_image
    
def gammaCorrection(src, gamma):
    invGamma = 1 / gamma
    table = [((i / 255) ** invGamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)
    return cv2.LUT(src, table)

def cstreaching(image):
    rmax = image.max()
    rmin = image.min()
    max_intensity_level = 255
    r_diff = rmax - rmin
    lut = [ (i - rmin) / r_diff * max_intensity_level for i in range(0, 256)]
    lut = np.array(lut, dtype='uint8')
    result = cv2.LUT(image, lut)
    return result

NEG = imgneg(img)
LOG = logtran(img)
GAM1 = gammaCorrection(img, 2)
GAM2 = gammaCorrection(img, 0.5)
CS = cstreaching(img)
cv2.imshow('Inverse ', NEG)
cv2.imshow('Logerithmic ', LOG)
cv2.imshow('GAMMA : 2 ', GAM1)
cv2.imshow('GAMMA : 0.5 ', GAM2)
cv2.imshow('Contrast Streching', CS)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()


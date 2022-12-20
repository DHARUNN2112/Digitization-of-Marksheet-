import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image = cv2.imread("D:\DHARUN\STUDY\SEM 5\Digital Image Processing\Project\Image1.jpg")


img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
rows,cols = img.shape
MI = np.float32([[1,0,0],
                [0,1,0]])
IDN = cv2.warpAffine(img,MI,(cols,rows))
MT = np.float32([[1,0,100],
                [0,1,50]])
TR = cv2.warpAffine(img,MT,(cols,rows))

SL = cv2.resize(img,dsize=(2*cols,2*rows), interpolation = cv2.INTER_CUBIC)

MR = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
ROT = cv2.warpAffine(img,MR,(cols,rows))


src_points = np.float32([[0,0], [cols-1,0], [0,rows-1]])
dst_points = np.float32([[0,0], [int(0.6*(cols-1)),0], [int(0.4*(cols-1)),rows-1]])
matrix = cv2.getAffineTransform(src_points, dst_points)
AT1 = cv2.warpAffine(image, matrix, (len(img[0]),len(img)))

src_points = np.float32([[0,0], [cols-1,0], [0,rows-1]])
dst_points = np.float32([[cols-1,0], [0,0], [cols-1,rows-1]])
matrix = cv2.getAffineTransform(src_points, dst_points)
MIR = cv2.warpAffine(image, matrix, (cols,rows))

src_points = np.float32([[0,0], [cols-1,0], [0,rows-1], [cols-1,rows-1]])
dst_points = np.float32([[0,0], [cols-1,0], [int(0.33*cols),rows-1], [int(0.66*cols),rows-1]])
projective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
perspective = cv2.warpPerspective(image, projective_matrix, (cols,rows))

cv2.imshow('IDENTITY ', IDN)
cv2.imshow('Scaling ', TR)
cv2.imshow('Transulation ', TR)
cv2.imshow('Rotation', ROT)
cv2.imshow('Affine Transformation ', AT1)
cv2.imshow('Mirror ', MIR)
cv2.imshow('Perspective', perspective)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
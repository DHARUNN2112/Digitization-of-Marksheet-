import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image = cv2.imread("D:\DHARUN\STUDY\SEM 5\Digital Image Processing\Project\Image1.jpg")
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

imgs = [255 * ((img& (1<<i)) >>i) for i in range(8)]
for i in range(8):
    string="Bit Plane"+str(i+1)
    plt.imshow(imgs[i],cmap='gray')
    plt.show()
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
print(img[7].shape)
'''
comb=np.array(img[7])*128+np.array(img[6])*64+np.array(img[5])*32+np.array(img[4])*16
plt.imshow(comb,cmap='gray')
plt.show()
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt
 

image = cv2.imread('D:\DHARUN\STUDY\SEM 5\Digital Image Processing\Project\Image1.jpg')


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ath1 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,14)

image = cv2.dilate(ath1, (1,1), iterations=0)

blur = cv2.GaussianBlur(gray, (11, 11), 0)
canny = cv2.Canny(blur, 30, 150, 3)
dilated = cv2.dilate(canny, (5, 5), iterations=0)

 
(cnt, hierarchy) = cv2.findContours(
    dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)
plt.imshow(rgb)
cv2.imshow('img', rgb)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
    
rgb.save('D:\plot1.jpg')
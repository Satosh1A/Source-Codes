import numpy as np
import cv2

img = np.zeros((400,400,3),np.uint8)
cv2.circle(img,(200,200),50,(255,0,0),1)
cv2.imwrite("c:/Source Codes/OpenCV3_beginner/images/circle1.jpg",img)
cv2.imshow('img1',img)

img = np.zeros((400,400,3),np.uint8)
cv2.circle(img,(200,200),100,(0,255,0),3)
cv2.imwrite("c:/Source Codes/OpenCV3_beginner/images/circle2.jpg",img)
cv2.imshow('img2',img)

img = np.zeros((400,400,3),np.uint8)
cv2.circle(img,(200,200),150,(0,0,255),-1)
cv2.imwrite("c:/Source Codes/OpenCV3_beginner/images/circle3.jpg",img)
cv2.imshow('img3',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
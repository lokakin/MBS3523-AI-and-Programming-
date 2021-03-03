

import cv2
print(cv2.__version__)
import numpy as np

img = cv2.imread('Resources/lkk.png')

img = cv2.resize(img, (int(img.shape[1]/1.5),int(img.shape[0]/1.5)))

imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

roi = img[120:260, 120:260].copy()
roiGray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
roiGray = cv2.cvtColor(roiGray,cv2.COLOR_GRAY2BGR)
img[120:260, 120:260] = roiGray

cv2.imshow('Lena',img)
cv2.imshow('Gray Image', imgGray)
cv2.imshow('ROI Image', roi)
cv2.imshow('Gray ROI', roiGray)

cv2.waitKey(0)

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('idn1.png',0)

ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

cv.imshow("THRESH_BINARY",thresh1)
cv.imshow("THRESH_BINARY_INV",thresh2)
cv.imshow("THRESH_TRUNC",thresh3)
cv.imshow("THRESH_TOZERO",thresh4)
cv.imshow("THRESH_TOZERO_INV",thresh5)
cv.waitKey(0)
cv.destroyAllWindows()

# cv2.imshow('BINARY',)
# titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

# for i in range(6):
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])

# plt.show()
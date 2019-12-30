import cv2
import numpy

while True :
    img = cv2.imread('idn1.png')

    width = 480
    height = 540
    dim = (width, height)
    res = cv2.resize(img,dim, interpolation = cv2.INTER_CUBIC)
    #res = cv2.resize(img,None,fx=0.4, fy=0.4, interpolation = cv2.INTER_CUBIC)

    cv2.imshow('frame',res)

    k = cv2.waitKey(0) & 0xFF

    if k == 27:
        print("hello")

cv2.destroyAllWindows()
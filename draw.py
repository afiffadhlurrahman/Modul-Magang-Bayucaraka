import cv2
import numpy as np

img = cv2.imread('idn1.png')

world  = 'world'
fontFace = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
fontScale = 2

cv2.rectangle(img, (25,50),(150,200),(0,255,0), 4)
cv2.circle(img, (250,60), 50, (155,100,0), 5)

cv2.putText(img, "hello " + world,(10,50), fontFace, fontScale,(0,0,255), 3) 

cv2.imshow('image',img)
cv2.waitKey(0)
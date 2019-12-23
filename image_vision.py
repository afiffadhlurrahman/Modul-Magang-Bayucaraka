import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("Trackbars")
cv2.createTrackbar("L-H", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L-S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L-V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U-H", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U-S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U-V", "Trackbars", 255, 255, nothing)


#hsv = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY)

while True:
    img = cv2.imread('lena.png')
    hsv = cv2.cvtColor( img, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("L-H", "Trackbars")
    l_s = cv2.getTrackbarPos("L-S", "Trackbars")
    l_v = cv2.getTrackbarPos("L-V", "Trackbars")
    u_h = cv2.getTrackbarPos("U-H", "Trackbars")
    u_s = cv2.getTrackbarPos("U-S", "Trackbars")
    u_v = cv2.getTrackbarPos("U-V", "Trackbars")

    low_red = np.array([l_h, l_s, l_v])
    high_red = np.array([u_h, u_s, u_v])
    
    mask = cv2.inRange(hsv, low_red, high_red)
    res = cv2.bitwise_and(img,img, mask= mask)

    _,contours, hierarcy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    for cnt in contours:    
        cv2.drawContours(res, [cnt], 0, (0,0,0), 5)
        
        x,y,w,h = cv2.boundingRect(cnt)
        ret,thresh1 = cv2.threshold(res,127,255,cv2.THRESH_BINARY_INV)
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)

    cv2.imshow('image',img)
    # cv2.imshow('res',res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()

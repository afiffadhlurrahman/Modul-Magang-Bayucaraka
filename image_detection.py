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

font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    img = cv2.imread('idn1.png')
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
    grey = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey,(5,5),0)
    ret,thresh1 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    _,contours, hierarcy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    jumlah = int (0)
    for cnt in contours:    
        cv2.drawContours(img, [cnt], 0, (0,0,0), 5)
        
        x,y,w,h = cv2.boundingRect(cnt)

    cv2.imshow('image',img)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()

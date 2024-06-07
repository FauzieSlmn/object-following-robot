import time
import cv2 as cv2
import matplotlib.pyplot as plt
from collections import deque
import numpy as np


cap = cv2.VideoCapture(0)
cv2.namedWindow('Image',2)
cv2.resizeWindow("Image", 550,550)
prevcircle = None
dist = lambda x1,y1,x2,y2:(x1-x2)**2*(y1-y2)**2

def callback(x):
    pass
R_L = 42
R_H = 88
G_L = 62
G_H = 255
B_L = 45
B_H = 150 
'''
cv2.createTrackbar('Red Low', 'Image', 0, 255, callback)
cv2.createTrackbar('Red High', 'Image', 255, 255, callback)

cv2.createTrackbar('Green Low', 'Image', 0, 255, callback)
cv2.createTrackbar('Green High', 'Image', 255, 255, callback)

cv2.createTrackbar('Blue Low', 'Image', 0, 255, callback)
cv2.createTrackbar('Blue High', 'Image', 255, 255, callback)
'''
while(1):
    stream = cv2.waitKey(1)
    ret, frame = cap.read()
    HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv_low = np.array([R_L, G_L, B_L], np.uint8)
    hsv_high = np.array([R_H, G_H, B_H], np.uint8)

    mask = cv2.inRange(HSV, hsv_low, hsv_high)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    
    #######################################   Circle    ###################################################
    circle = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1.2, 50, 
                                param1=1, param2=30, minRadius=5,maxRadius=4000)
    if circle is not None:
        circle = np.uint16(np.around(circle))
        chosen = None
        for i in circle[0, :]:
            center = (i[0], i[1])
            print("Tengah", center)
            if chosen is None: chosen = i
            if prevcircle is not None:
                if dist(chosen[0], chosen[1], prevcircle[0], prevcircle[1]) <= dist(i[0],i[1],prevcircle[0], prevcircle[1]):
                     chosen= i
        cv2.circle(frame, (chosen[0], chosen[1]), 1, (0,100,100),3)
        cv2.circle(frame, (chosen[0], chosen[1]), chosen[2], (255,0,255),3)
        prevcircle = chosen

    cv2.imshow("Detections",frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Res', res)
    '''
    R_L = cv2.getTrackbarPos('Red Low', 'Image')
    R_H = cv2.getTrackbarPos('Red High', 'Image')

    G_L = cv2.getTrackbarPos('Green Low', 'Image')
    G_H = cv2.getTrackbarPos('Green High', 'Image')

    B_L = cv2.getTrackbarPos('Blue Low', 'Image')
    B_H = cv2.getTrackbarPos('Blue High', 'Image')
    '''
    if stream & 0XFF == ord('q'):  #Letter 'q' is the escape key
        print("Video Berakhir")
        break                      #get out of loop
cap.release()
cv2.destroyAllWindows()

import time
import cv2 as cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse
from collections import deque
from imutils.video import VideoStream
from PIL import Image
import numpy as np
import imutils


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

def putText(frame,word,x,y,b,g,r,height,widht):
    textLine1 = '%s'%(word)
    cv2.putText(frame,textLine1,(int(x),int(y)),
            cv2.FONT_HERSHEY_SIMPLEX,height,(b,g,r),widht)
    return None
cv2.createTrackbar('Red Low', 'Image', 0, 255, callback)
cv2.createTrackbar('Red High', 'Image', 255, 255, callback)

cv2.createTrackbar('Green Low', 'Image', 0, 255, callback)
cv2.createTrackbar('Green High', 'Image', 255, 255, callback)

cv2.createTrackbar('Blue Low', 'Image', 0, 255, callback)
cv2.createTrackbar('Blue High', 'Image', 255, 255, callback)

while(1):
    stream = cv2.waitKey(1)
    ret, frame = cap.read()
    #frame = cv2.resize(frame, (0,0), fx=1, fy=1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray,(17,17),0)
    HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #cv2.imshow('Frame 3', HSV)
    hsv_low = np.array([R_L, G_L, B_L], np.uint8)
    hsv_high = np.array([R_H, G_H, B_H], np.uint8)

    mask = cv2.inRange(HSV, hsv_low, hsv_high)
    #print(mask)
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

    #cv2.imshow("circle", frame)

    cv2.line(img=frame, pt1=(0, 300), pt2=(4000, 300), color=(0, 255, 0), thickness=2, lineType=8, shift=1)
    cv2.line(img=frame, pt1=(0, 600), pt2=(4000, 600), color=(0, 255, 0), thickness=2, lineType=8, shift=1)
    cv2.line(img=frame, pt1=(400, 0), pt2=(400, 4500), color=(0, 255, 0), thickness=2, lineType=8, shift=1)
    cv2.line(img=frame, pt1=(850, 0), pt2=(850, 4500), color=(0, 255, 0), thickness=2, lineType=8, shift=1)

    #print('Point', center)
    putText(frame,'KEL.4',1,30,0,255,0,1,3)  
      
    #cv2.imshow("Blurred image", blurred)
    #cv2.imshow('Frame 2',gray)
    #cv2.imshow('Frame 1',frame)
    cv2.imshow("Detections",frame)
    cv2.imshow('Mask', mask)
    #cv2.imshow('Res', res)
    #print(frame)
    
    R_L = cv2.getTrackbarPos('Red Low', 'Image')
    R_H = cv2.getTrackbarPos('Red High', 'Image')

    G_L = cv2.getTrackbarPos('Green Low', 'Image')
    G_H = cv2.getTrackbarPos('Green High', 'Image')

    B_L = cv2.getTrackbarPos('Blue Low', 'Image')
    B_H = cv2.getTrackbarPos('Blue High', 'Image')
   
    if stream & 0XFF == ord('q'):  #Letter 'q' is the escape key
        print("Video Berakhir")
        break                      #get out of loop
cap.release()
cv2.destroyAllWindows()

import time
import cv2 as cv2
import matplotlib.pyplot as plt
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

def putText(frame,word,x,y,b,g,r,height,widht):
    textLine1 = '%s'%(word)
    cv2.putText(frame,textLine1,(int(x),int(y)),
            cv2.FONT_HERSHEY_SIMPLEX,height,(b,g,r),widht)
while(1):
    stream = cv2.waitKey(1)
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray,(17,17),0)
    HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    cv2.line(img=frame, pt1=(0, 300), pt2=(4000, 300), color=(0, 255, 0), thickness=2, lineType=8, shift=1)
    cv2.line(img=frame, pt1=(0, 600), pt2=(4000, 600), color=(0, 255, 0), thickness=2, lineType=8, shift=1)
    cv2.line(img=frame, pt1=(400, 0), pt2=(400, 4500), color=(0, 255, 0), thickness=2, lineType=8, shift=1)
    cv2.line(img=frame, pt1=(850, 0), pt2=(850, 4500), color=(0, 255, 0), thickness=2, lineType=8, shift=1)
    putText(frame,'Halloooo',1,30,0,255,0,1,3)  
      
    #cv2.imshow("Blurred image", blurred)
    #cv2.imshow('Frame 2',gray)
    #cv2.imshow('Frame 1',frame)
    cv2.imshow("Detections",frame)
   
    if stream & 0XFF == ord('q'):  #Letter 'q' is the escape key
        print("Video Berakhir")
        break                      #get out of loop
cap.release()
cv2.destroyAllWindows()

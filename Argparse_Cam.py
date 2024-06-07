from collections import deque
import serial
import numpy as np
import argparse
import imutils
import cv2
import string
import os
import math
import datetime
from imutils.video import WebcamVideoStream

#arduino = serial.Serial('/dev/ttyACM0',115200)

################################################################################
##Camera Parameter 
im_widht=600
im_height=450
center_im=im_widht/2,im_height/2
camera = cv2.VideoCapture(0)

#Nilainya sama dengan HSV
Hmin = 42
Hmax = 88
Smin = 62
Smax = 255
Vmin = 45
Vmax = 150

while (1):
  
        stream = cv2.waitKey(1)
        (grabbed,frame) = camera.read()
        frame = imutils.resize(frame, width=im_widht)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        Lower_val = np.array([Hmin,Smin,Vmin])
        Upper_val = np.array([Hmax,Smax,Vmax])
        mask = cv2.inRange(hsv, Lower_val, Upper_val)
        contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None
        cnts= cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None
        try :
                if len(contours) > 0:
                    cntr = max(contours, key=cv2.contourArea)
                    ((x, y), radius) = cv2.minEnclosingCircle(cntr)
                    hull = cv2.convexHull(cntr)
                    M = cv2.moments(cntr)
                    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                    cv2.drawContours(frame, [hull], 0, (0,255,255) ,2)
                    mask = np.zeros(frame.shape[:2], np.uint8)
                    cv2.drawContours(frame, [hull], 0, (0,255,255) ,2)
                    cv2.rectangle(frame, (int(x) - 3, int(y) - 3), (int(x) + 3, int(y) + 3), (0, 0, 255), -1)
                else:
                        pass
        except :
                pass
        cv2.line(img=frame, pt1=(0, 300), pt2=(4000, 300), color=(0, 255, 0), thickness=2, lineType=8, shift=1)
        cv2.line(img=frame, pt1=(0, 600), pt2=(4000, 600), color=(0, 255, 0), thickness=2, lineType=8, shift=1)
        cv2.line(img=frame, pt1=(400, 0), pt2=(400, 4500), color=(0, 255, 0), thickness=2, lineType=8, shift=1)
        cv2.line(img=frame, pt1=(850, 0), pt2=(850, 4500), color=(0, 255, 0), thickness=2, lineType=8, shift=1)
        img = imutils.resize(frame, width=800)
        cv2.imshow('image',img)
        
        arduino = serial.Serial('/dev/ttyACM0',115200)
        arduino.write(center)
        print(SendtoArduino)
        time.sleep(0.054)
        
        print("Tengah", center)
        if stream & 0XFF == ord('q'):  #Letter 'q' is the escape key
                print("Video Berakhir")
                break 
camera.release()
cv2.destroyAllWindows()
print("SElesai")

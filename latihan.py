import cv2 as cv2
import numpy as np

cam = cv2.VideoCapture(0)

def putText(frame,word,x,y,b,g,r,height,widht):
    textLine1 = '%s'%(word)
    cv2.putText(frame,textLine1,(int(x),int(y)),
            cv2.FONT_HERSHEY_SIMPLEX,height,(b,g,r),widht)
R_L = 42
R_H = 88
G_L = 62
G_H = 255
B_L = 45
B_H = 150     
while(1):
    stream = cv2.waitKey(1)
    hai,frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray,(17,17),0)
    HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv_low = np.array([R_L, G_L, B_L], np.uint8)
    hsv_high = np.array([R_H, G_H, B_H], np.uint8)
    mask = cv2.inRange(HSV, hsv_low, hsv_high)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    
    putText(frame,'Halloooo',1,30,0,255,0,1,3)  
    cv2.line(img=frame, pt1=(0, 300), pt2=(4000, 300), color=(0, 255, 0), thickness=2, lineType=8, shift=1)
    cv2.imshow("frame",frame)
    cv2.imshow("Blurred image", blurred)
    cv2.imshow('Frame 2',gray)
    cv2.imshow('Frame 1',HSV)
    cv2.imshow("Detections",res)
    cv2.imshow('Mask', mask)
    if stream & 0XFF == ord('q'):  #Letter 'q' is the escape key
        print("Video Berakhir")
        break                      #get out of loop
cam.release()
cv2.destroyAllWindows()

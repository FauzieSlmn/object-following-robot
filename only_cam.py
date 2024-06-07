import cv2 as cv2

cam = cv2.VideoCapture(0)
    
while(1):
    stream = cv2.waitKey(1)
    hai,frame = cam.read()

    cv2.imshow("frame",frame)
    if stream & 0XFF == ord('q'):  #Letter 'q' is the escape key
        print("Video Berakhir")
        break                      #get out of loop
cam.release()
cv2.destroyAllWindows()

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# print (cap.isOpened())

if cap.isOpened():
    while(True):
        ret, frame = cap.read()  # each for method return and function return 

        # Our operations on the frame come here
        if ret is True:
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("err")
            continue
else: 
    print("err opening camera")

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
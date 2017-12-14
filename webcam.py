import numpy as np
import cv2
from detection import Detector
import face_detection
import time

cap = cv2.VideoCapture(0)

if cap.isOpened():
    det_mod_path = 'det_nets_3.ckpt'
    cal_mod_path = 'cal_nets_14.ckpt'
    detector = Detector(det_mod_path, cal_mod_path)

    while(True):
        ret, frame = cap.read()  # each for method return and function return 

        # det_mod_path = 'det_nets_3.ckpt'
        # cal_mod_path = 'cal_nets_14.ckpt'
        # detetor = Detector(det_mod_path, cal_mod_path)

        # Our operations on the frame come here
        if ret is True:
            face_detection.faceD(frame, detector)
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # cv2.imshow('face', res)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("err")
            continue
else: 
    print ("Err opening camera.")

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
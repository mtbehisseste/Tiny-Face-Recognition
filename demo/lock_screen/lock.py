import cv2
import face_recognition as fr
import os
import getpass
cap = cv2.VideoCapture(0)
my_image = fr.load_image_file("me.jpg")
my_encoding = fr.face_encodings(my_image)[0] 
unknown_counter = 0
known_counter = 0
counter = 0
encode = []
process_time = True
lock = False
print("Please input your computer user password")
print("Your password will not be showed. Don't worry!")
password = getpass.getpass('Password:')
pswrd = " ".join(password)
if cap.isOpened():
        while(True):
            counter += 1
            if 50 / counter == 0:
                unknown_counter = 0
                counter = 0
                known_counter = 0
            ret, frame = cap.read()
            # if ret is True:
            #     cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            small_frame = cv2.resize(frame, (0,0), fx = 0.25, fy = 0.25)  
            if process_time:
                loc = fr.face_locations(small_frame)
                encode = fr.face_encodings(small_frame, loc)
                names = []

                for i in encode:
                    match = fr.compare_faces([my_encoding], i, 0.4)
                    name = "UNKNOWN"
                    unknown_counter += 1
                    if match[0]:
                        name = "USER"
                        known_counter += 1
                        unknown_counter -= 1
                    names.append(name)
            process_time = not process_time
            if unknown_counter >= 15:
                unknown_counter = 0
                os.system("gnome-screensaver-command -l")
                lock = True
            if known_counter >= 10 and lock == True:
                os.system("xdotool key --delay 50 " + pswrd + " Return")
                lock = False
            for (top, right, bottom, left), name in zip(loc, names):
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4
                cv2.rectangle(frame, (left, top), (right, bottom),(0,255,0), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255   ), cv2.FILLED)
                font = cv2.FONT_HERSHEY_COMPLEX
                cv2.putText(frame, name, (left+6, bottom-6), font, 1.0, (255,255,255), 1)
            # cv2.imshow("final", frame)
cap.release()
cv2.destroyAllWindows()

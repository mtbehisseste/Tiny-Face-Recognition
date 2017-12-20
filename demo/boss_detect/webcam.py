import numpy as np
import cv2
import face_recognition as fr
import os

cap = cv2.VideoCapture(0)

if cap.isOpened():
    my_img = fr.load_image_file("./me6.jpg")
    my_face_encoding = fr.face_encodings(my_img)[0]

    fake_code_img = fr.load_image_file("fakecode.png")
    fake_code_img = cv2.cvtColor(fake_code_img, cv2.COLOR_BGR2RGB)

    process_time = True
    count_boss = 0
    has_fake = False

    while True:
        ret, frame = cap.read()  # each for method return and function return 
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        if process_time:
            face_locations = fr.face_locations(small_frame)
            face_encodings = fr.face_encodings(small_frame, face_locations)

            face_name = []
            for i in face_encodings:
                match = fr.compare_faces([my_face_encoding], i, 0.4)
                
                if match[0]:
                    name = "boss"
                else:
                    name = "User"

                # print name
                face_name.append(name)

            if count_boss > 5:
                count_boss -= 1
            if count_boss < -5:
                count_boss += 1

            if "boss" in face_name:
                if count_boss < -3:
                    count_boss = 0
                count_boss += 1
            else:
                count_boss -= 1
            # print count_boss

            if count_boss > 3:
                cv2.namedWindow("fake", cv2.WINDOW_NORMAL)
                cv2.setWindowProperty("fake", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.imshow("fake", fake_code_img)
                has_fake = True
            elif count_boss <= 0 and has_fake:
                cv2.destroyWindow("fake")
                has_fake = False
            
        # process_time = not process_time

        for (top, right, bottom, left), name in zip(face_locations, face_name):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)

            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

else: 
    print ("Err opening camera.")

cap.release()
cv2.destroyAllWindows()
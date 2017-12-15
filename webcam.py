import numpy as np
import cv2
import face_recognition as fr

cap = cv2.VideoCapture(0)

if cap.isOpened():
    my_img = fr.load_image_file("./known/me.jpg")
    my_face_encoding = fr.face_encodings(my_img)[0]
    process_time = True
    
    while True:
        ret, frame = cap.read()  # each for method return and function return 
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        if process_time:
            face_locations = fr.face_locations(small_frame)
            face_encodings = fr.face_encodings(small_frame, face_locations)

            face_name = []
            for i in face_encodings:
                match = fr.compare_faces([my_face_encoding], i, 0.4)

                name = "Unknown"
                if match[0]:
                    name = "Jimmy"

                face_name.append(name)

        process_time = not process_time

        for (top, right, bottom, left), name in zip(face_locations, face_name):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)

            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

else: 
    print ("Err opening camera.")

cap.release()
cv2.destroyAllWindows()
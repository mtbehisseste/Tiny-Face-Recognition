=====Realtime Face Recognition with Webcam=====
This program shows where faces are by drawing a rectangle on the faces.
If the face is known, it will show the name you set, otherwise it will show "UNKNOWN".
All the above functions can be implement in realtime with the webcam.

*Usage: Change the image file at line 5 in recognition.py to your own face image.
Change the name you want to show at line 30 in recognition.py .
If more than one people want to be recognized, check out the example in https://github.com/ageitgey/face_recognition.

To run this program, you must download the things below first.
(python2.7 running on Ubuntu 16.04)

1.dlib
install boost : sudo apt-get install libboost-all-dev
clone the code : git clone https://github.com/davisking/dlib.git
cd dlib
mkdir build; cd build; cmake .. -DDLIB_USE_CUDA=0 -DUSE_AVX_INSTRUCTIONS=1; cmake --build
cd ..
python2 setup.py install --yes USE_AVX_INSTRUCTIONS --no DLIB_USE_CUDA

2.face_recognition
pip install face_recognition

(if you can't install dlib or face_recognition package successfully
try look up this website https://github.com/ageitgey/face_recognition)
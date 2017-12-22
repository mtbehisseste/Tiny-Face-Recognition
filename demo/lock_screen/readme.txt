=====Screen Locker=====
First you need to enter your password of the user. The password won't be showed out so there's no need to worry about password leaking. 
The Screen Locker will lock the screen when it detects some faces that is unknown.
It will automatically key in the password when detecting the known face.
Note that the program is only avalible with Linux and is testing on Ubuntu 16.04.

*Usage: Change the image file at line 6 in lock.py to your own face image.

To run this program, you must download the things below first.
(python2.7 running on Ubuntu 16.04)

1. dlib
install boost : sudo apt-get install libboost-all-dev
clone the code : git clone https://github.com/davisking/dlib.git
cd dlib
mkdir build; cd build; cmake .. -DDLIB_USE_CUDA=0 -DUSE_AVX_INSTRUCTIONS=1; cmake --build
cd ..
python2 setup.py install --yes USE_AVX_INSTRUCTIONS --no DLIB_USE_CUDA

2. face_recognition
pip install face_recognition

(if you can't install dlib or face_recognition package successfully
try look up this website https://github.com/ageitgey/face_recognition)

3. xdotool
sudo apt-get update
sudo apt-get install xdotool
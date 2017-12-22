=====Screen Locker=====

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
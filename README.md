# Facial Recognition on Raspberry Pi

Detect and identify faces on image files using python by training the machine beforehand. Tested on Raspberry Pi, macOS and Linux using Python 3.7

# Update: Live facial recognition from Raspberry Pi camera added.

# Dependencies
1) numpy
2) cv2 (OpenCV)
3) sys
4) glob
5) face_recognition
6) picamera

# face_recognition Library

This code has been developed using the face_recognition library.

Link: https://github.com/ageitgey/face_recognition

Detailed instructions on how to install and use the library has already been provided on the previous link. 

# OpenCV library

Follow the instruction here to install the OpenCV library on your Raspberry Pi: http://www.deciphertechnic.com/install-opencv-python-on-raspberry-pi/

(Should take about 2-3 hours on a Raspberry Pi)

# Procedure
# Facial Recognition from image file
(Tested with only one user for now)

1) Store the known images that will be used to train the machine in the "training_img" folder (make sure each image has only ONE face each).
2) Keep a "trained_data" folder in the same directory.
3) Run the "training.py" program from the command line.
4) After training is complete, there should be some data files in the "trained_data" folder.
5) Store the unknown images you want to test the machine with in the "unknown_img" folder.
6) Run the "Facial_Recognition_Full.py" program from the command line.
7) Follow the instructions. When asked for an image name, type in the name of any image file in the "unknown_img" folder that you want to test. 
8) Voila! There you have it. Facial recognition completed!

# Live Facial Recognition from Raspberry Pi camera

1) Training is the same as steps 1-4 as before.
2) Make sure the Camera is connected properly to the Raspberry Pi and it is enabled in the "Raspberry Pi Configuration".
3) Run the "Live_Facial_recognition.py" program from the command line.
4) Voila! Live facial recognition at your fingertips!


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
7) os

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
2) Run the "training_one_user.py" program from the terminal.
3) After training is complete, there should be some data files in the "trained_data" folder.
4) Store the unknown images you want to test the machine with in the "unknown_img" folder.
5) Run the "Facial_Recognition_Full.py" program from the terminal.
6) Follow the instructions. When asked for an image name, type in the name of any image file in the "unknown_img" folder that you want to test. 
7) Voila! There you have it. Facial recognition completed!

# Live Facial Recognition from Raspberry Pi camera (ONLY ONE USER)

1) Training is the same as steps 1-4 as before.
2) Make sure the Camera is connected properly to the Raspberry Pi and it is enabled in the "Raspberry Pi Configuration".
3) Run the "Live_Facial_recognition_one_user.py" program from the terminal.
4) Voila! Live facial recognition at your fingertips!

# Live Facial Recognition from Raspberry Pi camera (DYNAMIC USERS)

1) Store the images that will be used to train the machine in folders named "training_img_user1", "training_img_user2" and so on (one folder for each user).
2) Run the "training_dynamic.py" program from the terminal. 
3) After training is complete, there should be some data files in each of the "trained_data_userX" folders.
4) Make sure the Camera is connected properly to the Raspberry Pi and it is enabled in the "Raspberry Pi Configuration".
5) Run the "Live_Facial_recognition_dynamic.py" program from the terminal.
6) Voila! Live facial recognition at your fingertips!

# Live Facial Recognition from Raspberry Pi camera with audio feedback (DYNAMIC USERS)

1) Follow steps 1-4 as before
2) Store .wav files to be played on detection of a face in the "audio" directory. The filenames should be same as the user names, i.e, if there are two users named "user1" and "user2", the .wav files should be named "user1.wav" and "user2.wav"
5) Run the "Live_Facial_recognition_dynamic_with_audio_feedback.py" program from the terminal.
6) Voila! Live facial recognition at your fingertips (AND with audio feedback)!


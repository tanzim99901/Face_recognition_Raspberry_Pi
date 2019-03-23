import face_recognition
import cv2
import sys
import os
import glob

# Load all training images filenames
path = sorted(os.listdir('.'))
direct = path[:]

i = 0
while i <= (len(path) - 1):
    if "training_img_user" in path[i]:
        direct[i] = path[i]
    else:
        direct[i] = 0
    i += 1
print(direct)

i = 0
while i <= (len(direct) - 1):
    if direct[i] == 0:
        direct.pop(i)
        i = 0
    i += 1

i = 0
while i <= (len(direct) - 1):
    if direct[i] == 0:
        direct.pop(i)
        i = 0
    i += 1

print(direct) 

load_img = direct[:]

i = 0
while i <= (len(direct) - 1):
    load_img[i] = glob.glob(direct[i] + "/*.jpg")
    print("load_img[i] = ")
    print(load_img[i])
    i += 1

print("loaded\n")

# Initialize all arrays
loaded_img = load_img[:]
encoded_img = load_img[:]
face_img = load_img[:]
f = load_img[:]
counter = 0

# Load each image into an array
i = 0

while i <= (len(load_img) - 1):
    j = 0
    while j <= (len(load_img[i]) - 1):
        loaded_img[i][j] = face_recognition.load_image_file(load_img[i][j])
        j += 1
    i += 1

print("Training images loaded\n")
print("Encoding...\n")

# Recognize faces and encode them into separate arrays for each image
try:
    i = 0
    
    while i <= (len(loaded_img) - 1):
        j = 0
        print("Encoding for user {0}... \n".format(i+1))
        while j <= (len(loaded_img[i]) - 1):
            print("Encoding image {0}... \n".format(j+1))
            encoded_img[i][j] = face_recognition.face_encodings(loaded_img[i][j])
            j += 1
        i += 1
    i = 0
    while i <= (len(encoded_img) - 1):
        j = 0
        while j <= (len(encoded_img[i]) - 1):
            face_img[i][j] = encoded_img[i][j][0]
            j += 1
        i += 1
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

	
#Save the encoding into separate files
print("Creating training files...\n")

i = 0

while i <= (len(face_img) - 1):
    newpath = "trained_data_user{0}".format(i+1)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    j = 0
    while j <= (len(face_img[i]) - 1):
        f[i][j] = str(face_img[i][j])
        f[i][j] = f[i][j].replace("[", "")
        f[i][j] = f[i][j].replace("]", "")
        directory = "trained_data_user{0}/".format(i+1)
        data_dir = "data{0}.txt".format(j+1)
        filename = directory + data_dir
        fw = open(filename, "w")
        fw.write(str(f[i][j]))
        fw.close()
        j += 1
    i += 1

print("Training finished.\n")


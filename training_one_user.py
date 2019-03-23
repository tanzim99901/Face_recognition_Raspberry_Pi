import face_recognition
import cv2
import sys
import glob

# Load all training images filenames
load_img = glob.glob("training_img/*.jpg")

#Initialize all arrays
loaded_img = load_img[:]
encoded_img = load_img[:]
face_img = load_img[:]
f = load_img[:]
counter = 0

while counter <= (len(load_img)-1):
    loaded_img[counter] = 0
    encoded_img[counter] = 0
    f[counter] = 0
    face_img[counter] = 0
    counter += 1

# Load each image into an array
i = 0

while i <= (len(load_img) - 1):
    loaded_img[i] = face_recognition.load_image_file(load_img[i])
    
    
    i += 1

print("Training images loaded\n")
print("Encoding...\n")


#Recognize faces and encode them into separate arrays for each image
try:
    i = 0
    
    while i <= (len(loaded_img) - 1):
        print("Encoding image {0}... \n".format(i+1))
        encoded_img[i] = face_recognition.face_encodings(loaded_img[i])
        i += 1
    i = 0
    while i <= (len(encoded_img) - 1):
        face_img[i] = encoded_img[i][0]
        i += 1
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

	
#Save the encoding into separate files
print("Creating training files...\n")

newpath = "trained_data"
if not os.path.exists(newpath):
    os.makedirs(newpath)

i = 0

while i <= (len(face_img) - 1):
    f[i] = str(face_img[i])
    f[i] = f[i].replace("[", "")
    f[i] = f[i].replace("]", "")
    filename = "trained_data/data{0}.txt".format(i+1)
    fw = open(filename, "w")
    fw.write(str(f[i]))
    fw.close()
    i += 1

print("Training finished.\n")

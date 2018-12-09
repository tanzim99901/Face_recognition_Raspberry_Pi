import face_recognition
import picamera
import numpy as np
import cv2
import sys
import glob

resize = .5
r_mul = 2

users = ["Tanzim", "Iftekhar"] # add more values here if there are more users

trained_array = []
trained_array = users[:]

j = 0
while j <= (len(users) - 1):
    trained_array[j] = ""
    j += 1
j = 0

while j <= (len(trained_array) - 1):
    directory = "trained_data_user{0}".format(j+1)
    filenames = directory + "/data*"
    trained_array[j] = glob.glob(filenames)
    j += 1
j = 0
i = 0

tolerance = 1

camera = picamera.PiCamera()
camera.resolution = (640, 480)
output = np.empty((480, 640, 3), dtype=np.uint8)

while i <= (len(trained_array) - 1):
    j = 0
    while j <= (len(trained_array[i]) - 1):
        directory = "trained_data_user{0}/".format(i+1)
        trained_array[i][j] = trained_array[i][j].replace(directory, "")
        j += 1
    i += 1

j = 0
i = 0

while i <= (len(trained_array) - 1):
    j = 0
    while j <= (len(trained_array[i]) - 1):
        directory = "trained_data_user{0}/".format(i+1)
        trained_array[i][j] = directory + trained_array[i][j]
        j += 1
    i += 1
i = 0 
j = 0

t = []
encoding = []

t = trained_array[:]
encoding = trained_array[:]

i = 0
while i <= (len(trained_array) - 1):
    j = 0
    while j <= (len(trained_array[i]) - 1):
        fr = open(trained_array[i][j], 'r')
        t[i][j] = fr.read()
        encoding[i][j] = np.fromstring(t[i][j], dtype=np.float, sep = ' ')
        fr.close()
        j += 1
    i += 1
i = 0

known_faces = encoding[:]

while True:
    face_locations = []
    unknown_face_encoding = []

    camera.capture(output, format="bgr")
    frame = cv2.resize(output, (0, 0), fx=resize, fy=resize)
    unknown_image = frame[...,::-1]
    print("\nNew Image Loaded")
    print("\nProcessing...")
    try:
        face_locations = face_recognition.face_locations(unknown_image)
        unknown_face_encoding = face_recognition.face_encodings(unknown_image, face_locations)
    except IndexError:
        print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
        quit()

    print("\nNew Image encoded")
    
    print("Comparing...\n")

    test_var = 0 
    known_len = 0
    recog = unknown_face_encoding[:]
    det_users = unknown_face_encoding[:]
    counter = unknown_face_encoding[:]
    print("counting")
    count_counter = 0
    while count_counter <= (len(counter) - 1):
        #counter[count_counter] = 0
        recog[count_counter] = 0
        det_users[count_counter] = ""
        print("counted")
        count_counter += 1
        
    while test_var <= (len(unknown_face_encoding) - 1):
        known_len = 0
        print("Face number {0} :".format(test_var+1))
        while known_len <= (len(known_faces) - 1):
            results = face_recognition.compare_faces(known_faces[known_len], unknown_face_encoding[test_var])
            print(results)
            i = 0
            k = 0
            
            while i <= (len(results) - 1):
                if results[i] == 1:
                    k += 1
                i += 1
            counter[test_var][known_len] = k
            if counter[test_var][known_len] >= max(counter[test_var]):
                if counter[test_var][known_len] >= (len(trained_array[known_len]) - tolerance):
                    recog[test_var] = 1
                    det_users[test_var] = users[known_len]
                    tanzim = test_var
                    print(users[known_len] + " Detected")
                else:
                    print("Unknown")
                
            else:
                print("Unknown")
            print("Match count: {0}".format(counter[test_var][known_len]))
            print("\n")
            known_len += 1
        test_var += 1
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    face_len = 0
    print("Drawing rectangles on faces...\n")
    while face_len <= len(face_locations) - 1:
        cv2.rectangle(output, (face_locations[face_len][3]*r_mul, face_locations[face_len][0]*r_mul), (face_locations[face_len][1]*r_mul, face_locations[face_len][2]*r_mul), (0, 255, 0), 2)
        if recog[face_len] == 1:
            cv2.putText(output, det_users[face_len], (face_locations[face_len][3]*r_mul, (face_locations[face_len][2]*r_mul + 20)), font, 0.8, (0,255,2), 2)
        face_len += 1
    print("Completed!\n")
    cv2.imshow("Faces found", output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()

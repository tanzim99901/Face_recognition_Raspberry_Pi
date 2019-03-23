import face_recognition
import picamera
import numpy as np
import cv2
import sys
import glob

resize = .5
r_mul = 2

users = ["Tanzim", "Miraj"]

tolerance = 1
trained_array = glob.glob("trained_data/data*")		# Load all trained data filenames 

# Initialize camera object
camera = picamera.PiCamera()
camera.resolution = (640, 480)
output = np.empty((480, 640, 3), dtype=np.uint8)

# Initialize all arrays
t = []
encoding = []
t = trained_array[:]
encoding = trained_array[:]

j = 0
while (j <= (len(trained_array) - 1)):
    t[j] = ""
    encoding[j] = 0
    j += 1
j = 0


# Open all encoding files
i = 0
while i <= (len(trained_array) - 1):
    fr = open(trained_array[i], 'r')
    t[i] = fr.read()
    encoding[i] = np.fromstring(t[i], dtype=np.float, sep = ' ')
    fr.close()
    i += 1
i = 0

known_faces = encoding[:]		# Initialize Known faces array

while True:
    face_locations = []
    unknown_face_encoding = []

    camera.capture(output, format="bgr")		# capture an image frame from video stream
    frame = cv2.resize(output, (0, 0), fx=resize, fy=resize)		# resize the captured frame
    unknown_image = frame[...,::-1]		# convert bgr to rgb

    print("\nNew Image Loaded")
    print("\nProcessing...")
    try:
        face_locations = face_recognition.face_locations(unknown_image)		# Detect faces on the frame
        unknown_face_encoding = face_recognition.face_encodings(unknown_image, face_locations)
    except IndexError:
        print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
        quit()

    print("\nNew Image encoded")
    
    print("Comparing...\n")
    test_var = 0
    recog = 0 
    detection = -1
    counter = unknown_face_encoding[:]
    count_counter = 0
    while count_counter <= (len(counter) - 1):
        counter[count_counter] = 0
        count_counter += 1
    while test_var <= (len(unknown_face_encoding) - 1):
        results = face_recognition.compare_faces(known_faces, unknown_face_encoding[test_var])		# Compare faces in the frame with the known faces previously trained
        print("Face number {0} :".format(test_var+1))
        print(results)
        i = 0
        k = 0
        
        while i <= (len(results) - 1):
            if results[i] == 1:
                k += 1
            i += 1
        counter[test_var] = k
        if counter[test_var] >= max(counter):
            if counter[test_var] >= (len(trained_array) - tolerance):
                recog = 1
                detection = test_var
                print(users[0] + " Detected")
            else:
                print("Unknown")
            
        else:
            print("Unknown")
        print("Match count: {0}".format(counter[test_var]))
        print("\n")
        test_var += 1
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    face_len = 0
    print("Drawing rectangles on faces...\n")
    while face_len <= (len(face_locations) - 1):
        cv2.rectangle(output, (face_locations[face_len][3]*r_mul, face_locations[face_len][0]*r_mul), (face_locations[face_len][1]*r_mul, face_locations[face_len][2]*r_mul), (0, 255, 0), 2)		# Draw rectangle around faces
        if detection > -1:
            if recog == 1:
                if face_len == detection:
                    cv2.putText(output, users[0], (face_locations[face_len][3]*r_mul, (face_locations[face_len][2]*r_mul + 20)), font, 0.8, (0,255,2), 2)	# Put names of detected faces below the corresponding rectangle
        face_len += 1
    print("Completed!\n")
    cv2.imshow("Faces found", output)		#Display the image
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()

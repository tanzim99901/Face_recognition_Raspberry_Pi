import face_recognition
import numpy as np
import cv2
import sys
import glob

affirmative = ['y','yes','sure','ok','okay','yeah','ya','Y','YES','SURE','OK','OKAY','YEAH','YA']
negative = ['n','no','not sure','na','nah','nope','N','NO','NOT SURE','NA','NOPE','NAH']
users = ["Tanzim", "Miraj"]

tolerance = 1
trained_array = glob.glob("trained_data/*.txt")
i = 0
while (i <= (len(trained_array) - 1)):
    trained_array[i] = trained_array[i].replace("trained_data/", "")
    i += 1
i = 0

counter = 0
while (counter <= (len(trained_array) - 1)):
    trained_array[counter] = "trained_data/" + trained_array[counter]
    counter += 1

x = 1

while x == 1:
    face_locations = []
    unknown_face_encoding = []
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
    try:
        ans = str(input("Do you want to start?\n"))
        if ans in affirmative:
            try:
                insert = str(input("Enter image name: \n"))
                if ".jpg" in insert:
                    input_img = insert
                else:
                    input_img = insert + ".jpg"
                input_img = "unknown_img/" + input_img
                unknown_image = face_recognition.load_image_file(input_img)
                print("\nNew Image Loaded")
                print("\nProcessing...")
                try:
                    face_locations = face_recognition.face_locations(unknown_image)
                    unknown_face_encoding = face_recognition.face_encodings(unknown_image)
                except IndexError:
                    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
                    quit()
            
                print("\nNew Image encoded")
                
                i = 0
                while (i <= (len(trained_array) - 1)):
                    fr = open(trained_array[i], 'r')
                    t[i] = fr.read()
                    encoding[i] = np.fromstring(t[i], dtype=np.float, sep = ' ')
                    fr.close()
                    i += 1
                i = 0
                
                print("\nTrained Files read\n")
                print("Comparing...\n")
                known_faces = encoding[:]
                test_var = 0
                recog = 0 
                detection = -1
                counter = unknown_face_encoding[:]
                count_counter = 0
                while (count_counter <= len(counter) - 1):
                    counter[count_counter] = 0
                    count_counter += 1
                while (test_var <= len(unknown_face_encoding) - 1):
                    results = face_recognition.compare_faces(known_faces, unknown_face_encoding[test_var])
                    print("Face number {0} :".format(test_var+1))
                    print(results)
                    i = 0
                    k = 0
                    
                    while(i <= len(results) - 1):
                        if results[i] == 1:
                            k += 1
                        i += 1
                    counter[test_var] = k
                    if (counter[test_var] >= max(counter)):
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
                    
                image = cv2.imread(input_img)
                font = cv2.FONT_HERSHEY_SIMPLEX
                face_len = 0
                print("Drawing rectangles on faces...\n")
                while (face_len <= len(face_locations) - 1):
                    cv2.rectangle(image, (face_locations[face_len][3], face_locations[face_len][0]), (face_locations[face_len][1], face_locations[face_len][2]), (0, 255, 0), 2)
                    if (detection > -1):
                        if (recog == 1):
                            if (face_len == detection):
                                cv2.putText(image, users[0], (face_locations[face_len][3], face_locations[face_len][2]), font, 0.8, (0,255,2), 2)
                    face_len += 1
                print("Completed!\n")
                cv2.imshow("Faces found", image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                continue
            except:
                print("Error")
        elif ans in negative:
            try:
                fin = str(input("Do you want to stop?\n"))
                if fin in affirmative:
                    x = 0
                elif fin in negative:
                    x = 1
                else:
                    print("Error")
            except:
                print("Error")
    except:
        print("Error")
    

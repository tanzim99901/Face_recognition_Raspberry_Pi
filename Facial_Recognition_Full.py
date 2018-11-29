import face_recognition
import numpy as np
import cv2
import sys

affirmative = ['y','yes','sure','ok','okay','yeah','ya','Y','YES','SURE','OK','OKAY','YEAH','YA']
negative = ['n','no','not sure','na','nah','nope','N','NO','NOT SURE','NA','NOPE','NAH']
users = ["Tanzim", "Miraj"]

tolerance = 1
tanz_array = ["tanz1.txt", "tanz2.txt", "tanz3.txt", "tanz4.txt", "tanz5.txt", "tanz6.txt", "tanz7.txt", "tanz8.txt", "tanz9.txt"] 

counter = 0
while (counter <= (len(tanz_array) - 1)):
    tanz_array[counter] = "trained_data/" + tanz_array[counter]
    counter += 1

x = 1

while x == 1:
    face_locations = []
    unknown_face_encoding = []
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
            
                fr = open(tanz_array[0], 'r')
                tanz1 = fr.read()
                tanzim_face_encoding1 = np.fromstring(tanz1, dtype=np.float, sep = ' ')
                fr.close()
            
                fr = open(tanz_array[1], 'r')
                tanz2 = fr.read()
                tanzim_face_encoding2 = np.fromstring(tanz2, dtype=np.float, sep = ' ')
                fr.close()
            
                fr = open(tanz_array[2], 'r')
                tanz3 = fr.read()
                tanzim_face_encoding3 = np.fromstring(tanz3, dtype=np.float, sep = ' ')
                fr.close()
            
                fr = open(tanz_array[3], 'r')
                tanz4 = fr.read()
                tanzim_face_encoding4 = np.fromstring(tanz4, dtype=np.float, sep = ' ')
                fr.close()
            
                fr = open(tanz_array[4], 'r')
                tanz5 = fr.read()
                tanzim_face_encoding5 = np.fromstring(tanz5, dtype=np.float, sep = ' ')
                fr.close()
            
                fr = open(tanz_array[5], 'r')
                tanz6 = fr.read()
                tanzim_face_encoding6 = np.fromstring(tanz6, dtype=np.float, sep = ' ')
                fr.close()
            
                fr = open(tanz_array[6], 'r')
                tanz7 = fr.read()
                tanzim_face_encoding7 = np.fromstring(tanz7, dtype=np.float, sep = ' ')
                fr.close()
            
                fr = open(tanz_array[7], 'r')
                tanz8 = fr.read()
                tanzim_face_encoding8 = np.fromstring(tanz8, dtype=np.float, sep = ' ')
                fr.close()
            
                fr = open(tanz_array[8], 'r')
                tanz9 = fr.read()
                tanzim_face_encoding9 = np.fromstring(tanz9, dtype=np.float, sep = ' ')
                fr.close()
            
                print("\nTrained Files read\n")
                print("Comparing...\n")
                known_faces = [
                    tanzim_face_encoding1,
                    tanzim_face_encoding2,
                    tanzim_face_encoding3,
                    tanzim_face_encoding4,
                    tanzim_face_encoding5,
                    tanzim_face_encoding6,
                    tanzim_face_encoding7,
                    tanzim_face_encoding8,
                    tanzim_face_encoding9,
                ]
                
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
                        if counter[test_var] >= (len(tanz_array) - tolerance):
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
    

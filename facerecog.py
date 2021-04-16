import face_recognition
import numpy as np
import cv2
import os
import smtplib
try:
    name=input("Name: ")
    imgloaded=face_recognition.load_image_file('C:/Users/Kral/Pictures/Camera Roll/'+name+'.jpg')
    imgloaded=cv2.cvtColor(imgloaded,cv2.COLOR_BGR2RGB)

    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    cv2.imwrite(os.path.join('C:/Users/Kral/Pictures/Camera Roll' , 'testimage.jpg'), image)
    imgtest=face_recognition.load_image_file('C:/Users/Kral/Pictures/Camera Roll/testimage.jpg')
    imgtest=cv2.cvtColor(imgtest,cv2.COLOR_BGR2RGB)
    faceloc=face_recognition.face_locations(imgloaded)[0]
    encodeloaded=face_recognition.face_encodings(imgloaded)[0]
    cv2.rectangle(imgloaded,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),2)
    faceloctest=face_recognition.face_locations(imgtest)[0]
    encodetest=face_recognition.face_encodings(imgtest)[0]
    cv2.rectangle(imgtest,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),2)
    results=face_recognition.compare_faces([encodeloaded],encodetest)
    if(results[0]):
        print(name.capitalize+" Verified")
    else:
        print("Verification Failed")
    

except:
    print("Error In Loading File")
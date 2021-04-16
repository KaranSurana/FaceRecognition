
import cv2
import os
import smtplib

name=input("Name: ")
camera = cv2.VideoCapture(0)
return_value, image = camera.read()
cv2.imwrite(os.path.join('C:/Users/Kral/Pictures/Camera Roll' , name+'.jpg'), image)

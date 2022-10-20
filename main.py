import cv2
import numpy as np
import face_recognition

imgElon = face_recognition.load_image_file('imagesbasic/Elon Musk.jpg')
imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('imagesbasic/Elon Test.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgElon)


cv2.imshow('Elon Musk',imgElon)
cv2.imshow('Elon Test',imgTest)
cv2.waitKey(0)


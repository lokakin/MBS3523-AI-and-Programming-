

import cv2
print(cv2.__version__)
import face_recognition
print(face_recognition.__version__)
import numpy as np


imgKnown = face_recognition.load_image_file('Images_Known/lkk.png')
imgKnown = cv2.cvtColor(imgKnown, cv2.COLOR_RGB2BGR)
faceLocKnown = face_recognition.face_locations(imgKnown)[0]
encodeKnown = face_recognition.face_encodings(imgKnown)[0]

capture = cv2.VideoCapture(1)
capture.set(3,640)
capture.set(4,480)

while True:
    success, img = capture.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    faceLocsCam = face_recognition.face_locations(imgRGB)
    encodesCam = face_recognition.face_encodings(imgRGB, faceLocsCam)

    
    for (top,right,bottom,left),encodeCam in zip(faceLocsCam,encodesCam):
        results = face_recognition.compare_faces([encodeKnown],encodeCam)
        faceDist = face_recognition.face_distance([encodeKnown],encodeCam)
        print(faceDist)
        if faceDist < 0.5:
                cv2.rectangle(img, (left,top),(right,bottom), (0, 0, 0), 4)

    cv2.imshow('Frame', img)
  
    if cv2.waitKey(1) == 27:
        break

capture.release()
cv2.destroyAllWindows()

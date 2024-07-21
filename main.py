import os
# os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
# import tensorflow as tf
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
import cv2
from deepface import DeepFace

face_classifier = cv2.CascadeClassifier()
face_classifier.load(cv2.samples.findFile("haarcascade_frontalface_default.xml"))
# new_frame = cv2.imread('')

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(frame_gray)
    response = DeepFace.analyze(frame, actions=("emotion",), enforce_detection=False)
    # response = DeepFace.analyze(frame, actions=("emotion",), )
    # print(response)
    for face in faces:
        x, y, w, h = face
        cv2.putText(frame, text = response[0]['dominant_emotion'], org=(x,y), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1,color=(0, 225, 0) )
        new_frame = cv2.rectangle(frame, (x, y), (x+w,y+h), color=(255, 0, 0), thickness=2)
        cv2.imshow("camera", new_frame)
    if (cv2.waitKey(30) == 27):
        break
cap.release()
cv2.destroyAllWindows()
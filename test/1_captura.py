# https://www.youtube.com/watch?v=PGsAsuwBdw0
import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

#1. Grabar Video
cap = cv2.VideoCapture('squat.mp4')
alto = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
ancho = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
fps = cap.get(cv2.CAP_PROP_FPS)

videoWriter = cv2.VideoWriter('test.avi', cv2.VideoWriter_fourcc('P','I','M','1'), fps, (int(ancho), int(alto)))

while cap.isOpened():
    ret, frame = cap.read()
    
    try:
        cv2.imshow('test', frame)
        videoWriter.write(frame)
    except Exception as e:
        break

cap.release()
videoWriter.release()
cv2.destroyAllWindows()


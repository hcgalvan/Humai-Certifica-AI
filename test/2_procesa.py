
import csv
import cv2
import mediapipe as mp
import os
import numpy as np
from matplotlib import pyplot as plt

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

landmarks = ['class']
for val in range(1,33+1):
    landmarks += ['x{}'.format(val), 'y{}'.format(val), 'z{}'.format(val), 'v{}'.format(val)]

landmarks[1:]

with open('coords1.csv', mode='w', newline='') as f:
    csv_writer = csv.writer(f, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(landmarks)

def export_landmark(results, action):
    try:
        keypoints = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten().tolist()
        keypoints.insert(0, action)

        with open('coords1.scv', mode='a', newline='') as f:
            csv_writer = csv.writer(f, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(keypoints)
    except Exception as e:
        pass
    export_landmark(results, 'up' )

cap = cv2.VideoCapture('~/hcgmachlearn-gd/Humai-Certifica-AI/test/squat.mp4')    

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:

    while cap.isOpened():
        ret, frame = cap.read()

        #Recolorear 
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        
        #Detectar
        results = pose.process(image) 

        #Recolorear el fondo de la imagen para para renderizar
        image.flags.writeable = True
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS, 
                                 mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4),
                                 mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                                 )
        k = cv2.waitKey(1)
        if k == 117:
            export_landmark(results, 'up')
        if k == 117:
            export_landmark(results, 'down')
        
        cv2.imshow('Raw Webcam Feed', image)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()


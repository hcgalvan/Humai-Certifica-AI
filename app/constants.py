import cv2
import av
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import mediapipe as mp
import pathlib
import pickle 
from app import landmarks

from streamlit_webrtc import (
    RTCConfiguration,
    WebRtcMode,
    WebRtcStreamerContext,
    webrtc_streamer,
)

model_path_1 = pathlib.PurePath('data/manos.pkl')

RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)
class app_manos:
    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            model_complexity=0,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        def process(image):
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = self.hands.process(image)

            # Draw the hand annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    self.mp_drawing.draw_landmarks(
                        image,
                        hand_landmarks,
                        self.mp_hands.HAND_CONNECTIONS,
                        self.mp_drawing_styles.get_default_hand_landmarks_style(),
                        self.mp_drawing_styles.get_default_hand_connections_style())
            return cv2.flip(image, 1)

        class VideoProcessor:
            def recv(self, frame):
                img = frame.to_ndarray(format="bgr24")

                img = process(img)

                return av.VideoFrame.from_ndarray(img, format="bgr24")
            
        self.webrtc_ctx = webrtc_streamer(
        key="WYH",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints={"video": True, "audio": False},
        video_processor_factory=VideoProcessor,
        async_processing=True,
        )
        
class predict_manos:
    def __init__(self):
        #global current_stage
        #global counter
        #global body_language_class
        #global body_language_prob
        
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5)
        with open( model_path_1, 'rb') as f:
            self.model = pickle.load(f)
            self.current_stage = ''
            self.counter = 0
            self.body_language_prob  = np.array([0,0])
            self.body_language_class =  ''
            
        ## Setup mediapipe instance
        def process(image):
            with self.mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
                # Recolor image to RGB
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
            
                # Make detection
                results = self.pose.process(image)
            
                # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                
                # Detección de Pose
                self.mp_drawing.draw_landmarks(image, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS, 
                                        self.mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4),
                                        self.mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                                        )
                
                # Extract landmarks
                try:
                    
                    row = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten().tolist()
                    X = pd.DataFrame([row], columns=landmarks[1:])
                    
                    self.body_language_class = self.model.predict(X)[0]
                    
                    self.body_language_prob = self.model.predict_proba(X)[0]
                    print(self.body_language_class, self.body_language_prob)
                    
                    if self.body_language_class or self.body_language_prob:
                        print('predicted')
                    else :
                        print('prediction error')

                    if self.body_language_class == "derecha" and self.body_language_prob[self.body_language_prob.argmax()] >= 0.7:
                        self.current_stage = "derecha"
                    elif self.current_stage=="derecha" and self.body_language_class=="izquierda" and self.body_language_prob[self.body_language_prob.argmax()] >= 0.7:
                        self.current_stage = "izquierda"
                        self.counter +=1
                        
                    # obtener el estado del box
                    cv2.rectangle(image, (0,0), (250, 60), (245, 117, 16), -1)
                    
                    # Mostrar las clases
                    cv2.putText(image, 'CLASS'
                                , (95,12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                    cv2.putText(image, self.body_language_class.split(' ')[0]
                                , (90,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
                    
                    # Mostrar Probabilidad
                    cv2.putText(image, 'PROB'
                                , (15,12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                    cv2.putText(image, str(round(self.body_language_prob[np.argmax(self.body_language_prob)],2))
                            , (10,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
                    
                    # Mostrar Conteo
                    cv2.putText(image, 'COUNT'
                                , (180,12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                    cv2.putText(image, str(self.counter)
                                , (175,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        
                except Exception as e:
                    pass
            return cv2.flip(image, 1)
    
        class VideoProcessor:
            def recv(self, frame):
                img = frame.to_ndarray(format="bgr24")

                img = process(img)

                return av.VideoFrame.from_ndarray(img, format="bgr24")
            
        self.webrtc_ctx = webrtc_streamer(
        key="WYH",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints={"video": True, "audio": False},
        video_processor_factory=VideoProcessor,
        async_processing=True,
        )



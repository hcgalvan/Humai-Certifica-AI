import asyncio
import logging
import queue
import threading
import urllib.request
from pathlib import Path
from typing import List, NamedTuple, Optional
import pickle 
from app import landmarks

import av
import cv2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import mediapipe as mp
from aiortc.contrib.media import MediaPlayer
import pathlib

from streamlit_webrtc import (
    RTCConfiguration,
    WebRtcMode,
    WebRtcStreamerContext,
    webrtc_streamer,
)

HERE = Path(__file__).parent
model_path_1 = pathlib.PurePath('data/manos.pkl')
model_path_2 = pathlib.PurePath('data/manos.csv')
data = pd.read_csv(model_path_2)
logger = logging.getLogger(__name__)

RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

def main():
    st.header("Biomecánica: Detección en Tiempo real")
    
    pages = {
        "Detección de manos": app_manos,
        "Detección Manos Predict": manos_predict
        
    }
    page_titles = pages.keys()
    
    page_title = st.sidebar.selectbox(
        "Elegir Modelos",
        page_titles,
    )
    
    st.subheader(page_title)
    st.sidebar.title("Visualizar Seteos")
    page_func = pages[page_title]
    page_func()
    # ejemplos de que colocar en menu central
    st.text('Fixed width text')
    st.markdown('_Markdown_') # see *
    st.caption('Balloons. Hundreds of them...')
    st.latex(r''' e^{i\pi} + 1 = 0 ''')
    st.write('Most objects') # df, err, func, keras!
    st.write(['st', 'is <', 3]) # see *
    
    st.form('my_form_identifier')
    #st.form_submit_button('Submit to me')
    st.container()
    st.columns(2)
    col1, col2 = st.columns(2)
    col1.subheader('Columnisation')
    st.expander('Expander')
    with st.expander('Expand'):
         st.write('Juicy deets')

    st.dataframe(data)
    st.table(data.iloc[0:10])
    st.json({'foo':'bar','fu':'ba'})
    
    st.metric(label="Temp", value="273 K", delta="1.2 K")
    logger.debug("=== Alive threads ===")
    for thread in threading.enumerate():
        if thread.is_alive():
            logger.debug(f"  {thread.name} ({thread.ident})")



def app_manos():
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )
    def process(image):
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
         for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())
        return cv2.flip(image, 1)

    class VideoProcessor:
        def recv(self, frame):
            img = frame.to_ndarray(format="bgr24")

            img = process(img)

            return av.VideoFrame.from_ndarray(img, format="bgr24")
        
    webrtc_ctx = webrtc_streamer(
    key="WYH",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={"video": True, "audio": False},
    video_processor_factory=VideoProcessor,
    async_processing=True,
   )

def manos_predict():
    global current_stage
    global counter
    global body_language_class
    global body_language_prob
    
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5)
    with open( model_path_1, 'rb') as f:
        model = pickle.load(f)
        current_stage = ''
        counter = 0
        body_language_prob  = np.array([0,0])
        body_language_class =  ''
        
    ## Setup mediapipe instance
    def process(image, model):
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            # Recolor image to RGB
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
        
            # Make detection
            results = pose.process(image)
        
            # Recolor back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            # Detección de Pose
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS, 
                                    mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4),
                                    mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                                    )
            
            # Extract landmarks
            try:
                
                row = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten().tolist()
                X = pd.DataFrame([row], columns=landmarks[1:])
                
                body_language_class = model.predict(X)[0]
                
                body_language_prob = model.predict_proba(X)[0]
                print(body_language_class, body_language_prob)
                
                if body_language_class or body_language_prob:
                    print('predicted')
                else :
                    print('prediction error')

                if body_language_class == "derecha" and body_language_prob[body_language_prob.argmax()] >= 0.7:
                    current_stage = "derecha"
                elif current_stage=="derecha" and body_language_class=="izquierda" and body_language_prob[body_language_prob.argmax()] >= 0.7:
                    current_stage = "izquierda"
                    counter +=1
                    
                # obtener el estado del box
                cv2.rectangle(image, (0,0), (250, 60), (245, 117, 16), -1)
                
                # Mostrar las clases
                cv2.putText(image, 'CLASS'
                            , (95,12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, body_language_class.split(' ')[0]
                            , (90,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
                
                # Mostrar Probabilidad
                cv2.putText(image, 'PROB'
                            , (15,12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, str(round(body_language_prob[np.argmax(body_language_prob)],2))
                        , (10,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
                
                # Mostrar Conteo
                cv2.putText(image, 'COUNT'
                            , (180,12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, str(counter)
                            , (175,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    
            except Exception as e:
                pass
        return cv2.flip(image, 1)
   
    class VideoProcessor:
        def recv(self, frame):
            img = frame.to_ndarray(format="bgr24")

            img = process(img, model )

            return av.VideoFrame.from_ndarray(img, format="bgr24")
        
    webrtc_ctx = webrtc_streamer(
    key="WYH",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={"video": True, "audio": False},
    video_processor_factory=VideoProcessor,
    async_processing=True,
   )

if __name__ == "__main__":
    import os

    DEBUG = os.environ.get("DEBUG", "false").lower() not in ["false", "no", "0"]

    logging.basicConfig(
        format="[%(asctime)s] %(levelname)7s from %(name)s in %(pathname)s:%(lineno)d: "
        "%(message)s",
        force=True,
    )

    logger.setLevel(level=logging.DEBUG if DEBUG else logging.INFO)

    st_webrtc_logger = logging.getLogger("streamlit_webrtc")
    st_webrtc_logger.setLevel(logging.DEBUG)

    fsevents_logger = logging.getLogger("fsevents")
    fsevents_logger.setLevel(logging.WARNING)

    main()
import logging
import threading
from pathlib import Path
from typing import List, NamedTuple, Optional
from app import landmarks
## modelos ###
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline 
from sklearn.preprocessing import StandardScaler 

from app import landmarks, app_manos, predict_manos

from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

from sklearn.metrics import accuracy_score, precision_score, recall_score # Accuracy metrics 
##
import pandas as pd
import streamlit as st
import pathlib
##
import cv2
import mediapipe as mp
import numpy as np
###
import pathlib
import pickle 
import matplotlib.pyplot as plt

import tempfile
###
import streamlit as st
from streamlit_webrtc import (
    RTCConfiguration,
    WebRtcMode,
    WebRtcStreamerContext,
    webrtc_streamer,
)

HERE = Path(__file__).parent
model = pathlib.PurePath('data/flexiones_cb.pkl')
video_1 = pathlib.PurePath('data/flexiones_1.mp4')
logger = logging.getLogger(__name__)

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)
       

st.set_page_config(
    page_title="Biomecanica&ML",
    page_icon="🥟",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)



def main():
    st.header("Biomecánica: Detección en Tiempo real")
    pages = {
        "Ejemplo 1": modelos_1,
        "Ejemplo 2": modelos_2,
        "Ejemplo 3": modelos_3,
        #"Detección manos": app_manos,
        "Predict On Line": predict_manos
        
        
    }
    page_titles = pages.keys()
    page_title = st.sidebar.selectbox(
        "Elegir Actividad",
        page_titles,
    )
    st.subheader(page_title)
    page_func = pages[page_title]
    page_func()
    

def modelos_1():
    #video_file = open('notebooks/flexiones-demo.mp4', 'rb')
    #video_bytes = video_file.read()

    #st.video(video_bytes)

    DEFAULT_WIDTH = 80
    VIDEO_DATA = "https://youtu.be/Wfv2_328TQE"
        

    #st.set_page_config(layout="wide")

    width = st.sidebar.slider(
        label="Width", min_value=0, max_value=100, value=DEFAULT_WIDTH, format="%d%%"
    )

    width = max(width, 0.01)
    side = max((100 - width) / 2, 0.01)

    _, container, _ = st.columns([side, width, side])
    container.video(data=VIDEO_DATA)

def modelos_2():
    #video_file = open('notebooks/flexiones-demo.mp4', 'rb')
    #video_bytes = video_file.read()

    #st.video(video_bytes)

    DEFAULT_WIDTH = 80
    VIDEO_DATA = "https://youtu.be/DQATepYNVZ8"
 
    #st.set_page_config(layout="wide")

    width = st.sidebar.slider(
        label="Width", min_value=0, max_value=100, value=DEFAULT_WIDTH, format="%d%%"
    )

    width = max(width, 0.01)
    side = max((100 - width) / 2, 0.01)

    _, container, _ = st.columns([side, width, side])
    container.video(data=VIDEO_DATA)
    
    
def modelos_3():
    #video_file = open('notebooks/flexiones-demo.mp4', 'rb')
    #video_bytes = video_file.read()

    #st.video(video_bytes)

    DEFAULT_WIDTH = 80
    VIDEO_DATA = "notebooks/flexiones-demo.mp4"
 
    #st.set_page_config(layout="wide")

    width = st.sidebar.slider(
        label="Width", min_value=0, max_value=100, value=DEFAULT_WIDTH, format="%d%%"
    )

    width = max(width, 0.01)
    side = max((100 - width) / 2, 0.01)

    _, container, _ = st.columns([side, width, side])
    container.video(data=VIDEO_DATA)
        
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
import logging
import threading
from pathlib import Path
from typing import List, NamedTuple, Optional
from app import landmarks, app_manos, predict_manos
## modelos ###
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline 
from sklearn.preprocessing import StandardScaler 

from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

from sklearn.metrics import accuracy_score, precision_score, recall_score # Accuracy metrics 
##
import pandas as pd
import streamlit as st
import pathlib

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

HERE = Path(__file__).parent
model_rc = pathlib.PurePath('data/push_ups.pkl')
data_rc = pathlib.PurePath('data/pushups.csv')
model_path_1 = pathlib.PurePath('data/manos.pkl')
model_path_2 = pathlib.PurePath('data/manos.csv')
data = pd.read_csv(model_path_2)
logger = logging.getLogger(__name__)


def main():
    st.header("Biomecánica: Detección en Tiempo real")
    pages = {
        "Modelos Utilizados": modelos,
        "Predict Push UP": testRidgeClassifier,
        "Detección manos": app_manos,
        "Predict mov manos": predict_manos
        
    }
    page_titles = pages.keys()
    page_title = st.sidebar.selectbox(
        "Elegir Actividad",
        page_titles,
    )
    st.subheader(page_title)
    page_func = pages[page_title]
    page_func()

def modelos():
    # st.sidebar.title("Visualizar Seteos")
    # eleccion = st.sidebar.radio(
    #             "Modelos",
    #             ("RidgeClassifier","RandomForestClassifier","GradientBoostingClassifier")
    #         )
    #  st.write(eleccion)    

    df = data
    X = df.drop('class', axis=1) # features
    y = df['class'] # target
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1234)
    
    pipelines = {
    #'lr':make_pipeline(StandardScaler(), LogisticRegression()),
    'rc':make_pipeline(StandardScaler(), RidgeClassifier()),
    'rf':make_pipeline(StandardScaler(), RandomForestClassifier()),
    'gb':make_pipeline(StandardScaler(), GradientBoostingClassifier()),
    }
    
    fit_models = {}
    for algo, pipeline in pipelines.items():
        model = pipeline.fit(X_train, y_train)
        fit_models[algo] = model
    
    logger.debug("=== Alive threads ===")
    for thread in threading.enumerate():
        if thread.is_alive():
            logger.debug(f"  {thread.name} ({thread.ident})")

    rcp = fit_models['rc'].predict(X_test)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('_X test_')
        st.table(X_test.iloc[0:5])

    with col2:
        st.markdown('_y test_')
        st.table(y_test.iloc[0:5])

    with col3:
        st.markdown('_Predicción_')
        st.table(rcp[0:5])
        
    for algo, model in fit_models.items():
        yhat = model.predict(X_test)
        st.write('Modelo: ',algo, 'Accuracy Score: ', accuracy_score(y_test, yhat),'Precision Score: ',
          precision_score(y_test.values, yhat,average="weighted",pos_label="derecha"),'Recall Score: ',
          recall_score(y_test.values, yhat, average="weighted", pos_label="derecha"))

def testRidgeClassifier():
    
    df = data_rc.drop('class', axis=1) # features
    with open( model_path_1, 'rb') as f:
            self.model = pickle.load(f)    
    fit_models = {}
    for algo, pipeline in pipelines.items():
        model = pipeline.fit(X_train, y_train)
        fit_models[algo] = model
    
    logger.debug("=== Alive threads ===")
    for thread in threading.enumerate():
        if thread.is_alive():
            logger.debug(f"  {thread.name} ({thread.ident})")

    rcp = fit_models['rc'].predict(X_test)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('_X test_')
        st.table(X_test.iloc[0:5])

    with col2:
        st.markdown('_y test_')
        st.table(y_test.iloc[0:5])

    with col3:
        st.markdown('_Predicción_')
        st.table(rcp[0:5])
        
    for algo, model in fit_models.items():
        yhat = model.predict(X_test)
        st.write('Modelo: ',algo, 'Accuracy Score: ', accuracy_score(y_test, yhat),'Precision Score: ',
          precision_score(y_test.values, yhat,average="weighted",pos_label="derecha"),'Recall Score: ',
          recall_score(y_test.values, yhat, average="weighted", pos_label="derecha"))
 

    
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
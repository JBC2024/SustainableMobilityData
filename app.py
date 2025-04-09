import streamlit as st
import pandas as pd
import pydeck as pdk
import altair as alt
import functions as functions

st.cache_data.clear() # Si tienes problemas con la cache, descomenta esta linea


# Configuración inicial del proyecto
st.set_page_config(
    page_title="Sustainable Mobility Data",
    page_icon=":zap:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Carga y procesamiento de datos
df = pd.read_csv("data/red_recarga_acceso_publico_2024.csv", sep= ";")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            _profilePreview_gzau3_63 {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# Sistema de navegación
option = st.sidebar.selectbox(
    "Page:",
    ("Home", "Map", "Charts"),
)

# Lógica para navegar entre las páginas
if option == "Home":
    functions.home(df)
elif option=="Map":
    functions.map(df)
elif option=="Charts":
    functions.charts(df)
#$ pip install streamlit --upgrade
import streamlit as st
import pandas as pd
import numpy as np
import urllib.request
from PIL import Image
from datetime import datetime


st.markdown("SUNEDU - LICENCIAMIENTO INSTITUCIONAL-")    
@st.experimental_memo
def download_data():
    url ="https://raw.githubusercontent.com/Damazoisai/Codigograficos/main/Archivo%20para%20subir%20al%20github.csv"
    filename ="Archivo%20para%20subir%20al%20github.csv"
    urllib.request.urlretrieve(url,filename)
    Licenciamiento = pd.read_csv('Archivo%20para%20subir%20al%20github.csv')
    return Licenciamiento
download_data()
st.dataframe(download_data())        #lee la tabla


st.markdown("Cantidad de universidades en el peru")   
#codigo de graficos 
Licenciamiento = pd.read_csv('Archivo%20para%20subir%20al%20github.csv')
df_anho_freq = pd.DataFrame(Licenciamiento["DEPARTAMENTO"].value_counts())
st.bar_chart(df_anho_freq)
#Grafico con fechas 
start_time = st.slider("Ver universidades segun fecha",value=datetime(2010, 1, 1, 9, 30),format="DD/MM/YY - hh:mm")
st.write("Fecha seleccionada:", start_time)
start_time = st.slider(value=datetime(2010, 1, 1, 9, 30),format="DD/MM/YY - hh:mm")
st.write("Fecha seleccionada:", start_time)





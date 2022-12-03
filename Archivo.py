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
start_time = st.slider("Ver universidades segun fecha inicial",value=datetime(2000, 1, 1),format="DD/MM/YY")
st.write("Fecha seleccionada:", start_time)

#boton de link
image = Image.open('CBC.jpeg')    
if st.button(image):
    ('https://www.cayetano.edu.pe/cayetano/es/')
#if st.button("/html/body/div[2]/header/div/div/div[1]/div/a/img"):
   # ('https://www.cayetano.edu.pe/cayetano/es/')





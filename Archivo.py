#$ pip install streamlit --upgrade
import streamlit as st
import pandas as pd
import numpy as np
import urllib.request
from PIL import Image

    
@st.experimental_memo
def download_data():
    url ="https://raw.githubusercontent.com/Damazoisai/Codigograficos/main/Archivo%20para%20subir%20al%20github.csv"
    filename ="Archivo%20para%20subir%20al%20github.csv"
    urllib.request.urlretrieve(url,filename)
    Licenciamiento = pd.read_csv('Archivo%20para%20subir%20al%20github.csv')
    return Licenciamiento
download_data()
st.dataframe(download_data())        #lee la tabla
#para leer imagen 
image=Image.open("messi.jpeg")
st.image(image)


   
#codigo de graficos 
Licenciamiento = pd.read_csv('Archivo%20para%20subir%20al%20github.csv')
df_anho_freq = pd.DataFrame(Licenciamiento["Cantidad de unuviersidades licenciadas"].value_counts())
st.bar_chart(df_anho_freq)




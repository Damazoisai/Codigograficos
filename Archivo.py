#$ pip install streamlit --upgrade
import streamlit as st
import pandas as pd
import numpy as np
import urllib.request
from PIL import Image
import datetime
import matplotlib.pyplot as plt 
    
@st.experimental_memo
def df():
    url ="https://raw.githubusercontent.com/Damazoisai/Codigograficos/main/Archivo%20para%20subir%20al%20github.csv"
    filename ="Archivo%20para%20subir%20al%20github.csv"
    urllib.request.urlretrieve(url,filename)
    Licenciamiento = pd.read_csv('Archivo%20para%20subir%20al%20github.csv')
    return Licenciamiento
df()
#st.dataframe(download_data())        lee la tabla
#para leer imagen 
image=Image.open("messi.jpeg")
st.image(image)

   
#codigo de graficos 
#chart_data = pd.DataFrame(np.random.randn(20, 3),columns=["a", "b", "c"])
#st.bar_chart(chart_data)




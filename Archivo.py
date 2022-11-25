#$ pip install streamlit --upgrade
import streamlit as st
import urllib.request
import pandas as pd
import numpy as np
st.header("Licenciamiento institucional")
@st.experimental_memo

def download_data():
   url="https://www.datosabiertos.gob.pe/sites/default/files/Licenciamiento%20Institucional_7.csv"
   filename="Licenciamiento_institucional.xlsx"
   urllib.request.urlretrieve(url,filename)
   df=pd.read_csv('Licenciamiento_institucional.xlsx')
   return df
c=download_data()
st.write('Dimensiones: ' + str(c.shape[0]) + ' filas y ' + str(c.shape[1]) + ' columnas')
st.dataframe(c)
st.subheader("Características del Dataset")
st.write(c.describe())

st.title('Contaminantes') 

#url del archivo en formato raw
url = 'https://raw.githubusercontent.com/brigytt/G_PROGRA/main/Catalogo1960_2021.csv'
datos = pd.read_csv(url,sep= ',')
st.line_chart(data=datos, x='FECHA_UTC', y='MAGNITUD')



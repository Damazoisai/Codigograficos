#$ pip install streamlit --upgrade
import streamlit as st
import pandas as pd
import numpy as np
import urllib.request

#URL del archivo en formato raw
#url ='https://raw.githubusercontent.com/ximenarojo/prueba/main/Licenciamiento%20Institucional_2.csv'
#Descargar y leer el archivo y considerar las comas como separadores
#datos = pd.read_csv(url, sep=',')
#st.line_chart(data=datos, x='NOMBRE', y='ESTADO_LICENCIAMIENTO')


    
@st.experimental_memo
def download_data():
    url ="https://github.com/Damazoisai/Codigograficos/blob/main/Licenciamiento%20Institucional_7.csv"
    filename ="Licenciamiento%20Institucional_7.csv"
    urllib.request.urlretrieve(url,filename)
    df_LI = pd.read_csv('Licenciamiento%20Institucional_7.csv')
return df_LI

download_data()
st.dataframe(download_data())
st.caption('Para mayor información acceder a: https://www.datosabiertos.gob.pe/dataset/sunedu-licenciamiento-institucional')
    
#codigo de graficos 
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)

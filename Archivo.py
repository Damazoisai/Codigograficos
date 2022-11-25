#$ pip install streamlit --upgrade
import streamlit as st
import pandas as pd
import numpy as np
import urllib.request
    
@st.experimental_memo
def download_data():
    url ="https://github.com/Damazoisai/Codigograficos/blob/main/Licenciamiento%20Institucional.xlsx"
    filename ="Licenciamiento%20Institucional.xlsx"
    urllib.request.urlretrieve(url,filename)
    Licenciamiento = pd.read_xlxs('Licenciamiento%20Institucional.xlsx')
    return Licenciamiento
download_data()
   
#codigo de graficos 
chart_data = pd.DataFrame(np.random.randn(20, 3),columns=["a", "b", "c"])
st.bar_chart(chart_data)

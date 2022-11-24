# Codigograficos
import streamlit as st
import pandas as pd
import numpy as np
import urllib.request

@st.experimental_menu
def download_data():
  url= 'https://www.datosabiertos.gob.pe/dataset/sunedu-licenciamiento-institucional/resource/b582532d-3202-4de3-a7ea-b35bd97f7079'
  filename='data.csv'
  urllib.request.urlretrieve(url,filename)
download_data()



import pandas as pd
import datetime
import matplotlib.pyplot as plt 
archivo = 'https://raw.githubusercontent.com/Damazoisai/Codigograficos/main/Archivo%20para%20subir%20al%20github.csv'

df = pd.read_csv(archivo, sheet_name='Archivo%20para%20subir%20al%20github.csv')

df
#Genera el grafico
df = df.dropna()
df = df.reset_index(drop=True)
df

fechas = df["FECHA_INICIO_LICENCIAMIENTO"]
periodo = df["PERIODO_LICENCIAMIENTO"]
x=[datetime.datetime.strptime(str(date), '%Y-%m-%d %H:%M:%S').date() for date in fechas]

y=periodo

plt.barh(x,y)
plt.gcf().set_size_inches(15, 5)
plt.title("FECHA_INICIO_LICENCIAMIENTO vs PERIODO_LICENCIAMIENTO")
plt.xlabel("FECHA_INICIO_LICENCIAMIENTO")
plt.ylabel("PERIODO_LICENCIAMIENTO")
plt.grid(axis = 'x')
plt.show()

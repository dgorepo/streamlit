# #############################  IMPORTANDO MODULOS ############################# #
import pathlib
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
from dms2dec.dms_convert import dms2dec


# #############################  CLASSE PARA GRAFICOS ########################### #
class Grafico:
    def gera_grafico(self):
        pass



# #############################  CARREGANDO DATASETS ############################# #



# --- MAPA DE BARRAGENS NO BRASIL ------------------------------------------------ #

df = pd.read_csv('diego_autuacao_analise_2.csv',delimiter=',')
df.columns = ['id','lat','lon']
df.drop('id', axis=1, inplace=True)
df['lat'] = df['lat'].map(lambda x: x.rstrip('\\"'))
df['lon'] = df['lon'].map(lambda x: x.rstrip('\\"'))
df['lat'] = df.lat.apply(lambda x: x+"S" if x.startswith("-") else x+"N")
df['lon'] = df.lon.apply(lambda x: x+"W" if x.startswith("-") else x+"E")
df['lat'] = df['lat'].map(lambda x: x.lstrip('-'))
df['lon'] = df['lon'].map(lambda x: x.lstrip('-'))
df['lat'] = df.lat.apply(lambda x: dms2dec(x) if x.startswith("-") else dms2dec(x))
df['lon'] = df.lon.apply(lambda x: dms2dec(x) if x.startswith("-") else dms2dec(x))
df_barragens_brasil = df







# #############################  CORPO DA PAGINA ############################# #



# Titulo da pagina
st.title("Mineração")
# Divisor
st.markdown('---')
# Nome do grafico
st.markdown('### Conhecendo o setor ')

# Grafico conhecendo o setor
col1, col2, col3 = st.columns(3)
col1.metric("Mineradoras", "275")
col2.metric("Barragens", "907", "643")
col3.metric("Minérios", "255")
    

st.markdown('---')
# Titulo grafico
st.markdown('### Barragens no Brasil')
st.markdown('Mapa interativo mostra a distribuição de barragens no Brasil')

# Mapa de barragens
st.map(df_barragens_brasil)

    
    

    

st.markdown('----')
st.sidebar.markdown('BC8 Engenharia de Dados')
st.sidebar.markdown('SoulCode')



#st.write(pydicom)

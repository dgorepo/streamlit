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


# --- TOP 10 EMPRESAS AUTUADAS --------------------------------------------------- #
top10_autuacao_file = 'part-00000-c8ab9c0f-2156-4d7c-b5f3-32b5b2b55f2e-c000.csv'
df_top10_autuacao = pd.read_csv(top10_autuacao_file)
primeira_linha = df_top10_autuacao.columns
df_top10_autuacao.iloc[0, :] = primeira_linha
df_top10_autuacao.columns = ['Empresa','Quantidade']
df_top10_autuacao['Quantidade'] = pd.to_numeric(df_top10_autuacao['Quantidade'])


# --- SERIE HISTORICA DISTRIBUICAO ----------------------------------------------- #
filename = 'diego_distribuicao_analise_4.csv'
df = pd.read_csv(filename)
df.drop(df.columns[0], axis=1, inplace=True)
df = df.sort_values('mes')
df_serie_historica_distribuicao = df





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

    
st.markdown('---')
# Nome do grafico
st.markdown('### Produção de Ferro ')
st.markdown('Produção de Ferro no Brasil (em toneladas)')



fig = px.line(df, range_x=[1,12], x='mes', y='valor', color='substancia', labels = { "mes": "Ano 2020", "count": "Vendas", "substancia": "Ferro" }, title = '',)
meses = ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
fig.update_xaxes(tickangle=-45, dtick=1, visible=True, fixedrange=False)
fig.update_yaxes(dtick=10000, visible=True, fixedrange=False)
fig.update_layout(xaxis = dict(tickmode = 'array', tickvals = [1,2,3,4,5,6,7,8,9,10,11,12], ticktext = meses))


st.plotly_chart(fig)

    
    
st.markdown('---')
# Titulo grafico
st.markdown('### Ranking de autuação')
st.markdown('Lista das empresas mais autuadas no Brasil')


fig = px.bar(df_top10_autuacao, x='Empresa', y='Quantidade')
st.plotly_chart(fig)
    

    

st.markdown('---')
st.sidebar.markdown('BC8 Engenharia de Dados')
st.sidebar.markdown('SoulCode')



#st.write(pydicom)

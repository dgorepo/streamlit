# #############################  IMPORTANDO MODULOS ############################# #
import pathlib
import pandas as pd
import numpy as np
import streamlit as st
#!pip install dms2dec
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






# #############################  CORPO DA PAGINA ############################# #


base = "dark"


menu = st.sidebar.selectbox ('Selecione uma opção', ['Conhecendo o setor', 'Barragens pelo Brasil', 'Ranking de autuação'])


# --- CONHECENDO O SETOR ---------------------------------------------------------- #
if menu == 'Conhecendo o setor':

    # Path do site
    st.write(pathlib.Path.home())
    # Titulo da pagina
    st.title("Mineração")
    # Subtitulo da pagina
    st.header('Bootcamp de Engenharia de Dados SoulCode')
    # Divisor
    st.markdown('---')
    # Nome do grafico
    st.markdown('### Conhecendo o setor ')

    # Grafico conhecendo o setor
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")
    
    
# --- MAPA DE BARRAGENS NO BRASIL ------------------------------------------------ #
elif(menu=='Barragens pelo Brasil'):

    # Path do site
    st.write(pathlib.Path.home())
    # Titulo da pagina
    st.title("Mineração")
    # Subtitulo da pagina
    st.header('Bootcamp de Engenharia de Dados SoulCode')
    # Divisor
    st.markdown('---')
    # Titulo grafico
    st.markdown('### Barragens no Brasil')
    st.markdown('Mapa interativo mostra a distribuição de barragens no Brasil')
    
    # Mapa de barragens
    st.map(df_barragens_brasil)


# --- TOP 10 EMPRESAS AUTUADAS --------------------------------------------------- #
elif(menu=='Ranking de autuação'):
    
    # Path do site
    st.write(pathlib.Path.home())
    # Titulo da pagina
    st.title("Mineração")
    # Subtitulo da pagina
    st.header('Bootcamp de Engenharia de Dados SoulCode')
    # Divisor
    st.markdown('---')
    # Titulo grafico
    st.markdown('### Empresas mais autuadas')
    st.markdown('Lista das empresas mais autuadas no Brasil')

    
    colunas = df_top10_autuacao.columns.tolist()
    
    #chart_data = pd.DataFrame(np.random.randn(50, 3),columns=colunas)
    st.bar_chart(df_top10_autuacao['Valores'])
    #st.bar_chart(df_top10_autuacao)
    
    
    # Tabela com as top 10 empresas em autuacao
    #st.dataframe(df_top10_autuacao)  # Same as st.write(df)
    

st.markdown('---')
st.sidebar.write("<br><br><br>")
st.sidebar.markdown('BC8 Engenharia de Dados')

st.sidebar.markdown("- [Diego](https://www.linkedin.com/in/gabriel-marcial-6ba93a1a1/)")
st.sidebar.markdown("- [Rafael](https://www.linkedin.com/in/gabriel-marcial-6ba93a1a1/)")
st.sidebar.markdown("- [Rayssa](https://www.linkedin.com/in/gabriel-marcial-6ba93a1a1/)")
st.sidebar.markdown("- [Sandi](https://www.linkedin.com/in/gabriel-marcial-6ba93a1a1/)")



#st.write(pydicom)

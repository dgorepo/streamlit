
import pathlib
import pandas as pd
import numpy as np
import streamlit as st



analysis = st.sidebar.selectbox ('Selecione uma opção', ['Classificação da imagem', 'Análise e visualização de dados'])
if analysis == 'Análise e visualização de dados':

    st.markdown('---')

    st.markdown('### Streamlit is ')

    df = pd.DataFrame(
         np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
         columns=['lat', 'lon'])

    st.map(df)
else:

    st.markdown('### Streamlit is ')

    df = pd.DataFrame(
        np.random.randn(50, 20),
        columns=('col %d' % i for i in range(20)))

    st.dataframe(df)  # Same as st.write(df)
    st.markdown('---')





st.write(pathlib.Path.home())

st.title("Mineração")
st.header('Bootcamp de Engenharia de Dados SoulCode')


st.markdown('---')

st.markdown('### Streamlit is ')


col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")



st.markdown('---')

st.markdown('### Streamlit is ')

Email = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(Email)


st.markdown('---')


#st.write(pydicom)

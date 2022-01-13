
import pathlib
import pandas as pd
import numpy as np
import streamlit as st



add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

st.write(pathlib.Path.home())

st.title("Mineração")
st.header('Bootcamp de Engenharia de Dados SoulCode')



df = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
     columns=['lat', 'lon'])

st.map(df)


st.header('Bootcamp de Engenharia de Dados SoulCode')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.header('Bootcamp de Engenharia de Dados SoulCode')

df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)


#st.write(pydicom)

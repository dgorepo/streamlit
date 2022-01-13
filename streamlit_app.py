
import pathlib
import pandas as pd
import numpy as np
import streamlit as st



add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)



st.title("Mineração")
st.header('Bootcamp de Engenharia de Dados SoulCode')


st.write(pathlib.Path.home())


df = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
     columns=['lat', 'lon'])

st.map(df)


#st.write(pydicom)

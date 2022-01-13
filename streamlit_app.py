
import pathlib
import pandas as pd
import numpy as np
import streamlit as st




top10_autuacao_file = 'part-00000-c8ab9c0f-2156-4d7c-b5f3-32b5b2b55f2e-c000.csv'
df_top10_autuacao = pd.read_csv(top10_autuacao_file)
new_line = df_top10_autuacao.columns
df_top10_autuacao.iloc[0, :] = new_line
df_top10_autuacao.columns = ['Empresa','Quantidade']
df_top10_autuacao['Quantidade'] = pd.to_numeric(df_top10_autuacao['Quantidade'])



# menu
menu = st.sidebar.selectbox ('Selecione uma opção', ['menu 1', 'Análise e visualização de dados'])
if menu == 'menu 1':

    st.write(pathlib.Path.home())

    st.title("Mineração")
    st.header('Bootcamp de Engenharia de Dados SoulCode')
    
    st.markdown('---')

    st.markdown('### Streamlit is ')

    df = pd.DataFrame(
         np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
         columns=['lat', 'lon'])

    st.map(df)
else:

    
    st.write(pathlib.Path.home())

    st.title("Mineração")
    st.header('Bootcamp de Engenharia de Dados SoulCode')
    
    
    st.markdown('### Streamlit is ')

    df = pd.DataFrame(
        np.random.randn(50, 20),
        columns=('col %d' % i for i in range(20)))

    st.dataframe(df)  # Same as st.write(df)
    st.markdown('---')


    
    
    
st.markdown('---')

st.markdown('### Top 10 empresas em autuacao ')
#ax = df_top10_autuacao.plot.bar(x='Empresa',y='Quantidade', rot=0)
df = pd.DataFrame({'lab':['A', 'B', 'C'], 'val':[10, 30, 20]})
ax = df.plot.bar(x='lab', y='val', rot=0)

#st.bar_chart(df_top10_autuacao)
    



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

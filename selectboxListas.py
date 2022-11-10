import pandas as pd
import streamlit as st

st.title('Filtrado con lista desplegable')
names_link = 'dataset.csv'

@st.cache
def load_data():   
    df = pd.read_csv(names_link)
    return df

@st.cache
def load_data_porsexo(sexo):   
    df = pd.read_csv(names_link)
    df = df[df['sex'] == sexo]
    return df

datos = load_data()
selected_sex = st.selectbox('Selecciona sexo', datos['sex'].unique())
btnFiltrarSexo = st.button('Filtrar por sexo')


if (btnFiltrarSexo):
    df_sexo = load_data_porsexo(selected_sex)
    num_renglones = df_sexo.shape[0]
    st.write(f'Total nombres: {num_renglones}')
    st.dataframe(df_sexo)

import pandas as pd
import streamlit as st

st.title('Leer CSV, entrada de datos y algo de procesamiento')

names_link = 'dataset.csv'

@st.cache
def load_data(nombre):
    df = pd.read_csv(names_link)
    df = df[df['name'].str.contains(nombre)]
    return df

nombre = st.text_input('Nombre: ')
if (nombre):
    df_datos = load_data(nombre)
    num_renglones = df_datos.shape[0]
    st.write(f'Total nombres: {num_renglones}')
    st.dataframe(df_datos)

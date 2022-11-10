import pandas as pd
import streamlit as st

st.title('Read CSV')

names_link = 'dataset.csv'
#names_data = pd.read_csv(names_link)
#lo haremos con una función de caché

@st.cache
def load_data(nrows=10000000):
    return pd.read_csv(names_link, nrows=nrows)

texto_avance_lectura = st.text('Leyendo datos...')
names_data = load_data(500)
texto_avance_lectura.text('Listo, leído de caché '+str(names_data.shape[0])+
                        ' Renglones')

st.dataframe(names_data)
import pandas as pd
import streamlit as st

st.title('CSV, entrada de datos y botones')
names_link = 'dataset.csv'

@st.cache
def load_data(idInicio, idFinal):
    idInicio = int(idInicio)
    idFinal = int(idFinal)
    df = pd.read_csv(names_link)
    df = df[(df['index']>=idInicio) & (df['index']<=idFinal)]
    return df

idInicio = st.text_input('Indice inicial')
idFinal = st.text_input('Indice final')
btnRango = st.button('Busca rango')
if (btnRango):
    df_datos = load_data(int(idInicio), int(idFinal))
    num_renglones = df_datos.shape[0]
    st.write(f'Total nombres: {num_renglones}')
    st.dataframe(df_datos)

import pandas as pd
import streamlit as st

st.title('Read CSV')

# names_link = 'dataset.csv'
# Leeremos los datos de github
names_link = 'https://raw.githubusercontent.com/FranciscoJHernandezP/streamlit_lab/master/dataset.csv?token=GHSAT0AAAAAABZZ6VTIR5FSXM3IL7HSK4BQY3NHMOA'
# Ojo!!!! se pierde el token y hay que actualizar
#names_data = pd.read_csv(names_link)
#lo haremos con una función de caché

@st.cache
def load_data(nrows=10000000):
    return pd.read_csv(names_link, nrows=nrows)

# Leemos el archivo de datos csv
texto_avance_lectura = st.text('Leyendo datos...')
names_data = load_data()
texto_avance_lectura.text('Listo, leído de caché '
                            +str(names_data.shape[0])+
                            ' renglones')

# Desplegamos nuestro DataFrame
st.dataframe(names_data)
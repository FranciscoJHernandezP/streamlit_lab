import pandas as pd
import streamlit as st

def bienvenida(nombre):
    mimensaje = 'bienvanid@ '+nombre+'!!!'
    return mimensaje

minombre = st.text_input('Nombre:')
if (minombre):
    mensaje = bienvenida(minombre)
    st.write(f'{mensaje}')
    st.write(mensaje)



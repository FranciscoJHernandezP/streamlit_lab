import streamlit as st

minombre = st.text_input('Teclea tu nombre:')

if st.button('Buscar...'):
    st.write(f'Buscar {minombre}')


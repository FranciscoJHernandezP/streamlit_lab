import streamlit as st
import pandas as pd
import numpy as np

st.title("Título principal")
sidebar = st.sidebar
sidebar.title('Título de la barra')

if sidebar.checkbox('Show Dataframe'):
    chart_data = pd.DataFrame(np.random.randn(20,3),
                columns = ('C1', 'C2', 'C3'))
    st.dataframe(chart_data)



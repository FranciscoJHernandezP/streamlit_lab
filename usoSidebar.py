import streamlit as st
import pandas as pd
import numpy as np

st.title("Mi Primera App con Streamlit")
sidebar = st.sidebar
sidebar.header("Esta es la barra lateral.")

if sidebar.checkbox('Show Dataframe'):
    chart_data = pd.DataFrame(np.random.randn(20,3),
                columns = ('C1', 'C2', 'C3'))
    st.dataframe(chart_data)



# st.title('Uso Sidebar')
# sidebar = st.sidebar
# sidebar.title('Título barra lateral')
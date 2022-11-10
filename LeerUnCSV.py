import pandas as pd
import streamlit as st

names_link = 'dataset.csv'
names_data = pd.read_csv(names_link)

st.title('Read CSV')

st.dataframe(names_data)
import plotly.express as px
import streamlit as st
import pandas as pd

df = px.data.gapminder()
st.write(df)

year_options = df['year'].unique().tolist()
year = st.selectbox('Select year to see:', year_options,0)
df = df[df['year'] == year]
fig = px.scatter(df, x='gdpPercap', y = 'lifeExp', size='pop', 
        color='continent', hover_name='continent',
        log_x = True)
st.write(fig)

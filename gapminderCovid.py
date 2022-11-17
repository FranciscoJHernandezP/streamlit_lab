import plotly.express as px
import streamlit as st
import pandas as pd

df = px.data.gapminder()
year_options = df['year'].unique().tolist()


covid=pd.read_csv('https://raw.githubusercontent.com/shinokada/covid-19-stats/master/data/daily-new-confirmed-cases-of-covid-19-tests-per-case.csv')
covid.columns = ['Country', 'Code','Date','Confirmed','Days since confirmed']
covid['Date'] = pd.to_datetime(covid['Date']).dt.strftime('%Y-%m-%d')
country_options = covid['Country'].unique().tolist()
date_options = covid['Date'].unique().tolist()


st.write(df)
st.write(covid)



add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)
year = st.sidebar.selectbox('Which year would you like to see?', year_options, 0)
df = df[df['year']==year]

fig = px.scatter(df, x="gdpPercap", y="lifeExp",
			size="pop", color="continent", hover_name="continent",
			log_x=True, size_max=55, range_x=[100,100000], range_y=[25,50])

fig.update_layout(width=400)

st.write(fig)


with st.sidebar.form("test_form"):
   st.write("Inside the form")
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)

container1 = st.container()

with st.form("covid_form"):
	date = st.selectbox('Which date would like to see', date_options, 100)
	country = st.multiselect('Which country would like to see', country_options, ['Brazil'])
	submitted = st.form_submit_button("Submit")
	if submitted:
		covid = covid[covid['Date']==date]
		covid = covid[covid['Country'].isin(country)]
		st.write("Date", date, "Country", country)
		fig2 = px.bar(covid, x="Country", y="Confirmed", color="Country", range_y=[0,35000])
		fig2.update_layout(width=400)
		container1.write(fig2)


with st.sidebar.form("covid_form_sidebar"):
	date = st.selectbox('Which date would like to see', date_options, 100)
	country = st.multiselect('Which country would like to see', country_options, ['Brazil'])
	submitted = st.form_submit_button("Submit")
	if submitted:
		covid = covid[covid['Date']==date]
		covid = covid[covid['Country'].isin(country)]
		st.write("Date", date, "Country", country)
		fig2 = px.bar(covid, x="Country", y="Confirmed", color="Country", range_y=[0,35000])
		fig2.update_layout(width=400)
		container1.write(fig2)
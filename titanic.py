import streamlit as st
import pandas as pd
import datetime

titanic_link = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
titanic_data = pd.read_csv(titanic_link)


# Create the title for the web app
st.title("My First Streamlit App")
sidebar = st.sidebar
sidebar.title("This is the sidebar.")
sidebar.write("You can add any elements to the sidebar.")

# ask user the current date
today = datetime.date.today()
today_date = sidebar.date_input('Current date', today)
st.success(f'Current date: {today_date}')
# Display the content of the dataset if checkbox is true
st.header("Dataset")
agree = sidebar.checkbox("show DataSet Overview ? ")
if agree:
    st.dataframe(titanic_data)

st.header("Data Description")
selected_class = sidebar.radio("Select Class", titanic_data['class'].unique())
sidebar.write("Selected Class:", selected_class)
st.markdown("___")
selected_sex = sidebar.selectbox("Select Sex", titanic_data['sex'].unique())
sidebar.success(f"Selected Option: {selected_sex!r}")
st.markdown("___")
optionals = sidebar.expander("Optional Configurations", True) 
fare_select = optionals.slider( "Select the Fare",
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
)
subset_fare = titanic_data[(titanic_data['fare'] >= fare_select)]
st.write(f"Number of Records With Fare greater than {fare_select}: {subset_fare.shape[0]}")
st.dataframe(subset_fare)
st.markdown("________")

conten1 = st.container()
with conten1:
    cols = st.columns(3)


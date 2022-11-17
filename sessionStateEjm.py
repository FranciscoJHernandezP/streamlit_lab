import streamlit as st
import datetime 

st.title('Ejemplo Session State')

if 'count' not in st.session_state:
    st.session_state['count'] = 0
    st.session_state['last_update'] = datetime.time(0,0)

def update_counter():
    st.session_state['count']+=st.session_state.increment_value
    st.session_state['last_update'] = st.session_state.update_time

with st.form(key='forma1'):
    st.time_input(label='Enter the time', value=datetime.datetime.now().time(), 
                    key='update_time')
    st.number_input('Enter a value', value=0, step=1, key='increment_value')
    submit = st.form_submit_button(label = 'update', on_click = update_counter)

st.write('Current count = ', st.session_state['count'])
st.write('Last updated = ', st.session_state['last_update'])
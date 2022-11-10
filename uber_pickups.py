# Streamlit is more than just a way to make data apps, 
# it’s also a community of creators that share their apps 
# and ideas and help each other make their work better. 
# Please come join us on the community forum. 
# We love to hear your questions, ideas, and help you work 
# through your bugs — stop by today!
# The first step is to create a new Python script. 
# Let's call it uber_pickups.py.
# Open uber_pickups.py in your favorite IDE or text editor, 
# then add these lines:

import streamlit as st
import pandas as pd
import numpy as np

# Every good app has a title, so let's add one:

st.title('Uber pickups in NYC')

#Now it's time to run Streamlit from the command line:

#streamlit run uber_pickups.py

#Running a Streamlit app is no different than any other Python script. Whenever you need to view the app, you can use this command.

#Did you know you can also pass a URL to streamlit run? This is great when combined with Github Gists. For example:

# $ streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py

# As usual, the app should automatically open in a new tab in your browser.

# Fetch some data
# Now that you have an app, the next thing you'll 
# need to do is fetch the Uber dataset for pickups 
# and drop-offs in New York City.

# Let's start by writing a function to load the data. 
# Add this code to your script:

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# You'll notice that load_data is a plain old function 
# that downloads some data, puts it in a Pandas dataframe, 
# and converts the date column from text to datetime. The 
# function accepts a single parameter (nrows), which 
# specifies the number of rows that you want to load into 
# the dataframe.

# Now let's test the function and review the output. 
# Below your function, add these lines:

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data (using @st.cache)...done!')
# You'll see a few buttons in the upper-right corner of your app asking if you'd like to rerun the app. Choose Always rerun, and you'll see your changes automatically each time you save.

# Ok, that's underwhelming...

# It turns out that it takes a long time to download data, 
# and load 10,000 lines into a dataframe. Converting the 
# date column into datetime isn’t a quick job either. You 
# don’t want to reload the data each time the app is updated – 
# luckily Streamlit allows you to cache the data.

# Inspect the raw data
# It's always a good idea to take a look at the raw data you're 
# working with before you start working with it. Let's add a 
# subheader and a printout of the raw data to the app:

# st.subheader('Raw data')
# st.write(data)

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


# In the Main concepts guide you learned that st.write 
# will render almost anything you pass to it. In this 
# case, you're passing in a dataframe and it's rendering 
# as an interactive table.

# st.write tries to do the right thing based on the data 
# type of the input. If it isn't doing what you expect you 
# can use a specialized command like st.dataframe instead. 
# For a full list, see API reference.


# Draw a histogram
# Now that you've had a chance to take a look at the 
# dataset and observe what's available, let's take 
# things a step further and draw a histogram to see 
# what Uber's busiest hours are in New York City.

# To start, let's add a subheader just below the 
# raw data section:

st.subheader('Number of pickups by hour')

# Use NumPy to generate a histogram that breaks down 
# pickup times binned by hour:

hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

# Now, let's use Streamlit's st.bar_chart() method 
# to draw this histogram.

st.bar_chart(hist_values)

# Save your script. This histogram should show up in your 
# app right away. After a quick review, it looks like the 
# busiest time is 17:00 (5 P.M.).

# To draw this diagram we used Streamlit's native bar_chart() 
# method, but it's important to know that Streamlit supports 
# more complex charting libraries like Altair, Bokeh, Plotly, 
# Matplotlib and more. For a full list, see supported charting 
# libraries.

# Plot data on a map
# Using a histogram with Uber's dataset helped us 
# determine what the busiest times are for pickups, 
# but what if we wanted to figure out where pickups 
# were concentrated throughout the city. While you 
# could use a bar chart to show this data, it wouldn't 
# be easy to interpret unless you were intimately 
# familiar with latitudinal and longitudinal coordinates
#  in the city. To show pickup concentration, let's use 
# Streamlit st.map() function to overlay the data on a 
# map of New York City.

# Add a subheader for the section:

st.subheader('Map of all pickups')

# Use the st.map() function to plot the data:

st.map(data)

# Save your script. The map is fully interactive. Give it a try by panning or zooming in a bit.

# After drawing your histogram, you determined that the busiest hour for Uber pickups was 17:00. Let's redraw the map to show the concentration of pickups at 17:00.

# Locate the following code snippet:

# st.subheader('Map of all pickups')
# st.map(data)

# Replace it with:

hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)

# You should see the data update instantly.

# To draw this map we used the st.map function that's built 
# into Streamlit, but if you'd like to visualize complex map 
# data, we encourage you to take a look at the st.pydeck_chart.
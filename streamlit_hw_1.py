import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd
import altair as alt
from vega_datasets import data

st.header('Homework 1')

st.markdown(
"**QUESTION 1**: In previous homeworks you created dataframes from random numbers.\n"
"Create a datframe where the x axis limit is 100 and the y values are random values.\n"
"Print the dataframe you create and use the following code block to help get you started"
)

st.code(

''' 
x_limit = 100

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange(0,x_limit,1)

# Create a random array of data that we will use for our y values
y_data = np.random.randint(100, x_limit)

df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)''',language='python')

x_limit = 100
# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange(0,x_limit,1)

# Create a random array of data that we will use for our y values
#y_data = np.random.randint(1,101, x_limit)
y_data = [random.random() for value in x_axis]

df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)


st.markdown(
"**QUESTION 2**: Using the dataframe you just created, create a basic scatterplot and Print it.\n"
"Use the following code block to help get you started."
)

st.code(
''' 
scatter = alt.Chart().mark_point().encode()

st.altair_chart(scatter, use_container_width=True)''',language='python')

scatter = alt.Chart(df).mark_circle().encode(x='x', y='y')

st.altair_chart(scatter, theme = "streamlit", use_container_width=True)


st.markdown(
"**QUESTION 3**: Lets make some edits to the chart by reading the documentation on Altair.\n"
"https://docs.streamlit.io/library/api-reference/charts/st.altair_chart.  "
"Make 5 changes to the graph, document the 5 changes you made using st.markdown(), and print the new scatterplot.  \n"
"To make the bullet points and learn more about st.markdown() refer to the following discussion.\n"
"https://discuss.streamlit.io/t/how-to-indent-bullet-point-list-items/28594/3"
)

st.markdown("The five changes I made were.....")
st.markdown("""
The 5 changes I made were:
- Made a streamlit theme
- Made it Interactive 
- Made it a circle
- Change color
- Change 5
""")



st.markdown(
"**QUESTION 4**: Explore on your own!  Go visit https://altair-viz.github.io/gallery/index.html.\n "
"Pick a random visual, make two visual changes to it, document those changes, and plot the visual.  \n"
"You may need to pip install in our terminal for example pip install vega_datasets "
)


source = data.seattle_weather()

line = alt.Chart(source).mark_line(
    color='purple',
    size=3
).transform_window(
    rolling_mean='mean(temp_max)',
    frame=[-20, 20]
).encode(
    x='date:T',
    y='rolling_mean:Q'
)

points = alt.Chart(source).mark_point().encode(
    x='date:T',
    y=alt.Y('temp_max:Q',
            axis=alt.Axis(title='Max Temp'))
)

points+line


#New Chart here
source1 = data.iris()

iris_chart = alt.Chart(source1).transform_fold(
    ['petalWidth',
     'petalLength',
     'sepalWidth',
     'sepalLength'],
    as_ = ['Measurement_type', 'value']
).transform_density(
    density='value',
    bandwidth=0.3,
    groupby=['Measurement_type'],
    extent= [0, 8],
    counts = True,
    steps=200
).mark_area().encode(
    alt.X('value:Q'),
    alt.Y('density:Q', stack='zero'),
    alt.Color('Measurement_type:N')
).properties(width=400, height=100)


iris_chart

st.markdown("""
The 2 changes I made were:
- Change 1
- Change 2
"""
)


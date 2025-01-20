import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd

df = px.data.gapminder()

fig = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
                 size="pop", color="continent", hover_name="country",
                 log_x=True, size_max=55, range_x=[100, 100000], range_y=[25, 90])
st.plotly_chart(fig)


# what do animation groupes do?
fig2 = px.scatter(
    data_frame=df,
    x='lifeExp',
    y='gdpPercap',
    animation_frame='year',
    range_x=[30, 90],
    range_y=[-2000, 60000],
    hover_name="country",
    color="continent"
)
st.plotly_chart(fig2)




# Generate sample data for time series in 3D
np.random.seed(42)  # For reproducibility
num_time_steps = 50
num_points = 100

time_steps = np.arange(num_time_steps)
x_coords = np.random.rand(num_points, num_time_steps) * 10
y_coords = np.random.rand(num_points, num_time_steps) * 10
z_coords = np.random.rand(num_points, num_time_steps) * 10


data = []
for time_step in time_steps:
   for i in range(num_points):
     data.append({
        'time': time_step,
        'x': x_coords[i, time_step],
        'y': y_coords[i, time_step],
        'z': z_coords[i, time_step],
        'id': i
     })

df = pd.DataFrame(data)


# Create Animated 3D Scatter Plot
fig = px.scatter_3d(
    df,
    x="x",
    y="y",
    z="z",
    animation_frame="time",
    range_x=[0, 10],  # Set x-axis range
    range_y=[0, 10],  # Set y-axis range
    range_z=[0, 10],  # Set z-axis range
    title="Animated 3D Time Series Scatter Plot",
    labels={"x": "X-Coordinate", "y": "Y-Coordinate", "z": "Z-Coordinate"},
    hover_name='id'
)

fig.update_traces(marker=dict(size=5))

st.plotly_chart(fig)
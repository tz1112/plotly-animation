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
import pandas as pd
import numpy as np
import plotly.express as px

t = np.linspace(0, 10, 50)
x, y, z = np.cos(t), np.sin(t), t

df = pd.DataFrame({
    "time" : z,
    "x" : x,
    "y" : y,
    "z" : z,
    "label" : "A" 
})

df.loc[df.tail(25).index, 'label'] = "B"

data = []
history = []

for index, elem in df.iterrows():  
    data_point = elem
    # BEGIN dummy (we need to add dummies, otherwise the tail does not work)
    data.append({"time" : data_point["time"], "x" : -1, "y" : -1, "z" : -1, "label" : "A" 
    })
    data.append({"time" : data_point["time"], "x" : -1, "y" : -1, "z" : -1, "label" : "B" 
    })
    data.append({"time" : data_point["time"], "x" : -1, "y" : -1, "z" : -1, "label" : "C" 
    })
    # END dummy
    data.append(data_point)
    history.append(data_point)

    for elem in history[-9:]:
        data.append({
            "time" : data_point["time"],
            "x" : elem["x"],
            "y" : elem["y"],
            "z" : elem["z"],
            "label" : elem["label"]
        })


df = pd.DataFrame(data[1:])
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#     print(df)


fig = px.scatter_3d(
    df,
    x="x",
    y="y",
    z="z",
    animation_frame="time",
    range_x=[-1, 1], 
    range_y=[-1 , 1],
    range_z=[0,10], 
    title="Animated 3D Time Series Scatter Plot",
    labels={"x": "X-Coordinate", "y": "Y-Coordinate", "z": "Z-Coordinate"},
    color="label",
    color_discrete_map={
                "A": "red",
                "B": "green",
                "C": "blue"}            
)

fig.update_traces(marker=dict(size=5))
fig.layout.scene.aspectratio = {'x':1, 'y':1, 'z':1}
# fig.update_scenes(xaxis_visible=False, yaxis_visible=False,zaxis_visible=False )
fig.update_layout(scene = dict(xaxis = dict(showgrid = False,showticklabels = False),
                                   yaxis = dict(showgrid = False,showticklabels = False),
                                   zaxis = dict(showgrid = False,showticklabels = False)
             ))
fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 50
fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 50
st.plotly_chart(fig)



st.divider()

# 2d 3d selector

import plotly.express as px
df = px.data.iris()

col1, col2 = st.columns(2)

with col1:
    x_axis = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    y_axis = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    z_axis = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

    selection_x = st.segmented_control("X-AXIS", x_axis, selection_mode="single", key="selection_x", label_visibility="collapsed")
    selection_y = st.segmented_control("Y-AXIS", y_axis, selection_mode="single", key="selection_y", label_visibility="collapsed")
    selection_z = st.segmented_control("Z-AXIS", z_axis, selection_mode="single", key="selection_z")

with col2:
    color = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    selection_color = st.segmented_control("COLOR", color, selection_mode="single", key="color")
    marker_size = st.slider("Marker size", 1, 10, 3)

if(selection_x is not None and selection_y is not None and selection_z is None):
    fig = px.scatter(df, x=selection_x, y=selection_y, color=selection_color)
    fig.update_traces(marker=dict(size=marker_size))
    st.plotly_chart(fig)
else:
    if (selection_x is not None and selection_y is not None and selection_z and not None):
        fig = px.scatter_3d(df, x=selection_x, y=selection_y, z=selection_z, color=selection_color)
        fig.update_traces(marker=dict(size=marker_size))
        st.plotly_chart(fig)

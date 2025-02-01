import streamlit as st
import plotly.express as px
from pygwalker.api.streamlit import StreamlitRenderer

st.set_page_config(layout="wide")

df = px.data.iris()
df["manual_index"] = df.index

fig = px.scatter_matrix(df, dimensions=["sepal_length", "sepal_width", "petal_length", "petal_width"], color="species")
fig.update_traces(marker=dict(size=2))
events = st.plotly_chart(fig, on_select="rerun", selection_mode=('points', 'box', 'lasso'))

col1, col2 = st.columns(2)

with col1:
    if(events["selection"]["points"] != []):
        sepal_length_list = []
        for elem in events["selection"]["points"]:
            sepal_length_list.append(elem["dimensions[0]_values"])
        
        st.write(events)
        st.write(df.iloc[events["selection"]["point_indices"]])
        st.write(len(df.index))



with col2:
    sc1, sc2, sc3, sc4, sc5 = st.columns(5)
    with sc1:
        selection_x = st.selectbox(label="x-axis", options=("None", "sepal_length", "sepal_width", "petal_length", "petal_width"))
    with sc2:
        selection_y = st.selectbox(label="y-axis", options=("None", "sepal_length", "sepal_width", "petal_length", "petal_width"))
    with sc3:
        selection_z = st.selectbox(label="z-axis", options=("None", "sepal_length", "sepal_width", "petal_length", "petal_width"))
    with sc4:
        selection_color = st.selectbox(label="color", options=("None", "sepal_length", "sepal_width", "petal_length", "petal_width", "species"))
    with sc5:
        marker_size = st.slider("Marker size", 1, 10, 3)
    

    if(selection_x is not "None" and selection_y is not "None" and selection_z is "None"):
        if(selection_color is "None"):
            fig = px.scatter(df, x=selection_x, y=selection_y)
        else:    
            fig = px.scatter(df, x=selection_x, y=selection_y, color=selection_color)
        fig.update_traces(marker=dict(size=marker_size))
        st.plotly_chart(fig)
    else:
        if (selection_x is not "None" and selection_y is not "None" and selection_z is not "None"):
            if(selection_color is "None"):
                fig = px.scatter_3d(df, x=selection_x, y=selection_y, z=selection_z)
            else:
                fig = px.scatter_3d(df, x=selection_x, y=selection_y, z=selection_z, color=selection_color)    
            fig.update_traces(marker=dict(size=marker_size))
            st.plotly_chart(fig)
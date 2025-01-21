import plotly.express as px
from pygwalker.api.streamlit import StreamlitRenderer
import streamlit as st

st.set_page_config(layout="wide")

df = px.data.iris()
st.write(df)

pyg_app = StreamlitRenderer(df)
 
pyg_app.explorer()
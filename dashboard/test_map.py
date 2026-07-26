import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(layout="wide")

st.title("Folium Test")

m = folium.Map(
    location=[12.9716, 77.5946],
    zoom_start=10
)

folium.Marker(
    [12.9716, 77.5946],
    popup="Bangalore"
).add_to(m)

st_folium(
    m,
    width=1200,
    height=700
)
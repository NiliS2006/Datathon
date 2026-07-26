import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Crime Map",
    page_icon="🗺️",
    layout="wide"
)

st.sidebar.title("🚔 Karnataka Police Crime Intelligence System")

st.title("🗺️ Karnataka Crime Map")

API = "http://127.0.0.1:8000/crime-locations"

try:
    response = requests.get(API)

    if response.status_code != 200:
        st.error("Backend is not responding.")
        st.stop()

    df = pd.DataFrame(response.json())
    st.write("Columns received from API:")
    st.write(df.columns.tolist())

    st.write("First record:")
    st.json(df.iloc[0].to_dict())

except Exception as e:
    st.error(f"Cannot connect to backend:\n{e}")
    st.stop()

if df.empty:
    st.warning("No crime data found.")
    st.stop()

# -----------------------------
# Clean Data
# -----------------------------

df.columns = df.columns.str.strip()

df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")

df = df.dropna(subset=["Latitude", "Longitude"])

# Create missing columns if backend doesn't send them

defaults = {
    "District": "Unknown",
    "Crime": "Unknown",
    "Priority": "Unknown",
    "PoliceStation": "Unknown",
    "Officer": "Unknown",
    "Status": "Unknown",
}

for col, value in defaults.items():
    if col not in df.columns:
        df[col] = value

# -----------------------------
# Sidebar Filters
# -----------------------------

district = st.sidebar.selectbox(
    "District",
    ["All"] + sorted(df["District"].unique().tolist())
)

crime = st.sidebar.selectbox(
    "Crime",
    ["All"] + sorted(df["Crime"].unique().tolist())
)

priority = st.sidebar.selectbox(
    "Priority",
    ["All"] + sorted(df["Priority"].unique().tolist())
)

if district != "All":
    df = df[df["District"] == district]

if crime != "All":
    df = df[df["Crime"] == crime]

if priority != "All":
    df = df[df["Priority"] == priority]

# -----------------------------
# KPIs
# -----------------------------

c1, c2, c3 = st.columns(3)

c1.metric("Cases", len(df))
c2.metric("Districts", df["District"].nunique())
c3.metric("Crime Types", df["Crime"].nunique())

st.divider()

# -----------------------------
# Plotly Map
# -----------------------------

st.write("Rows:", len(df))

st.dataframe(df.head(10))

st.dataframe(
    pd.DataFrame(df.dtypes, columns=["dtype"])
)

import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(
    go.Scattermapbox(
        lat=df["Latitude"].tolist(),
        lon=df["Longitude"].tolist(),
        mode="markers",
        marker=dict(
            size=9,
            color="red"
        ),
        text=df["Crime"],
        hovertemplate=
        "<b>%{text}</b><br>" +
        "Lat: %{lat}<br>" +
        "Lon: %{lon}<extra></extra>"
    )
)

fig.update_layout(
    mapbox=dict(
        style="open-street-map",
        zoom=6,
        center=dict(
            lat=float(df["Latitude"].mean()),
            lon=float(df["Longitude"].mean())
        )
    ),
    margin=dict(l=0, r=0, t=0, b=0),
    height=700
)

st.plotly_chart(fig, use_container_width=True)

st.write(df[["Latitude", "Longitude"]].head(20))
st.write(df[["Latitude", "Longitude"]].describe())
st.write(df.dtypes)
st.plotly_chart(fig, use_container_width=True)
st.write("Rows being plotted:", len(df))
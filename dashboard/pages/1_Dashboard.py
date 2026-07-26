import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.sidebar.title("🚔 Karnataka Police Crime Intelligence System")

st.title("📊 Crime Intelligence Dashboard")

API = "http://127.0.0.1:8000/dashboard"

try:
    response = requests.get(API, timeout=5)

    if response.status_code != 200:
        st.error(f"Backend Error ({response.status_code})")
        st.write(response.text)
        st.stop()

    data = response.json()

except Exception as e:
    st.error("⚠ Unable to connect to the FastAPI backend.")
    st.exception(e)
    st.stop()

# ==============================
# Summary Cards
# ==============================

summary = data["summary"]

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Cases",
    summary["total_cases"]
)

col2.metric(
    "Open Cases",
    summary["open_cases"]
)

col3.metric(
    "Solved Cases",
    summary["solved_cases"]
)

col4.metric(
    "Repeat Offenders",
    summary["repeat_offenders"]
)

st.divider()

# ==============================
# Charts
# ==============================

left, right = st.columns(2)

crime_df = pd.DataFrame(data["crime_types"])

if not crime_df.empty:

    fig = px.bar(
        crime_df,
        x="_id",
        y="count",
        title="Crime Distribution"
    )

    left.plotly_chart(
        fig,
        use_container_width=True
    )

priority_df = pd.DataFrame(data["priority"])

if not priority_df.empty:

    fig = px.pie(
        priority_df,
        names="_id",
        values="count",
        title="Priority Distribution"
    )

    right.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

district_df = pd.DataFrame(data["districts"])

if not district_df.empty:

    fig = px.bar(
        district_df,
        x="_id",
        y="count",
        title="Cases by District",
        color="count"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

st.subheader("🗂 Recent Cases")

recent_df = pd.DataFrame(data["recent_cases"])

st.dataframe(
    recent_df,
    use_container_width=True,
    hide_index=True
)
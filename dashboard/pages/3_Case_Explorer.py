import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="Case Explorer",
    page_icon="🔍",
    layout="wide"
)

st.sidebar.title("Karnataka Police Crime Intelligence System")





st.title("🔍 Case Explorer")

API = "http://127.0.0.1:8000/intelligence/cases"

try:
    response = requests.get(API)

    if response.status_code != 200:
        st.error("Backend not responding.")
        st.stop()

    df = pd.DataFrame(response.json())

except Exception:
    st.error("Cannot connect to FastAPI.")
    st.stop()

if df.empty:
    st.warning("No cases found.")
    st.stop()

# ------------------------
# Sidebar Filters
# ------------------------

st.sidebar.header("Search & Filters")

case_id = st.sidebar.text_input("Case ID")

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

status = st.sidebar.selectbox(
    "Status",
    ["All"] + sorted(df["Status"].unique().tolist())
)

# ------------------------
# Apply Filters
# ------------------------

filtered = df.copy()

if case_id:
    filtered = filtered[
        filtered["CaseID"].astype(str).str.contains(case_id)
    ]

if district != "All":
    filtered = filtered[
        filtered["District"] == district
    ]

if crime != "All":
    filtered = filtered[
        filtered["Crime"] == crime
    ]

if priority != "All":
    filtered = filtered[
        filtered["Priority"] == priority
    ]

if status != "All":
    filtered = filtered[
        filtered["Status"] == status
    ]

# ------------------------
# KPIs
# ------------------------

c1, c2, c3 = st.columns(3)

c1.metric("Matching Cases", len(filtered))
c2.metric("Districts", filtered["District"].nunique())
c3.metric("Crime Types", filtered["Crime"].nunique())

st.divider()

# ------------------------
# Table
# ------------------------

st.subheader("Cases")

st.dataframe(
    filtered,
    use_container_width=True,
    hide_index=True
)

# ------------------------
# Case Details
# ------------------------

st.divider()

st.subheader("📄 Case Details")

if len(filtered):

    selected = st.selectbox(
        "Select Case",
        filtered["CaseID"]
    )

    case = filtered[
        filtered["CaseID"] == selected
    ].iloc[0]

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"### Case #{case['CaseID']}")
        st.write("**FIR Number:**", case["FIRNumber"])
        st.write("**Crime:**", case["Crime"])
        st.write("**Sub Crime:**", case["SubCrime"])
        st.write("**Priority:**", case["Priority"])
        st.write("**Status:**", case["Status"])
        st.write("**Date:**", case["Date"])

    with col2:
        st.markdown("### Investigation")
        st.write("**Officer:**", case["Officer"])
        st.write("**District:**", case["District"])
        st.write("**Police Station:**", case["PoliceStation"])
        st.write("**Latitude:**", case["Latitude"])
        st.write("**Longitude:**", case["Longitude"])
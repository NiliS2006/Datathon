import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="Reports",
    layout="wide"
)

st.title("📄 Crime Intelligence Reports")

API = "http://127.0.0.1:8000"

try:
    dashboard = requests.get(f"{API}/dashboard").json()

    summary = dashboard["summary"]

    crime = pd.DataFrame(dashboard["crime_types"])
    crime.columns = ["Crime Type", "Cases"]

    district = pd.DataFrame(dashboard["districts"])
    district.columns = ["District", "Cases"]

    priority = pd.DataFrame(dashboard["priority"])
    priority.columns = ["Priority", "Cases"]

    recent = pd.DataFrame(dashboard["recent_cases"])

except:
    st.error("Backend is not running.")
    st.stop()


st.header("Executive Summary")

st.markdown(f"""
### Karnataka Crime Intelligence Report

**Total Cases:** {summary['total_cases']}

**Open Cases:** {summary['open_cases']}

**Solved Cases:** {summary['solved_cases']}

**Repeat Offenders:** {summary['repeat_offenders']}

---

This report summarizes crime patterns across Karnataka using police records,
district-wise analysis, crime classification, and investigation status.
""")


st.divider()

st.subheader("Crime Type Distribution")

st.dataframe(
    crime,
    use_container_width=True
)

st.subheader("District-wise Cases")

st.dataframe(
    district,
    use_container_width=True
)

st.subheader("Priority Distribution")

st.dataframe(
    priority,
    use_container_width=True
)

st.subheader("Recent Cases")

st.dataframe(
    recent,
    use_container_width=True
)

csv = recent.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Recent Cases CSV",
    data=csv,
    file_name="recent_cases.csv",
    mime="text/csv"
)
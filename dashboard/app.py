import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="Karnataka Crime Intelligence Platform",
    page_icon="🚔",
    layout="wide"
)

st.title("🚔 Karnataka Crime Intelligence Platform")
st.caption("AI Powered Crime Analysis & Intelligence Dashboard")

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------

API = "http://127.0.0.1:8000/dashboard"

try:
    response = requests.get(API)

    if response.status_code != 200:
        st.error("Backend is not responding.")
        st.stop()

    dashboard = response.json()

except Exception:
    st.error("Cannot connect to FastAPI Backend.")
    st.stop()

summary = dashboard["summary"]

# -------------------------------------------------
# KPI CARDS
# -------------------------------------------------

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "📁 Total Cases",
        f"{summary['total_cases']:,}"
    )

with c2:
    st.metric(
        "🔍 Under Investigation",
        f"{summary['open_cases']:,}"
    )

with c3:
    st.metric(
        "✅ Solved Cases",
        f"{summary['solved_cases']:,}"
    )

with c4:
    st.metric(
        "🚨 Repeat Offenders",
        f"{summary['repeat_offenders']:,}"
    )

st.divider()

# -------------------------------------------------
# DATAFRAMES
# -------------------------------------------------

crime_df = pd.DataFrame(dashboard["crime_types"])
priority_df = pd.DataFrame(dashboard["priority"])
district_df = pd.DataFrame(dashboard["districts"])
recent_df = pd.DataFrame(dashboard["recent_cases"])

crime_df.rename(columns={"_id": "Crime", "count": "Cases"}, inplace=True)
priority_df.rename(columns={"_id": "Priority", "count": "Cases"}, inplace=True)
district_df.rename(columns={"_id": "District", "count": "Cases"}, inplace=True)

# -------------------------------------------------
# CHARTS
# -------------------------------------------------

left, right = st.columns(2)

with left:

    fig = px.pie(
        crime_df,
        names="Crime",
        values="Cases",
        hole=0.45,
        title="Crime Distribution"
    )

    fig.update_traces(textposition="inside")

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    fig = px.bar(
        priority_df,
        x="Priority",
        y="Cases",
        color="Priority",
        title="Priority Distribution"
    )

    fig.update_layout(
        xaxis_title="Priority",
        yaxis_title="Cases"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -------------------------------------------------
# DISTRICT CHART
# -------------------------------------------------

fig = px.bar(
    district_df,
    x="District",
    y="Cases",
    color="Cases",
    title="Cases by District",
    text="Cases"
)

fig.update_layout(
    xaxis_title="District",
    yaxis_title="Cases"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -------------------------------------------------
# RECENT CASES
# -------------------------------------------------

st.subheader("📋 Latest Cases")

st.dataframe(
    recent_df,
    use_container_width=True,
    hide_index=True
)

# -------------------------------------------------
# QUICK INSIGHTS
# -------------------------------------------------

st.subheader("🧠 AI Insights")

top_crime = crime_df.iloc[0]
top_district = district_df.iloc[0]
top_priority = priority_df.iloc[0]

st.success(
    f"""
• **Most common crime:** {top_crime['Crime']} ({top_crime['Cases']} cases)

• **Highest crime district:** {top_district['District']} ({top_district['Cases']} cases)

• **Highest priority category:** {top_priority['Priority']} ({top_priority['Cases']} cases)

### Recommendation

Increase surveillance and police deployment in **{top_district['District']}**, particularly focusing on **{top_crime['Crime']}** incidents. Allocate additional investigative resources toward **{top_priority['Priority']}** priority cases.
"""
)
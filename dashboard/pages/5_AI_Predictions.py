import streamlit as st
import requests

st.set_page_config(
    page_title="AI Predictions",
    page_icon="🤖",
    layout="wide"
)

st.sidebar.title("🚔 Karnataka Police Crime Intelligence System")

st.title("🤖 AI Crime Priority Prediction")

st.markdown(
    """
Predict the expected **priority level** of a new crime case using the trained
Machine Learning model.
"""
)

API = "http://127.0.0.1:8000/predict"

# --------------------------------------------------
# User Inputs
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    crime = st.selectbox(
        "Crime Type",
        [
            "Murder",
            "Robbery",
            "Fraud",
            "Cyber Crime",
            "Assault",
            "Kidnapping",
            "Vehicle Theft",
            "Drug Offence",
            "Burglary",
            "Domestic Violence",
            "Attempt to Murder",
            "Missing Person"
        ]
    )

    district = st.selectbox(
        "District",
        [
            "Bengaluru Urban",
            "Mysuru",
            "Dakshina Kannada"
        ]
    )

    police_station = st.text_input(
        "Police Station",
        placeholder="Example: Koramangala Police Station"
    )

with col2:

    weapon = st.text_input(
        "Weapon Used",
        placeholder="Knife / Gun / Unknown"
    )

    vehicle = st.text_input(
        "Vehicle Used",
        placeholder="Car / Bike / None"
    )

st.divider()

# --------------------------------------------------
# Prediction
# --------------------------------------------------

if st.button("🔮 Predict Crime Priority", use_container_width=True):

    payload = {
        "Crime": crime,
        "District": district,
        "PoliceStation": police_station,
        "Weapon": weapon,
        "Vehicle": vehicle
    }

    try:

        response = requests.post(API, json=payload, timeout=10)

        if response.status_code != 200:

            st.error(response.text)
            st.stop()

        result = response.json()

        priority = result["predicted_priority"]
        confidence = result.get("confidence", 0)

        st.success("Prediction Complete")

        c1, c2 = st.columns(2)

        c1.metric(
            "Predicted Priority",
            priority
        )

        c2.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )

        st.divider()

        if priority == "Critical":

            st.error(
                "🚨 Immediate police intervention recommended."
            )

        elif priority == "High":

            st.warning(
                "⚠ High priority case. Rapid response advised."
            )

        elif priority == "Medium":

            st.info(
                "🟡 Medium priority investigation."
            )

        else:

            st.success(
                "🟢 Low priority case."
            )

        st.subheader("Prediction Summary")

        st.write(f"**Crime:** {crime}")
        st.write(f"**District:** {district}")
        st.write(f"**Police Station:** {police_station}")
        st.write(f"**Weapon:** {weapon}")
        st.write(f"**Vehicle:** {vehicle}")

    except Exception as e:

        st.error("Unable to connect to FastAPI backend.")
        st.exception(e)
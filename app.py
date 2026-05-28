import streamlit as st

# MUST BE FIRST STREAMLIT COMMAND
st.set_page_config(
    page_title="AI Smart Analytics Dashboard",
    page_icon="🤖",
    layout="wide"
)

# IMPORT AFTER PAGE CONFIG
import home
import accident
import churn

# ---------------- SIDEBAR ----------------
st.sidebar.title("🤖 AI Suite")
st.sidebar.caption("Smart Detection & Analytics")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🚗 Accident Detection",
        "📉 Customer Churn Prediction"
    ]
)

# ---------------- PAGE ROUTING ----------------
if page == "🏠 Home":
    home.render()

elif page == "🚗 Accident Detection":
    accident.render()

elif page == "📉 Customer Churn Prediction":
    churn.render()

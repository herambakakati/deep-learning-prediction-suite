import streamlit as st

# ================= PAGE CONFIG =================

st.set_page_config(
    page_title="AI Smart Analytics Dashboard",
    page_icon="🤖",
    layout="wide"
)

# ================= IMPORT PAGES =================

import home
import accident
import churn

# ================= SIDEBAR =================

st.sidebar.title("📌 Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "🏠 Home",
        "🚗 Accident Detection",
        "📉 Churn Prediction"
    ]
)

# ================= PAGE ROUTING =================

if page == "🏠 Home":
    home.render()

elif page == "🚗 Accident Detection":
    accident.render()

elif page == "📉 Churn Prediction":
    churn.render()

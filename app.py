# =========================================================
# app.py
# FINAL STREAMLIT CLOUD READY VERSION
# =========================================================

import streamlit as st
import home
import accident
import churn


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Smart Analytics Dashboard",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# GLOBAL PREMIUM CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"]{
    font-family:'Inter',sans-serif;
}

/* MAIN APP */

.stApp{

    background:
    linear-gradient(
        135deg,
        #f8fbff 0%,
        #eef4ff 45%,
        #ffffff 100%
    );
}

/* MAIN CONTAINER */

.block-container{

    max-width:1450px;

    padding-top:1.8rem;

    padding-bottom:2rem;
}

/* SIDEBAR */

section[data-testid="stSidebar"]{

    background:
    linear-gradient(
        180deg,
        #0f172a,
        #1e3a8a
    );
}

/* SIDEBAR TEXT */

section[data-testid="stSidebar"] *{

    color:white !important;
}

/* SIDEBAR RADIO */

.stRadio label{

    font-size:16px !important;

    font-weight:700 !important;
}

/* BUTTON */

.stButton > button{

    width:100%;

    height:55px;

    border:none;

    border-radius:18px;

    font-size:17px;

    font-weight:700;

    color:white;

    background:
    linear-gradient(
        135deg,
        #6366f1,
        #8b5cf6
    );

    box-shadow:
    0 10px 25px rgba(99,102,241,0.30);

    transition:0.3s;
}

.stButton > button:hover{

    transform:translateY(-2px);
}

/* FILE UPLOADER */

[data-testid="stFileUploader"]{

    border-radius:18px;

    border:
    2px dashed rgba(99,102,241,0.25);

    background:white;
}

/* INPUTS */

.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] > div{

    border-radius:14px !important;
}

/* SUCCESS */

.stSuccess,
.stError,
.stWarning{

    border-radius:16px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR HEADER
# =========================================================

st.sidebar.markdown("""

<div style="
text-align:center;
padding-top:20px;
padding-bottom:20px;
">

<h1 style="
font-size:50px;
margin-bottom:0;
">
🤖
</h1>

<h1 style="
font-size:32px;
font-weight:800;
margin-top:0;
">
AI Suite
</h1>

<p style="
font-size:14px;
opacity:0.85;
">
Smart Detection & Analytics
</p>

</div>

""", unsafe_allow_html=True)


# =========================================================
# NAVIGATION
# =========================================================

page = st.sidebar.radio(
    "📌 Navigation",
    [
        "🏠 Home",
        "🚗 Accident Detection",
        "📉 Customer Churn Prediction"
    ]
)


# =========================================================
# ROUTING
# =========================================================

if page == "🏠 Home":

    home.render()

elif page == "🚗 Accident Detection":

    accident.render()

elif page == "📉 Customer Churn Prediction":

    churn.render()

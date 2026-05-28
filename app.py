import streamlit as st
import home
import accident
import churn


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Smart Analytics Dashboard",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =====================================================
# GLOBAL CSS
# =====================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

/* GLOBAL FONT */

html,
body,
[class*="css"]{
    font-family:'Inter',sans-serif;
}

/* MAIN APP */

.stApp{
    background-color:#f1f5f9;
}

/* CONTAINER */

.block-container{
    max-width:1450px;
    padding-top:2rem;
    padding-bottom:2rem;
}

/* SIDEBAR */

section[data-testid="stSidebar"]{

    background:
    linear-gradient(
        180deg,
        #ffffff,
        #eef4ff
    );

    border-right:
    1px solid rgba(99,102,241,0.10);
}

/* SIDEBAR TEXT */

section[data-testid="stSidebar"] *{
    color:#1e3a8a !important;
}

/* RADIO */

.stRadio label{

    font-size:16px !important;

    font-weight:700 !important;

    padding:6px 4px;
}

/* BUTTONS */

.stButton > button{

    border-radius:16px;

    border:none;

    font-weight:700;
}

/* INPUTS */

.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] > div{

    border-radius:14px !important;
}

/* FILE UPLOADER */

[data-testid="stFileUploader"]{

    border-radius:18px;
}

/* ALERTS */

.stSuccess,
.stError,
.stWarning{

    border-radius:18px;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# SIDEBAR HEADER
# =====================================================

st.sidebar.markdown("""
<div style="
    text-align:center;
    padding-top:20px;
    padding-bottom:20px;
">

    <h1 style="
        font-size:42px;
        margin-bottom:5px;
    ">
        🤖
    </h1>

    <h1 style="
        font-size:34px;
        color:#1e3a8a;
        margin:0;
        font-weight:800;
    ">
        AI Suite
    </h1>

    <p style="
        font-size:16px;
        color:#64748b;
        margin-top:6px;
    ">
        Smart Detection & Analytics
    </p>

</div>
""", unsafe_allow_html=True)


# =====================================================
# NAVIGATION
# =====================================================

module = st.sidebar.radio(
    "📌 Navigation",
    [
        "🏠 Home",
        "🚗 Accident Detection",
        "📉 Customer Churn Prediction"
    ]
)


# =====================================================
# ROUTING
# =====================================================

if module == "🏠 Home":

    home.render()

elif module == "🚗 Accident Detection":

    accident.render()

elif module == "📉 Customer Churn Prediction":

    churn.render()

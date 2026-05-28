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
# GLOBAL PREMIUM CSS
# =====================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

/* GLOBAL */

html,
body,
[class*="css"]{
    font-family:'Inter',sans-serif;
}

.stApp{
    background:
    linear-gradient(
        135deg,
        #f8fbff 0%,
        #eef4ff 50%,
        #fdfcff 100%
    );
}

/* MAIN CONTAINER */

.block-container{
    max-width:1450px;
    padding-top:2rem;
    padding-bottom:2rem;
}

/* SIDEBAR */

section[data-testid="stSidebar"]{

    background:
    rgba(255,255,255,0.90);

    backdrop-filter:blur(18px);

    border-right:
    1px solid rgba(99,102,241,0.12);
}

section[data-testid="stSidebar"] *{
    color:#1e3a8a !important;
}

/* NAVIGATION */

.stRadio > div{
    gap:10px;
}

.stRadio label{

    font-size:16px !important;

    font-weight:700 !important;

    padding:10px 12px;

    border-radius:14px;

    transition:0.3s ease;
}

/* BUTTONS */

.stButton > button{

    width:100%;

    border-radius:18px;

    height:56px;

    font-size:18px;

    font-weight:700;

    border:none;

    color:white;

    background:
    linear-gradient(
        135deg,
        #6366f1,
        #8b5cf6
    );

    box-shadow:
    0 12px 30px rgba(99,102,241,0.30);

    transition:0.3s ease;
}

.stButton > button:hover{

    transform:translateY(-2px);

    box-shadow:
    0 16px 35px rgba(99,102,241,0.40);
}

/* INPUTS */

.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] > div{

    border-radius:16px !important;

    border:
    1px solid rgba(99,102,241,0.18) !important;

    background:
    rgba(255,255,255,0.96) !important;
}

/* FILE UPLOADER */

[data-testid="stFileUploader"]{

    background:
    rgba(255,255,255,0.92);

    border:
    2px dashed rgba(99,102,241,0.28);

    border-radius:22px;

    padding:18px;
}

/* ALERT BOXES */

.stSuccess,
.stError,
.stWarning{
    border-radius:18px;
}

/* SCROLLBAR */

::-webkit-scrollbar{
    width:10px;
}

::-webkit-scrollbar-thumb{

    background:
    rgba(99,102,241,0.35);

    border-radius:20px;
}

/* RESPONSIVE */

@media(max-width: 992px){

    .block-container{
        padding-top:1rem;
    }

    section[data-testid="stSidebar"]{
        width:100% !important;
    }
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
        color:#5b6f99;
        margin-top:6px;
    ">
        Smart Detection & Analytics
    </p>

</div>
""", unsafe_allow_html=True)


# =====================================================
# SIDEBAR NAVIGATION
# =====================================================

page = st.sidebar.radio(
    "📌 Navigation",
    [
        "🏠 Home",
        "🚗 Accident Detection",
        "📉 Churn Prediction"
    ]
)


# =====================================================
# PAGE ROUTING
# =====================================================

if page == "🏠 Home":

    home.render()

elif page == "🚗 Accident Detection":

    accident.render()

elif page == "📉 Churn Prediction":

    churn.render()

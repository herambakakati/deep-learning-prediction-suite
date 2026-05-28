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

.stApp{
    background: linear-gradient(
        135deg,
        #f8fbff 0%,
        #eef4ff 50%,
        #ffffff 100%
    );
}

.block-container{
    max-width:1400px;
    padding-top:2rem;
    padding-bottom:2rem;
}

section[data-testid="stSidebar"]{
    background:
    linear-gradient(
        180deg,
        #ffffff,
        #eef4ff
    );
}

section[data-testid="stSidebar"] *{
    color:#1e3a8a !important;
}

.stButton > button{
    border:none;
    border-radius:18px;
    height:55px;
    font-weight:700;
    color:white;
    background:
    linear-gradient(
        135deg,
        #6366f1,
        #8b5cf6
    );
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.markdown("""
<div style="text-align:center;padding-top:20px;">

<h1 style="font-size:42px;">🤖</h1>

<h1 style="
font-size:34px;
color:#1e3a8a;
margin:0;
">
AI Suite
</h1>

<p style="
color:#64748b;
font-size:15px;
">
Smart Detection & Analytics
</p>

</div>
""", unsafe_allow_html=True)


page = st.sidebar.radio(
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

if page == "🏠 Home":

    home.render()

elif page == "🚗 Accident Detection":

    accident.render()

elif page == "📉 Customer Churn Prediction":

    churn.render()

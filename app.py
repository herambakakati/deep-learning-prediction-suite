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

st.markdown(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"]{
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

    .block-container{
        max-width:1450px;
        padding-top:2rem;
        padding-bottom:2rem;
    }

    section[data-testid="stSidebar"]{

        background:
            rgba(255,255,255,0.92);

        backdrop-filter:blur(18px);

        border-right:
            1px solid rgba(99,102,241,0.12);
    }

    section[data-testid="stSidebar"] *{
        color:#1e3a8a !important;
    }

    .stRadio label{
        font-size:16px !important;
        font-weight:700 !important;
    }

    .stButton > button{

        width:100%;

        height:56px;

        border:none;

        border-radius:18px;

        font-size:18px;

        font-weight:700;

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

        transform:translateY(-3px);

        box-shadow:
            0 18px 35px rgba(99,102,241,0.40);
    }

    .stTextInput input,
    .stNumberInput input,
    .stSelectbox div[data-baseweb="select"] > div{

        border-radius:16px !important;

        border:
            1px solid rgba(99,102,241,0.18) !important;

        background:
            rgba(255,255,255,0.95) !important;
    }

    [data-testid="stFileUploader"]{

        background:
            rgba(255,255,255,0.92);

        border:
            2px dashed rgba(99,102,241,0.28);

        border-radius:22px;

        padding:18px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.markdown(
    """
    <div style="
        text-align:center;
        padding-top:25px;
        padding-bottom:25px;
    ">

        <h1 style="
            font-size:48px;
            margin-bottom:8px;
        ">
            🤖
        </h1>

        <h1 style="
            font-size:38px;
            color:#1e3a8a;
            margin:0;
            font-weight:800;
        ">
            AI Suite
        </h1>

        <p style="
            font-size:16px;
            color:#5b6f99;
            margin-top:10px;
        ">
            Smart Detection & Analytics
        </p>

    </div>
    """,
    unsafe_allow_html=True
)


# =====================================================
# NAVIGATION
# =====================================================

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🚗 Accident Detection",
        "📉 Customer Churn Prediction"
    ]
)


# =====================================================
# ROUTING
# =====================================================

try:

    if page == "🏠 Home":

        home.render()

    elif page == "🚗 Accident Detection":

        accident.render()

    elif page == "📉 Customer Churn Prediction":

        churn.render()

except Exception as e:

    st.error(
        f"Application Error: {e}"
    )

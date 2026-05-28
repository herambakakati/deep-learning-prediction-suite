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

GLOBAL_CSS = """
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html,
body,
[class*="css"]{
    font-family:'Inter',sans-serif;
}

/* APP */

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
    rgba(255,255,255,0.92);

    backdrop-filter:blur(18px);

    border-right:
    1px solid rgba(99,102,241,0.12);
}

/* REMOVE STREAMLIT HEADER */

header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

/* RADIO */

.stRadio label{
    font-size:16px !important;
    font-weight:700 !important;
    color:#1e3a8a !important;
}

/* BUTTON */

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

/* INPUTS */

.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] > div{

    border-radius:16px !important;

    border:
    1px solid rgba(99,102,241,0.18) !important;

    background:
    rgba(255,255,255,0.95) !important;
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

/* ALERTS */

.stSuccess,
.stError{
    border-radius:18px;
}

</style>
"""

st.markdown(
    GLOBAL_CSS,
    unsafe_allow_html=True
)

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.markdown("")

st.sidebar.markdown(
    "# 🤖"
)

st.sidebar.markdown(
    """
    <h1 style="
        color:#1e3a8a;
        font-size:34px;
        font-weight:800;
        margin-bottom:0;
    ">
        AI Suite
    </h1>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown(
    """
    <p style="
        color:#5b6f99;
        font-size:15px;
        margin-top:-10px;
        margin-bottom:30px;
    ">
        Smart Detection & Analytics
    </p>
    """,
    unsafe_allow_html=True
)

# =====================================================
# NAVIGATION
# =====================================================

module = st.sidebar.radio(
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

    if module == "🏠 Home":

        home.render()

    elif module == "🚗 Accident Detection":

        accident.render()

    elif module == "📉 Customer Churn Prediction":

        churn.render()

except Exception as e:

    st.error(f"Application Error: {str(e)}")

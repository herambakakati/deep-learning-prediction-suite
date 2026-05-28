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
# SAFE GLOBAL CSS
# =====================================================

GLOBAL_CSS = """
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

/* FONT */

html, body, [class*="css"]{
    font-family:'Inter',sans-serif;
}

/* APP BACKGROUND */

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

/* REMOVE STREAMLIT DEFAULT TOP SPACE */

header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

/* FIX MARKDOWN HTML RENDERING */

div[data-testid="stMarkdownContainer"] p{
    margin-bottom:0px;
}

</style>
"""

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

# =====================================================
# SIDEBAR
# =====================================================

sidebar_html = """
<div style="text-align:center;padding-top:25px;padding-bottom:25px;">

    <div style="font-size:48px;margin-bottom:8px;">
        🤖
    </div>

    <div style="
        font-size:38px;
        color:#1e3a8a;
        font-weight:800;
        margin-bottom:8px;
    ">
        AI Suite
    </div>

    <div style="
        font-size:16px;
        color:#5b6f99;
    ">
        Smart Detection & Analytics
    </div>

</div>
"""

st.sidebar.markdown(
    sidebar_html,
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

    st.error(f"Application Error: {str(e)}")

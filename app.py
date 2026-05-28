import streamlit as st
import home
import accident
import churn


st.set_page_config(
    page_title="AI Analytics Suite",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family:'Poppins',sans-serif;
}

.stApp{
    background:
    linear-gradient(
        135deg,
        #f8fbff 0%,
        #eef4ff 45%,
        #ffffff 100%
    );
}

/* main container */
.block-container{
    max-width:1450px;
    padding-top:1.5rem;
    padding-bottom:2rem;
}

/* sidebar */
section[data-testid="stSidebar"]{
    background:
    linear-gradient(
        180deg,
        #0f172a,
        #1e3a8a
    );
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

/* buttons */
.stButton > button{
    width:100%;
    height:52px;
    border:none;
    border-radius:18px;
    font-weight:700;
    color:white;
    font-size:16px;

    background:
    linear-gradient(
        135deg,
        #6366f1,
        #8b5cf6
    );

    transition:0.3s;
}

.stButton > button:hover{
    transform:translateY(-2px);
}

</style>
""", unsafe_allow_html=True)


st.sidebar.markdown("""

<div style="text-align:center;padding-top:20px;">

<h1 style="
font-size:48px;
margin-bottom:0;
">
🚀
</h1>

<h1 style="
font-size:30px;
margin-top:0;
font-weight:700;
">
AI Analytics
</h1>

<p style="
font-size:14px;
opacity:0.85;
">
Deep Learning Dashboard
</p>

</div>

""", unsafe_allow_html=True)


page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🚗 Accident Detection",
        "📉 Churn Prediction"
    ]
)


if page == "🏠 Home":
    home.render()

elif page == "🚗 Accident Detection":
    accident.render()

elif page == "📉 Churn Prediction":
    churn.render()

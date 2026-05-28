import streamlit as st


def render():

    st.markdown("""
    <style>

    .block-container{
        max-width:1400px;
        padding-top:2rem;
        padding-bottom:2rem;
    }

    .hero{
        background:#0f172a;
        padding:50px;
        border-radius:24px;
        margin-bottom:35px;
    }

    .hero h1{
        color:white;
        font-size:50px;
        margin-bottom:15px;
    }

    .hero p{
        color:#e2e8f0;
        font-size:20px;
        line-height:1.8;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero">
        <h1>🤖 AI Smart Analytics Dashboard</h1>
        <p>
        Premium intelligent platform for accident detection,
        customer churn prediction, and AI analytics.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        st.info("""
🚗 Accident Detection

Upload traffic images and detect accident scenarios
using deep learning CNN models.
""")

    with col2:

        st.warning("""
📉 Customer Churn Prediction

Predict customer churn probability using
AI-powered analytics systems.
""")

    st.markdown("## Features")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.success("🚀 Fast")

    with c2:
        st.success("🧠 Deep Learning")

    with c3:
        st.success("📊 Analytics")

    with c4:
        st.success("🔒 Reliable")

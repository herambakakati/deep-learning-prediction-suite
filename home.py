import streamlit as st


def render():

    st.markdown("""
    <style>

    .hero{
        background:
        linear-gradient(
            rgba(15,23,42,0.82),
            rgba(30,58,138,0.82)
        ),
        url("https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1600&q=80");

        background-size:cover;
        background-position:center;

        padding:60px;

        border-radius:28px;

        margin-bottom:35px;
    }

    .hero h1{
        color:white;
        font-size:54px;
        font-weight:800;
    }

    .hero p{
        color:#e2e8f0;
        font-size:20px;
        line-height:1.8;
    }

    .feature-card{
        background:white;
        padding:30px;
        border-radius:24px;
        box-shadow:0 10px 30px rgba(0,0,0,0.06);
        height:220px;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero">

        <h1>
            🤖 AI Smart Analytics Dashboard
        </h1>

        <p>
            Premium intelligent platform for
            accident detection, customer churn
            prediction, and AI analytics.
        </p>

    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="feature-card">

        <h2>🚗 Accident Detection</h2>

        <p>
        Upload traffic images and detect
        accident scenarios using
        deep learning CNN models.
        </p>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="feature-card">

        <h2>📉 Customer Churn Prediction</h2>

        <p>
        Predict customer churn probability
        using AI-powered analytics systems.
        </p>

        </div>
        """, unsafe_allow_html=True)

    st.write("")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.success("🚀 Fast")

    with c2:
        st.success("🧠 Deep Learning")

    with c3:
        st.success("📊 Analytics")

    with c4:
        st.success("🔒 Reliable")

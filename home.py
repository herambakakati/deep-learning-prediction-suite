import streamlit as st


def render():

    # ================= CUSTOM CSS =================

    st.markdown("""
    <style>

    /* MAIN PAGE */

    .stApp{
        background-color:#f1f5f9;
    }

    .block-container{
        max-width:1400px;
        padding-top:2rem;
        padding-bottom:2rem;
    }

    /* HERO SECTION */

    .hero{

        background-image:
        linear-gradient(rgba(15,23,42,0.82),
        rgba(30,58,138,0.78)),
        url('https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1600&q=80');

        background-size:cover;
        background-position:center;
        background-repeat:no-repeat;

        padding:65px;

        border-radius:28px;

        margin-bottom:40px;

        box-shadow:
        0 16px 40px rgba(0,0,0,0.18);
    }

    .hero h1{
        color:white;
        font-size:58px;
        font-weight:800;
        margin-bottom:20px;
        line-height:1.2;
    }

    .hero p{
        color:rgba(255,255,255,0.94);
        font-size:22px;
        line-height:1.9;
        max-width:1000px;
        font-weight:500;
    }

    /* MAIN CARDS */

    .custom-card{

        padding:35px;

        border-radius:24px;

        min-height:230px;

        box-shadow:
        0 10px 30px rgba(0,0,0,0.08);

        transition:0.3s ease;
    }

    .custom-card:hover{

        transform:translateY(-8px);

        box-shadow:
        0 18px 35px rgba(0,0,0,0.12);
    }

    .blue-card{
        background:
        linear-gradient(135deg,#edf4ff,#dbeafe);
    }

    .orange-card{
        background:
        linear-gradient(135deg,#fff7ed,#ffedd5);
    }

    .card-title{
        color:#1e3a8a;
        font-size:34px;
        font-weight:800;
        margin-bottom:18px;
    }

    .card-text{
        color:#334155;
        font-size:19px;
        line-height:1.9;
        font-weight:500;
    }

    /* FEATURES */

    .feature-heading{
        font-size:34px;
        font-weight:800;
        color:#0f172a;
        margin-top:15px;
        margin-bottom:22px;
    }

    .feature-box{

        background:white;

        padding:24px;

        border-radius:20px;

        text-align:center;

        min-height:120px;

        box-shadow:
        0 8px 24px rgba(0,0,0,0.08);

        transition:0.3s ease;
    }

    .feature-box:hover{

        transform:translateY(-6px);

        box-shadow:
        0 16px 32px rgba(0,0,0,0.12);
    }

    .feature-icon{
        font-size:38px;
        margin-bottom:10px;
    }

    .feature-text{
        color:#1e3a8a;
        font-size:20px;
        font-weight:700;
    }

    /* RESPONSIVE */

    @media(max-width: 992px){

        .hero{
            padding:40px 30px;
        }

        .hero h1{
            font-size:40px;
        }

        .hero p{
            font-size:18px;
        }

        .card-title{
            font-size:26px;
        }

        .card-text{
            font-size:17px;
        }

        .feature-text{
            font-size:16px;
        }
    }

    </style>
    """, unsafe_allow_html=True)

    # ================= HERO SECTION =================

    st.markdown("""
    <div class="hero">

        <h1>
            🤖 AI Smart Analytics Dashboard
        </h1>

        <p>
            Premium intelligent platform for accident detection,
            customer churn prediction, and AI analytics powered
            by advanced deep learning intelligence systems.
        </p>

    </div>
    """, unsafe_allow_html=True)

    # ================= MAIN CARDS =================

    col1, col2 = st.columns(2, gap="large")

    with col1:

        st.markdown("""
        <div class="custom-card blue-card">

            <div class="card-title">
                🚗 Accident Detection
            </div>

            <div class="card-text">
                Upload traffic images and detect accident scenarios
                using powerful deep learning CNN models with
                real-time intelligent prediction systems.
            </div>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="custom-card orange-card">

            <div class="card-title">
                📉 Customer Churn Prediction
            </div>

            <div class="card-text">
                Predict customer churn probability using
                AI-powered analytics systems and advanced
                business intelligence prediction models.
            </div>

        </div>
        """, unsafe_allow_html=True)

    # ================= SPACE =================

    st.markdown("<br>", unsafe_allow_html=True)

    # ================= FEATURES TITLE =================

    st.markdown("""
    <div class="feature-heading">
        ✨ Features
    </div>
    """, unsafe_allow_html=True)

    # ================= FEATURE BOXES =================

    c1, c2, c3, c4 = st.columns(4, gap="medium")

    with c1:

        st.markdown("""
        <div class="feature-box">

            <div class="feature-icon">
                🚀
            </div>

            <div class="feature-text">
                Fast
            </div>

        </div>
        """, unsafe_allow_html=True)

    with c2:

        st.markdown("""
        <div class="feature-box">

            <div class="feature-icon">
                🧠
            </div>

            <div class="feature-text">
                Deep Learning
            </div>

        </div>
        """, unsafe_allow_html=True)

    with c3:

        st.markdown("""
        <div class="feature-box">

            <div class="feature-icon">
                📊
            </div>

            <div class="feature-text">
                Analytics
            </div>

        </div>
        """, unsafe_allow_html=True)

    with c4:

        st.markdown("""
        <div class="feature-box">

            <div class="feature-icon">
                🔒
            </div>

            <div class="feature-text">
                Reliable
            </div>

        </div>
        """, unsafe_allow_html=True)

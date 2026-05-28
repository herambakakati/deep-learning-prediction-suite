import streamlit as st

def render():
    st.markdown("""
    <style>

    .block-container{
        max-width:1400px;
        padding-top:2rem;
        padding-bottom:2rem;
    }

    .hero-box{
        background:#0f172a;
        padding:60px;
        border-radius:28px;
        margin-bottom:40px;
    }

    .hero-title{
        color:white;
        font-size:48px;
        font-weight:800;
        margin-bottom:20px;
    }

    .hero-text{
        color:#e2e8f0;
        font-size:20px;
        line-height:1.8;
    }

    .card{
        padding:30px;
        border-radius:24px;
        min-height:220px;
    }

    .blue-card{
        background:#dbeafe;
    }

    .orange-card{
        background:#ffedd5;
    }

    .card-title{
        font-size:28px;
        font-weight:800;
        margin-bottom:18px;
        color:#1e3a8a;
    }

    .card-text{
        font-size:18px;
        line-height:1.8;
        color:#334155;
    }

    .feature-card{
        background:white;
        padding:25px;
        border-radius:20px;
        text-align:center;
        min-height:200px;
    }

    .feature-icon{
        font-size:40px;
        margin-bottom:12px;
    }

    .feature-title{
        font-size:22px;
        font-weight:700;
        margin-bottom:10px;
        color:#0f172a;
    }

    .feature-text{
        color:#475569;
        font-size:16px;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero-box">

        <div class="hero-title">
            🤖 AI Smart Analytics Dashboard
        </div>

        <div class="hero-text">
            Premium intelligent platform for accident detection,
            customer churn prediction, and AI analytics.
        </div>

    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="card blue-card">

            <div class="card-title">
                🚗 Accident Detection
            </div>

            <div class="card-text">
                Upload traffic images and detect accident scenarios
                using deep learning CNN models.
            </div>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="card orange-card">

            <div class="card-title">
                📉 Customer Churn Prediction
            </div>

            <div class="card-text">
                Predict customer churn probability using
                AI-powered analytics systems.
            </div>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    features = [
        ("🚀", "Fast", "Optimized AI inference."),
        ("🧠", "Deep Learning", "Advanced neural models."),
        ("📊", "Analytics", "Business-focused prediction."),
        ("🔒", "Reliable", "Stable deployment.")
    ]

    cols = [c1, c2, c3, c4]

    for col, feature in zip(cols, features):

        icon, title, desc = feature

        with col:

            st.markdown(f"""
            <div class="feature-card">

                <div class="feature-icon">
                    {icon}
                </div>

                <div class="feature-title">
                    {title}
                </div>

                <div class="feature-text">
                    {desc}
                </div>

            </div>
            """, unsafe_allow_html=True)

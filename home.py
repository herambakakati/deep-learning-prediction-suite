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
        background-image:
        linear-gradient(
            rgba(15,23,42,0.78),
            rgba(30,58,138,0.78)
        ),
        url('https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1600&q=80');

        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;

        padding: 70px 60px;
        border-radius: 28px;
        margin-bottom: 40px;

        box-shadow: 0 16px 40px rgba(0,0,0,0.20);
    }

    .hero-title{
        color: white;
        font-size: 54px;
        font-weight: 800;
        margin-bottom: 18px;
    }

    .hero-text{
        color: rgba(255,255,255,0.96);
        font-size: 21px;
        line-height: 1.8;
        max-width: 900px;
    }

    .card{
        padding: 32px;
        border-radius: 24px;
        min-height: 220px;

        box-shadow: 0 10px 28px rgba(0,0,0,0.10);
    }

    .blue-card{
        background: linear-gradient(135deg,#eef4ff,#dbeafe);
    }

    .orange-card{
        background: linear-gradient(135deg,#fff7ed,#ffedd5);
    }

    .card-title{
        color:#1e3a8a;
        font-size:30px;
        font-weight:800;
        margin-bottom:18px;
    }

    .card-text{
        color:#334155;
        font-size:18px;
        line-height:1.8;
    }

    .feature-card{
        background:white;
        padding:28px;
        border-radius:22px;
        text-align:center;
        min-height:220px;

        box-shadow:0 8px 24px rgba(0,0,0,0.08);
    }

    .feature-icon{
        font-size:42px;
        margin-bottom:14px;
    }

    .feature-title{
        color:#1e293b;
        font-size:22px;
        font-weight:700;
        margin-bottom:10px;
    }

    .feature-text{
        color:#475569;
        font-size:16px;
        line-height:1.7;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero-box">

        <div class="hero-title">
            🤖 AI Smart Analytics Dashboard
        </div>

        <div class="hero-text">
            Premium intelligent platform for real-time accident detection,
            customer churn prediction, and advanced business analytics
            powered by deep learning intelligence systems.
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
                Upload road traffic images and instantly detect
                accident scenarios using trained deep learning
                convolutional neural network models.
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
                AI-powered analytics and business intelligence
                prediction systems.
            </div>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    features = [
        ("🚀", "Fast Performance", "Optimized AI inference engine."),
        ("🧠", "Deep Learning", "Advanced neural network systems."),
        ("📊", "Analytics Ready", "Business-focused AI prediction."),
        ("🔒", "Reliable", "Stable deployment architecture.")
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

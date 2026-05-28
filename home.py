import streamlit as st


def render():

    st.markdown("""
    <style>

    .block-container{
        max-width:1400px;
        padding-top:2rem;
    }

    .hero-box{
        background-image:
        linear-gradient(rgba(15,23,42,0.75),
        rgba(30,58,138,0.75)),
        url('https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1600&q=80');

        background-size:cover;
        background-position:center;
        padding:60px;
        border-radius:28px;
        margin-bottom:35px;
    }

    .hero-title{
        color:white;
        font-size:52px;
        font-weight:800;
        margin-bottom:18px;
    }

    .hero-text{
        color:white;
        font-size:20px;
        line-height:1.8;
        max-width:850px;
    }

    .card{
        padding:30px;
        border-radius:24px;
        min-height:220px;
        margin-bottom:25px;
    }

    .blue-card{
        background:#dbeafe;
    }

    .orange-card{
        background:#ffedd5;
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
        padding:25px;
        border-radius:22px;
        text-align:center;
        min-height:220px;
        box-shadow:0 8px 20px rgba(0,0,0,0.08);
    }

    .feature-icon{
        font-size:42px;
        margin-bottom:12px;
    }

    .feature-title{
        color:#1e3a8a;
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

    # HERO
    st.markdown("""
    <div class="hero-box">

        <div class="hero-title">
            🤖 AI Smart Analytics Dashboard
        </div>

        <div class="hero-text">
            Premium intelligent platform for real-time accident detection,
            customer churn prediction, and advanced business analytics
            powered by deep learning intelligence.
        </div>

    </div>
    """, unsafe_allow_html=True)

    # MAIN CARDS
    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="card blue-card">

            <div class="card-title">
                🚗 Accident Detection
            </div>

            <div class="card-text">
                Upload road traffic images and instantly detect
                accident scenarios using trained deep learning CNN models.
            </div>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="card orange-card">

            <div class="card-title">
                📉 Churn Prediction
            </div>

            <div class="card-text">
                Predict customer churn risk using AI-powered analytics
                and actionable business intelligence.
            </div>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # FEATURES
    c1, c2, c3, c4 = st.columns(4)

    features = [
        ("🚀", "Fast Performance", "Optimized AI inference."),
        ("🧠", "Deep Learning", "Advanced neural networks."),
        ("📊", "Analytics Ready", "Business-focused prediction output."),
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

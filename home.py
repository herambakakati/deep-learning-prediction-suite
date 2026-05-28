import streamlit as st


def render():

    st.markdown("""
    <style>

    .block-container{
        padding-top:2rem;
        padding-bottom:2rem;
        max-width:1400px;
    }

    /* HERO */

    .hero-box{

        background-image:
            linear-gradient(
                rgba(15,23,42,0.78),
                rgba(30,58,138,0.78)
            ),
            url('https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1600&q=80');

        background-size:cover;
        background-position:center;
        background-repeat:no-repeat;

        padding:65px;

        border-radius:28px;

        box-shadow:
        0 18px 45px rgba(0,0,0,0.20);

        margin-bottom:35px;
    }

    .hero-title{

        font-size:56px;

        font-weight:800;

        color:white;

        margin-bottom:18px;
    }

    .hero-text{

        font-size:21px;

        color:rgba(255,255,255,0.95);

        line-height:1.8;

        font-weight:500;

        max-width:900px;
    }

    /* MAIN CARDS */

    .card{

        padding:32px;

        border-radius:24px;

        box-shadow:
        0 12px 30px rgba(0,0,0,0.08);

        min-height:250px;

        transition:0.3s ease;
    }

    .card:hover{

        transform:translateY(-6px);
    }

    .blue-card{

        background:
        linear-gradient(
            135deg,
            #eef4ff,
            #dbeafe
        );
    }

    .orange-card{

        background:
        linear-gradient(
            135deg,
            #fff7ed,
            #ffedd5
        );
    }

    .card-title{

        color:#1e3a8a;

        font-size:32px;

        font-weight:800;

        margin-bottom:18px;
    }

    .card-text{

        color:#334155;

        font-size:18px;

        line-height:1.8;

        font-weight:500;
    }

    /* FEATURE */

    .feature-card{

        background:white;

        padding:24px;

        border-radius:22px;

        box-shadow:
        0 8px 24px rgba(0,0,0,0.08);

        text-align:center;

        min-height:260px;

        transition:0.3s ease;
    }

    .feature-card:hover{

        transform:translateY(-8px);

        box-shadow:
        0 14px 35px rgba(0,0,0,0.12);
    }

    .feature-icon{

        font-size:46px;

        margin-bottom:16px;
    }

    .feature-title{

        color:#1e3a8a;

        font-size:24px;

        font-weight:700;

        margin-bottom:14px;
    }

    .feature-text{

        color:#475569;

        font-size:16px;

        line-height:1.8;
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
            customer churn prediction, and advanced AI-powered business analytics
            using deep learning intelligence.
        </div>

    </div>
    """, unsafe_allow_html=True)

    # MAIN CARDS

    col1, col2 = st.columns(2, gap="large")

    with col1:

        st.markdown("""
        <div class="card blue-card">

            <div class="card-title">
                🚗 Accident Detection
            </div>

            <div class="card-text">
                Upload road traffic images and instantly detect accident
                scenarios using advanced CNN deep learning models.
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
                Predict customer churn risk using intelligent neural
                network analytics and business intelligence.
            </div>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # FEATURES

    c1, c2, c3, c4 = st.columns(4, gap="medium")

    features = [

        (
            "🚀",
            "Fast Performance",
            "Optimized AI inference for smooth and fast predictions."
        ),

        (
            "🧠",
            "Deep Learning",
            "Advanced neural network architecture for accurate results."
        ),

        (
            "📊",
            "Analytics Ready",
            "Business-focused prediction outputs and scoring systems."
        ),

        (
            "🔒",
            "Reliable",
            "Stable production-ready Streamlit deployment architecture."
        )
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

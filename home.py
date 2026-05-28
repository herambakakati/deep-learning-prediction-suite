import streamlit as st


def render():

    # =====================================================
    # PREMIUM CSS
    # =====================================================

    st.markdown("""
    <style>

    .block-container{
        padding-top:2rem;
        padding-bottom:2rem;
        max-width:1400px;
    }

    /* HERO SECTION */

    .hero-box{

        background-image:
        linear-gradient(
            rgba(15, 23, 42, 0.78),
            rgba(30, 58, 138, 0.78)
        ),
        url('https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1600&q=80');

        background-size:cover;

        background-position:center;

        background-repeat:no-repeat;

        padding:70px;

        border-radius:28px;

        box-shadow:
        0 20px 50px rgba(0,0,0,0.20);

        margin-bottom:40px;
    }

    .hero-title{

        font-size:58px;

        font-weight:800;

        color:white !important;

        margin-bottom:18px;

        line-height:1.2;
    }

    .hero-text{

        font-size:21px;

        color:rgba(255,255,255,0.96) !important;

        line-height:1.9;

        font-weight:500;

        max-width:920px;
    }

    /* MAIN ANALYTICS CARDS */

    .card{

        padding:34px;

        border-radius:24px;

        box-shadow:
        0 12px 35px rgba(0,0,0,0.08);

        min-height:260px;

        transition:0.35s ease;

        position:relative;

        overflow:hidden;
    }

    .card:hover{

        transform:translateY(-8px);

        box-shadow:
        0 18px 45px rgba(0,0,0,0.12);
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

        color:#1e3a8a !important;

        font-size:32px;

        font-weight:800;

        margin-bottom:20px;
    }

    .card-text{

        color:#334155 !important;

        font-size:18px;

        line-height:1.9;

        font-weight:500;
    }

    /* FEATURE SECTION */

    .feature-card{

        background:white;

        padding:28px;

        border-radius:22px;

        box-shadow:
        0 10px 28px rgba(0,0,0,0.08);

        text-align:center;

        min-height:260px;

        transition:0.35s ease;
    }

    .feature-card:hover{

        transform:translateY(-10px);

        box-shadow:
        0 18px 40px rgba(0,0,0,0.12);
    }

    .feature-icon{

        font-size:46px;

        margin-bottom:16px;
    }

    .feature-title{

        color:#1e3a8a !important;

        font-size:24px;

        font-weight:700;

        margin-bottom:16px;
    }

    .feature-text{

        color:#475569 !important;

        font-size:16px;

        line-height:1.8;

        font-weight:500;
    }

    /* SECTION SPACING */

    .section-gap{
        margin-top:20px;
    }

    </style>
    """, unsafe_allow_html=True)

    # =====================================================
    # HERO BANNER
    # =====================================================

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

    # =====================================================
    # MAIN MODULE CARDS
    # =====================================================

    col1, col2 = st.columns(
        2,
        gap="large"
    )

    with col1:

        st.markdown("""
        <div class="card blue-card">

            <div class="card-title">
                🚗 Accident Detection
            </div>

            <div class="card-text">
                Upload road traffic images and instantly detect accident
                scenarios using trained deep learning CNN models
                with real-time intelligent classification.
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
                Predict customer churn risk using AI-powered analytics,
                deep learning models, and actionable business intelligence
                systems for decision optimization.
            </div>

        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-gap"></div>',
        unsafe_allow_html=True
    )

    # =====================================================
    # FEATURE SECTION
    # =====================================================

    c1, c2, c3, c4 = st.columns(
        4,
        gap="medium"
    )

    features = [

        (
            "🚀",
            "Fast Performance",
            "Optimized AI inference engine for fast and smooth prediction performance."
        ),

        (
            "🧠",
            "Deep Learning",
            "Advanced neural network architecture for intelligent AI classification."
        ),

        (
            "📊",
            "Analytics Ready",
            "Business-focused probability scoring and predictive analytics engine."
        ),

        (
            "🔒",
            "Reliable",
            "Stable production-ready Streamlit deployment architecture and workflow."
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

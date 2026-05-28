import streamlit as st


def render():

    # =====================================================
    # PREMIUM CSS
    # =====================================================

    st.markdown("""
    <style>

    .block-container{
        max-width:1400px;
        padding-top:2rem;
        padding-bottom:2rem;
    }

    /* HERO */

    .hero-box{

        background-image:
        linear-gradient(
            rgba(15,23,42,0.82),
            rgba(30,58,138,0.82)
        ),
        url('https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1600&q=80');

        background-size:cover;
        background-position:center;
        background-repeat:no-repeat;

        padding:70px;

        border-radius:30px;

        margin-bottom:40px;

        box-shadow:
        0 18px 45px rgba(0,0,0,0.18);
    }

    .hero-title{

        font-size:56px;

        font-weight:800;

        color:white;

        margin-bottom:18px;

        line-height:1.2;
    }

    .hero-text{

        font-size:20px;

        color:white;

        line-height:1.9;

        max-width:900px;
    }

    /* MAIN CARDS */

    .main-card{

        padding:35px;

        border-radius:24px;

        min-height:240px;

        box-shadow:
        0 10px 28px rgba(0,0,0,0.08);

        transition:0.3s ease;
    }

    .main-card:hover{

        transform:translateY(-6px);

        box-shadow:
        0 18px 40px rgba(0,0,0,0.12);
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

        font-size:30px;

        font-weight:800;

        color:#1e3a8a;

        margin-bottom:18px;
    }

    .card-text{

        font-size:18px;

        color:#334155;

        line-height:1.9;
    }

    /* FEATURE CARDS */

    .feature-card{

        background:white;

        padding:28px;

        border-radius:22px;

        text-align:center;

        box-shadow:
        0 10px 25px rgba(0,0,0,0.08);

        min-height:250px;

        transition:0.3s ease;
    }

    .feature-card:hover{

        transform:translateY(-8px);

        box-shadow:
        0 18px 40px rgba(0,0,0,0.12);
    }

    .feature-icon{

        font-size:44px;

        margin-bottom:15px;
    }

    .feature-title{

        font-size:24px;

        font-weight:700;

        color:#1e3a8a;

        margin-bottom:14px;
    }

    .feature-text{

        font-size:15px;

        color:#475569;

        line-height:1.8;
    }

    </style>
    """, unsafe_allow_html=True)

    # =====================================================
    # HERO SECTION
    # =====================================================

    hero_html = """
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
    """

    st.markdown(
        hero_html,
        unsafe_allow_html=True
    )

    # =====================================================
    # MAIN MODULE CARDS
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        card1 = """
        <div class="main-card blue-card">

            <div class="card-title">
                🚗 Accident Detection
            </div>

            <div class="card-text">
                Upload road traffic images and instantly detect accident
                scenarios using trained deep learning CNN models
                with real-time intelligent classification.
            </div>

        </div>
        """

        st.markdown(
            card1,
            unsafe_allow_html=True
        )

    with col2:

        card2 = """
        <div class="main-card orange-card">

            <div class="card-title">
                📉 Customer Churn Prediction
            </div>

            <div class="card-text">
                Predict customer churn risk using AI-powered analytics,
                deep learning models, and actionable business intelligence.
            </div>

        </div>
        """

        st.markdown(
            card2,
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # FEATURE SECTION
    # =====================================================

    c1, c2, c3, c4 = st.columns(4)

    features = [

        (
            "🚀",
            "Fast Performance",
            "Optimized AI inference for smooth prediction performance."
        ),

        (
            "🧠",
            "Deep Learning",
            "Advanced neural networks for intelligent classification."
        ),

        (
            "📊",
            "Analytics Ready",
            "Business-focused prediction output and probability scoring."
        ),

        (
            "🔒",
            "Reliable",
            "Stable production-ready Streamlit deployment architecture."
        )

    ]

    columns = [c1, c2, c3, c4]

    for col, feature in zip(columns, features):

        icon, title, desc = feature

        feature_html = f"""
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
        """

        with col:

            st.markdown(
                feature_html,
                unsafe_allow_html=True
            )

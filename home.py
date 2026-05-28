import streamlit as st


def render():

    # =====================================================
    # UNIQUE HOME CSS
    # =====================================================

    st.markdown("""
    <style>

    /* HOME PAGE */

    .home-wrapper{
        padding-top:10px;
    }

    /* HERO */

    .home-hero-box{

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

        margin-bottom:35px;

        box-shadow:
        0 18px 45px rgba(0,0,0,0.18);
    }

    .home-hero-title{

        font-size:56px;

        font-weight:800;

        color:white;

        margin-bottom:18px;

        line-height:1.2;
    }

    .home-hero-text{

        font-size:21px;

        color:rgba(255,255,255,0.95);

        line-height:1.8;

        max-width:900px;

        font-weight:500;
    }

    /* MAIN CARDS */

    .home-main-card{

        padding:32px;

        border-radius:24px;

        min-height:250px;

        transition:0.3s ease;

        box-shadow:
        0 12px 35px rgba(0,0,0,0.08);
    }

    .home-main-card:hover{

        transform:translateY(-6px);

        box-shadow:
        0 18px 40px rgba(0,0,0,0.12);
    }

    .home-blue-card{

        background:
        linear-gradient(
            135deg,
            #eef4ff,
            #dbeafe
        );
    }

    .home-orange-card{

        background:
        linear-gradient(
            135deg,
            #fff7ed,
            #ffedd5
        );
    }

    .home-card-title{

        color:#1e3a8a;

        font-size:30px;

        font-weight:800;

        margin-bottom:18px;
    }

    .home-card-text{

        color:#334155;

        font-size:18px;

        line-height:1.8;

        font-weight:500;
    }

    /* FEATURE CARDS */

    .home-feature-card{

        background:white;

        padding:24px;

        border-radius:22px;

        text-align:center;

        min-height:250px;

        transition:0.3s ease;

        box-shadow:
        0 10px 28px rgba(0,0,0,0.08);
    }

    .home-feature-card:hover{

        transform:translateY(-8px);

        box-shadow:
        0 16px 35px rgba(0,0,0,0.12);
    }

    .home-feature-icon{

        font-size:42px;

        margin-bottom:14px;
    }

    .home-feature-title{

        color:#1e3a8a;

        font-size:22px;

        font-weight:700;

        margin-bottom:14px;
    }

    .home-feature-text{

        color:#475569;

        font-size:16px;

        line-height:1.7;
    }

    /* RESPONSIVE */

    @media(max-width: 992px){

        .home-hero-box{
            padding:40px 30px;
        }

        .home-hero-title{
            font-size:40px;
        }

        .home-hero-text{
            font-size:18px;
        }

        .home-card-title{
            font-size:24px;
        }

        .home-card-text{
            font-size:16px;
        }

        .home-feature-title{
            font-size:20px;
        }

        .home-feature-text{
            font-size:15px;
        }
    }

    </style>
    """, unsafe_allow_html=True)

    # =====================================================
    # HERO SECTION
    # =====================================================

    st.markdown("""
    <div class="home-wrapper">

        <div class="home-hero-box">

            <div class="home-hero-title">
                🤖 AI Smart Analytics Dashboard
            </div>

            <div class="home-hero-text">
                Premium intelligent platform for real-time accident detection,
                customer churn prediction, and advanced business analytics
                powered by deep learning intelligence.
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # MAIN CARDS
    # =====================================================

    col1, col2 = st.columns(2, gap="large")

    with col1:

        st.markdown("""
        <div class="home-main-card home-blue-card">

            <div class="home-card-title">
                🚗 Accident Detection
            </div>

            <div class="home-card-text">
                Upload road traffic images and instantly detect accident
                scenarios using trained deep learning CNN models.
            </div>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="home-main-card home-orange-card">

            <div class="home-card-title">
                📉 Churn Prediction
            </div>

            <div class="home-card-text">
                Predict customer churn risk using AI-powered analytics
                and actionable business intelligence.
            </div>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # FEATURES
    # =====================================================

    c1, c2, c3, c4 = st.columns(4, gap="medium")

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

    cols = [c1, c2, c3, c4]

    for col, feature in zip(cols, features):

        icon, title, desc = feature

        with col:

            st.markdown(f"""
            <div class="home-feature-card">

                <div class="home-feature-icon">
                    {icon}
                </div>

                <div class="home-feature-title">
                    {title}
                </div>

                <div class="home-feature-text">
                    {desc}
                </div>

            </div>
            """, unsafe_allow_html=True)

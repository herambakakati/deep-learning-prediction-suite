import streamlit as st


def render():

    st.markdown("""
    <style>

    /* PAGE */
    .stApp{
        background: #f1f5f9;
    }

    .block-container{
        max-width: 1450px;
        padding-top: 1.8rem;
        padding-bottom: 2rem;
    }

    /* SIDEBAR */
    section[data-testid="stSidebar"]{
        background: #ffffff;
        border-right: 1px solid #e2e8f0;
    }

    section[data-testid="stSidebar"] .css-ng1t4o{
        padding-top: 1rem;
    }

    /* HERO SECTION */
    .hero-box{
        background-image:
        linear-gradient(rgba(15,23,42,0.78),
        rgba(30,41,59,0.80)),
        url('https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1600&q=80');

        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;

        padding: 65px 70px;
        border-radius: 28px;

        box-shadow:
        0 10px 40px rgba(15,23,42,0.18);

        margin-bottom: 40px;
    }

    .hero-title{
        color: white;
        font-size: 64px;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 22px;
        letter-spacing: -1px;
    }

    .hero-text{
        color: rgba(255,255,255,0.92);
        font-size: 24px;
        line-height: 1.8;
        max-width: 1050px;
        font-weight: 500;
    }

    /* MAIN FEATURE CARDS */
    .main-card{
        padding: 38px;
        border-radius: 28px;
        min-height: 270px;

        box-shadow:
        0 8px 30px rgba(15,23,42,0.08);

        transition: all 0.35s ease;
    }

    .main-card:hover{
        transform: translateY(-8px);
        box-shadow:
        0 20px 40px rgba(15,23,42,0.14);
    }

    .blue-card{
        background:
        linear-gradient(135deg,
        #edf4ff 0%,
        #dbeafe 100%);
    }

    .orange-card{
        background:
        linear-gradient(135deg,
        #fff7ed 0%,
        #ffedd5 100%);
    }

    .card-title{
        color: #1e3a8a;
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 24px;
        letter-spacing: -0.5px;
    }

    .card-text{
        color: #334155;
        font-size: 24px;
        line-height: 1.9;
        font-weight: 500;
    }

    /* FEATURE BOXES */
    .feature-card{
        background: white;
        border-radius: 24px;

        padding: 35px 25px;

        text-align: center;

        min-height: 290px;

        box-shadow:
        0 8px 25px rgba(15,23,42,0.07);

        transition: all 0.3s ease;
    }

    .feature-card:hover{
        transform: translateY(-10px);
        box-shadow:
        0 18px 35px rgba(15,23,42,0.12);
    }

    .feature-icon{
        font-size: 54px;
        margin-bottom: 22px;
    }

    .feature-title{
        color: #1e3a8a;
        font-size: 34px;
        font-weight: 800;
        margin-bottom: 18px;
        letter-spacing: -0.5px;
    }

    .feature-text{
        color: #475569;
        font-size: 21px;
        line-height: 1.9;
        font-weight: 500;
    }

    /* MOBILE RESPONSIVE */
    @media(max-width: 992px){

        .hero-box{
            padding: 40px 30px;
        }

        .hero-title{
            font-size: 42px;
        }

        .hero-text{
            font-size: 18px;
        }

        .card-title{
            font-size: 30px;
        }

        .card-text{
            font-size: 18px;
        }

        .feature-title{
            font-size: 24px;
        }

        .feature-text{
            font-size: 16px;
        }
    }

    </style>
    """, unsafe_allow_html=True)

    # HERO SECTION
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
    col1, col2 = st.columns(2, gap="large")

    with col1:

        st.markdown("""
        <div class="main-card blue-card">

            <div class="card-title">
                🚗 Accident Detection
            </div>

            <div class="card-text">
                Upload road traffic images and instantly detect accident
                scenarios using trained deep learning CNN models.
            </div>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="main-card orange-card">

            <div class="card-title">
                📉 Churn Prediction
            </div>

            <div class="card-text">
                Predict customer churn risk using AI-powered analytics
                and actionable business intelligence.
            </div>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # FEATURE SECTION
    c1, c2, c3, c4 = st.columns(4, gap="large")

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

import streamlit as st

def render():

    # ================= CUSTOM CSS =================
    st.markdown("""
    <style>

    .block-container{
        max-width:1400px;
        padding-top:2rem;
        padding-bottom:2rem;
    }

    /* HERO SECTION */
    .hero{
        background-image:
            linear-gradient(
                rgba(15,23,42,0.82),
                rgba(30,58,138,0.82)
            ),
            url('https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1600&q=80');

        background-size:cover;
        background-position:center;
        background-repeat:no-repeat;

        padding:70px 60px;

        border-radius:28px;

        margin-bottom:40px;

        box-shadow:0 18px 45px rgba(0,0,0,0.22);
    }

    .hero h1{
        color:white;
        font-size:58px;
        font-weight:800;
        margin-bottom:20px;
        line-height:1.2;
    }

    .hero p{
        color:rgba(255,255,255,0.96);
        font-size:21px;
        line-height:1.8;
        max-width:900px;
        font-weight:500;
    }

    /* CARD DESIGN */
    .custom-card{
        border-radius:24px;
        padding:30px;
        min-height:220px;

        box-shadow:0 12px 30px rgba(0,0,0,0.10);

        transition:0.3s ease;
    }

    .custom-card:hover{
        transform:translateY(-6px);
        box-shadow:0 18px 38px rgba(0,0,0,0.16);
    }

    .blue-card{
        background:linear-gradient(
            135deg,
            #eef4ff,
            #dbeafe
        );
    }

    .orange-card{
        background:linear-gradient(
            135deg,
            #fff7ed,
            #ffedd5
        );
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
        font-weight:500;
    }

    /* FEATURE CARDS */
    .feature-card{
        background:white;

        border-radius:22px;

        padding:28px;

        text-align:center;

        min-height:220px;

        box-shadow:0 8px 24px rgba(0,0,0,0.08);

        transition:0.3s ease;
    }

    .feature-card:hover{
        transform:translateY(-8px);
        box-shadow:0 16px 34px rgba(0,0,0,0.12);
    }

    .feature-icon{
        font-size:42px;
        margin-bottom:16px;
    }

    .feature-title{
        color:#0f172a;
        font-size:24px;
        font-weight:800;
        margin-bottom:12px;
    }

    .feature-text{
        color:#475569;
        font-size:16px;
        line-height:1.7;
    }

    /* SIDEBAR */
    section[data-testid="stSidebar"]{
        background:linear-gradient(
            180deg,
            #111827,
            #1e293b
        );
    }

    section[data-testid="stSidebar"] *{
        color:white !important;
    }

    </style>
    """, unsafe_allow_html=True)

    # ================= HERO =================
    st.markdown("""
    <div class="hero">

        <h1>
            🤖 AI Smart Analytics Dashboard
        </h1>

        <p>
            Premium intelligent platform for accident detection,
            customer churn prediction, and advanced AI-powered
            business analytics systems.
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
                Upload traffic images and detect accident
                scenarios instantly using advanced deep
                learning CNN models.
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
                AI-powered analytics and business
                intelligence systems.
            </div>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ================= FEATURES =================
    st.markdown("## Features")

    c1, c2, c3, c4 = st.columns(4, gap="medium")

    features = [
        (
            "🚀",
            "Fast Performance",
            "Optimized AI inference for smooth prediction."
        ),
        (
            "🧠",
            "Deep Learning",
            "Advanced neural network intelligence systems."
        ),
        (
            "📊",
            "Analytics Ready",
            "Business-focused prediction and reporting."
        ),
        (
            "🔒",
            "Reliable",
            "Stable production-ready deployment architecture."
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

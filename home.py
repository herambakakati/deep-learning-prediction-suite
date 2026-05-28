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

    /* REMOVE STREAMLIT DEFAULT TOP SPACE */
    .stApp {
        background-color:#020617;
    }

    /* HERO SECTION */
    .hero-box{
        background-image:
        linear-gradient(rgba(15,23,42,0.82),
        rgba(30,58,138,0.82)),
        url('https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1600&q=80');

        background-size:cover;
        background-position:center;

        padding:70px 60px;
        border-radius:30px;
        margin-bottom:35px;

        box-shadow:0 15px 40px rgba(0,0,0,0.35);
    }

    .hero-title{
        color:white;
        font-size:54px;
        font-weight:800;
        margin-bottom:18px;
    }

    .hero-text{
        color:#e2e8f0;
        font-size:20px;
        line-height:1.9;
        max-width:850px;
    }

    /* MAIN CARDS */
    .card{
        padding:35px;
        border-radius:26px;
        min-height:230px;
        margin-bottom:25px;

        box-shadow:0 10px 28px rgba(0,0,0,0.18);

        transition:0.3s;
    }

    .card:hover{
        transform:translateY(-6px);
    }

    .blue-card{
        background:linear-gradient(135deg,#dbeafe,#bfdbfe);
    }

    .orange-card{
        background:linear-gradient(135deg,#ffedd5,#fed7aa);
    }

    .card-title{
        color:#0f172a;
        font-size:32px;
        font-weight:800;
        margin-bottom:18px;
    }

    .card-text{
        color:#334155;
        font-size:18px;
        line-height:1.9;
        font-weight:500;
    }

    /* FEATURE CARDS */
    .feature-card{
        background:white;
        padding:28px;
        border-radius:24px;
        text-align:center;
        min-height:220px;

        box-shadow:0 8px 20px rgba(0,0,0,0.12);

        transition:0.3s;
    }

    .feature-card:hover{
        transform:translateY(-6px);
    }

    .feature-icon{
        font-size:48px;
        margin-bottom:16px;
    }

    .feature-title{
        color:#1e293b;
        font-size:24px;
        font-weight:800;
        margin-bottom:12px;
    }

    .feature-text{
        color:#475569;
        font-size:16px;
        line-height:1.8;
        font-weight:500;
    }

    </style>
    """, unsafe_allow_html=True)

    # ================= HERO =================
    st.markdown("""
    <div class="hero-box">

        <div class="hero-title">
            🤖 AI Smart Analytics Dashboard
        </div>

        <div class="hero-text">
            Premium intelligent platform for real-time accident detection,
            customer churn prediction, and advanced business analytics
            powered by advanced deep learning intelligence systems.
        </div>

    </div>
    """, unsafe_allow_html=True)

    # ================= MAIN SECTION =================
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

    # ================= FEATURES =================
    c1, c2, c3, c4 = st.columns(4)

    features = [
        (
            "🚀",
            "Fast Performance",
            "Optimized AI inference engine for real-time prediction."
        ),
        (
            "🧠",
            "Deep Learning",
            "Advanced neural network architecture for smart analytics."
        ),
        (
            "📊",
            "Analytics Ready",
            "Business-focused prediction and reporting intelligence."
        ),
        (
            "🔒",
            "Reliable",
            "Stable deployment architecture with scalable design."
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

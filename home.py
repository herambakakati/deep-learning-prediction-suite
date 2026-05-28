```python
import streamlit as st


def render():

    # ================= PAGE STYLE =================
    st.markdown("""
    <style>

    .block-container{
        max-width:1400px;
        padding-top:2rem;
        padding-bottom:2rem;
    }

    .hero-box{
        background-image:
        linear-gradient(rgba(15,23,42,0.75),
        rgba(30,58,138,0.75)),
        url('https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1600&q=80');

        background-size:cover;
        background-position:center;
        background-repeat:no-repeat;

        padding:60px;
        border-radius:28px;
        margin-bottom:35px;

        box-shadow:0 18px 45px rgba(0,0,0,0.18);
    }

    .hero-title{
        color:white;
        font-size:54px;
        font-weight:800;
        margin-bottom:18px;
    }

    .hero-text{
        color:white;
        font-size:21px;
        line-height:1.8;
        max-width:900px;
    }

    .card{
        padding:32px;
        border-radius:24px;
        min-height:220px;
        box-shadow:0 12px 30px rgba(0,0,0,0.08);
    }

    .blue-card{
        background:linear-gradient(135deg,#eef4ff,#dbeafe);
    }

    .orange-card{
        background:linear-gradient(135deg,#fff7ed,#ffedd5);
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
        padding:24px;
        border-radius:22px;
        text-align:center;
        min-height:220px;
        box-shadow:0 10px 24px rgba(0,0,0,0.08);
    }

    .feature-icon{
        font-size:42px;
        margin-bottom:14px;
    }

    .feature-title{
        color:#1e3a8a;
        font-size:22px;
        font-weight:700;
        margin-bottom:14px;
    }

    .feature-text{
        color:#475569;
        font-size:16px;
        line-height:1.7;
    }

    </style>
    """, unsafe_allow_html=True)

    # ================= HERO =================
    st.markdown(
        """
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
        """,
        unsafe_allow_html=True
    )

    # ================= MAIN CARDS =================
    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div class="card blue-card">

                <div class="card-title">
                    🚗 Accident Detection
                </div>

                <div class="card-text">
                    Upload road traffic images and instantly detect
                    accident scenarios using trained deep learning CNN models.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="card orange-card">

                <div class="card-title">
                    📉 Churn Prediction
                </div>

                <div class="card-text">
                    Predict customer churn risk using AI-powered analytics
                    and actionable business intelligence.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ================= FEATURES =================
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

    cols = [c1, c2, c3, c4]

    for col, feature in zip(cols, features):

        icon, title, desc = feature

        with col:

            st.markdown(
                f"""
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
                """,
                unsafe_allow_html=True
            )
```

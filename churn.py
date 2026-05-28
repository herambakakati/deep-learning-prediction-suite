import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd
import os
import gdown

# =====================================================
# CSS
# =====================================================

def load_css():

    st.markdown("""
    <style>

    .hero-banner{

        background:
            linear-gradient(
                rgba(15,23,42,0.80),
                rgba(30,58,138,0.80)
            ),
            url("https://images.unsplash.com/photo-1554224155-6726b3ff858f?auto=format&fit=crop&w=1600&q=80");

        background-size:cover;
        background-position:center;

        padding:65px;

        border-radius:28px;

        margin-bottom:35px;

        box-shadow:
            0 18px 45px rgba(0,0,0,0.18);
    }

    .hero-title{

        color:white;

        font-size:54px;

        font-weight:800;

        margin-bottom:16px;
    }

    .hero-text{

        color:rgba(255,255,255,0.95);

        font-size:20px;

        line-height:1.9;

        max-width:900px;
    }

    .glass-card{

        background:
            rgba(255,255,255,0.92);

        padding:28px;

        border-radius:24px;

        box-shadow:
            0 12px 30px rgba(0,0,0,0.08);

        margin-bottom:20px;
    }

    .result-danger{

        background:
            linear-gradient(
                135deg,
                #fee2e2,
                #fecaca
            );

        padding:35px;

        border-radius:24px;

        text-align:center;
    }

    .result-safe{

        background:
            linear-gradient(
                135deg,
                #dcfce7,
                #bbf7d0
            );

        padding:35px;

        border-radius:24px;

        text-align:center;
    }

    .result-title{

        font-size:42px;

        font-weight:800;

        margin-bottom:10px;

        color:#1e293b;
    }

    .result-subtitle{

        font-size:26px;

        font-weight:700;

        color:#334155;
    }

    </style>
    """, unsafe_allow_html=True)

# =====================================================
# DOWNLOAD MODEL
# =====================================================

def download_model():

    model_path = "churn_model.keras"

    if not os.path.exists(model_path):

        with st.spinner("Downloading churn model..."):

            file_id = "YOUR_GOOGLE_DRIVE_FILE_ID"

            url = f"https://drive.google.com/uc?id={file_id}"

            gdown.download(
                url,
                model_path,
                quiet=False
            )

    return model_path

# =====================================================
# LOAD MODEL
# =====================================================

@st.cache_resource
def load_model():

    model_path = download_model()

    model = tf.keras.models.load_model(
        model_path
    )

    return model

# =====================================================
# MAIN RENDER
# =====================================================

def render():

    load_css()

    st.html("""
    <div class="hero-banner">

        <div class="hero-title">
            📉 AI Customer Churn Intelligence
        </div>

        <div class="hero-text">
            Predict customer churn risk using intelligent
            deep learning analytics and business-focused
            prediction intelligence.
        </div>

    </div>
    """)

    st.html("""
    <div class="glass-card">
        <h2 style="color:#1e3a8a;">
            Customer Information
        </h2>
    </div>
    """)

    col1, col2 = st.columns(2)

    with col1:

        credit_score = st.number_input(
            "Credit Score",
            300,
            900,
            650
        )

        age = st.number_input(
            "Age",
            18,
            100,
            35
        )

        balance = st.number_input(
            "Balance",
            0.0,
            300000.0,
            50000.0
        )

    with col2:

        products = st.number_input(
            "Products",
            1,
            4,
            2
        )

        active = st.selectbox(
            "Is Active Member",
            [0, 1]
        )

        salary = st.number_input(
            "Estimated Salary",
            0.0,
            300000.0,
            70000.0
        )

    if st.button("✨ Predict Churn Risk"):

        try:

            model = load_model()

            input_data = np.array([[
                credit_score,
                age,
                balance,
                products,
                active,
                salary
            ]])

            prediction = model.predict(
                input_data,
                verbose=0
            )[0][0]

            if prediction > 0.5:

                confidence = prediction * 100

                st.html(f"""
                <div class="result-danger">

                    <div class="result-title">
                        ⚠️ High Churn Risk
                    </div>

                    <div class="result-subtitle">
                        {confidence:.2f}% Confidence
                    </div>

                </div>
                """)

            else:

                confidence = (1 - prediction) * 100

                st.html(f"""
                <div class="result-safe">

                    <div class="result-title">
                        ✅ Customer Retained
                    </div>

                    <div class="result-subtitle">
                        {confidence:.2f}% Confidence
                    </div>

                </div>
                """)

        except Exception as e:

            st.error(
                f"Prediction failed: {str(e)}"
            )

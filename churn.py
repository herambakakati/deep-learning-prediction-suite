import streamlit as st
import tensorflow as tf
import pandas as pd
import pickle
import os

# =====================================================
# LOAD MODEL
# =====================================================

@st.cache_resource
def load_assets():

    model_path = "models/churn_model.h5"
    scaler_path = "models/scaler.pkl"
    columns_path = "models/feature_columns.pkl"

    # CHECK FILES

    if not os.path.exists(model_path):
        raise FileNotFoundError(
            f"Missing model file: {model_path}"
        )

    if not os.path.exists(scaler_path):
        raise FileNotFoundError(
            f"Missing scaler file: {scaler_path}"
        )

    if not os.path.exists(columns_path):
        raise FileNotFoundError(
            f"Missing feature columns file: {columns_path}"
        )

    # LOAD MODEL

    model = tf.keras.models.load_model(
        model_path
    )

    # LOAD SCALER

    with open(
        scaler_path,
        "rb"
    ) as f:

        scaler = pickle.load(f)

    # LOAD FEATURE COLUMNS

    with open(
        columns_path,
        "rb"
    ) as f:

        feature_columns = pickle.load(f)

    return model, scaler, feature_columns


# =====================================================
# MAIN PAGE
# =====================================================

def render():

    # =====================================================
    # CSS
    # =====================================================

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

        border-radius:28px;

        padding:60px;

        margin-bottom:35px;

        box-shadow:
        0 18px 45px rgba(0,0,0,0.18);
    }

    .hero-title{

        font-size:54px;

        font-weight:800;

        color:white;

        margin-bottom:15px;
    }

    .hero-text{

        font-size:20px;

        color:rgba(255,255,255,0.95);

        line-height:1.9;
    }

    .form-card{

        background:
        linear-gradient(
            135deg,
            #ffffff,
            #eef4ff
        );

        padding:28px;

        border-radius:24px;

        margin-bottom:22px;

        box-shadow:
        0 12px 28px rgba(0,0,0,0.08);
    }

    .card-title{

        color:#1e3a8a;

        font-size:30px;

        font-weight:800;
    }

    .prediction-box{

        background:
        linear-gradient(
            135deg,
            #dbeafe,
            #bfdbfe
        );

        padding:32px;

        border-radius:22px;

        text-align:center;

        margin-top:30px;
    }

    .prediction-title{

        color:#1e3a8a;

        font-size:28px;

        font-weight:700;
    }

    .prediction-score{

        color:#1e3a8a;

        font-size:58px;

        font-weight:800;
    }

    .danger-box{

        background:
        linear-gradient(
            135deg,
            #fee2e2,
            #fecaca
        );

        padding:30px;

        border-radius:22px;

        text-align:center;

        margin-top:20px;
    }

    .safe-box{

        background:
        linear-gradient(
            135deg,
            #dcfce7,
            #bbf7d0
        );

        padding:30px;

        border-radius:22px;

        text-align:center;

        margin-top:20px;
    }

    .danger-title,
    .safe-title{

        font-size:42px;

        font-weight:800;
    }

    .danger-sub,
    .safe-sub{

        font-size:30px;

        font-weight:700;
    }

    .danger-title{
        color:#991b1b;
    }

    .danger-sub{
        color:#b91c1c;
    }

    .safe-title{
        color:#166534;
    }

    .safe-sub{
        color:#15803d;
    }

    </style>
    """, unsafe_allow_html=True)

    # =====================================================
    # HERO
    # =====================================================

    st.markdown("""
    <div class="hero-banner">

        <div class="hero-title">
            📉 AI Customer Churn Intelligence
        </div>

        <div class="hero-text">
            Predict customer churn risk using intelligent
            deep learning analytics and business-ready
            customer retention intelligence.
        </div>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # LOAD FILES
    # =====================================================

    try:

        model, scaler, feature_columns = load_assets()

    except Exception as e:

        st.error(
            f"Model loading failed: {str(e)}"
        )

        return

    # =====================================================
    # INPUTS
    # =====================================================

    left, right = st.columns(2)

    with left:

        st.markdown("""
        <div class="form-card">
            <div class="card-title">
                👤 Customer Profile
            </div>
        </div>
        """, unsafe_allow_html=True)

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

        tenure = st.number_input(
            "Tenure",
            0,
            10,
            5
        )

        balance = st.number_input(
            "Balance",
            0.0,
            300000.0,
            50000.0
        )

        estimated_salary = st.number_input(
            "Estimated Salary",
            0.0,
            300000.0,
            50000.0
        )

        num_products = st.number_input(
            "Number of Products",
            1,
            4,
            1
        )

    with right:

        st.markdown("""
        <div class="form-card">
            <div class="card-title">
                🏦 Banking Attributes
            </div>
        </div>
        """, unsafe_allow_html=True)

        has_cr_card = st.selectbox(
            "Has Credit Card",
            ["No", "Yes"]
        )

        is_active_member = st.selectbox(
            "Is Active Member",
            ["No", "Yes"]
        )

        geography = st.selectbox(
            "Geography",
            ["France", "Germany", "Spain"]
        )

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

    # =====================================================
    # PREDICTION
    # =====================================================

    if st.button(
        "✨ Analyze Customer Churn Risk"
    ):

        input_data = {

            "CreditScore":
            credit_score,

            "Age":
            age,

            "Tenure":
            tenure,

            "Balance":
            balance,

            "EstimatedSalary":
            estimated_salary,

            "NumOfProducts":
            num_products,

            "HasCrCard":
            1 if has_cr_card == "Yes" else 0,

            "IsActiveMember":
            1 if is_active_member == "Yes" else 0,

            "Geography_Germany":
            1 if geography == "Germany" else 0,

            "Geography_Spain":
            1 if geography == "Spain" else 0,

            "Gender_Male":
            1 if gender == "Male" else 0
        }

        input_df = pd.DataFrame(
            [input_data]
        )

        for col in feature_columns:

            if col not in input_df.columns:

                input_df[col] = 0

        input_df = input_df[
            feature_columns
        ]

        scaled_data = scaler.transform(
            input_df
        )

        prediction = model.predict(
            scaled_data,
            verbose=0
        )[0][0]

        st.markdown(f"""
        <div class="prediction-box">

            <div class="prediction-title">
                Prediction Score
            </div>

            <div class="prediction-score">
                {prediction:.4f}
            </div>

        </div>
        """, unsafe_allow_html=True)

        if prediction > 0.5:

            st.markdown(f"""
            <div class="danger-box">

                <div class="danger-title">
                    ⚠️ High Churn Risk
                </div>

                <div class="danger-sub">
                    {prediction * 100:.2f}% Probability
                </div>

            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown(f"""
            <div class="safe-box">

                <div class="safe-title">
                    ✅ Customer Likely To Stay
                </div>

                <div class="safe-sub">
                    {(1 - prediction) * 100:.2f}% Confidence
                </div>

            </div>
            """, unsafe_allow_html=True)

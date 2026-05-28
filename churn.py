import streamlit as st
import tensorflow as tf
import pandas as pd
import pickle
import os

# =====================================================
# LOAD MODEL + FILES
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
        model_path,
        compile=False
    )

    # LOAD SCALER

    with open(scaler_path, "rb") as f:
        scaler = pickle.load(f)

    # LOAD FEATURE COLUMNS

    with open(columns_path, "rb") as f:
        feature_columns = pickle.load(f)

    return model, scaler, feature_columns


# =====================================================
# MAIN FUNCTION
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
            rgba(15,23,42,0.82),
            rgba(30,58,138,0.82)
        ),
        url("https://images.unsplash.com/photo-1554224155-6726b3ff858f?auto=format&fit=crop&w=1600&q=80");

        background-size:cover;
        background-position:center;

        border-radius:28px;

        padding:65px;

        margin-bottom:35px;

        box-shadow:
        0 18px 45px rgba(0,0,0,0.18);
    }

    .hero-title{

        font-size:58px;

        font-weight:800;

        color:white;

        margin-bottom:18px;
    }

    .hero-text{

        font-size:21px;

        color:rgba(255,255,255,0.96);

        line-height:1.9;
    }

    .section-card{

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

        font-size:34px;

        font-weight:800;
    }

    .prediction-box{

        background:
        linear-gradient(
            135deg,
            #dbeafe,
            #bfdbfe
        );

        padding:35px;

        border-radius:24px;

        text-align:center;

        margin-top:30px;

        box-shadow:
        0 10px 25px rgba(59,130,246,0.18);
    }

    .prediction-title{

        color:#1e3a8a;

        font-size:30px;

        font-weight:700;

        margin-bottom:15px;
    }

    .prediction-score{

        color:#1e3a8a;

        font-size:64px;

        font-weight:800;
    }

    .danger-box{

        background:
        linear-gradient(
            135deg,
            #fee2e2,
            #fecaca
        );

        padding:34px;

        border-radius:24px;

        text-align:center;

        margin-top:24px;

        box-shadow:
        0 10px 25px rgba(239,68,68,0.15);
    }

    .safe-box{

        background:
        linear-gradient(
            135deg,
            #dcfce7,
            #bbf7d0
        );

        padding:34px;

        border-radius:24px;

        text-align:center;

        margin-top:24px;

        box-shadow:
        0 10px 25px rgba(34,197,94,0.15);
    }

    .danger-title,
    .safe-title{

        font-size:42px;

        font-weight:800;

        margin-bottom:14px;
    }

    .danger-sub,
    .safe-sub{

        font-size:28px;

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

    div[data-baseweb="select"] > div{
        border-radius:16px !important;
    }

    .stNumberInput input{
        border-radius:14px !important;
    }

    </style>
    """, unsafe_allow_html=True)

    # =====================================================
    # HERO SECTION
    # =====================================================

    st.html("""
    <div class="hero-banner">

        <div class="hero-title">
            📉 AI Customer Churn Intelligence
        </div>

        <div class="hero-text">
            Predict customer churn risk using intelligent
            deep learning analytics and business-focused
            customer retention intelligence.
        </div>

    </div>
    """)

    # =====================================================
    # LOAD ASSETS
    # =====================================================

    try:

        model, scaler, feature_columns = load_assets()

    except Exception as e:

        st.error(
            f"Model loading failed: {str(e)}"
        )

        return

    # =====================================================
    # INPUT SECTION
    # =====================================================

    left, right = st.columns(2)

    # =====================================================
    # LEFT SIDE
    # =====================================================

    with left:

        st.html("""
        <div class="section-card">

            <div class="card-title">
                👤 Customer Profile
            </div>

        </div>
        """)

        credit_score = st.number_input(
            "Credit Score",
            min_value=300,
            max_value=900,
            value=650
        )

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=35
        )

        tenure = st.number_input(
            "Tenure",
            min_value=0,
            max_value=10,
            value=5
        )

        balance = st.number_input(
            "Balance",
            min_value=0.0,
            max_value=300000.0,
            value=50000.0
        )

        estimated_salary = st.number_input(
            "Estimated Salary",
            min_value=0.0,
            max_value=300000.0,
            value=50000.0
        )

        num_products = st.number_input(
            "Number of Products",
            min_value=1,
            max_value=4,
            value=1
        )

    # =====================================================
    # RIGHT SIDE
    # =====================================================

    with right:

        st.html("""
        <div class="section-card">

            <div class="card-title">
                🏦 Banking Attributes
            </div>

        </div>
        """)

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

    st.markdown("")

    # =====================================================
    # PREDICT BUTTON
    # =====================================================

    if st.button(
        "✨ Analyze Customer Churn Risk"
    ):

        # =====================================================
        # INPUT DATA
        # =====================================================

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

        # =====================================================
        # DATAFRAME
        # =====================================================

        input_df = pd.DataFrame(
            [input_data]
        )

        # =====================================================
        # FEATURE ALIGNMENT
        # =====================================================

        for col in feature_columns:

            if col not in input_df.columns:

                input_df[col] = 0

        input_df = input_df[
            feature_columns
        ]

        # =====================================================
        # SCALE
        # =====================================================

        scaled_data = scaler.transform(
            input_df
        )

        # =====================================================
        # PREDICT
        # =====================================================

        prediction = model.predict(
            scaled_data,
            verbose=0
        )[0][0]

        # =====================================================
        # SCORE BOX
        # =====================================================

        st.html(f"""
        <div class="prediction-box">

            <div class="prediction-title">
                Prediction Score
            </div>

            <div class="prediction-score">
                {prediction:.4f}
            </div>

        </div>
        """)

        # =====================================================
        # RESULT
        # =====================================================

        if prediction > 0.5:

            st.html(f"""
            <div class="danger-box">

                <div class="danger-title">
                    ⚠️ High Churn Risk
                </div>

                <div class="danger-sub">
                    {prediction * 100:.2f}% Probability
                </div>

            </div>
            """)

        else:

            st.html(f"""
            <div class="safe-box">

                <div class="safe-title">
                    ✅ Customer Likely To Stay
                </div>

                <div class="safe-sub">
                    {(1 - prediction) * 100:.2f}% Confidence
                </div>

            </div>
            """)

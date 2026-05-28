import streamlit as st
import tensorflow as tf
import pandas as pd
import pickle
import os
import gdown

# =====================================================
# DOWNLOAD MODEL FILES
# =====================================================

def download_assets():

    os.makedirs("models", exist_ok=True)

    files = {

        "models/churn_model.keras":
        "YOUR_CHURN_MODEL_FILE_ID",

        "models/scaler.pkl":
        "YOUR_SCALER_FILE_ID",

        "models/feature_columns.pkl":
        "YOUR_FEATURE_COLUMNS_FILE_ID"
    }

    for path, file_id in files.items():

        if not os.path.exists(path):

            with st.spinner(f"Downloading {os.path.basename(path)}..."):

                url = f"https://drive.google.com/uc?id={file_id}"

                gdown.download(
                    url,
                    path,
                    quiet=False
                )

# =====================================================
# LOAD ASSETS
# =====================================================

@st.cache_resource
def load_assets():

    download_assets()

    model_path = "models/churn_model.keras"

    scaler_path = "models/scaler.pkl"

    columns_path = "models/feature_columns.pkl"

    model = tf.keras.models.load_model(
        model_path
    )

    with open(scaler_path, "rb") as f:

        scaler = pickle.load(f)

    with open(columns_path, "rb") as f:

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
            rgba(15,23,42,0.78),
            rgba(30,58,138,0.78)
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

        margin-bottom:14px;
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

        margin-top:20px;
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

        margin-top:20px;
    }

    .result-title{

        font-size:40px;

        font-weight:800;

        color:#1e293b;

        margin-bottom:10px;
    }

    .result-text{

        font-size:28px;

        font-weight:700;

        color:#334155;
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
            prediction intelligence.
        </div>

    </div>
    """)

    # =====================================================
    # LOAD MODEL
    # =====================================================

    try:

        model, scaler, feature_columns = load_assets()

    except Exception as e:

        st.error(
            f"Model loading failed: {str(e)}"
        )

        return

    # =====================================================
    # INPUT SECTIONS
    # =====================================================

    left, right = st.columns(2)

    with left:

        st.html("""
        <div class="form-card">

            <div class="card-title">
                👤 Customer Profile
            </div>

        </div>
        """)

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

    with right:

        st.html("""
        <div class="form-card">

            <div class="card-title">
                🏦 Banking Attributes
            </div>

        </div>
        """)

        geography = st.selectbox(
            "Geography",
            ["France", "Germany", "Spain"]
        )

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        has_cr_card = st.selectbox(
            "Has Credit Card",
            ["No", "Yes"]
        )

        is_active_member = st.selectbox(
            "Is Active Member",
            ["No", "Yes"]
        )

    # =====================================================
    # PREDICTION
    # =====================================================

    if st.button(
        "✨ Analyze Customer Churn Risk"
    ):

        try:

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
                1,

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

            if prediction > 0.5:

                st.html(f"""
                <div class="result-danger">

                    <div class="result-title">
                        ⚠️ High Churn Risk
                    </div>

                    <div class="result-text">
                        {prediction*100:.2f}% Probability
                    </div>

                </div>
                """)

            else:

                st.html(f"""
                <div class="result-safe">

                    <div class="result-title">
                        ✅ Customer Likely To Stay
                    </div>

                    <div class="result-text">
                        {(1-prediction)*100:.2f}% Confidence
                    </div>

                </div>
                """)

        except Exception as e:

            st.error(
                f"Prediction failed: {str(e)}"
            )

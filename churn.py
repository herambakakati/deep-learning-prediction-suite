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

    if (
        not os.path.exists(model_path)
        or not os.path.exists(scaler_path)
        or not os.path.exists(columns_path)
    ):
        return None, None, None

    try:

        model = tf.keras.models.load_model(
            model_path
        )

        with open(scaler_path, "rb") as f:
            scaler = pickle.load(f)

        with open(columns_path, "rb") as f:
            feature_columns = pickle.load(f)

        return model, scaler, feature_columns

    except Exception as e:

        st.error(
            f"Asset loading failed: {e}"
        )

        return None, None, None


# =====================================================
# MAIN UI
# =====================================================

def render():

    # =====================================================
    # LOAD ASSETS
    # =====================================================

    model, scaler, feature_columns = load_assets()

    # =====================================================
    # UNIQUE CHURN CSS
    # =====================================================

    st.markdown("""
    <style>

    /* HERO */

    .churn-hero-banner{

        background:
        linear-gradient(
            rgba(15,23,42,0.78),
            rgba(30,58,138,0.78)
        ),
        url("https://images.unsplash.com/photo-1554224155-6726b3ff858f?auto=format&fit=crop&w=1600&q=80");

        background-size:cover;
        background-position:center;

        border-radius:28px;

        padding:55px;

        margin-bottom:35px;

        box-shadow:
        0 18px 45px rgba(0,0,0,0.18);
    }

    .churn-hero-title{

        font-size:52px;

        font-weight:800;

        color:white;

        margin-bottom:14px;
    }

    .churn-hero-text{

        font-size:20px;

        color:rgba(255,255,255,0.95);

        line-height:1.8;

        max-width:850px;

        font-weight:500;
    }

    /* FORM CARD */

    .churn-form-card{

        background:
        linear-gradient(
            135deg,
            #ffffff,
            #eef4ff
        );

        padding:28px;

        border-radius:24px;

        box-shadow:
        0 12px 35px rgba(0,0,0,0.08);

        margin-bottom:22px;
    }

    .churn-orange-card{

        background:
        linear-gradient(
            135deg,
            #ffffff,
            #fff7ed
        );
    }

    .churn-card-title{

        color:#1e3a8a;

        font-size:32px;

        font-weight:800;

        margin-bottom:10px;
    }

    .churn-card-subtitle{

        color:#475569;

        font-size:16px;

        line-height:1.7;

        font-weight:600;
    }

    /* INFO BOX */

    .churn-info-box{

        background:white;

        border:1px solid #e2e8f0;

        padding:16px 18px;

        border-radius:16px;

        margin-bottom:14px;

        box-shadow:
        0 8px 20px rgba(0,0,0,0.05);

        font-size:16px;

        font-weight:700;

        color:#0f172a;
    }

    /* PREDICTION BOX */

    .churn-prediction-box{

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

    .churn-prediction-title{

        color:#1e3a8a;

        font-size:28px;

        font-weight:700;
    }

    .churn-prediction-score{

        color:#1e3a8a;

        font-size:58px;

        font-weight:800;
    }

    /* DANGER */

    .churn-danger-box{

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

    .churn-danger-title{

        color:#991b1b;

        font-size:42px;

        font-weight:800;
    }

    .churn-danger-sub{

        color:#b91c1c;

        font-size:30px;

        font-weight:700;
    }

    /* SAFE */

    .churn-safe-box{

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

    .churn-safe-title{

        color:#166534;

        font-size:42px;

        font-weight:800;
    }

    .churn-safe-sub{

        color:#15803d;

        font-size:30px;

        font-weight:700;
    }

    </style>
    """, unsafe_allow_html=True)

    # =====================================================
    # HERO
    # =====================================================

    st.markdown("""
    <div class="churn-hero-banner">

        <div class="churn-hero-title">
            📉 AI Customer Churn Intelligence
        </div>

        <div class="churn-hero-text">
            Predict customer churn risk using intelligent deep learning analytics,
            customer behavior intelligence, and business-ready probability insights.
        </div>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # MODEL WARNING
    # =====================================================

    if model is None:

        st.warning("""
        Model files not found.

        Upload:

        - models/churn_model.h5
        - models/scaler.pkl
        - models/feature_columns.pkl
        """)

    # =====================================================
    # LAYOUT
    # =====================================================

    left, right = st.columns(2)

    # =====================================================
    # LEFT
    # =====================================================

    with left:

        st.markdown("""
        <div class="churn-form-card">

            <div class="churn-card-title">
                👤 Customer Profile
            </div>

            <div class="churn-card-subtitle">
                Complete customer demographic,
                financial, and product information.
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

    # =====================================================
    # RIGHT
    # =====================================================

    with right:

        st.markdown("""
        <div class="churn-form-card churn-orange-card">

            <div class="churn-card-title">
                🏦 Banking Attributes
            </div>

        </div>
        """, unsafe_allow_html=True)

        info_items = [

            "📊 Customer engagement indicators",

            "💳 Product ownership insights",

            "🌍 Geographic segmentation",

            "🎯 Retention intelligence signals"
        ]

        for item in info_items:

            st.markdown(f"""
            <div class="churn-info-box">
                {item}
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

        has_cr_card = (
            1 if has_cr_card == "Yes"
            else 0
        )

        is_active_member = (
            1 if is_active_member == "Yes"
            else 0
        )

    # =====================================================
    # PREDICTION BUTTON
    # =====================================================

    if st.button(
        "✨ Analyze Customer Churn Risk"
    ):

        if model is None:

            st.error("""
            Prediction unavailable.

            Upload model files first.
            """)

            return

        input_data = {

            'CreditScore': credit_score,

            'Age': age,

            'Tenure': tenure,

            'Balance': balance,

            'EstimatedSalary': estimated_salary,

            'NumOfProducts': num_products,

            'HasCrCard': has_cr_card,

            'IsActiveMember': is_active_member,

            'Geography_Germany':
            1 if geography == "Germany" else 0,

            'Geography_Spain':
            1 if geography == "Spain" else 0,

            'Gender_Male':
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

        # =====================================================
        # SCORE
        # =====================================================

        st.markdown(f"""
        <div class="churn-prediction-box">

            <div class="churn-prediction-title">
                Prediction Score
            </div>

            <div class="churn-prediction-score">
                {prediction:.4f}
            </div>

        </div>
        """, unsafe_allow_html=True)

        # =====================================================
        # FINAL RESULT
        # =====================================================

        if prediction > 0.5:

            st.markdown(f"""
            <div class="churn-danger-box">

                <div class="churn-danger-title">
                    ⚠️ High Churn Risk
                </div>

                <div class="churn-danger-sub">
                    {prediction * 100:.2f}% Probability
                </div>

            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown(f"""
            <div class="churn-safe-box">

                <div class="churn-safe-title">
                    ✅ Customer Likely To Stay
                </div>

                <div class="churn-safe-sub">
                    {(1 - prediction) * 100:.2f}% Confidence
                </div>

            </div>
            """, unsafe_allow_html=True)

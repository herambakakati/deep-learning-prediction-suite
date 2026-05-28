import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
import os

# =========================
# LOAD MODEL
# =========================
@st.cache_resource
def load_accident_model():

    model_path = "models/best_accident_model.keras"

    # Model not uploaded yet
    if not os.path.exists(model_path):
        return None

    try:
        model = tf.keras.models.load_model(model_path)
        return model

    except Exception as e:
        st.error(f"Model loading failed: {e}")
        return None


# =========================
# PREPROCESS IMAGE
# =========================
def preprocess_image(uploaded_file):

    file_bytes = np.asarray(
        bytearray(uploaded_file.read()),
        dtype=np.uint8
    )

    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if img is None:
        return None, None

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    resized = cv2.resize(img_rgb, (224, 224))
    resized = resized.astype(np.float32) / 255.0

    img_input = np.expand_dims(resized, axis=0)

    return img_rgb, img_input


# =========================
# MAIN UI
# =========================
def render():

    # ================= CSS =================
    st.markdown("""
    <style>

    .block-container{
        max-width:1450px;
        padding-top:2rem;
    }

    .hero-banner{
        background:
        linear-gradient(rgba(15,23,42,0.75),
        rgba(30,58,138,0.75)),
        url("https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=1600&q=80");

        background-size:cover;
        background-position:center;
        border-radius:28px;
        padding:60px;
        margin-bottom:30px;
        box-shadow:0 18px 45px rgba(0,0,0,0.18);
    }

    .hero-title{
        color:white;
        font-size:52px;
        font-weight:800;
        margin-bottom:12px;
    }

    .hero-text{
        color:rgba(255,255,255,0.95);
        font-size:20px;
        line-height:1.8;
        max-width:850px;
        font-weight:500;
    }

    .card{
        background:white;
        padding:24px;
        border-radius:24px;
        box-shadow:0 10px 25px rgba(0,0,0,0.08);
        margin-bottom:18px;
    }

    .card-title{
        color:#1e3a8a;
        font-size:30px;
        font-weight:800;
    }

    .card-text{
        color:#475569;
        font-size:16px;
        font-weight:600;
        margin-top:8px;
    }

    .engine-item{
        background:linear-gradient(135deg,#ecfdf5,#d1fae5);
        color:#065f46;
        padding:18px;
        border-radius:16px;
        margin-bottom:14px;
        font-size:16px;
        font-weight:700;
        box-shadow:0 8px 18px rgba(0,0,0,0.05);
    }

    div.stButton > button{
        width:100%;
        height:70px;
        border-radius:18px;
        border:none;
        background:linear-gradient(135deg,#6366f1,#8b5cf6);
        color:white !important;
        font-size:20px;
        font-weight:800;
        box-shadow:0 14px 30px rgba(99,102,241,0.28);
    }

    .prediction-box{
        background:linear-gradient(135deg,#dbeafe,#bfdbfe);
        padding:35px;
        border-radius:24px;
        text-align:center;
        box-shadow:0 12px 25px rgba(0,0,0,0.08);
    }

    .prediction-box h3{
        color:#1e3a8a;
        font-size:30px;
        font-weight:700;
    }

    .prediction-box h1{
        color:#1e40af;
        font-size:64px;
        font-weight:900;
    }

    .danger-box{
        background:linear-gradient(135deg,#fee2e2,#fecaca);
        padding:35px;
        border-radius:24px;
        text-align:center;
        box-shadow:0 12px 25px rgba(0,0,0,0.08);
    }

    .danger-box h1{
        color:#991b1b;
        font-size:42px;
        font-weight:800;
    }

    .danger-box h2{
        color:#b91c1c;
        font-size:30px;
        font-weight:700;
    }

    .safe-box{
        background:linear-gradient(135deg,#dcfce7,#bbf7d0);
        padding:35px;
        border-radius:24px;
        text-align:center;
        box-shadow:0 12px 25px rgba(0,0,0,0.08);
    }

    .safe-box h1{
        color:#166534;
        font-size:42px;
        font-weight:800;
    }

    .safe-box h2{
        color:#15803d;
        font-size:30px;
        font-weight:700;
    }

    </style>
    """, unsafe_allow_html=True)

    # ================= HERO =================
    st.markdown("""
    <div class="hero-banner">

        <div class="hero-title">
            🚗 AI Accident Detection Intelligence
        </div>

        <div class="hero-text">
            Upload traffic images and let the AI engine instantly
            detect accident scenarios using deep learning intelligence.
        </div>

    </div>
    """, unsafe_allow_html=True)

    # ================= LOAD MODEL =================
    model = load_accident_model()

    # ================= MODEL MISSING =================
    if model is None:

        st.warning("""
        Accident model file is missing.

        Upload later:
        models/best_accident_model.keras
        """)

    # ================= TOP SECTION =================
    left, right = st.columns([1.2, 1])

    # ================= LEFT =================
    with left:

        st.markdown("""
        <div class="card">

            <div class="card-title">
                📤 Upload Traffic Image
            </div>

            <div class="card-text">
                Supported formats: JPG, JPEG, PNG
            </div>

        </div>
        """, unsafe_allow_html=True)

        uploaded_file = st.file_uploader(
            "Choose traffic image",
            type=["jpg", "jpeg", "png"],
            key="accident_upload"
        )

    # ================= RIGHT =================
    with right:

        st.markdown("""
        <div class="card">

            <div class="card-title">
                🧠 AI Detection Engine
            </div>

        </div>
        """, unsafe_allow_html=True)

        features = [
            "⚡ Real-time CNN image inference",
            "🎯 Confidence-based classification",
            "🚀 Fast local processing",
            "🧠 Deep learning detection engine"
        ]

        for item in features:

            st.markdown(
                f'<div class="engine-item">{item}</div>',
                unsafe_allow_html=True
            )

    # ================= PROCESS IMAGE =================
    if uploaded_file is not None:

        display_img, img_input = preprocess_image(uploaded_file)

        if display_img is None:
            st.error("Invalid image uploaded.")
            return

        st.markdown("---")

        st.markdown("""
        <div class="card">

            <div class="card-title">
                🖼 Uploaded Preview
            </div>

            <div class="card-text">
                Uploaded image ready for intelligent analysis
            </div>

        </div>
        """, unsafe_allow_html=True)

        st.image(display_img, width=950)

        st.markdown("<br>", unsafe_allow_html=True)

        b1, b2, b3 = st.columns([1,2,1])

        with b2:

            analyze = st.button(
                "✨ Analyze Accident Risk",
                key="analyze_accident_button"
            )

        # ================= PREDICTION =================
        if analyze:

            # MODEL MISSING
            if model is None:

                st.error("""
                Prediction unavailable.

                Upload model file:
                models/best_accident_model.keras
                """)

                return

            with st.spinner("AI analyzing image..."):

                prediction = model.predict(
                    img_input,
                    verbose=0
                )[0][0]

                st.markdown("<br>", unsafe_allow_html=True)

                col1, col2 = st.columns(2)

                # ================= SCORE =================
                with col1:

                    st.markdown(f"""
                    <div class="prediction-box">

                        <h3>Prediction Score</h3>

                        <h1>{prediction:.4f}</h1>

                    </div>
                    """, unsafe_allow_html=True)

                # ================= RESULT =================
                with col2:

                    if prediction < 0.5:

                        confidence = (1 - prediction) * 100

                        st.markdown(f"""
                        <div class="danger-box">

                            <h1>⚠️ Accident Detected</h1>

                            <h2>{confidence:.2f}% Confidence</h2>

                        </div>
                        """, unsafe_allow_html=True)

                    else:

                        confidence = prediction * 100

                        st.markdown(f"""
                        <div class="safe-box">

                            <h1>✅ No Accident Detected</h1>

                            <h2>{confidence:.2f}% Confidence</h2>

                        </div>
                        """, unsafe_allow_html=True)


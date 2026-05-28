import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
import os


# =====================================================
# LOAD MODEL
# =====================================================

@st.cache_resource
def load_accident_model():

    model_path = "models/best_accident_model.keras"

    if not os.path.exists(model_path):

        raise FileNotFoundError(
            f"Model file not found: {model_path}"
        )

    model = tf.keras.models.load_model(
        model_path
    )

    return model


# =====================================================
# IMAGE PREPROCESS
# =====================================================

def preprocess_image(uploaded_file):

    file_bytes = np.asarray(
        bytearray(uploaded_file.read()),
        dtype=np.uint8
    )

    img = cv2.imdecode(
        file_bytes,
        cv2.IMREAD_COLOR
    )

    if img is None:

        return None, None

    img_rgb = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2RGB
    )

    resized = cv2.resize(
        img_rgb,
        (224, 224)
    )

    resized = resized.astype(
        np.float32
    ) / 255.0

    img_input = np.expand_dims(
        resized,
        axis=0
    )

    return img_rgb, img_input


# =====================================================
# MAIN PAGE
# =====================================================

def render():

    st.markdown("""
    <style>

    .hero-banner{

        background:
        linear-gradient(
            rgba(15,23,42,0.75),
            rgba(30,58,138,0.75)
        ),
        url("https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=1600&q=80");

        background-size:cover;
        background-position:center;

        border-radius:28px;

        padding:60px;

        margin-bottom:30px;

        box-shadow:
        0 18px 45px rgba(0,0,0,0.18);
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

        box-shadow:
        0 10px 25px rgba(0,0,0,0.08);

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

        background:
        linear-gradient(
            135deg,
            #ecfdf5,
            #d1fae5
        );

        color:#065f46;

        padding:18px;

        border-radius:16px;

        margin-bottom:14px;

        font-size:16px;

        font-weight:700;
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
    }

    .danger-box{

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

    .safe-box{

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

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero-banner">

        <div class="hero-title">
            🚗 AI Accident Detection Intelligence
        </div>

        <div class="hero-text">
            Upload traffic images and let the AI engine instantly detect
            accident scenarios using real-time deep learning intelligence.
        </div>

    </div>
    """, unsafe_allow_html=True)

    left, right = st.columns([1.2, 1])

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
            type=["jpg", "jpeg", "png"]
        )

    with right:

        st.markdown("""
        <div class="card">

            <div class="card-title">
                🧠 AI Detection Engine
            </div>

        </div>
        """, unsafe_allow_html=True)

        features = [

            "⚡ Real-time CNN inference",

            "🎯 Confidence-based prediction",

            "🚀 Fast local processing",

            "🧠 Deep learning intelligence"
        ]

        for item in features:

            st.markdown(
                f'<div class="engine-item">{item}</div>',
                unsafe_allow_html=True
            )

    if uploaded_file is not None:

        display_img, img_input = preprocess_image(
            uploaded_file
        )

        if display_img is None:

            st.error("Invalid image uploaded.")

            return

        st.image(
            display_img,
            use_column_width=True
        )

        if st.button(
            "✨ Analyze Accident Risk"
        ):

            try:

                model = load_accident_model()

                with st.spinner(
                    "AI analyzing image..."
                ):

                    prediction = model.predict(
                        img_input,
                        verbose=0
                    )[0][0]

                col1, col2 = st.columns(2)

                with col1:

                    st.markdown(f"""
                    <div class="prediction-box">

                        <h2>
                            Prediction Score
                        </h2>

                        <h1>
                            {prediction:.4f}
                        </h1>

                    </div>
                    """, unsafe_allow_html=True)

                with col2:

                    if prediction < 0.5:

                        confidence = (
                            1 - prediction
                        ) * 100

                        st.markdown(f"""
                        <div class="danger-box">

                            <h1>
                                ⚠️ Accident Detected
                            </h1>

                            <h2>
                                {confidence:.2f}% Confidence
                            </h2>

                        </div>
                        """, unsafe_allow_html=True)

                    else:

                        confidence = prediction * 100

                        st.markdown(f"""
                        <div class="safe-box">

                            <h1>
                                ✅ No Accident Detected
                            </h1>

                            <h2>
                                {confidence:.2f}% Confidence
                            </h2>

                        </div>
                        """, unsafe_allow_html=True)

            except Exception as e:

                st.error(
                    f"Prediction failed: {e}"
                )

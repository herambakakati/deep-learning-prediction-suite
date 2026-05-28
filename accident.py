import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
import os
import gdown


# =====================================================
# LOAD MODEL
# =====================================================

@st.cache_resource
def load_accident_model():

    # FULL MODEL FILE

    model_path = "best_accident_model.keras"

    # GOOGLE DRIVE FILE ID

    file_id = "1PH-D7uz2f9dzcbW0u7hLqtMGwSH81ljr"

    # DIRECT DOWNLOAD URL

    url = f"https://drive.google.com/uc?id={file_id}"

    # =====================================================
    # DOWNLOAD MODEL IF NOT EXISTS
    # =====================================================

    if not os.path.exists(model_path):

        with st.spinner("Downloading AI model..."):

            gdown.download(
                url,
                model_path,
                quiet=False
            )

    # =====================================================
    # LOAD MODEL
    # =====================================================

    try:

        model = tf.keras.models.load_model(
            model_path
        )

        return model

    except Exception as e:

        st.error(
            f"Model loading failed: {e}"
        )

        return None


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

    # =====================================================
    # CSS
    # =====================================================

    st.markdown("""
    <style>

    .accident-hero-banner{

        background:
        linear-gradient(
            rgba(15,23,42,0.78),
            rgba(30,58,138,0.78)
        ),
        url("https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=1600&q=80");

        background-size:cover;
        background-position:center;

        border-radius:28px;

        padding:60px;

        margin-bottom:35px;

        box-shadow:
        0 18px 45px rgba(0,0,0,0.18);
    }

    .accident-hero-title{

        color:white;

        font-size:52px;

        font-weight:800;

        margin-bottom:14px;
    }

    .accident-hero-text{

        color:rgba(255,255,255,0.95);

        font-size:20px;

        line-height:1.8;

        max-width:850px;

        font-weight:500;
    }

    .accident-main-card{

        background:white;

        padding:28px;

        border-radius:24px;

        box-shadow:
        0 10px 30px rgba(0,0,0,0.08);

        margin-bottom:20px;
    }

    .accident-card-title{

        color:#1e3a8a;

        font-size:30px;

        font-weight:800;

        margin-bottom:10px;
    }

    .accident-card-text{

        color:#475569;

        font-size:16px;

        font-weight:600;

        line-height:1.7;
    }

    .accident-engine-item{

        background:
        linear-gradient(
            135deg,
            #ecfdf5,
            #d1fae5
        );

        color:#065f46;

        padding:18px;

        border-radius:18px;

        margin-bottom:14px;

        font-size:16px;

        font-weight:700;

        box-shadow:
        0 8px 18px rgba(0,0,0,0.05);
    }

    .accident-prediction-box{

        background:
        linear-gradient(
            135deg,
            #dbeafe,
            #bfdbfe
        );

        padding:35px;

        border-radius:24px;

        text-align:center;

        margin-top:20px;

        box-shadow:
        0 12px 25px rgba(0,0,0,0.08);
    }

    .accident-prediction-box h3{

        color:#1e3a8a;

        font-size:30px;

        font-weight:700;
    }

    .accident-prediction-box h1{

        color:#1e40af;

        font-size:64px;

        font-weight:900;
    }

    .accident-danger-box{

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

        box-shadow:
        0 12px 25px rgba(0,0,0,0.08);
    }

    .accident-danger-box h1{

        color:#991b1b;

        font-size:42px;

        font-weight:800;
    }

    .accident-danger-box h2{

        color:#b91c1c;

        font-size:30px;

        font-weight:700;
    }

    .accident-safe-box{

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

        box-shadow:
        0 12px 25px rgba(0,0,0,0.08);
    }

    .accident-safe-box h1{

        color:#166534;

        font-size:42px;

        font-weight:800;
    }

    .accident-safe-box h2{

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
    <div class="accident-hero-banner">

        <div class="accident-hero-title">
            🚗 AI Accident Detection Intelligence
        </div>

        <div class="accident-hero-text">
            Upload traffic images and let the AI engine instantly detect
            accident scenarios using deep learning intelligence.
        </div>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # LOAD MODEL
    # =====================================================

    model = load_accident_model()

    if model is None:

        st.error("""
        Model could not be loaded.

        Check:
        - Google Drive sharing permission
        - Internet access
        - File availability
        """)

        return

    # =====================================================
    # TOP SECTION
    # =====================================================

    left, right = st.columns([1.2, 1])

    with left:

        st.markdown("""
        <div class="accident-main-card">

            <div class="accident-card-title">
                📤 Upload Traffic Image
            </div>

            <div class="accident-card-text">
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
        <div class="accident-main-card">

            <div class="accident-card-title">
                🧠 AI Detection Engine
            </div>

        </div>
        """, unsafe_allow_html=True)

        features = [

            "⚡ Real-time CNN inference",

            "🎯 Confidence classification",

            "🚀 Fast image processing",

            "🧠 Deep learning engine"
        ]

        for item in features:

            st.markdown(
                f'<div class="accident-engine-item">{item}</div>',
                unsafe_allow_html=True
            )

    # =====================================================
    # IMAGE PREVIEW
    # =====================================================

    if uploaded_file is not None:

        display_img, img_input = preprocess_image(
            uploaded_file
        )

        if display_img is None:

            st.error("Invalid image uploaded.")

            return

        st.markdown("---")

        st.image(
            display_img,
            width=950
        )

        st.markdown("<br>", unsafe_allow_html=True)

        b1, b2, b3 = st.columns([1,2,1])

        with b2:

            analyze = st.button(
                "✨ Analyze Accident Risk"
            )

        # =====================================================
        # PREDICTION
        # =====================================================

        if analyze:

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
                    <div class="accident-prediction-box">

                        <h3>Prediction Score</h3>

                        <h1>{prediction:.4f}</h1>

                    </div>
                    """, unsafe_allow_html=True)

                with col2:

                    if prediction < 0.5:

                        confidence = (
                            1 - prediction
                        ) * 100

                        st.markdown(f"""
                        <div class="accident-danger-box">

                            <h1>
                                ⚠️ Accident Detected
                            </h1>

                            <h2>
                                {confidence:.2f}% Confidence
                            </h2>

                        </div>
                        """, unsafe_allow_html=True)

                    else:

                        confidence = (
                            prediction
                        ) * 100

                        st.markdown(f"""
                        <div class="accident-safe-box">

                            <h1>
                                ✅ No Accident Detected
                            </h1>

                            <h2>
                                {confidence:.2f}% Confidence
                            </h2>

                        </div>
                        """, unsafe_allow_html=True)

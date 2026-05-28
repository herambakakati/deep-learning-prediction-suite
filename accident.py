import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
import os
import gdown


# =====================================================
# PAGE CSS
# =====================================================

def load_css():

    st.markdown(
        """
        <style>

        .hero-banner{

            background:
                linear-gradient(
                    rgba(15,23,42,0.78),
                    rgba(30,58,138,0.78)
                ),
                url("https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=1600&q=80");

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

        .section-title{

            color:#1e3a8a;

            font-size:30px;

            font-weight:800;

            margin-bottom:12px;
        }

        .section-text{

            color:#475569;

            font-size:17px;

            line-height:1.8;
        }

        .feature-box{

            background:
                linear-gradient(
                    135deg,
                    #ecfeff,
                    #dbeafe
                );

            padding:18px;

            border-radius:16px;

            margin-bottom:14px;

            color:#1e3a8a;

            font-weight:700;

            font-size:16px;
        }

        .danger-result{

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

        .safe-result{

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

        .score-box{

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

        </style>
        """,
        unsafe_allow_html=True
    )


# =====================================================
# DOWNLOAD MODEL
# =====================================================

def download_model():

    model_path = "best_accident_model.keras"

    if not os.path.exists(model_path):

        with st.spinner("Downloading AI model..."):

            file_id = "1PH-D7uz2f9dzcbW0u7hLqtMGwSH81ljr"

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
# IMAGE PREPROCESS
# =====================================================

def preprocess_image(uploaded_file):

    file_bytes = np.asarray(
        bytearray(uploaded_file.read()),
        dtype=np.uint8
    )

    image = cv2.imdecode(
        file_bytes,
        cv2.IMREAD_COLOR
    )

    if image is None:

        return None, None

    image_rgb = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2RGB
    )

    resized = cv2.resize(
        image_rgb,
        (224, 224)
    )

    normalized = resized.astype(
        np.float32
    ) / 255.0

    input_image = np.expand_dims(
        normalized,
        axis=0
    )

    return image_rgb, input_image


# =====================================================
# MAIN RENDER FUNCTION
# =====================================================

def render():

    load_css()

    # HERO

    st.markdown(
        """
        <div class="hero-banner">

            <div class="hero-title">
                🚗 AI Accident Detection Intelligence
            </div>

            <div class="hero-text">
                Upload traffic images and let the AI engine instantly
                detect accident scenarios using advanced deep learning
                intelligence and CNN-powered classification.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # MAIN SECTION

    left, right = st.columns(
        [1.2, 1]
    )

    with left:

        st.markdown(
            """
            <div class="glass-card">

                <div class="section-title">
                    📤 Upload Traffic Image
                </div>

                <div class="section-text">
                    Supported image formats:
                    JPG, JPEG, PNG
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        uploaded_file = st.file_uploader(
            "Choose an image",
            type=["jpg", "jpeg", "png"]
        )

    with right:

        st.markdown(
            """
            <div class="glass-card">

                <div class="section-title">
                    🧠 AI Detection Engine
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        features = [

            "⚡ Real-time CNN inference",

            "🎯 Confidence-based prediction",

            "🚀 Fast image classification",

            "🧠 Deep learning intelligence"
        ]

        for item in features:

            st.markdown(
                f"""
                <div class="feature-box">
                    {item}
                </div>
                """,
                unsafe_allow_html=True
            )

    # IMAGE DISPLAY

    if uploaded_file is not None:

        display_image, processed_image = preprocess_image(
            uploaded_file
        )

        if display_image is None:

            st.error(
                "Invalid image uploaded."
            )

            return

        st.image(
            display_image,
            use_column_width=True
        )

        # PREDICTION BUTTON

        if st.button(
            "✨ Analyze Accident Risk"
        ):

            try:

                model = load_model()

                with st.spinner(
                    "AI analyzing image..."
                ):

                    prediction = model.predict(
                        processed_image,
                        verbose=0
                    )[0][0]

                score_col, result_col = st.columns(2)

                # SCORE

                with score_col:

                    st.markdown(
                        f"""
                        <div class="score-box">

                            <h2>
                                Prediction Score
                            </h2>

                            <h1>
                                {prediction:.4f}
                            </h1>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                # RESULT

                with result_col:

                    if prediction < 0.5:

                        confidence = (
                            1 - prediction
                        ) * 100

                        st.markdown(
                            f"""
                            <div class="danger-result">

                                <h1>
                                    ⚠️ Accident Detected
                                </h1>

                                <h2>
                                    {confidence:.2f}% Confidence
                                </h2>

                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    else:

                        confidence = (
                            prediction
                        ) * 100

                        st.markdown(
                            f"""
                            <div class="safe-result">

                                <h1>
                                    ✅ No Accident Detected
                                </h1>

                                <h2>
                                    {confidence:.2f}% Confidence
                                </h2>

                            </div>
                            """,
                            unsafe_allow_html=True
                        )

            except Exception as e:

                st.error(
                    f"Prediction failed: {e}"
                )

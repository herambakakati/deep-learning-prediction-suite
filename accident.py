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

    model_path = "best_accident_model.keras"

    file_id = "1PH-D7uz2f9dzcbW0u7hLqtMGwSH81ljr"

    url = f"https://drive.google.com/uc?id={file_id}"

    if not os.path.exists(model_path):

        with st.spinner("Downloading AI model..."):

            gdown.download(
                url,
                model_path,
                quiet=False
            )

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

    st.markdown("""
    <style>

    .hero{
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
    }

    .hero h1{
        color:white;
        font-size:52px;
        font-weight:800;
    }

    .hero p{
        color:white;
        font-size:20px;
        line-height:1.8;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero">

        <h1>
            🚗 AI Accident Detection Intelligence
        </h1>

        <p>
            Upload traffic images and let AI detect
            accident scenarios instantly.
        </p>

    </div>
    """, unsafe_allow_html=True)

    model = load_accident_model()

    if model is None:

        st.error("Model loading failed.")

        return

    uploaded_file = st.file_uploader(
        "Upload Traffic Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:

        display_img, img_input = preprocess_image(
            uploaded_file
        )

        st.image(
            display_img,
            width=900
        )

        if st.button("Analyze Accident"):

            with st.spinner(
                "Analyzing image..."
            ):

                prediction = model.predict(
                    img_input,
                    verbose=0
                )[0][0]

                if prediction < 0.5:

                    confidence = (
                        1 - prediction
                    ) * 100

                    st.error(
                        f"⚠️ Accident Detected ({confidence:.2f}% confidence)"
                    )

                else:

                    confidence = (
                        prediction
                    ) * 100

                    st.success(
                        f"✅ No Accident Detected ({confidence:.2f}% confidence)"
                    )

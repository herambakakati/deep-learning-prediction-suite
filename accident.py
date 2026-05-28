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

    model_path = "best_accident_weights.weights.h5"

    file_id = "1PH-D7uz2f9dzcbW0u7hLqtMGwSH81ljr"

    url = f"https://drive.google.com/uc?id={file_id}"

    # DOWNLOAD MODEL

    if not os.path.exists(model_path):

        with st.spinner("Downloading AI model..."):

            gdown.download(
                url,
                model_path,
                quiet=False
            )

    try:

        # =====================================================
        # MODEL ARCHITECTURE
        # =====================================================

        model = tf.keras.models.Sequential([

            tf.keras.layers.Input(
                shape=(224,224,3)
            ),

            tf.keras.layers.Conv2D(
                32,
                (3,3),
                activation='relu'
            ),

            tf.keras.layers.MaxPooling2D(2,2),

            tf.keras.layers.Conv2D(
                64,
                (3,3),
                activation='relu'
            ),

            tf.keras.layers.MaxPooling2D(2,2),

            tf.keras.layers.Flatten(),

            tf.keras.layers.Dense(
                128,
                activation='relu'
            ),

            tf.keras.layers.Dropout(0.5),

            tf.keras.layers.Dense(
                1,
                activation='sigmoid'
            )
        ])

        # LOAD WEIGHTS

        model.load_weights(model_path)

        return model

    except Exception as e:

        st.error(
            f"Model loading failed: {e}"
        )

        return None

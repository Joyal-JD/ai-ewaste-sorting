import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2,
    preprocess_input,
    decode_predictions
)

st.title("AI-Based E-Waste Sorting System (Real CNN Model)")
st.write("Upload an electronic image for AI classification")

# Load pretrained model
@st.cache_resource
def load_model():
    return MobileNetV2(weights="imagenet")

model = load_model()

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

ewaste_keywords = ["battery", "cellular telephone", "computer keyboard", "mouse", "monitor", "laptop"]

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    img = image.resize((224, 224))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    predictions = model.predict(img_array)
    decoded = decode_predictions(predictions, top=3)[0]

    label = decoded[0][1]
    confidence = float(decoded[0][2])

    st.write("Detected Object:", label)
    st.write("Confidence:", round(confidence * 100, 2), "%")

    if any(keyword in label.lower() for keyword in ewaste_keywords) and confidence > 0.4:
        st.success("Recognized as Electronic Waste Component")
    else:
        st.error("Not recognized as E-Waste material")

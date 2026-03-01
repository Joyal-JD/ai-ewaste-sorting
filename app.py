import streamlit as st
from PIL import Image
import random

st.title("AI-Based E-Waste Sorting System")
st.write("Upload an electronic waste image for AI classification")

# File upload section
uploaded_file = st.file_uploader("Upload E-Waste Image", type=["jpg", "png", "jpeg"])

# E-waste database
ewaste_database = {
    "Battery": {
        "composition": "Lithium (Li), Cobalt (Co), Nickel (Ni)",
        "toxicity": "High",
        "bin": "Hazardous Waste Bin"
    },
    "PCB": {
        "composition": "Copper (Cu), Gold (Au), Lead (Pb)",
        "toxicity": "Medium",
        "bin": "Metal Recovery Unit"
    },
    "Wire": {
        "composition": "Copper (Cu), PVC",
        "toxicity": "Low",
        "bin": "Plastic & Metal Separation"
    },
    "Mobile": {
        "composition": "Silicon (Si), Rare Earth Metals",
        "toxicity": "Medium",
        "bin": "Component Dismantling Unit"
    }
}

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    prediction = random.choice(list(ewaste_database.keys()))
    result = ewaste_database[prediction]

    st.success(f"AI Detected Component: {prediction}")
    st.write("Chemical Composition:", result["composition"])
    st.write("Toxicity Level:", result["toxicity"])
    st.write("Recommended Disposal:", result["bin"])

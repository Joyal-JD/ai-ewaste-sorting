import streamlit as st
from PIL import Image
import random
import time

# Page config
st.set_page_config(page_title="AI E-Waste Sorting System", page_icon="♻️", layout="wide")

# Custom CSS for colorful UI
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        color: white;
    }
    .stButton>button {
        background-color: #00c9a7;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 16px;
    }
    .stFileUploader {
        border: 2px dashed #00c9a7;
        padding: 10px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; color:#00c9a7;'>♻️ AI-Based E-Waste Sorting System</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Upload an image to classify and get disposal recommendations</h4>", unsafe_allow_html=True)

# Sidebar info
st.sidebar.title("Project Info")
st.sidebar.info("""
This AI system classifies electronic waste and suggests proper disposal methods.

Technologies:
- Streamlit
- Image Processing
- AI Simulation (Extendable to ML models)
""")

# File uploader
uploaded_file = st.file_uploader("📤 Upload E-Waste Image", type=["jpg", "png", "jpeg"])

# Extended database
ewaste_database = {
    "Battery": {
        "composition": "Lithium (Li), Cobalt (Co), Nickel (Ni)",
        "toxicity": "High",
        "bin": "Hazardous Waste Bin",
        "recycle": "Recover metals via chemical processing"
    },
    "PCB": {
        "composition": "Copper (Cu), Gold (Au), Lead (Pb)",
        "toxicity": "Medium",
        "bin": "Metal Recovery Unit",
        "recycle": "Smelting & metal extraction"
    },
    "Wire": {
        "composition": "Copper (Cu), PVC",
        "toxicity": "Low",
        "bin": "Plastic & Metal Separation",
        "recycle": "Strip insulation & reuse copper"
    },
    "Mobile": {
        "composition": "Silicon (Si), Rare Earth Metals",
        "toxicity": "Medium",
        "bin": "Component Dismantling Unit",
        "recycle": "Disassemble and recover valuable parts"
    }
}

# Processing
if uploaded_file is not None:
    col1, col2 = st.columns([1,1])

    with col1:
        image = Image.open(uploaded_file)
        st.image(image, caption="📷 Uploaded Image", use_column_width=True)

    with col2:
        with st.spinner("🔍 Analyzing Image with AI Model..."):
            time.sleep(2)
            prediction = random.choice(list(ewaste_database.keys()))
            result = ewaste_database[prediction]

        st.success(f"✅ Detected: {prediction}")

        # Progress bar for toxicity
        toxicity_level = result["toxicity"]
        if toxicity_level == "High":
            progress = 90
        elif toxicity_level == "Medium":
            progress = 60
        else:
            progress = 30

        st.markdown("### ☣️ Toxicity Level")
        st.progress(progress)
        st.write(toxicity_level)

        # Expandable sections
        with st.expander("🧪 Chemical Composition"):
            st.write(result["composition"])

        with st.expander("♻️ Recycling Method"):
            st.write(result["recycle"])

        with st.expander("🗑️ Disposal Recommendation"):
            st.write(result["bin"])

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>🚀 Final Year Project | AI + Sustainability</p>", unsafe_allow_html=True)

# Future improvement section
st.sidebar.markdown("---")
st.sidebar.subheader("Future Enhancements")
st.sidebar.write("""
- Integrate real AI model (TensorFlow / PyTorch)
- Use camera for live detection
- Add IoT-based smart bins
- GPS-based recycling center locator
""")

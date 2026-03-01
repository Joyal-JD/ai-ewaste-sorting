import streamlit as st
from PIL import Image
import torch
import torchvision.transforms as transforms
from torchvision import models
import numpy as np

st.title("AI-Based E-Waste Sorting System (Real CNN - PyTorch)")

# Load pretrained model
@st.cache_resource
def load_model():
    model = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.DEFAULT)
    model.eval()
    return model

model = load_model()

# ImageNet labels
from torchvision.models import MobileNet_V2_Weights
labels = MobileNet_V2_Weights.DEFAULT.meta["categories"]

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])

    img_tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(img_tensor)
        probabilities = torch.nn.functional.softmax(outputs[0], dim=0)

    confidence, predicted_class = torch.max(probabilities, 0)
    label = labels[predicted_class]

    st.write("Detected Object:", label)
    st.write("Confidence:", round(confidence.item() * 100, 2), "%")

    # Basic electronic filtering
    electronic_keywords = ["laptop", "keyboard", "monitor", "cellular", "mouse"]

    if any(word in label.lower() for word in electronic_keywords):
        st.success("Recognized as Electronic/E-Waste Component")
    else:
        st.error("Not recognized as Electronic Waste")

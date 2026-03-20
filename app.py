import streamlit as st
import cv2
import numpy as np
from PIL import Image
from enhance import enhance_image, gamma_correction

st.title("🌙 Low Light Image Enhancement for CCTV Surveillance")

uploaded_file = st.file_uploader("Upload a low-light image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Read image safely
    image = Image.open(uploaded_file).convert("RGB")
    img = np.array(image)

    # Convert RGB → BGR
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Enhance
    enhanced = enhance_image(img_bgr)
    gamma_img = gamma_correction(enhanced)

    # Convert back to RGB
    enhanced_rgb = cv2.cvtColor(enhanced, cv2.COLOR_BGR2RGB)
    gamma_rgb = cv2.cvtColor(gamma_img, cv2.COLOR_BGR2RGB)


    # Display
    st.subheader("Results")
    st.image([img, enhanced_rgb, gamma_rgb],
             caption=["Original", "CLAHE Enhanced", "Final Output"],
             use_container_width=True)
import streamlit as st
import cv2
import numpy as np
from PIL import Image
from enhance import enhance_image, gamma_correction, detect_faces

st.title("🌙 Low Light Image Enhancement for CCTV Surveillance")

uploaded_file = st.file_uploader("Upload a low-light image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Load image safely
    image = Image.open(uploaded_file).convert("RGB")
    img = np.array(image)

    # Convert RGB → BGR
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Enhancement
    enhanced = enhance_image(img_bgr)

    # 🎚️ Gamma slider
    gamma_value = st.slider("Adjust Brightness (Gamma)", 0.5, 3.0, 1.5)
    gamma_img = gamma_correction(enhanced, gamma_value)

    # 👤 Face detection
    face_img = detect_faces(gamma_img.copy())

    # Convert back to RGB
    enhanced_rgb = cv2.cvtColor(enhanced, cv2.COLOR_BGR2RGB)
    gamma_rgb = cv2.cvtColor(gamma_img, cv2.COLOR_BGR2RGB)
    face_rgb = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)

    # Display images
    st.subheader("Results")
    st.image([img, enhanced_rgb, gamma_rgb, face_rgb],
             caption=["Original", "CLAHE Enhanced", "Gamma Adjusted", "Face Detection"],
             use_container_width=True)

    # 📄 Download button
    result = Image.fromarray(face_rgb)
    st.download_button("📥 Download Final Image", result.tobytes(), file_name="enhanced.png")
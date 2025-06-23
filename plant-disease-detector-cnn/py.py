# 🌿 Streamlit Plant Disease Detection App (Styled)

import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import PIL

# ---------------- UI Styling ----------------

st.set_page_config(page_title="Plant Disease Detector")
st.markdown("<h1 style='text-align: center; color: green;'>🌿 Plant Disease Detector</h1>", unsafe_allow_html=True)

def set_background(url):
    st.markdown(
        f"<style>.stApp {{background-image: url({url}); background-size: cover; background-attachment: fixed;}}</style>", 
        unsafe_allow_html=True
    )
# 🌿 You can replace this GIF with any leaf animation
set_background("https://i.pinimg.com/originals/e1/e5/f5/e1e5f51d06cf76be63ed4072cc77d5cf.gif")

# ---------------- Sidebar ----------------

st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2907/2907233.png", width=120)
st.sidebar.markdown("### 🌿 About This App")
st.sidebar.info("Upload a tomato leaf image to detect plant diseases using AI.")

st.sidebar.markdown("### 🤖 Model Info")
st.sidebar.success("Trained on 4 tomato leaf classes using CNN\nInput Image Size: 128x128\nFramework: Keras/TensorFlow")

st.markdown("---")

# ---------------- Image Upload + Prediction ----------------

uploaded_file = st.file_uploader("📤 Upload a tomato leaf image", type=["jpg", "jpeg", "png"])
if uploaded_file:
    st.markdown("### 📷 Image Preview:")
    img = image.load_img(uploaded_file, target_size=(128, 128))
    st.image(img, caption='Uploaded Leaf Image', use_column_width=True)

    # Load trained model (make sure plant_disease_model.h5 is in same folder)
    model = load_model("F:/plant_disease_model.h5")
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    pred = model.predict(img_array)[0]

    classes = ['Bacterial Spot', 'Early Blight', 'Late Blight', 'Healthy']
    prediction = classes[np.argmax(pred)]
    confidence = np.max(pred) * 100

    st.markdown(f"### 🩺 **Prediction:** `{prediction}`")
    st.markdown(f"📊 **Confidence:** `{confidence:.2f}%`")
    st.progress(confidence / 100)

# ---------------- Footer ----------------

st.markdown("<hr><center>Made with ❤️ for Elevate Labs Internship</center>", unsafe_allow_html=True)

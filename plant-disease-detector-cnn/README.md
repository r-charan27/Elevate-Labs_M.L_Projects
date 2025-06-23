# 🌿 Plant Disease Detector using CNN

This project is a deep learning-based web application that detects plant leaf diseases — specifically for tomato plants — using a Convolutional Neural Network (CNN). It allows users to upload an image of a leaf and receive an instant diagnosis.

---

## 🧠 Model Overview

The model is trained on 4 tomato leaf classes from the PlantVillage dataset:
- 🍅 Tomato___Bacterial_spot
- 🍅 Tomato___Early_blight
- 🍅 Tomato___Late_blight
- 🌿 Tomato___Healthy

It uses a CNN built with TensorFlow/Keras and is saved as a `.h5` file.

---

## 🎯 Features

- 🖼 Upload leaf image (JPG/PNG)
- ⚙️ Backend CNN model prediction
- 📊 Confidence score visualized
- 🎨 Animated background for an engaging UI
- ✅ Internship-ready project

---

## 🚀 How to Run the App

1. Clone the repo and install dependencies:

pip install -r requirements.txt

2.Ensure your model file is named plant_disease_model.h5 and located in the same directory.

3.Run the app:

streamlit run app.py
---
📦 Folder Structure

 plant-disease-detector-cnn/

 -app.py                    
 -plant_disease_model.h5   
 -requirements.txt          
 -README.md                 
 -Plant_Disease_Report.docx 
---
💡 Tech Stack
Python

TensorFlow / Keras

NumPy

Pillow

Streamlit
---
📌 Dataset:

 Used the PlantVillage Tomato Subset for training.
   "https://www.kaggle.com/datasets/emmarex/plantdisease"
---
📷 Demo Preview
(Optional: Add screenshot or Loom/YT link)
---
👨‍💻 Author
Developed by RamCharan Mummadi as part of the Elevate Labs Internship.

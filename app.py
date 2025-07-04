# app.py

import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("diabetes_model.pkl")

# Set up the page config
st.set_page_config(page_title="Diabetes Prediction App", layout="centered", page_icon="🩺")


with st.sidebar:
    st.title("ℹ️ About This App")
    st.markdown("""
    This is a **Diabetes Prediction Web App** built using **Streamlit** and a **Decision Tree Classifier**.

    The model is trained on the **Pima Indians Diabetes Dataset** from the UCI Machine Learning Repository.

    ---
    ### 👨‍⚕️ Inputs Required:
    - Medical values like Glucose, Blood Pressure, etc.
    - Gender-based filtering of unnecessary input (e.g., Pregnancies ignored for males)

    ---
    ### 🧠 Model Used:
    - Decision Tree Classifier
    - Accuracy: ~71%

    ---
    Built by **Akrit Pathania**
    """)

st.title("🩺 Diabetes Prediction App")
st.subheader("Predict whether you are likely to have diabetes based on your health data.")
st.markdown("Enter the following medical information to get an instant prediction.")

st.markdown("---")
name = st.text_input("👤 Enter your Name:")
gender = st.selectbox("Gender", ["Male", "Female"])

with st.form("prediction_form"):
    if gender == "Female":
        pregnancies = st.number_input("🤰 Number of Pregnancies", min_value=0, max_value=20, value=0)
    else:
        pregnancies = 0

    glucose = st.number_input("🍬 Glucose Level", min_value=1, max_value=200, value=100)
    bp = st.number_input("💓 Blood Pressure (mm Hg)", min_value=1, max_value=150, value=70)
    skin = st.number_input("💉 Skin Thickness (mm)", min_value=1, max_value=100, value=20)
    insulin = st.number_input("🧪 Insulin Level (mu U/ml)", min_value=1, max_value=900, value=80)
    bmi = st.number_input("⚖️ BMI (Body Mass Index)", min_value=1.0, max_value=70.0, value=25.0)
    dpf = st.number_input("🧬 Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
    age = st.number_input("🎂 Age", min_value=1, max_value=120, value=30)

    submitted = st.form_submit_button("🔍 Predict")

# Prediction
if submitted:
    input_data = pd.DataFrame([{
        'Pregnancies': pregnancies,
        'Glucose': glucose,
        'BloodPressure': bp,
        'SkinThickness': skin,
        'Insulin': insulin,
        'BMI': bmi,
        'DiabetesPedigreeFunction': dpf,
        'Age': age
    }])

    prediction = model.predict(input_data)[0]

    st.markdown(f"### 🧾 Results for **{name}**:")
    if prediction == 1:
        st.error("⚠️ You are likely to have **diabetes**. Please consult a medical professional.")
    else:
        st.success("✅ You are unlikely to have diabetes. Keep maintaining a healthy lifestyle!")

    st.markdown("---")
    st.caption(
        "Disclaimer: This prediction is based on machine learning and is **not a substitute for professional medical advice**.")


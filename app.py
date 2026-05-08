import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("diabetes_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Diabetes Prediction App")
st.write("Enter patient details to predict diabetes:")

# Input widgets
pregnancies = st.number_input("Pregnancies", 0, 20, 0)
glucose = st.number_input("Glucose", 0, 200, 120)
bp = st.number_input("Blood Pressure", 0, 140, 70)
skin_thickness = st.number_input("Skin Thickness", 0, 100, 20)
insulin = st.number_input("Insulin", 0, 900, 79)
bmi = st.number_input("BMI", 0.0, 70.0, 20.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
age = st.number_input("Age", 0, 120, 33)

# Predict button
if st.button("Predict"):
    features = np.array([[pregnancies, glucose, bp, skin_thickness, insulin, bmi, dpf, age]])
    prediction = model.predict(features)
    probability = model.predict_proba(features)[0][1]

    if prediction[0] == 1:
        st.error(f"Patient is likely diabetic. Risk: {probability:.2f}")
    else:
        st.success(f"Patient is not diabetic. Risk: {probability:.2f}")

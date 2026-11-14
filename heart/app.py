
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

model = joblib.load(BASE_DIR / 'svm_heart.pkl')
scaler = joblib.load(BASE_DIR / 'scaler.pkl')
expected_columns = joblib.load(BASE_DIR / 'columns.pkl')


st.title("Heart Disease Prediction by Devansh❤️")
st.markdown("Provide the following details")

age = st.slider("Age", 0, 100, 40)
sex = st.selectbox("Sex", ["M", "F"])
chest_pain = st.selectbox("Chest pain type", ["ATA", "NAP", "ASY", "TA"])
resting_bp = st.number_input("Resting blood pressure", 0, 200, 120)
cholesterol = st.number_input("Cholesterol", 0, 600, 200)
fasting_bs = st.selectbox("Fasting blood sugar > 120 mg/dl", [0, 1])
max_hr = st.slider("Maximum heart rate achieved", 60, 220, 150)
exercise_angina = st.selectbox("Exercise induced angina", ["Y", "N"])
oldpeak = st.slider("Oldpeak", 0.0, 6.0, 1.0)
st_slope = st.selectbox("ST slope", ["Up", "Flat", "Down"])

if st.button("Predict"):

    raw_input = {
        "Age": age,
        "Sex": 1 if sex == "M" else 0,
        "RestingBP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": fasting_bs,
        "MaxHR": max_hr,
        "Oldpeak": oldpeak,
        "ChestPainType": chest_pain,
        "ExerciseAngina": exercise_angina,
        "ST_Slope": st_slope
    }

    input_df = pd.DataFrame([raw_input])

    input_df = pd.get_dummies(
        input_df,
        columns=['ChestPainType', 'ExerciseAngina', 'ST_Slope']
    )

    input_df = input_df.reindex(
        columns=expected_columns,
        fill_value=0
    )

    scaled_input = scaler.transform(input_df)

    prediction = model.predict(scaled_input)[0]

    if prediction == 1:
        st.error("The person is likely to have heart disease.☠️")
    else:
        st.success("The person is unlikely to have heart disease.💚")


import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

st.title("Insurance Cost Prediction")

st.write("Enter Customer Details")

age = st.number_input("Age", 18, 100, 35)

sex = st.selectbox("Gender", ["male", "female"])

bmi = st.number_input("BMI", 10.0, 60.0, 27.5)

children = st.number_input(
    "Number of Children", 0, 10, 2
)

smoker = st.selectbox(
    "Smoker", ["yes", "no"]
)

region = st.selectbox(
    "Region",
    ["southwest", "southeast", "northwest", "northeast"]
)

if st.button("Predict Insurance Charges"):

    new_customer = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'bmi': [bmi],
        'children': [children],
        'smoker': [smoker],
        'region': [region]
    })

    new_customer_encoded = pd.get_dummies(
        new_customer,
        columns=['sex', 'smoker', 'region'],
        dtype=int
    )

    new_customer_encoded = new_customer_encoded.reindex(
        columns=columns,
        fill_value=0
    )

    scale_columns = ['age', 'bmi', 'children']

    new_customer_encoded[scale_columns] = scaler.transform(
        new_customer_encoded[scale_columns]
    )

    prediction = model.predict(new_customer_encoded)

    st.success("Prediction Successful!")

    st.subheader("Predicted Insurance Charges")

    st.write(f"${prediction[0]:,.2f}")

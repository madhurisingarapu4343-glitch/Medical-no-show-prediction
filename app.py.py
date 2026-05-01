import streamlit as st
import pandas as pd
import joblib

# Load model and columns
model = joblib.load("no_show_model.pkl")
columns = joblib.load("model_columns.pkl")

# App title
st.title("Medical Appointment Prediction App")
st.header("No Show Prediction")

# Inputs
age = st.number_input("Enter Age", min_value=0, max_value=100, value=25)
sms = st.selectbox("SMS Received", [0, 1])

# Predict button
if st.button("Predict"):

    # Step 1: Create full input structure
    input_dict = dict.fromkeys(columns, 0)

    # Step 2: Fill user inputs
    input_dict['age'] = age
    input_dict['SMS_received'] = sms

    # Step 3: Convert to DataFrame
    input_data = pd.DataFrame([input_dict])

    # Step 4: Match column order
    input_data = input_data[columns]

    # Step 5: Prediction
    result = model.predict(input_data)

    # Step 6: Probability (Risk Score)
    prob = model.predict_proba(input_data)[0][1]

    # Step 7: Show result
    if result[0] == 1:
        st.error("⚠️ High Risk: Patient may NOT show")
    else:
        st.success("✅ Low Risk: Patient likely to show")

    # Step 8: Show probability
    st.write(f"📊 Risk Score: {round(prob * 100, 2)}%")
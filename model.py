

import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load trained pipeline/model
@st.cache_resource
def load_model():
    return joblib.load("model/churn_model.pkl")

def run_prediction():
    st.title("🔮 Customer Churn Prediction")
    st.write("Fill in customer details below to predict churn:")

    # Input form
    with st.form("prediction_form"):
        st.subheader("📌 Customer Information")
        col1, col2 = st.columns(2)
        with col1:
            gender = st.radio("Gender", ["Male", "Female"], horizontal=True)
            senior = st.radio("Senior Citizen", [0, 1], horizontal=True)
            partner = st.radio("Partner", ["Yes", "No"], horizontal=True)
            dependents = st.radio("Dependents", ["Yes", "No"], horizontal=True)
            tenure = st.slider("Tenure (months)", 0, 72, 12)
        with col2:
            phone_service = st.radio("Phone Service", ["Yes", "No"], horizontal=True)
            multiple_lines = st.radio("Multiple Lines", ["Yes", "No", "No phone service"])
            internet = st.radio("Internet Service", ["DSL", "Fiber optic", "No"])
            contract = st.radio("Contract", ["Month-to-month", "One year", "Two year"])
            paperless = st.radio("Paperless Billing", ["Yes", "No"], horizontal=True)

        st.subheader("📡 Services")
        col3, col4 = st.columns(2)
        with col3:
            online_security = st.radio("Online Security", ["Yes", "No", "No internet service"])
            online_backup = st.radio("Online Backup", ["Yes", "No", "No internet service"])
            device_protection = st.radio("Device Protection", ["Yes", "No", "No internet service"])
        with col4:
            tech_support = st.radio("Tech Support", ["Yes", "No", "No internet service"])
            streaming_tv = st.radio("Streaming TV", ["Yes", "No", "No internet service"])
            streaming_movies = st.radio("Streaming Movies", ["Yes", "No", "No internet service"])

        st.subheader("💳 Billing Information")
        col5, col6 = st.columns(2)
        with col5:
            payment = st.radio("Payment Method", [
                "Electronic check", "Mailed check", 
                "Bank transfer (automatic)", "Credit card (automatic)"
            ])
        with col6:
            monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=200.0, value=70.0, step=1.0)
            total_charges = st.number_input("Total Charges ($)", min_value=0.0, max_value=10000.0, value=1000.0, step=10.0)

        # Submit button
        submitted = st.form_submit_button("🚀 Predict")

    if submitted:
        model = load_model()

        # Prepare input DataFrame (single row)
        input_dict = {
            "gender": gender,
            "SeniorCitizen": senior,
            "Partner": partner,
            "Dependents": dependents,
            "tenure": tenure,
            "PhoneService": phone_service,
            "MultipleLines": multiple_lines,
            "InternetService": internet,
            "OnlineSecurity": online_security,
            "OnlineBackup": online_backup,
            "DeviceProtection": device_protection,
            "TechSupport": tech_support,
            "StreamingTV": streaming_tv,
            "StreamingMovies": streaming_movies,
            "Contract": contract,
            "PaperlessBilling": paperless,
            "PaymentMethod": payment,
            "MonthlyCharges": monthly_charges,
            "TotalCharges": total_charges
        }
        input_df = pd.DataFrame([input_dict])

        try:
            # Predict probability
            prob = model.predict_proba(input_df)[0][1]
            pred = model.predict(input_df)[0]


            st.subheader("📊 Prediction Result")

            # Convert probability to percentage
            prob_percent = prob * 100

            if pred == 1 or pred == "Yes":
                color = "#E53935"  # red
                status = "⚠️ High Risk of Churn"
            else:
                color = "#43A047"  # green
                status = "✅ Low Risk of Churn"

            # Display status
            st.markdown(f"### {status}")

            # Custom probability bar
            st.markdown(
                f"""
                <div style="background-color:#E0E0E0; border-radius:10px; width:100%; height:30px; margin-top:10px;">
                    <div style="
                        width:{prob_percent}%;
                        background-color:{color};
                        height:30px;
                        border-radius:10px;
                        text-align:center;
                        color:white;
                        font-weight:bold;
                        line-height:30px;
                    ">
                        {prob_percent:.2f}%
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )






            # ✅ Return model so app.py can use it
            return model

                        
        except Exception as e:
            st.error(f"Prediction failed: {e}")
            return None










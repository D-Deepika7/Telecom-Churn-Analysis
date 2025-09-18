# import streamlit as st
# import pandas as pd
# import joblib

# # Load trained pipeline/model
# @st.cache_resource
# def load_model():
#     model = joblib.load("model/churn_model.pkl")
#     return model

# def run_prediction():
#     st.title("🔮 Customer Churn Prediction")

#     st.write("Enter customer details below to predict churn:")

#     # Input form
#     with st.form("prediction_form"):
#         col1, col2 = st.columns(2)

#         with col1:
#             gender = st.selectbox("Gender", ["Male", "Female"])
#             senior = st.selectbox("Senior Citizen", [0, 1])
#             partner = st.selectbox("Partner", ["Yes", "No"])
#             dependents = st.selectbox("Dependents", ["Yes", "No"])
#             tenure = st.slider("Tenure (months)", 0, 72, 12)

#             phone_service = st.selectbox("Phone Service", ["Yes", "No"])
#             multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
#             internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

#         with col2:
#             # 🔹 Extra fields your model expects
#             online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
#             online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
#             device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
#             tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
#             streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
#             streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
#             contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
#             paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
#             payment = st.selectbox("Payment Method", [
#                 "Electronic check", "Mailed check", 
#                 "Bank transfer (automatic)", "Credit card (automatic)"
#             ])

#         monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=200.0, value=70.0, step=1.0)
#         total_charges = st.number_input("Total Charges ($)", min_value=0.0, max_value=10000.0, value=1000.0, step=10.0)

#         # Submit button
#         submitted = st.form_submit_button("Predict")

#     if submitted:
#         model = load_model()

#         # Prepare input DataFrame (single row)
#         input_dict = {
#             "gender": gender,
#             "SeniorCitizen": senior,
#             "Partner": partner,
#             "Dependents": dependents,
#             "tenure": tenure,
#             "PhoneService": phone_service,
#             "MultipleLines": multiple_lines,
#             "InternetService": internet,
#             "OnlineSecurity": online_security,
#             "OnlineBackup": online_backup,
#             "DeviceProtection": device_protection,
#             "TechSupport": tech_support,
#             "StreamingTV": streaming_tv,
#             "StreamingMovies": streaming_movies,
#             "Contract": contract,
#             "PaperlessBilling": paperless_billing,
#             "PaymentMethod": payment,
#             "MonthlyCharges": monthly_charges,
#             "TotalCharges": total_charges
#         }
#         input_df = pd.DataFrame([input_dict])

#         try:
#             # Predict probability
#             prob = model.predict_proba(input_df)[0][1]
#             pred = model.predict(input_df)[0]

#             st.subheader("📌 Prediction Result")
#             if pred == 1 or pred == "Yes":
#                 st.error(f"⚠️ High Risk of Churn (Probability: {prob:.2f})")
#             else:
#                 st.success(f"✅ Low Risk of Churn (Probability: {prob:.2f})")
#         except Exception as e:
#             st.error(f"Prediction failed: {e}")






























# # section wise input


# import streamlit as st
# import pandas as pd
# import joblib

# # Load trained pipeline/model
# @st.cache_resource
# def load_model():
#     return joblib.load("model/churn_model.pkl")

# def run_prediction():
#     st.title("🔮 Customer Churn Prediction")
#     st.write("Fill in customer details below to predict churn:")

#     # Input form
#     with st.form("prediction_form"):
#         st.subheader("📌 Customer Information")
#         col1, col2 = st.columns(2)
#         with col1:
#             gender = st.selectbox("Gender", ["Male", "Female"])
#             senior = st.selectbox("Senior Citizen", [0, 1])
#             partner = st.selectbox("Partner", ["Yes", "No"])
#             dependents = st.selectbox("Dependents", ["Yes", "No"])
#             tenure = st.slider("Tenure (months)", 0, 72, 12)
#         with col2:
#             phone_service = st.selectbox("Phone Service", ["Yes", "No"])
#             multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
#             internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
#             contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
#             paperless = st.selectbox("Paperless Billing", ["Yes", "No"])

#         st.subheader("📡 Services")
#         col3, col4 = st.columns(2)
#         with col3:
#             online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
#             online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
#             device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
#         with col4:
#             tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
#             streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
#             streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])

#         st.subheader("💳 Billing Information")
#         col5, col6 = st.columns(2)
#         with col5:
#             payment = st.selectbox("Payment Method", [
#                 "Electronic check", "Mailed check", 
#                 "Bank transfer (automatic)", "Credit card (automatic)"
#             ])
#         with col6:
#             monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=200.0, value=70.0, step=1.0)
#             total_charges = st.number_input("Total Charges ($)", min_value=0.0, max_value=10000.0, value=1000.0, step=10.0)

#         # Submit button
#         submitted = st.form_submit_button("🚀 Predict")

#     if submitted:
#         model = load_model()

#         # Prepare input DataFrame (single row)
#         input_dict = {
#             "gender": gender,
#             "SeniorCitizen": senior,
#             "Partner": partner,
#             "Dependents": dependents,
#             "tenure": tenure,
#             "PhoneService": phone_service,
#             "MultipleLines": multiple_lines,
#             "InternetService": internet,
#             "OnlineSecurity": online_security,
#             "OnlineBackup": online_backup,
#             "DeviceProtection": device_protection,
#             "TechSupport": tech_support,
#             "StreamingTV": streaming_tv,
#             "StreamingMovies": streaming_movies,
#             "Contract": contract,
#             "PaperlessBilling": paperless,
#             "PaymentMethod": payment,
#             "MonthlyCharges": monthly_charges,
#             "TotalCharges": total_charges
#         }
#         input_df = pd.DataFrame([input_dict])

#         try:
#             # Predict probability
#             prob = model.predict_proba(input_df)[0][1]
#             pred = model.predict(input_df)[0]

#             st.subheader("📊 Prediction Result")
#             if pred == 1 or pred == "Yes":
#                 st.error(f"⚠️ High Risk of Churn\nProbability: **{prob:.2f}**")
#             else:
#                 st.success(f"✅ Low Risk of Churn\nProbability: **{prob:.2f}**")
#         except Exception as e:
#             st.error(f"Prediction failed: {e}")














# radio button input



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

            # st.subheader("📊 Prediction Result")
            # if pred == 1 or pred == "Yes":
            #     st.error(f"⚠️ High Risk of Churn\nProbability: **{prob:.2f}**")
            # else:
            #     st.success(f"✅ Low Risk of Churn\nProbability: **{prob:.2f}**")


            # st.subheader("📊 Prediction Result")

            # if pred == 1 or pred == "Yes":
            #     st.markdown(
            #         f"""
            #         <div style="background-color:#FFCDD2; padding:20px; border-radius:10px; text-align:center">
            #             <h3>⚠️ High Risk of Churn</h3>
            #             <p style="font-size:20px;">Probability: <strong>{prob:.2f}</strong></p>
            #         </div>
            #         """, unsafe_allow_html=True
            #     )
            # else:
            #     st.markdown(
            #         f"""
            #         <div style="background-color:#C8E6C9; padding:20px; border-radius:10px; text-align:center">
            #             <h3>✅ Low Risk of Churn</h3>
            #             <p style="font-size:20px;">Probability: <strong>{prob:.2f}</strong></p>
            #         </div>
            #         """, unsafe_allow_html=True
            #     )



            # st.subheader("📊 Prediction Result")

            # # Convert probability to percentage
            # prob_percent = prob * 100

            # if pred == 1 or pred == "Yes":
            #     st.markdown("⚠️ **High Risk of Churn**", unsafe_allow_html=True)
            #     st.markdown(f"Probability: **{prob_percent:.2f}%**")
                
            #     # Custom red progress bar
            #     st.progress(min(int(prob_percent), 100))  # progress bar max is 100
            #     st.markdown(
            #         f"""
            #         <div style="background-color:#FFCDD2; border-radius:5px; height:20px; width:{prob_percent}%; margin-top:-20px"></div>
            #         """, unsafe_allow_html=True
            #     )
            # else:
            #     st.markdown("✅ **Low Risk of Churn**", unsafe_allow_html=True)
            #     st.markdown(f"Probability: **{prob_percent:.2f}%**")
                
            #     # Custom green progress bar
            #     st.progress(min(int(prob_percent), 100))
            #     st.markdown(
            #         f"""
            #         <div style="background-color:#C8E6C9; border-radius:5px; height:20px; width:{prob_percent}%; margin-top:-20px"></div>
            #         """, unsafe_allow_html=True
            #     )




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


    # # ℹ️ Model Information (hidden until expanded)
    # with st.expander("ℹ️ See Model Details"):
    #     st.markdown("""
    #     ### Model Used
    #     - **Random Forest Classifier**
    #     - Tuned Hyperparameters:
    #         - `n_estimators = 300`
    #         - `max_depth = 10`
    #         - `min_samples_split = 2`
    #         - `min_samples_leaf = 1`
    #         - `random_state = 42`

    #     ### Training & Evaluation
    #     - Train-test split with **SMOTE** balancing
    #     - Numerical features standardized with **StandardScaler**
    #     - Categorical features encoded with **OneHotEncoder**
    #     - Best model selected after GridSearchCV on multiple classifiers

    #     ### Evaluation Metrics (on validation set)
    #     - **Accuracy:** 0.8557
    #     - **Precision:** 0.8780
    #     - **Recall:** 0.8261
    #     - **F1 Score:** 0.8513
    #     - **AUC-ROC:** 0.8557
    #     """)

    #     # 🔥 Show Feature Importances
    #     try:
    #         st.subheader("🔑 Top 10 Important Features")
    #         feature_names = model.named_steps["preprocessor"].get_feature_names_out()
    #         importances = model.named_steps["classifier"].feature_importances_

    #         # Sort and pick top 10
    #         importance_df = pd.DataFrame({
    #             "Feature": feature_names,
    #             "Importance": importances
    #         }).sort_values(by="Importance", ascending=False).head(10)

    #         # Plot
    #         fig, ax = plt.subplots(figsize=(8, 5))
    #         ax.barh(importance_df["Feature"], importance_df["Importance"])
    #         ax.invert_yaxis()
    #         ax.set_xlabel("Importance")
    #         ax.set_title("Top 10 Feature Importances")
    #         st.pyplot(fig)

    #     except Exception as e:
    #         st.warning(f"Could not display feature importances: {e}")












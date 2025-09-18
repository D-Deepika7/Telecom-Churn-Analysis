# import streamlit as st
# import pandas as pd
# import pickle

# # -----------------
# # Helper Functions
# # -----------------
# @st.cache_data
# def load_data():
#     return pd.read_csv("data/EDA_cleaned_telecom_churn_data.csv")

# # @st.cache_resource
# # def load_model():
# #     with open("model/churn_model.pkl", "rb") as file:
# #         model = pickle.load(file)
# #     return model

# # -----------------
# # Sidebar Navigation
# # -----------------
# st.sidebar.title("📊 Telecom Churn App")
# page = st.sidebar.radio("Go to", ["Dashboard", "Prediction"])

# # -----------------
# # Page 1: Dashboard
# # -----------------
# if page == "Dashboard":
#     st.title("📊 Customer Churn Dashboard")
    
#     # Load data
#     df = load_data()

#     # KPI Cards
#     total_customers = len(df)
#     churned = df[df["Churn"] == "Yes"].shape[0]
#     active = df[df["Churn"] == "No"].shape[0]
#     churn_rate = round(churned / total_customers * 100, 2)

#     col1, col2, col3, col4 = st.columns(4)
#     col1.metric("Total Customers", total_customers)
#     col2.metric("Active Customers", active)
#     col3.metric("Churned Customers", churned)
#     col4.metric("Churn Rate", f"{churn_rate}%")

#     st.write("### Interactive Visuals")
#     # You can add bar charts, donut charts, etc. here later
#     st.bar_chart(df["Contract"].value_counts())

# # -----------------
# # Page 2: Prediction
# # -----------------
# elif page == "Prediction":
#     st.title("🔮 Customer Churn Prediction")

#     st.write("Enter customer details below:")

#     # Example Inputs (expand later with all model features)
#     tenure = st.number_input("Tenure (months)", min_value=0, max_value=72, value=12)
#     monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
#     contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])

#     # Load model
#     # model = load_model()

#     if st.button("Predict Churn"):
#         # For demo → simple example, later map inputs to model features
#         features = [[tenure, monthly_charges, 1]]  # dummy encoding
#         # prediction = model.predict(features)[0]
#         # prob = model.predict_proba(features)[0][1]

#         # st.write(f"**Prediction:** {'Yes' if prediction == 1 else 'No'}")
#         # st.write(f"**Churn Probability:** {prob:.2%}")








# import streamlit as st
# from dashboard import show_dashboard
# # from model import show_model_page

# # Sidebar navigation
# st.sidebar.title("Telecom Churn App")
# page = st.sidebar.radio("Go to", ["Dashboard", "Predictive Model"])

# # Route to selected page
# if page == "Dashboard":
#     show_dashboard()
# # elif page == "Predictive Model":
# #     show_model_page()











# import streamlit as st
# import dashboard
# import model

# st.sidebar.title("Navigation")
# page = st.sidebar.radio("Go to:", ["Dashboard", "Prediction"])

# if page == "Dashboard":
#     dashboard.run_dashboard()
# elif page == "Prediction":
#     model.run_prediction()









# import streamlit as st
# from model import run_prediction
# import dashboard
# import pandas as pd
# import matplotlib.pyplot as plt

# st.sidebar.title("Navigation")
# page = st.sidebar.radio("Go to:", ["Dashboard", "Prediction"])

# if page == "Dashboard":
#     dashboard.run_dashboard()
# elif page == "Prediction":
#     model = run_prediction()  # returns the trained model

#     if model is not None:
#         with st.expander("ℹ️ Model Information", expanded=False):
#             st.write("**Model Used:** Random Forest Classifier")
#             st.write("**Best Hyperparameters:**")
#             st.json({
#                 "n_estimators": 300,
#                 "max_depth": 10,
#                 "min_samples_split": 2,
#                 "min_samples_leaf": 1,
#                 "random_state": 42
#             })
#             st.write("**Evaluation Metrics (on validation set):**")
#             st.json({
#                 "Accuracy": 0.855,
#                 "Precision": 0.878,
#                 "Recall": 0.826,
#                 "F1 Score": 0.851,
#                 "AUC-ROC": 0.856
#             })
                
            # # Load precomputed feature importances
            # try:
            #     feature_df = pd.read_csv("data/feature_importances.csv")
            #     top_features = feature_df.head(10)

            #     st.subheader("🔝 Top 10 Important Features")

            #     fig, ax = plt.subplots(figsize=(6,4))
            #     ax.barh(top_features["Feature"], top_features["Importance"])
            #     ax.invert_yaxis()
            #     ax.set_xlabel("Importance")
            #     ax.set_ylabel("Feature")
            #     st.pyplot(fig)

            # except Exception as e:
            #     st.warning(f"Could not load feature importances: {e}")







# import streamlit as st
# from model import run_prediction
# import dashboard

# # Sidebar navigation
# st.sidebar.title("Navigation")
# page = st.sidebar.radio("Go to:", ["Home", "Dashboard", "Prediction"])

# # --------------------- HOME PAGE ---------------------
# if page == "Home":
#     st.title("📡 Telecom Customer Churn App")
#     st.markdown(
#         """
#         Welcome to the **Telecom Customer Churn Analysis & Prediction App**.
        
#         **Features:**
#         - Visualize customer churn insights and key metrics on the Dashboard.
#         - Predict churn probability for individual customers on the Prediction page.
#         - Explore feature importance and model evaluation metrics.
        
#         **Instructions:**
#         1. Use the sidebar to navigate between pages.
#         2. On the Dashboard page, interact with filters to explore churn drivers.
#         3. On the Prediction page, enter customer details and get churn predictions.
#         """
#     )
#     # st.image("images/telecom_churn_banner.png", use_column_width=True)  # optional banner

# # --------------------- DASHBOARD PAGE ---------------------
# elif page == "Dashboard":
#     dashboard.run_dashboard()

# # --------------------- PREDICTION PAGE ---------------------
# elif page == "Prediction":
#     model = run_prediction()  # returns trained model

#     # Display model info in an expander
#     if model is not None:
#         with st.expander("ℹ️ Model Information", expanded=False):
#             st.write("**Model Used:** Random Forest Classifier")
#             st.write("**Best Hyperparameters:**")
#             st.json({
#                 "n_estimators": 300,
#                 "max_depth": 10,
#                 "min_samples_split": 2,
#                 "min_samples_leaf": 1,
#                 "random_state": 42
#             })
#             st.write("**Evaluation Metrics (on validation set):**")
#             st.json({
#                 "Accuracy": 0.855,
#                 "Precision": 0.878,
#                 "Recall": 0.826,
#                 "F1 Score": 0.851,
#                 "AUC-ROC": 0.856
#             })








## final working


# import streamlit as st
# from model import run_prediction
# import dashboard
# import pandas as pd
# from datetime import datetime


# st.image("data/Telecom_2.jpg", use_column_width=True)  # banner need to reduce height

# # ------------------ SESSION STATE INIT ------------------
# if "logged_in" not in st.session_state:
#     st.session_state["logged_in"] = False
#     st.session_state["username"] = ""

# # ------------------ CREDENTIALS ------------------
# USER_CREDENTIALS = {
#     "admin": "admin123",
#     "user": "user123"
# }

# # ------------------ SIDEBAR NAVIGATION ------------------
# st.sidebar.title("Navigation")
# page = st.sidebar.radio("Go to:", ["Home", "Dashboard", "Prediction"])

# # Show logged in user in sidebar
# if st.session_state["logged_in"]:
#     st.sidebar.info(f"👤 Logged in as: **{st.session_state['username']}**")
#     if st.sidebar.button("Logout"):
#         st.session_state["logged_in"] = False
#         st.session_state["username"] = ""
#         st.success("You have been logged out ✅")
# else:
#     st.sidebar.info("❌ Not logged in")


# # ------------------ HOME PAGE ------------------
# if page == "Home":
#     st.title("📡 Telecom Customer Churn App")

#     # Create two columns: left (main info) and right (login)
#     col1, col2 = st.columns([3, 1])  # 3:1 ratio

#     with col1:
#         st.markdown("""
#         Welcome to the **Telco Customer Churn Analysis** app!  

#         This project allows you to:
#         - Explore customer churn trends and drivers through interactive dashboards.
#         - Predict whether a customer is likely to churn based on their profile.
#         - Submit feedback to improve the tool.
#         """)

#         st.markdown("### 📄 Dataset & Instructions")
#         st.markdown("""
#         - **Dataset:** Telco Customer Churn (cleaned version used in this app).  
#         - **Instructions:** Use the sidebar to navigate between **Dashboard** and **Prediction** pages.  
#         - **Login:** Some pages require login. Please log in to access prediction and feedback features.
#         """)



#     with col2:
#         st.subheader("🔐 Login")
#         if not st.session_state["logged_in"]:
#             with st.container():
#                 username = st.text_input("Username")
#                 password = st.text_input("Password", type="password")
#                 login_btn = st.button("Login")
#                 if login_btn:
#                     if username in USER_CREDENTIALS and password == USER_CREDENTIALS[username]:
#                         st.session_state["logged_in"] = True
#                         st.session_state["username"] = username
#                         st.success(f"Welcome {username}! ✅")
#                     else:
#                         st.error("❌ Invalid username or password")
#         else:
#             st.success("You are already logged in ✅")

#     st.markdown("---")
#     st.markdown("### 📝 Feedback")

#     with st.container():
#         feedback = st.text_area("Enter your feedback here")
#         if st.button("Submit Feedback"):
#             if feedback.strip() != "":
#                 feedback_df = pd.DataFrame({
#                     "timestamp": [datetime.now()],
#                     "username": [st.session_state["username"]],
#                     "feedback": [feedback]
#                 })
#                 # Append to feedback CSV
#                 try:
#                     feedback_df.to_csv("data/feedback.csv", mode="a", index=False, header=False)
#                 except FileNotFoundError:
#                     feedback_df.to_csv("data/feedback.csv", index=False)
#                 st.success("Thank you for your feedback! ✅")
#             else:
#                 st.warning("Please enter some feedback before submitting.")

#     # Optional: Show past feedback if admin
#     if st.session_state["username"] == "admin":
#         st.subheader("📝 Past Feedback (Admin View)")
#         try:
#             past_feedback = pd.read_csv("data/feedback.csv", names=["timestamp", "username", "feedback"])
#             st.dataframe(past_feedback)
#         except FileNotFoundError:
#             st.info("No feedback submitted yet.")

# # ------------------ DASHBOARD PAGE ------------------
# elif page == "Dashboard":
#     if st.session_state["logged_in"]:
#         dashboard.run_dashboard()
#     else:
#         st.warning("⚠️ Please login first to access this page.")

# # ------------------ PREDICTION PAGE ------------------
# elif page == "Prediction":
#     if st.session_state["logged_in"]:
#         model = run_prediction()  # returns trained model

#         if model is not None:
#             with st.expander("ℹ️ Model Information", expanded=False):
#                 st.write("**Model Used:** Random Forest Classifier")
#                 st.write("**Best Hyperparameters:**")
#                 st.json({
#                     "n_estimators": 300,
#                     "max_depth": 10,
#                     "min_samples_split": 2,
#                     "min_samples_leaf": 1,
#                     "random_state": 42
#                 })
#                 st.write("**Evaluation Metrics (on validation set):**")
#                 st.json({
#                     "Accuracy": 0.855,
#                     "Precision": 0.878,
#                     "Recall": 0.826,
#                     "F1 Score": 0.851,
#                     "AUC-ROC": 0.856
#                 })
#     else:
#         st.warning("⚠️ Please login first to access this page.")

















## prettified 1




# import streamlit as st
# from model import run_prediction
# import dashboard
# import pandas as pd
# from datetime import datetime

# # ------------------ CUSTOM CSS ------------------
# st.markdown(
#     """
#     <style>
#     /* Banner styling */
#     .banner-container img {
#         height: 180px;  /* control banner height */
#         object-fit: cover;
#         border-radius: 10px;
#         box-shadow: 2px 2px 12px #aaa;
#     }

#     /* Sidebar background */
#     [data-testid="stSidebar"] {
#         background-color: #fdfefe;
#     }

#     /* Sidebar button styling */
#     [data-testid="stSidebar"] .stButton>button {
#         background-color: #d35400;
#         color: white;
#         border-radius: 8px;
#     }
#     [data-testid="stSidebar"] .stButton>button:hover {
#         background-color: #e67e22;
#         color: white;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # ------------------ BANNER ------------------
# st.markdown(
#     """
#     <div class="banner-container">
#         <img src="data/Telecom_2.jpg">
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# # ------------------ SESSION STATE INIT ------------------
# if "logged_in" not in st.session_state:
#     st.session_state["logged_in"] = False
#     st.session_state["username"] = ""

# # ------------------ CREDENTIALS ------------------
# USER_CREDENTIALS = {
#     "admin": "admin123",
#     "user": "user123"
# }

# # ------------------ SIDEBAR NAVIGATION ------------------
# st.sidebar.title("📌 Navigation")
# page = st.sidebar.radio("Go to:", ["Home", "Dashboard", "Prediction"])

# # Show logged in user in sidebar
# if st.session_state["logged_in"]:
#     st.sidebar.success(f"👤 Logged in as: **{st.session_state['username']}**")
#     if st.sidebar.button("Logout"):
#         st.session_state["logged_in"] = False
#         st.session_state["username"] = ""
#         st.success("You have been logged out ✅")
# else:
#     st.sidebar.info("❌ Not logged in")

# # ------------------ HOME PAGE ------------------
# if page == "Home":
#     st.title("📡 Telecom Customer Churn App")

#     # Create two columns: left (main info) and right (login)
#     col1, col2 = st.columns([3, 1])

#     with col1:
#         # Project Overview Block
#         st.markdown(
#             """
#             <div style="background-color:#f0f8ff;padding:15px;border-radius:10px;margin-bottom:20px;">
#                 <h3 style="color:#1f618d;">📖 Project Overview</h3>
#                 <p>
#                 Welcome to the <b>Telco Customer Churn Analysis</b> app!  
#                 This project allows you to:
#                 <ul>
#                     <li>📊 Explore customer churn trends and drivers through interactive dashboards.</li>
#                     <li>🔮 Predict whether a customer is likely to churn based on their profile.</li>
#                     <li>💬 Submit feedback to improve the tool.</li>
#                 </ul>
#                 </p>
#             </div>
#             """,
#             unsafe_allow_html=True
#         )

#         # Dataset & Instructions Block
#         st.markdown(
#             """
#             <div style="background-color:#eafaf1;padding:15px;border-radius:10px;margin-bottom:20px;">
#                 <h3 style="color:#117a65;">📄 Dataset & Instructions</h3>
#                 <ul>
#                     <li><b>Dataset:</b> Telco Customer Churn (cleaned version used in this app).</li>
#                     <li><b>Instructions:</b> Use the sidebar to navigate between Dashboard and Prediction pages.</li>
#                     <li><b>Login:</b> Some pages require login. Please log in to access prediction and feedback features.</li>
#                 </ul>
#             </div>
#             """,
#             unsafe_allow_html=True
#         )

#     with col2:
#         # Login Block
#         st.markdown("### 🔐 Login")
#         if not st.session_state["logged_in"]:
#             username = st.text_input("Username")
#             password = st.text_input("Password", type="password")
#             login_btn = st.button("Login")
#             if login_btn:
#                 if username in USER_CREDENTIALS and password == USER_CREDENTIALS[username]:
#                     st.session_state["logged_in"] = True
#                     st.session_state["username"] = username
#                     st.success(f"Welcome {username}! ✅")
#                 else:
#                     st.error("❌ Invalid username or password")
#         else:
#             st.success("You are already logged in ✅")

#     # Feedback Section
#     st.markdown("---")
#     st.markdown(
#         """
#         <div style="background-color:#fdebd0;padding:20px;border-radius:10px;">
#             <h3 style="color:#d35400;">💬 We value your feedback!</h3>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

#     feedback = st.text_area("Enter your feedback here")
#     if st.button("Submit Feedback"):
#         if feedback.strip() != "":
#             feedback_df = pd.DataFrame({
#                 "timestamp": [datetime.now()],
#                 "username": [st.session_state["username"]],
#                 "feedback": [feedback]
#             })
#             try:
#                 feedback_df.to_csv("data/feedback.csv", mode="a", index=False, header=False)
#             except FileNotFoundError:
#                 feedback_df.to_csv("data/feedback.csv", index=False)
#             st.success("Thank you for your feedback! ✅")
#         else:
#             st.warning("⚠️ Please enter some feedback before submitting.")

#     # Optional: Show past feedback if admin
#     if st.session_state["username"] == "admin":
#         st.subheader("📝 Past Feedback (Admin View)")
#         try:
#             past_feedback = pd.read_csv("data/feedback.csv", names=["timestamp", "username", "feedback"])
#             st.dataframe(past_feedback)
#         except FileNotFoundError:
#             st.info("No feedback submitted yet.")

# # ------------------ DASHBOARD PAGE ------------------
# elif page == "Dashboard":
#     if st.session_state["logged_in"]:
#         dashboard.run_dashboard()
#     else:
#         st.warning("⚠️ Please login first to access this page.")

# # ------------------ PREDICTION PAGE ------------------
# elif page == "Prediction":
#     if st.session_state["logged_in"]:
#         model = run_prediction()

#         if model is not None:
#             with st.expander("ℹ️ Model Information", expanded=False):
#                 st.write("**Model Used:** Random Forest Classifier")
#                 st.write("**Best Hyperparameters:**")
#                 st.json({
#                     "n_estimators": 300,
#                     "max_depth": 10,
#                     "min_samples_split": 2,
#                     "min_samples_leaf": 1,
#                     "random_state": 42
#                 })
#                 st.write("**Evaluation Metrics (on validation set):**")
#                 st.json({
#                     "Accuracy": 0.855,
#                     "Precision": 0.878,
#                     "Recall": 0.826,
#                     "F1 Score": 0.851,
#                     "AUC-ROC": 0.856
#                 })
#     else:
#         st.warning("⚠️ Please login first to access this page.")














## prettified 2






import streamlit as st
from model import run_prediction
import dashboard
import pandas as pd
from datetime import datetime

# ------------------ SESSION STATE INIT ------------------
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
    st.session_state["username"] = ""

# ------------------ CREDENTIALS ------------------
USER_CREDENTIALS = {
    "admin": "admin123",
    "user": "user123"
}

# ------------------ SIDEBAR NAVIGATION ------------------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Dashboard", "Prediction"])

# Show logged in user in sidebar
if st.session_state["logged_in"]:
    st.sidebar.success(f"👤 Logged in as: **{st.session_state['username']}**")
    if st.sidebar.button("Logout"):
        st.session_state["logged_in"] = False
        st.session_state["username"] = ""
        st.success("You have been logged out ✅")
else:
    st.sidebar.info("❌ Not logged in")



from PIL import Image

# Banner Image (resized to keep height smaller)
try:
    banner = Image.open("data/Telecom_2.jpg")
    banner = banner.resize((1200, 300))  # width, height
    st.image(banner, use_column_width=True)
except Exception:
    st.warning("⚠️ Banner image not found in `data/Telecom_2.jpg`")


# ------------------ HOME PAGE ------------------
if page == "Home":

    st.title("📡 Telecom Customer Churn App")

    # Two columns: left (main info) and right (login)
    col1, col2 = st.columns([3, 1])  # 3:1 ratio

    with col1:
        # Overview Section in shaded box
        st.markdown(
            """
            <div style="background-color:#f5f7fa; padding:20px; border-radius:10px; margin-bottom:20px;">
                <h3 style="color:#1f618d;">📖 Project Overview</h3>
                <p>
                Welcome to the <b>Telco Customer Churn Analysis</b> app!  
                </p>
                <ul>
                    <li>🔍 Explore churn trends and drivers through interactive dashboards.</li>
                    <li>🔮 Predict customer churn using machine learning models.</li>
                    <li>📝 Submit feedback to improve the tool.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Dataset & Instructions Section in shaded box
        st.markdown(
            """
            <div style="background-color:#eef5ff; padding:20px; border-radius:10px; margin-bottom:20px;">
                <h3 style="color:#154360;">📄 Dataset & Instructions</h3>
                <ul>
                    <li><b>Dataset:</b> Telco Customer Churn (cleaned version used here).</li>
                    <li><b>Instructions:</b> Use the sidebar to navigate to <b>Dashboard</b> or <b>Prediction</b>.</li>
                    <li><b>Login:</b> Required to access prediction and feedback features.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.subheader("🔐 Login")
        if not st.session_state["logged_in"]:
            with st.container():
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")
                login_btn = st.button("Login")
                if login_btn:
                    if username in USER_CREDENTIALS and password == USER_CREDENTIALS[username]:
                        st.session_state["logged_in"] = True
                        st.session_state["username"] = username
                        st.success(f"Welcome {username}! ✅")
                    else:
                        st.error("❌ Invalid username or password")
        else:
            st.success("You are already logged in ✅")





# ------------------ DASHBOARD PAGE ------------------
elif page == "Dashboard":
    if st.session_state["logged_in"]:
        dashboard.run_dashboard()
    else:
        st.warning("⚠️ Please login first to access this page.")

# ------------------ PREDICTION PAGE ------------------
elif page == "Prediction":
    if st.session_state["logged_in"]:
        model = run_prediction()

        if model is not None:
            with st.expander("ℹ️ Model Information", expanded=False):
                st.write("**Model Used:** Random Forest Classifier")
                st.write("**Best Hyperparameters:**")
                st.json({
                    "n_estimators": 300,
                    "max_depth": 10,
                    "min_samples_split": 2,
                    "min_samples_leaf": 1,
                    "random_state": 42
                })
                st.write("**Evaluation Metrics (on validation set):**")
                st.json({
                    "Accuracy": 0.855,
                    "Precision": 0.878,
                    "Recall": 0.826,
                    "F1 Score": 0.851,
                    "AUC-ROC": 0.856
                })
    else:
        st.warning("⚠️ Please login first to access this page.")



# Feedback Section - Full width
st.markdown("---")
st.markdown(
    """
    <div style="background-color:#fef9e7; padding:20px; border-radius:10px;">
        <h3 style="color:#7d6608;">💬 We value your feedback!</h3>
    </div>
    """,
    unsafe_allow_html=True
)

with st.container():
    feedback = st.text_area("Enter your feedback here")
    if st.button("Submit Feedback"):
        if feedback.strip() != "":
            feedback_df = pd.DataFrame({
                "timestamp": [datetime.now()],
                "username": [st.session_state["username"]],
                "feedback": [feedback]
            })
            try:
                feedback_df.to_csv("data/feedback.csv", mode="a", index=False, header=False)
            except FileNotFoundError:
                feedback_df.to_csv("data/feedback.csv", index=False)
            st.success("Thank you for your feedback! ✅")
        else:
            st.warning("Please enter some feedback before submitting.")

# Optional: Show past feedback if admin
if st.session_state["username"] == "admin":
    st.subheader("📝 Past Feedback (Admin View)")
    try:
        past_feedback = pd.read_csv("data/feedback.csv", names=["timestamp", "username", "feedback"])
        st.dataframe(past_feedback)
    except FileNotFoundError:
        st.info("No feedback submitted yet.")

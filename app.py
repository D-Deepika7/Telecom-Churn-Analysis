

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


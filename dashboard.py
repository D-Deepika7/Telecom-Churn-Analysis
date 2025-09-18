

import streamlit as st
import pandas as pd
import plotly.express as px

# Load cleaned data
@st.cache_data
def load_data():
    df = pd.read_csv("data/EDA_cleaned_telecom_churn_data.csv")
    return df

def show_kpis(df):
    total_customers = len(df)
    churned_customers = df[df['Churn'] == 'Yes'].shape[0]
    active_customers = total_customers - churned_customers
    churn_rate = round((churned_customers / total_customers) * 100, 2) if total_customers > 0 else 0
    avg_tenure = round(df['tenure'].mean(), 1) if total_customers > 0 else 0
    avg_monthly = round(df['MonthlyCharges'].mean(), 2) if total_customers > 0 else 0

    st.subheader("📊 Key Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Customers", total_customers)
    col2.metric("Active Customers", active_customers)
    col3.metric("Churned Customers", churned_customers)

    col4, col5, col6 = st.columns(3)
    col4.metric("Churn Rate (%)", churn_rate)
    col5.metric("Avg Tenure (Months)", avg_tenure)
    col6.metric("Avg Monthly Charges ($)", avg_monthly)

def churn_distribution(df):
    st.subheader("🔄 Churn Distribution")
    if df.empty:
        st.warning("No data available for the selected filters.")
        return
    fig = px.pie(df, names="Churn", hole=0.4, color="Churn",
                 color_discrete_map={"Yes": "red", "No": "green"})
    st.plotly_chart(fig, use_container_width=True)

def contract_vs_churn(df):
    st.subheader("📑 Contract Type vs Churn")
    if df.empty:
        st.warning("No data available for the selected filters.")
        return
    fig = px.histogram(df, x="Contract", color="Churn", barmode="group",
                       title="Churn by Contract Type")
    st.plotly_chart(fig, use_container_width=True)

def payment_vs_churn(df):
    st.subheader("💳 Payment Method vs Churn")
    if df.empty:
        st.warning("No data available for the selected filters.")
        return
    fig = px.histogram(df, y="PaymentMethod", color="Churn", barmode="group",
                       title="Churn by Payment Method")
    st.plotly_chart(fig, use_container_width=True)

def internet_vs_churn(df):
    st.subheader("🌐 Internet Service vs Churn")
    if df.empty:
        st.warning("No data available for the selected filters.")
        return
    fig = px.histogram(df, x="InternetService", color="Churn", barmode="group",
                       title="Churn by Internet Service")
    st.plotly_chart(fig, use_container_width=True)

def run_dashboard():
    st.title("📈 Telecom Customer Dashboard")
    df = load_data()

    # Sidebar Filters
    with st.sidebar:
        st.header("🔍 Filters")

        # Defaults
        default_gender = df['gender'].unique().tolist()
        default_contract = df['Contract'].unique().tolist()
        default_internet = df['InternetService'].unique().tolist()
        min_tenure, max_tenure = int(df['tenure'].min()), int(df['tenure'].max())

        # Filters
        gender_filter = st.multiselect("Select Gender", default_gender, default=default_gender)
        contract_filter = st.multiselect("Select Contract", default_contract, default=default_contract)
        internet_filter = st.multiselect("Select Internet Service", default_internet, default=default_internet)
        tenure_filter = st.slider("Select Tenure Range (months)", min_tenure, max_tenure, (min_tenure, max_tenure))

        # Clear Filters button
        if st.button("🔄 Clear Filters"):
            gender_filter = default_gender
            contract_filter = default_contract
            internet_filter = default_internet
            tenure_filter = (min_tenure, max_tenure)

    # Handle empty filters → reset to defaults
    if not gender_filter:
        gender_filter = default_gender
    if not contract_filter:
        contract_filter = default_contract
    if not internet_filter:
        internet_filter = default_internet

    # Apply Filters
    df_filtered = df[
        (df['gender'].isin(gender_filter)) &
        (df['Contract'].isin(contract_filter)) &
        (df['InternetService'].isin(internet_filter)) &
        (df['tenure'].between(tenure_filter[0], tenure_filter[1]))
    ]

    # Show KPIs & Visuals
    show_kpis(df_filtered)
    churn_distribution(df_filtered)
    contract_vs_churn(df_filtered)
    internet_vs_churn(df_filtered)
    payment_vs_churn(df_filtered)
















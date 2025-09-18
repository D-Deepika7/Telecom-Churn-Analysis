

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ------------------------------
# Load Data
# ------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/EDA_cleaned_telecom_churn_data.csv")
    return df


# ------------------------------
# KPIs
# ------------------------------
def show_kpis(df):
    total_customers = len(df)
    churned_customers = df[df['Churn'] == 'Yes'].shape[0]
    active_customers = total_customers - churned_customers
    churn_rate = round((churned_customers / total_customers) * 100, 2) if total_customers > 0 else 0
    avg_tenure = round(df['tenure'].mean(), 1) if total_customers > 0 else 0
    avg_monthly = round(df['MonthlyCharges'].mean(), 2) if total_customers > 0 else 0
    total_monthly_revenue = df['MonthlyCharges'].sum().round(2)

    st.subheader("📊 Key Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Customers", total_customers)
    col2.metric("Active Customers", active_customers)
    col3.metric("Churned Customers", churned_customers)

    col4, col5, col6 = st.columns(3)
    col4.metric("Churn Rate (%)", churn_rate)
    col5.metric("Avg Tenure (Months)", avg_tenure)
    col6.metric("Total Monthly Revenue ($)", total_monthly_revenue)


# ------------------------------
# Donut Charts
# ------------------------------
def gender_distribution(df):
    fig = px.pie(df, names="gender", hole=0.4, title="Customer Distribution by Gender")
    st.plotly_chart(fig, use_container_width=True)

def churn_distribution(df):
    fig = px.pie(df, names="Churn", hole=0.4, title="Churn Distribution",
                 color="Churn", color_discrete_map={"Yes": "red", "No": "green"})
    st.plotly_chart(fig, use_container_width=True)


# ------------------------------
# Line Chart
# ------------------------------
def churn_by_tenure(df):
    churn_rate = df.groupby("tenure")["Churn"].apply(lambda x: (x == "Yes").mean()).reset_index()
    fig = px.line(churn_rate, x="tenure", y="Churn",
                  title="Churn Rate by Tenure",
                  labels={"Churn": "Churn Rate"})
    st.plotly_chart(fig, use_container_width=True)


# ------------------------------
# Dynamic Clustered Column Chart
# ------------------------------
def churn_by_category(df, cat_col):
    if df.empty:
        st.warning("No data available for the selected filters.")
        return
    fig = px.histogram(
        df, 
        x=cat_col, 
        color="Churn", 
        barmode="group",
        title=f"Customer Distribution by {cat_col} and Churn"
    )
    st.plotly_chart(fig, use_container_width=True)


# ------------------------------
# Waterfall Chart
# ------------------------------
def revenue_waterfall(df, billing_parameter):
    if df.empty:
        st.warning("No data available for the selected filters.")
        return

    total_rev = df['MonthlyCharges'].sum()
    rev_by_cat = (
        df[df['Churn'] == 'Yes']
        .groupby(billing_parameter)['MonthlyCharges']
        .sum()
        .reset_index()
    )
    lost_total = rev_by_cat['MonthlyCharges'].sum()
    remaining_rev = total_rev - lost_total

    measures = ["absolute"] + ["relative"] * len(rev_by_cat) + ["total"]
    x = ["Total Revenue"] + rev_by_cat[billing_parameter].tolist() + ["Remaining Revenue"]
    y = [total_rev] + (-rev_by_cat['MonthlyCharges']).tolist() + [remaining_rev]

    fig = go.Figure(go.Waterfall(
        name="Revenue",
        orientation="v",
        measure=measures,
        x=x,
        y=y,
        connector={"line": {"color": "gray"}},
        decreasing={"marker": {"color": "red"}},
        increasing={"marker": {"color": "green"}},
        totals={"marker": {"color": "blue"}}
    ))
    fig.update_layout(title=f"Revenue Lost by {billing_parameter}", showlegend=False)
    st.plotly_chart(fig, use_container_width=True)


# ------------------------------
# Main Dashboard
# ------------------------------
def run_dashboard():
    st.title("📈 Telecom Customer Churn Dashboard")
    df = load_data()

    # Sidebar Filters
    with st.sidebar:
        st.header("🔍 Filters")
        gender_filter = st.multiselect("Select Gender", df['gender'].unique(), default=df['gender'].unique())
        contract_filter = st.multiselect("Select Contract", df['Contract'].unique(), default=df['Contract'].unique())
        internet_filter = st.multiselect("Select Internet Service", df['InternetService'].unique(), default=df['InternetService'].unique())
        tenure_filter = st.slider("Select Tenure Range (months)", int(df['tenure'].min()), int(df['tenure'].max()), 
                                  (int(df['tenure'].min()), int(df['tenure'].max())))

    # Apply Filters
    df_filtered = df[
        (df['gender'].isin(gender_filter)) &
        (df['Contract'].isin(contract_filter)) &
        (df['InternetService'].isin(internet_filter)) &
        (df['tenure'].between(tenure_filter[0], tenure_filter[1]))
    ]

    # KPIs
    show_kpis(df_filtered)

    # Donut Charts (2 cols)
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        gender_distribution(df_filtered)
    with col2:
        churn_distribution(df_filtered)

    # Line Chart: Churn by Tenure
    st.markdown("---")
    churn_by_tenure(df_filtered)

    # Dynamic Clustered Column Chart
    st.markdown("---")
    st.subheader("📊 Customer Distribution by Category")
    category_options = [
        "Contract", "PaymentMethod", "InternetService", "TechSupport",
        "DeviceProtection", "OnlineSecurity", "OnlineBackup", 
        "StreamingTV", "StreamingMovies", "gender"
    ]
    selected_cat = st.selectbox("Select Category", category_options)
    churn_by_category(df_filtered, selected_cat)

    # Waterfall Chart
    st.markdown("---")
    st.subheader("💡 Revenue Decomposition")
    wf_col1, wf_col2 = st.columns([1, 4])
    billing_options = [
        "PaymentMethod", "Contract", "InternetService", "TechSupport",
        "DeviceProtection", "OnlineSecurity", "OnlineBackup", "StreamingTV", "StreamingMovies"
    ]
    billing_param = st.selectbox("Billing Parameter", billing_options, key="billing_param")
    with wf_col2:
        revenue_waterfall(df_filtered, billing_param)


# Run app
if __name__ == "__main__":
    run_dashboard()

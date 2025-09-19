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
    total_monthly_revenue = df['MonthlyCharges'].sum()
    lifetime_revenue = df['TotalCharges'].sum() / 1e6  # in Millions

    # At-risk = churned OR on month-to-month contract with <12 months tenure
    at_risk_customers = df[
        (df['Churn'] == 'Yes') | ((df['Contract'] == 'Month-to-month') & (df['tenure'] < 12))
    ].shape[0]

    st.subheader("📊 Key Metrics")

    # Row 1: Customer counts
    c1, c2, c3 = st.columns(3)
    c1.metric("👥 Total Customers", total_customers)
    c2.metric("✅ Active Customers", active_customers)
    c3.metric("❌ Churned Customers", churned_customers)
    
    # Row 2: Churn & Tenure
    c4, c5, c6 = st.columns(3)
    c5.metric("📉 Churn Rate (%)", churn_rate)
    c4.metric("⚠️ At-Risk Customers", at_risk_customers)
    c6.metric("📆 Avg Tenure (Months)", avg_tenure)

    # Row 3: Revenue & Charges
    c7, c8, c9 = st.columns(3)
    c7.metric("💳 Avg Monthly Charges", f"${avg_monthly}")
    c8.metric("💵 Total Monthly Revenue", f"${total_monthly_revenue/1000:.2f}K")
    c9.metric("🏦 Total Lifetime Revenue", f"${lifetime_revenue:.2f}M")


# ------------------------------
# Donut Charts
# ------------------------------
def churn_distribution(df):
    fig = px.pie(df, names="Churn", hole=0.4, title="Churn Distribution",
                 color="Churn", color_discrete_map={"Yes": "red", "No": "green"})
    st.plotly_chart(fig, use_container_width=True)

def at_risk_distribution(df):
    df['AtRisk'] = df.apply(lambda x: "Yes" if (x['Churn'] == 'Yes') or (x['Contract'] == 'Month-to-month' and x['tenure'] < 12) else "No", axis=1)
    fig = px.pie(df, names="AtRisk", hole=0.4, title="At-Risk Customer Distribution",
                 color="AtRisk", color_discrete_map={"Yes": "orange", "No": "blue"})
    st.plotly_chart(fig, use_container_width=True)

def small_donut(df, col_name, title):
    fig = px.pie(df, names=col_name, hole=0.4, title=title)
    st.plotly_chart(fig, use_container_width=True)


# ------------------------------
# Line Chart
# ------------------------------
def churn_by_tenure(df):
    churn_rate = df.groupby("tenure")["Churn"].apply(lambda x: (x == "Yes").mean()).reset_index()
    fig = px.line(churn_rate, x="tenure", y="Churn",
                  title="📉 Churn Rate by Tenure",
                  labels={"Churn": "Churn Rate"})
    st.plotly_chart(fig, use_container_width=True)


# ------------------------------
# Scatter Plot
# ------------------------------
def scatter_tenure_monthly(df):
    fig = px.scatter(df, x="tenure", y="MonthlyCharges", size="TotalCharges",
                     color="Churn", hover_data=["Contract"],
                     title="🔵 Tenure vs Monthly Charges (Bubble by TotalCharges)")
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
        title=f"📊 Customer Distribution by {cat_col} and Churn"
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
    fig.update_layout(title=f"💡 Revenue Lost by {billing_parameter}", showlegend=False)
    st.plotly_chart(fig, use_container_width=True)


# ------------------------------
# Main Dashboard
# ------------------------------
def run_dashboard():
    st.title("📈 Telecom Customer Churn Dashboard")
    df = load_data()


    # Sidebar Filters
    with st.sidebar:

        # Defaults
        default_gender = df['gender'].unique().tolist()
        default_contract = df['Contract'].unique().tolist()
        default_internet = df['InternetService'].unique().tolist()
        min_tenure, max_tenure = int(df['tenure'].min()), int(df['tenure'].max())

        st.header("🔍 Filters")
        gender_filter = st.multiselect("Select Gender", df['gender'].unique(), default=df['gender'].unique())
        contract_filter = st.multiselect("Select Contract", df['Contract'].unique(), default=df['Contract'].unique())
        internet_filter = st.multiselect("Select Internet Service", df['InternetService'].unique(), default=df['InternetService'].unique())
        tenure_filter = st.slider("Select Tenure Range (months)", int(df['tenure'].min()), int(df['tenure'].max()), 
                                  (int(df['tenure'].min()), int(df['tenure'].max())))

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

    # KPIs
    show_kpis(df_filtered)

    # Donut Charts (2 cols)
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        churn_distribution(df_filtered)
    with col2:
        at_risk_distribution(df_filtered)

    # 4 small donuts
    st.markdown("---")
    st.subheader("👥 Customer Demographics")
    col1, col2 = st.columns(2)
    with col1:
        small_donut(df_filtered, "gender", "Gender")
    with col2:
        small_donut(df_filtered, "SeniorCitizen", "Senior Citizen")
    with col1:
        small_donut(df_filtered, "Dependents", "Dependents")
    with col2:
        small_donut(df_filtered, "Partner", "Partner")


    # Dynamic Clustered Column Chart
    st.markdown("---")
    st.subheader("📊 Customer Distribution by Category")
    category_options = [
        "Contract", "PaymentMethod", "InternetService", "TechSupport",
        "DeviceProtection", "OnlineSecurity", "OnlineBackup", 
        "StreamingTV", "StreamingMovies"
    ]
    selected_cat = st.selectbox("Select Category", category_options)
    churn_by_category(df_filtered, selected_cat)


    # Line Chart: Churn by Tenure
    st.markdown("---")
    churn_by_tenure(df_filtered)

    # Scatter Plot
    st.markdown("---")
    scatter_tenure_monthly(df_filtered)

    # Waterfall Chart
    st.markdown("---")
    st.subheader("💡 Revenue Decomposition")
    billing_options = [
        "PaymentMethod", "Contract", "InternetService", "TechSupport",
        "DeviceProtection", "OnlineSecurity", "OnlineBackup", "StreamingTV", "StreamingMovies"
    ]
    billing_param = st.selectbox("Billing Parameter", billing_options, key="billing_param")
    revenue_waterfall(df_filtered, billing_param)


# Run app
if __name__ == "__main__":
    run_dashboard()

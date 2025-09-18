# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# # Load data once here (best practice: cache it)
# @st.cache_data
# def load_data():
#     return pd.read_csv("data/EDA_cleaned_telecom_churn_data.csv")

# def show_dashboard():
#     st.title("📊 Customer Churn Dashboard")
#     df = load_data()

#     # Example KPI cards
#     total_customers = len(df)
#     churned = df[df["Churn"] == "Yes"].shape[0]
#     active = df[df["Churn"] == "No"].shape[0]
#     churn_rate = round(churned / total_customers * 100, 2)

#     col1, col2, col3, col4 = st.columns(4)
#     col1.metric("Total Customers", total_customers)
#     col2.metric("Active Customers", active)
#     col3.metric("Churned Customers", churned)
#     col4.metric("Churn Rate", f"{churn_rate}%")

#     # Example visual
#     st.subheader("Churn by Contract Type")
#     st.bar_chart(df["Contract"].value_counts())

#     # churn_by_contract = data.groupby("Contract")["Churn"].mean().reset_index()

#     # fig, ax = plt.subplots()
#     # ax.bar(churn_by_contract["Contract"], churn_by_contract["Churn"]*100)
#     # ax.set_ylabel("Churn Rate (%)")
#     # ax.set_xlabel("Contract Type")
#     # st.pyplot(fig)





# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load cleaned data
# @st.cache_data
# def load_data():
#     df = pd.read_csv("data/EDA_cleaned_telecom_churn_data.csv")
#     return df

# def show_kpis(df):
#     total_customers = len(df)
#     churned_customers = df[df['Churn'] == 'Yes'].shape[0]
#     active_customers = total_customers - churned_customers
#     churn_rate = round((churned_customers / total_customers) * 100, 2)
#     avg_tenure = round(df['tenure'].mean(), 1)
#     avg_monthly = round(df['MonthlyCharges'].mean(), 2)

#     st.subheader("📊 Key Metrics")
#     col1, col2, col3, col4, col5 = st.columns(5)
#     col1.metric("Total Customers", total_customers)
#     col2.metric("Active Customers", active_customers)
#     col3.metric("Churned Customers", churned_customers)
#     col4.metric("Churn Rate (%)", churn_rate)
#     col5.metric("Avg Tenure (Months)", avg_tenure)
#     st.metric("Avg Monthly Charges ($)", avg_monthly)

# def churn_distribution(df):
#     st.subheader("🔄 Churn Distribution")
#     fig, ax = plt.subplots()
#     churn_counts = df['Churn'].value_counts()
#     ax.pie(churn_counts, labels=churn_counts.index, autopct="%1.1f%%", startangle=90)
#     st.pyplot(fig)

# def contract_vs_churn(df):
#     st.subheader("📑 Contract Type vs Churn")
#     fig, ax = plt.subplots()
#     sns.countplot(data=df, x="Contract", hue="Churn", ax=ax)
#     ax.set_title("Churn by Contract Type")
#     st.pyplot(fig)

# def payment_vs_churn(df):
#     st.subheader("💳 Payment Method vs Churn")
#     fig, ax = plt.subplots()
#     sns.countplot(data=df, y="PaymentMethod", hue="Churn", ax=ax)
#     ax.set_title("Churn by Payment Method")
#     st.pyplot(fig)

# def run_dashboard():
#     st.title("📈 Telecom Customer Churn Dashboard")
#     df = load_data()

#     # Filters
#     with st.sidebar:
#         st.header("🔍 Filters")
#         gender_filter = st.selectbox("Select Gender", ["All"] + df['gender'].unique().tolist())
#         contract_filter = st.selectbox("Select Contract", ["All"] + df['Contract'].unique().tolist())

#     # Apply filters
#     if gender_filter != "All":
#         df = df[df['gender'] == gender_filter]
#     if contract_filter != "All":
#         df = df[df['Contract'] == contract_filter]

#     # Show KPIs & Visuals
#     show_kpis(df)
#     churn_distribution(df)
#     contract_vs_churn(df)
#     payment_vs_churn(df)




















# ## plotly + filters



# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # Load cleaned data
# @st.cache_data
# def load_data():
#     df = pd.read_csv("data/EDA_cleaned_telecom_churn_data.csv")
#     return df

# def show_kpis(df):
#     total_customers = len(df)
#     churned_customers = df[df['Churn'] == 'Yes'].shape[0]
#     active_customers = total_customers - churned_customers
#     churn_rate = round((churned_customers / total_customers) * 100, 2)
#     avg_tenure = round(df['tenure'].mean(), 1)
#     avg_monthly = round(df['MonthlyCharges'].mean(), 2)

#     st.subheader("📊 Key Metrics")
#     col1, col2, col3 = st.columns(3)
#     col1.metric("Total Customers", total_customers)
#     col2.metric("Active Customers", active_customers)
#     col3.metric("Churned Customers", churned_customers)

#     col4, col5, col6 = st.columns(3)
#     col4.metric("Churn Rate (%)", churn_rate)
#     col5.metric("Avg Tenure (Months)", avg_tenure)
#     col6.metric("Avg Monthly Charges ($)", avg_monthly)

# def churn_distribution(df):
#     st.subheader("🔄 Churn Distribution")
#     fig = px.pie(df, names="Churn", hole=0.4, color="Churn",
#                  color_discrete_map={"Yes": "red", "No": "green"})
#     st.plotly_chart(fig, use_container_width=True)

# def contract_vs_churn(df):
#     st.subheader("📑 Contract Type vs Churn")
#     fig = px.histogram(df, x="Contract", color="Churn", barmode="group",
#                        title="Churn by Contract Type")
#     st.plotly_chart(fig, use_container_width=True)

# def payment_vs_churn(df):
#     st.subheader("💳 Payment Method vs Churn")
#     fig = px.histogram(df, y="PaymentMethod", color="Churn", barmode="group",
#                        title="Churn by Payment Method")
#     st.plotly_chart(fig, use_container_width=True)

# def internet_vs_churn(df):
#     st.subheader("🌐 Internet Service vs Churn")
#     fig = px.histogram(df, x="InternetService", color="Churn", barmode="group",
#                        title="Churn by Internet Service")
#     st.plotly_chart(fig, use_container_width=True)

# def run_dashboard():
#     st.title("📈 Telecom Customer Churn Dashboard")
#     df = load_data()

#     # Sidebar Filters
#     with st.sidebar:
#         st.header("🔍 Filters")
#         gender_filter = st.multiselect("Select Gender", df['gender'].unique(), default=df['gender'].unique())
#         contract_filter = st.multiselect("Select Contract", df['Contract'].unique(), default=df['Contract'].unique())
#         internet_filter = st.multiselect("Select Internet Service", df['InternetService'].unique(), default=df['InternetService'].unique())

#     # Apply Filters
#     df_filtered = df[
#         (df['gender'].isin(gender_filter)) &
#         (df['Contract'].isin(contract_filter)) &
#         (df['InternetService'].isin(internet_filter))
#     ]

#     # Show KPIs & Visuals
#     show_kpis(df_filtered)
#     churn_distribution(df_filtered)
#     contract_vs_churn(df_filtered)
#     internet_vs_churn(df_filtered)
#     payment_vs_churn(df_filtered)


















# ## tenure slider + clear filter button


# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # Load cleaned data
# @st.cache_data
# def load_data():
#     df = pd.read_csv("data/EDA_cleaned_telecom_churn_data.csv")
#     return df

# def show_kpis(df):
#     total_customers = len(df)
#     churned_customers = df[df['Churn'] == 'Yes'].shape[0]
#     active_customers = total_customers - churned_customers
#     churn_rate = round((churned_customers / total_customers) * 100, 2)
#     avg_tenure = round(df['tenure'].mean(), 1)
#     avg_monthly = round(df['MonthlyCharges'].mean(), 2)

#     st.subheader("📊 Key Metrics")
#     col1, col2, col3 = st.columns(3)
#     col1.metric("Total Customers", total_customers)
#     col2.metric("Active Customers", active_customers)
#     col3.metric("Churned Customers", churned_customers)

#     col4, col5, col6 = st.columns(3)
#     col4.metric("Churn Rate (%)", churn_rate)
#     col5.metric("Avg Tenure (Months)", avg_tenure)
#     col6.metric("Avg Monthly Charges ($)", avg_monthly)

# def churn_distribution(df):
#     st.subheader("🔄 Churn Distribution")
#     fig = px.pie(df, names="Churn", hole=0.4, color="Churn",
#                  color_discrete_map={"Yes": "red", "No": "green"})
#     st.plotly_chart(fig, use_container_width=True)

# def contract_vs_churn(df):
#     st.subheader("📑 Contract Type vs Churn")
#     fig = px.histogram(df, x="Contract", color="Churn", barmode="group",
#                        title="Churn by Contract Type")
#     st.plotly_chart(fig, use_container_width=True)

# def payment_vs_churn(df):
#     st.subheader("💳 Payment Method vs Churn")
#     fig = px.histogram(df, y="PaymentMethod", color="Churn", barmode="group",
#                        title="Churn by Payment Method")
#     st.plotly_chart(fig, use_container_width=True)

# def internet_vs_churn(df):
#     st.subheader("🌐 Internet Service vs Churn")
#     fig = px.histogram(df, x="InternetService", color="Churn", barmode="group",
#                        title="Churn by Internet Service")
#     st.plotly_chart(fig, use_container_width=True)

# def run_dashboard():
#     st.title("📈 Telecom Customer Churn Dashboard")
#     df = load_data()

#     # Sidebar Filters
#     with st.sidebar:
#         st.header("🔍 Filters")

#         # Default selections
#         default_gender = df['gender'].unique().tolist()
#         default_contract = df['Contract'].unique().tolist()
#         default_internet = df['InternetService'].unique().tolist()
#         min_tenure, max_tenure = int(df['tenure'].min()), int(df['tenure'].max())

#         # Filters
#         gender_filter = st.multiselect("Select Gender", df['gender'].unique(), default=default_gender)
#         contract_filter = st.multiselect("Select Contract", df['Contract'].unique(), default=default_contract)
#         internet_filter = st.multiselect("Select Internet Service", df['InternetService'].unique(), default=default_internet)
#         tenure_filter = st.slider("Select Tenure Range (months)", min_tenure, max_tenure, (min_tenure, max_tenure))

#         # Clear Filters button
#         if st.button("🔄 Clear Filters"):
#             gender_filter = default_gender
#             contract_filter = default_contract
#             internet_filter = default_internet
#             tenure_filter = (min_tenure, max_tenure)

#     # Apply Filters
#     df_filtered = df[
#         (df['gender'].isin(gender_filter)) &
#         (df['Contract'].isin(contract_filter)) &
#         (df['InternetService'].isin(internet_filter)) &
#         (df['tenure'].between(tenure_filter[0], tenure_filter[1]))
#     ]

#     # Show KPIs & Visuals
#     show_kpis(df_filtered)
#     churn_distribution(df_filtered)
#     contract_vs_churn(df_filtered)
#     internet_vs_churn(df_filtered)
#     payment_vs_churn(df_filtered)
















## error handling empty filters


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















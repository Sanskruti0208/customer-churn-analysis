import streamlit as st
import pandas as pd
import plotly.express as px
from charts import *
from segmentation import customer_segment
from ml_model import train_churn_model 
from load_data import load_dataset
from analysis import clean_data

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Customer Churn Dashboard",
    layout="wide"
)

# -----------------------------------
# LOAD DATA
# -----------------------------------

df = load_dataset()
df = clean_data(df)

# -----------------------------------
# TITLE
# -----------------------------------

st.title("📊 Customer Churn Analysis Dashboard")

st.markdown("""
Analyze customer churn trends, identify high-risk customers,
and generate business retention insights.
""")

# -----------------------------------
# SIDEBAR FILTERS
# -----------------------------------

st.sidebar.header("FILTERS")

contract_filter = st.sidebar.multiselect(
    "Contract Type",
    options=df["Contract"].unique(),
    default=df["Contract"].unique()
)

internet_filter = st.sidebar.multiselect(
    "Internet Service",
    options=df["InternetService"].unique(),
    default=df["InternetService"].unique()
)

gender_filter = st.sidebar.multiselect(
    "Gender",
    options=df["gender"].unique(),
    default=df["gender"].unique()
)

# -----------------------------------
# APPLY FILTERS
# -----------------------------------

filtered_df = df[
    (df["Contract"].isin(contract_filter)) &
    (df["InternetService"].isin(internet_filter)) &
    (df["gender"].isin(gender_filter))
]

# -----------------------------------
# KPI SECTION
# -----------------------------------

total_customers = filtered_df.shape[0]

churned_customers = filtered_df[
    filtered_df["Churn"] == "Yes"
].shape[0]

active_customers = filtered_df[
    filtered_df["Churn"] == "No"
].shape[0]

churn_rate = round(
    (churned_customers / total_customers) * 100,
    2
)

avg_monthly_charge = round(
    filtered_df["MonthlyCharges"].mean(),
    2
)

# KPI CARDS

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Customers", total_customers)
col2.metric("Churned", churned_customers)
col3.metric("Active", active_customers)
col4.metric("Churn Rate", f"{churn_rate}%")
col5.metric("Avg Monthly Charge", f"${avg_monthly_charge}")



# -----------------------------------
# CHURN RISK SCORE SYSTEM
# -----------------------------------

def calculate_risk(row):

    score = 0

    # Contract Risk
    if row["Contract"] == "Month-to-month":
        score += 40

    # Internet Service Risk
    if row["InternetService"] == "Fiber optic":
        score += 30

    # New Customer Risk
    if row["tenure"] < 12:
        score += 20

    # Payment Risk
    if row["PaymentMethod"] == "Electronic check":
        score += 10

    return score

# Create Risk Score Column
filtered_df["RiskScore"] = filtered_df.apply(
    calculate_risk,
    axis=1
)
filtered_df["CustomerSegment"] = filtered_df.apply(
    customer_segment,
    axis=1
)

# Identify High Risk Customers
high_risk = filtered_df[
    filtered_df["RiskScore"] >= 70
]

# -----------------------------------
# HIGH RISK CUSTOMER TABLE
# -----------------------------------

st.subheader("⚠️ High Risk Customers")

st.write(
    f"Identified {high_risk.shape[0]} high-risk customers."
)

st.dataframe(
    high_risk[
        [
            "customerID",
            "RiskScore",
            "tenure",
            "MonthlyCharges",
            "Contract",
            "InternetService",
            "PaymentMethod"
        ]
    ]
    .sort_values(
        by="RiskScore",
        ascending=False
    )
    .head(15)
)

# -----------------------------------
# CUSTOMER SEGMENTATION
# -----------------------------------

st.subheader("🧩 Customer Segmentation")

segment_counts = (
    filtered_df["CustomerSegment"]
    .value_counts()
    .reset_index()
)

segment_counts.columns = [
    "CustomerSegment",
    "Count"
]

segment_chart = px.pie(
    segment_counts,
    names="CustomerSegment",
    values="Count",
    title="Customer Segmentation Distribution"
)

st.plotly_chart(
    segment_chart,
    use_container_width=True,
    key="segment_chart"
)

st.dataframe(
    segment_counts
)

# -----------------------------------
# RETENTION RECOMMENDATION ENGINE
# -----------------------------------

st.subheader("🧠 Retention Recommendation Engine")

st.markdown("""
### Recommended Retention Strategies

✅ Offer discounts for yearly contracts

✅ Improve onboarding for new customers

✅ Create loyalty rewards for high-value users

✅ Improve support quality for Fiber Optic users

✅ Target Electronic Check customers with offers
""")

# -----------------------------------
# REVENUE IMPACT ANALYSIS
# -----------------------------------

monthly_revenue_loss = filtered_df[
    filtered_df["Churn"] == "Yes"
]["MonthlyCharges"].sum()

annual_revenue_loss = monthly_revenue_loss * 12

st.subheader("💰 Revenue Impact")

col1, col2 = st.columns(2)

col1.metric(
    "Estimated Monthly Revenue Loss",
    f"${round(monthly_revenue_loss, 2)}"
)

col2.metric(
    "Estimated Annual Revenue Loss",
    f"${round(annual_revenue_loss, 2)}"
)

# -----------------------------------
# BUSINESS INSIGHTS
# -----------------------------------

st.subheader("📌 Business Insights")

st.markdown("""
### Key Findings

- Month-to-month customers churn the most
- Fiber optic users show high churn probability
- Electronic check users are high-risk customers
- Customers with low tenure churn earlier

### Business Impact

- High churn affects recurring revenue
- Retaining early-stage customers improves profitability
- Long-term contracts reduce churn significantly
""")

# -----------------------------------
# MACHINE LEARNING PREDICTION
# -----------------------------------

st.header("🤖 Churn Prediction Model")

accuracy, importance_df = train_churn_model(filtered_df)

st.metric(
    "Model Accuracy",
    f"{round(accuracy * 100, 2)}%"
)

st.subheader("📌 Feature Importance")

importance_chart = px.bar(
    importance_df.head(10),
    x="Importance",
    y="Feature",
    orientation="h",
    title="Top Features Affecting Churn"
)

st.plotly_chart(
    importance_chart,
    use_container_width=True,
    key="importance_chart"
)

st.dataframe(
    importance_df.head(10)
)

# -----------------------------------
# VISUAL ANALYTICS
# -----------------------------------

st.header("📊 Visual Analytics")

chart1 = churn_by_contract_chart(filtered_df)
st.plotly_chart(
    chart1,
    use_container_width=True,
    key="contract_chart"
)

chart2 = churn_by_internet_chart(filtered_df)
st.plotly_chart(
    chart2,
    use_container_width=True,
    key="internet_chart"
)

chart3 = churn_by_payment_chart(filtered_df)
st.plotly_chart(
    chart3,
    use_container_width=True,
    key="payment_chart"
)

chart4 = tenure_distribution_chart(filtered_df)
st.plotly_chart(
    chart4,
    use_container_width=True,
    key="tenure_chart"
)
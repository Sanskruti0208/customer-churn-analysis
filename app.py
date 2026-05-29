from load_data import load_dataset
from analysis import (
    clean_data,
    calculate_kpis,
    churn_analysis
)
from insights import generate_business_insights
from charts import (
    plot_churn_distribution,
    plot_contract_churn
)

# Load dataset
df = load_dataset()

# Clean dataset
df = clean_data(df)

# KPIs
calculate_kpis(df)

# Analysis
churn_analysis(df)

# Insights
generate_business_insights(df)

# Charts
plot_churn_distribution(df)
plot_contract_churn(df)
def generate_business_insights(df):

    print("\nBUSINESS INSIGHTS")
    print("----------------------")

    contract_churn = (
        df.groupby("Contract")["Churn"]
        .apply(lambda x: (x == "Yes").mean() * 100)
        .sort_values(ascending=False)
    )

    print(f"""
1. Customers with Month-to-month contracts are churning the most.
   Churn Rate: {contract_churn.iloc[0]:.2f}%
""")

    internet_churn = (
        df.groupby("InternetService")["Churn"]
        .apply(lambda x: (x == "Yes").mean() * 100)
        .sort_values(ascending=False)
    )

    print(f"""
2. Fiber optic users show the highest churn.
   Churn Rate: {internet_churn.iloc[0]:.2f}%
""")

    payment_churn = (
        df.groupby("PaymentMethod")["Churn"]
        .apply(lambda x: (x == "Yes").mean() * 100)
        .sort_values(ascending=False)
    )

    print(f"""
3. Customers using Electronic Check payment churn the most.
   Churn Rate: {payment_churn.iloc[0]:.2f}%
""")

    avg_tenure_churn = df[df["Churn"] == "Yes"]["tenure"].mean()

    print(f"""
4. Churned customers have low average tenure.
   Average Tenure: {avg_tenure_churn:.2f} months
""")

    print("""
5. RECOMMENDED ACTION PLAN:
   - Promote yearly contracts using discounts
   - Improve service quality for fiber users
   - Target new customers within first 6 months
   - Create retention campaigns for electronic check users
""")
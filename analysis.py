import pandas as pd


def clean_data(df):

    print("\nFIRST 5 ROWS:")
    print(df.head())

    print("\nDATASET SHAPE:")
    print(df.shape)

    print("\nCOLUMN NAMES:")
    print(df.columns)

    print("\nMISSING VALUES:")
    print(df.isnull().sum())

    print("\nDATA TYPES:")
    print(df.dtypes)

    # Convert TotalCharges to numeric
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    # Remove null values
    df.dropna(inplace=True)

    print("\nUPDATED DATA TYPES:")
    print(df.dtypes)

    print("\nUPDATED DATASET SHAPE:")
    print(df.shape)

    return df


def calculate_kpis(df):

    total_customers = df.shape[0]

    churned_customers = df[df["Churn"] == "Yes"].shape[0]

    active_customers = total_customers - churned_customers

    churn_rate = (
        churned_customers / total_customers
    ) * 100

    print("\nBUSINESS KPIs")
    print("-------------------")

    print(f"Total Customers: {total_customers}")
    print(f"Active Customers: {active_customers}")
    print(f"Churned Customers: {churned_customers}")
    print(f"Churn Rate: {churn_rate:.2f}%")


def churn_analysis(df):

    print("\nCHURN BY CONTRACT TYPE (%)")

    contract_churn = pd.crosstab(
        df["Contract"],
        df["Churn"],
        normalize="index"
    ) * 100

    print(contract_churn)

    print("\nCHURN BY INTERNET SERVICE (%)")

    internet_churn = pd.crosstab(
        df["InternetService"],
        df["Churn"],
        normalize="index"
    ) * 100

    print(internet_churn)

    print("\nCHURN BY PAYMENT METHOD (%)")

    payment_churn = pd.crosstab(
        df["PaymentMethod"],
        df["Churn"],
        normalize="index"
    ) * 100

    print(payment_churn)

    print("\nAVERAGE TENURE BY CHURN STATUS")

    avg_tenure = df.groupby("Churn")["tenure"].mean()

    print(avg_tenure)
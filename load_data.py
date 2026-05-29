import pandas as pd


def load_dataset():

    df = pd.read_csv("C:/Users/sansk/Downloads/customer-churn-analysis/data/customer_churn.csv")

    print(df.head())

    print("\nDataset Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns)

    return df
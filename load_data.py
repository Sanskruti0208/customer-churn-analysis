import pandas as pd

def load_dataset():

    df = pd.read_csv("data/customer_churn.csv")

    return df

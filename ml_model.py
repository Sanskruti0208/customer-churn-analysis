from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import pandas as pd


def train_churn_model(df):

    # -----------------------------
    # DROP UNNECESSARY COLUMN
    # -----------------------------

    model_df = df.drop(columns=["customerID"])

    # -----------------------------
    # CONVERT TARGET VARIABLE
    # -----------------------------

    model_df["Churn"] = model_df["Churn"].map({
        "Yes": 1,
        "No": 0
    })

    # -----------------------------
    # ONE-HOT ENCODING
    # -----------------------------

    model_df = pd.get_dummies(
        model_df,
        drop_first=True
    )

    # -----------------------------
    # FEATURES & TARGET
    # -----------------------------

    X = model_df.drop("Churn", axis=1)
    y = model_df["Churn"]

    # -----------------------------
    # TRAIN TEST SPLIT
    # -----------------------------

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # -----------------------------
    # MODEL TRAINING
    # -----------------------------

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    # -----------------------------
    # PREDICTIONS
    # -----------------------------

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    # -----------------------------
    # FEATURE IMPORTANCE
    # -----------------------------

    importance_df = pd.DataFrame({
        "Feature": X.columns,
        "Importance": model.feature_importances_
    })

    importance_df = importance_df.sort_values(
        by="Importance",
        ascending=False
    )

    return accuracy, importance_df
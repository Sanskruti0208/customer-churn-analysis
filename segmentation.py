def customer_segment(row):

    # Loyal Customers
    if row["tenure"] >= 48 and row["Churn"] == "No":
        return "Loyal Customer"

    # High Value Customers
    elif row["MonthlyCharges"] > 80:
        return "High Value Customer"

    # At Risk Customers
    elif (
        row["Contract"] == "Month-to-month"
        and row["InternetService"] == "Fiber optic"
    ):
        return "At Risk Customer"

    # New Customers
    elif row["tenure"] < 12:
        return "New Customer"

    else:
        return "Regular Customer"
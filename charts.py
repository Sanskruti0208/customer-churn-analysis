import plotly.express as px


def churn_by_contract_chart(df):

    return px.histogram(
        df,
        x="Contract",
        color="Churn",
        barmode="group",
        title="Churn by Contract Type"
    )


def churn_by_internet_chart(df):

    return px.histogram(
        df,
        x="InternetService",
        color="Churn",
        barmode="group",
        title="Churn by Internet Service"
    )


def churn_by_payment_chart(df):

    return px.histogram(
        df,
        x="PaymentMethod",
        color="Churn",
        barmode="group",
        title="Churn by Payment Method"
    )


def tenure_distribution_chart(df):

    return px.box(
        df,
        x="Churn",
        y="tenure",
        color="Churn",
        title="Customer Tenure Distribution"
    )
from sqlalchemy import create_engine


def connect_database():

    username = "postgres"
    password = "0208"
    host = "localhost"
    port = "5432"
    database = "customer_churn_db"

    engine = create_engine(
        f"postgresql://{username}:{password}@{host}:{port}/{database}"
    )

    return engine
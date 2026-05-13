import pandas as pd
from scripts.load_data import load_data

def clean_participants(df=None):
    if df is None:
        df = load_data("participants")

    df = df.copy()  # never modify the original

    # Parse date
    df["enrolled_date"] = pd.to_datetime(df["enrolled_date"])

    # Fill missing age
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["age"] = df["age"].fillna(df["age"].median())

    # Clean text fields
    df["name"] = df["name"].str.strip().str.title()
    df["status"] = df["status"].str.strip().str.lower()

    # Add computed columns
    df["age_category"] = df["age"].apply(lambda a:
        "minor" if a < 18 else ("senior" if a >= 65 else "adult"))
    df["enroll_month"] = df["enrolled_date"].dt.month
    df = df.rename(columns={
        "enrolled_date":"enrollment date",
        "age_category":"age category",
        "enroll_month":"enrollment month"
    })
    df.columns = [name.title() for name in df.columns]

    return df


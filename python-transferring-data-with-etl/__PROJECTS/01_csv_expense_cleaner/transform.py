import pandas as pd

def transform(df: pd.DataFrame) -> pd.DataFrame:
    print(f"🔄 Starting transform — {len(df)} rows")

    # 1. Drop rows missing critical fields
    df = df.dropna(subset=["vendor", "date"])
    print(f"   After dropping nulls: {len(df)} rows")

    # 2. Normalize casing
    df["category"] = df["category"].str.lower()
    df["vendor"] = df["vendor"].str.strip()

    # 3. Standardize date format
    df["date"] = pd.to_datetime(df["date"], format="mixed")
    df["date"] = df["date"].dt.strftime("%Y-%m-%d")

    # 4. Remove duplicates
    # df = df.drop_duplicates()
    df = df.drop_duplicates(subset=["date", "vendor", "amount", "category"])

    print(f"   After deduplication: {len(df)} rows")

    print("✅ Transform complete")
    print(df)
    return df

if __name__ == "__main__":
    from extract import extract
    raw = extract("expenses_raw.csv")
    clean = transform(raw)
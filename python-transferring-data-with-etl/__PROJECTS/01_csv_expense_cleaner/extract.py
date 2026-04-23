import pandas as pd

def extract(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    print(f"✅ Extracted {len(df)} rows from {filepath}")
    print(df)
    return df

if __name__ == "__main__":
    df = extract("expenses_raw.csv")
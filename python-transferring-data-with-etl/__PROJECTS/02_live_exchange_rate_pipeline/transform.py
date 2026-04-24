import pandas as pd

CURRENCIES = ["EUR", "GBP", "JPY", "CAD", "MXN", "CHF", "AUD"]

def transform(df: pd.DataFrame) -> pd.DataFrame:
    print(f"🔄 Starting transform — {len(df)} currencies")

    # Filter to only relevant currencies
    df = df[df["currency"].isin(CURRENCIES)].copy()

    # Round rates
    df["rate"] = df["rate"].round(6)

    # Compute USD-adjusted total (how much 1000 USD buys in each currency)
    df["usd_1000_equivalent"] = (1000 * df["rate"]).round(2)

    df = df.reset_index(drop=True)

    print(f"✅ Transform complete — {len(df)} rows")
    print(df)
    return df

if __name__ == "__main__":
    from extract import extract
    raw = extract()
    transform(raw)
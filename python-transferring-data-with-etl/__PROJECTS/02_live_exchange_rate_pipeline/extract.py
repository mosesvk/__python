import requests
import pandas as pd 
from datetime import date

def extract() -> pd.DataFrame:
    url = "https://open.er-api.com/v6/latest/USD"

    res = requests.get(url)
    res.raise_for_status()

    data = res.json()
    print(f"✅ API responded — base: {data['base_code']}, date: {data['time_last_update_utc']}")

    rates = data["rates"]
    df = pd.DataFrame(rates.items(), columns=["currency", "rate"])
    df["base_currency"] = data["base_code"]
    df['extracted_date'] = date.today().isoformat()

    print(df.head())
    return df

if __name__ == '__main__':
    extract()
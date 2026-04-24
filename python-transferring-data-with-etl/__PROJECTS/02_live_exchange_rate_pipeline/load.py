import psycopg2
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

def load(df: pd.DataFrame):
    conn = get_connection()
    cur = conn.cursor()

    # Create table if it doesn't exist yet
    cur.execute("""
        CREATE TABLE IF NOT EXISTS exchange_rates (
            currency        TEXT,
            rate            NUMERIC,
            base_currency   TEXT,
            extracted_date  DATE,
            usd_1000_equivalent NUMERIC
        )
    """)

    # Incremental append — insert each row
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO exchange_rates 
            VALUES (%s, %s, %s, %s, %s)
        """, tuple(row))

    conn.commit()
    cur.close()
    conn.close()
    print(f"✅ Loaded {len(df)} rows into PostgreSQL (incremental append)")

if __name__ == "__main__":
    from extract import extract
    from transform import transform
    raw = extract()
    clean = transform(raw)
    load(clean)
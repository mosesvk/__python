import sqlite3
import pandas as pd

def load(df: pd.DataFrame, db_path: str = "expenses.db"):
    conn = sqlite3.connect(db_path)
    
    df.to_sql("expenses", conn, if_exists="replace", index=False)
    
    print(f"✅ Loaded {len(df)} rows into '{db_path}'")
    
    # Verify it landed correctly
    result = pd.read_sql("SELECT * FROM expenses", conn)
    print(result)
    
    conn.close()

if __name__ == "__main__":
    from extract import extract
    from transform import transform
    raw = extract("expenses_raw.csv")
    clean = transform(raw)
    load(clean)
# pipeline.py
from extract import extract
from transform import transform
from load import load

def run():
    print("🚀 Starting ETL Pipeline")
    raw = extract("expenses_raw.csv")
    clean = transform(raw)
    load(clean)
    print("🏁 Pipeline complete")

if __name__ == "__main__":
    run()
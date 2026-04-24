# 01 CSV Expense Cleaner (ETL)

This project is a small local ETL pipeline that reads raw expense data from a CSV file, cleans and standardizes it, and writes the cleaned dataset into a SQLite database.

## What this project does

- **Extract**: reads `expenses_raw.csv` into a pandas DataFrame.
- **Transform**:
  - drops rows missing required values (`vendor`, `date`)
  - normalizes text fields (`category`, `vendor`)
  - standardizes date format to `YYYY-MM-DD`
  - removes duplicate records by business key
- **Load**: writes cleaned data to the `expenses` table in `expenses.db`.
- **Pipeline**: orchestrates `extract -> transform -> load`.

## Files and how they connect

- `extract.py`: loads raw CSV data.
- `transform.py`: applies cleaning and standardization rules.
- `load.py`: persists transformed rows to SQLite.
- `pipeline.py`: main entry point that runs the full ETL flow.
- `requirements.txt`: Python dependencies for this project.

## Prerequisites

- Python 3.10+ recommended
- `pip`

## Install dependencies

From this folder:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Input and output

- **Input**: `expenses_raw.csv` in this project directory
- **Output**: `expenses.db` SQLite database with an `expenses` table

## Run the pipeline

```bash
python pipeline.py
```

You should see logs for each ETL stage and a completion message.

## Run stages individually (optional)

```bash
python extract.py
python transform.py
python load.py
```

Use this when debugging a specific ETL stage.

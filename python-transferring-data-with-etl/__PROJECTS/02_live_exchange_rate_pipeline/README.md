# 02 Live Exchange Rate Pipeline (ETL)

This project is an API-driven ETL pipeline that fetches live exchange rates (USD base), transforms selected currencies for analytics, and appends results into PostgreSQL.

## What this project does

- **Extract**: calls ExchangeRate-API (`https://open.er-api.com/v6/latest/USD`) and converts rates to a pandas DataFrame.
- **Transform**:
  - filters to a target currency list
  - rounds exchange rates
  - computes `usd_1000_equivalent` for quick comparison metrics
- **Load**:
  - connects to PostgreSQL using environment variables
  - ensures `exchange_rates` table exists
  - appends transformed records
- **Pipeline**: orchestrates `extract -> transform -> load`.

## Files and how they connect

- `extract.py`: fetches live rates from the external API.
- `transform.py`: keeps relevant currencies and computes derived columns.
- `load.py`: writes records to PostgreSQL.
- `pipeline.py`: main entry point that runs the full ETL flow.
- `.env`: database connection variables used by `load.py`.
- `requirements.txt`: Python dependencies for this project.

## Prerequisites

- Python 3.10+ recommended
- `pip`
- Running PostgreSQL instance reachable from your machine

## Install dependencies

From this folder:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Configure environment variables

Create/update `.env` in this folder with:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database
DB_USER=your_username
DB_PASSWORD=your_password
```

## Run the pipeline

```bash
python pipeline.py
```

The run flow is:

1. Pull latest USD-based rates from the API.
2. Transform data for selected currencies.
3. Insert rows into PostgreSQL `exchange_rates`.

## Run stages individually (optional)

```bash
python extract.py
python transform.py
python load.py
```

Use individual scripts when validating one ETL stage at a time.

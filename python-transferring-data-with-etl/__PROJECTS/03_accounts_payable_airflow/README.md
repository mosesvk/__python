# 03 Accounts Payable Airflow

This project demonstrates a simple **accounts payable ETL pipeline** orchestrated with Apache Airflow.

At a high level, the DAG in `dags/ap_pipeline.py` runs three tasks daily:

1. **Extract**: builds an in-memory invoice dataset (sample data).
2. **Transform**: deduplicates invoices, parses dates, computes a late-payment flag, and masks vendor names.
3. **Load**: prints curated rows that are ready to be loaded to a downstream warehouse.

## Project Layout

- `dags/ap_pipeline.py`: main Airflow DAG (`accounts_payable_pipeline`).
- `docker-compose.yaml`: local Airflow stack (webserver, scheduler, worker, postgres, redis).
- `.env`: local environment variables (currently `AIRFLOW_UID`).
- `logs/`, `plugins/`, `config/`: Airflow runtime folders.

## Prerequisites

- Docker Desktop (or Docker Engine + Compose plugin)
- Python 3.10+ (optional, if you want local non-Docker testing)

## Setup (Docker - Recommended)

From this folder:

```bash
docker compose up airflow-init
docker compose up -d
```

Then open Airflow UI at [http://localhost:8080](http://localhost:8080).

Default credentials from the compose config:

- Username: `airflow`
- Password: `airflow`

## Running the DAG

1. In Airflow UI, locate DAG `accounts_payable_pipeline`.
2. Toggle it **On**.
3. Trigger a run manually (or wait for schedule).
4. View task logs for `extract`, `transform`, and `load` to inspect ETL outputs.

## Stop the Stack

```bash
docker compose down
```

To also remove persisted Postgres data volume:

```bash
docker compose down -v
```

## Python Dependencies

Install project dependencies (if needed outside Docker):

```bash
pip install -r requirements.txt
```

The DAG currently depends on:

- `apache-airflow` for orchestration
- `pandas` for ETL transformations


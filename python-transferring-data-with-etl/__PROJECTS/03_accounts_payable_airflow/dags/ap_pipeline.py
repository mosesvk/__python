from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def extract_invoices(**context):
    import pandas as pd
    data = {
        "invoice_id": [1, 2, 3, 4],
        "vendor":     ["Acme Corp", "Dell", "Acme Corp", "Staples"],
        "amount":     [1500.00, 899.99, 1500.00, 45.00],
        "due_date":   ["2024-01-10", "2024-01-15", "2024-01-10", "2024-02-01"],
        "paid_date":  ["2024-01-20", "2024-01-14", "2024-01-20", None],
        "currency":   ["USD", "EUR", "USD", "USD"]
    }
    df = pd.DataFrame(data)
    context["ti"].xcom_push(key="invoices", value=df.to_json())
    print(f"✅ Extracted {len(df)} invoices")

def transform_invoices(**context):
    import pandas as pd
    raw = context["ti"].xcom_pull(key="invoices", task_ids="extract")
    df = pd.read_json(raw)
    df = df.drop_duplicates(subset=["vendor", "amount", "due_date"])
    df["due_date"]  = pd.to_datetime(df["due_date"])
    df["paid_date"] = pd.to_datetime(df["paid_date"], errors="coerce")
    df["late"] = df["paid_date"] > df["due_date"]
    df["vendor_masked"] = df["vendor"].apply(lambda x: x[:2] + "***")
    context["ti"].xcom_push(key="clean_invoices", value=df.to_json())
    print(f"✅ Transformed — {len(df)} rows")
    print(df)

def load_invoices(**context):
    import pandas as pd
    clean = context["ti"].xcom_pull(key="clean_invoices", task_ids="transform")
    df = pd.read_json(clean)
    print("✅ Load complete — rows ready for warehouse:")
    print(df[["invoice_id", "vendor_masked", "amount", "late"]])

with DAG(
    dag_id="accounts_payable_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule=timedelta(days=1),
    catchup=False
) as dag:

    extract = PythonOperator(
        task_id="extract",
        python_callable=extract_invoices
    )

    transform = PythonOperator(
        task_id="transform",
        python_callable=transform_invoices
    )

    load = PythonOperator(
        task_id="load",
        python_callable=load_invoices
    )

    extract >> transform >> load
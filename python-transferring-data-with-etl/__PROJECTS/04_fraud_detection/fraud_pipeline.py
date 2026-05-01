from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os, sys

sys.path.insert(0, os.path.dirname(__file__))

from helper import (extract, transform_day_of_week,
                    transform_total_revenue, transform_flag_fraud,
                    create_data_mart)

def task_extract(**context):
    import pandas as pd
    # Use pandas for simple CSV read — no Spark needed here
    df = pd.read_csv("/opt/airflow/dags/transactions.csv")
    print(f"✅ Extracted {len(df)} rows")
    context["ti"].xcom_push(key="raw", value=df.to_json())

    
def task_transform1(**context):
    import pandas as pd
    from pyspark.sql import SparkSession
    raw = context["ti"].xcom_pull(key="raw", task_ids="extract")
    spark = SparkSession.builder.appName("FraudDAG").getOrCreate()
    df = spark.createDataFrame(pd.read_json(raw))
    df = transform_day_of_week(df)
    context["ti"].xcom_push(key="t1", value=df.toPandas().to_json())

def task_transform2(**context):
    import pandas as pd
    from pyspark.sql import SparkSession
    t1 = context["ti"].xcom_pull(key="t1", task_ids="transform_1")
    spark = SparkSession.builder.appName("FraudDAG").getOrCreate()
    df = spark.createDataFrame(pd.read_json(t1))
    df = transform_total_revenue(df)
    context["ti"].xcom_push(key="t2", value=df.toPandas().to_json())

def task_transform3(**context):
    import pandas as pd
    from pyspark.sql import SparkSession
    t2 = context["ti"].xcom_pull(key="t2", task_ids="transform_2")
    spark = SparkSession.builder.appName("FraudDAG").getOrCreate()
    df = spark.createDataFrame(pd.read_json(t2))
    df = transform_flag_fraud(df)
    context["ti"].xcom_push(key="t3", value=df.toPandas().to_json())

def task_create_mart(**context):
    import pandas as pd
    from pyspark.sql import SparkSession
    t3 = context["ti"].xcom_pull(key="t3", task_ids="transform_3")
    spark = SparkSession.builder.appName("FraudDAG").getOrCreate()
    df = spark.createDataFrame(pd.read_json(t3))
    mart = create_data_mart(df)
    mart.toPandas().to_csv("/opt/airflow/dags/fraud_mart.csv", index=False)
    print("✅ Fraud mart saved to fraud_mart.csv")

with DAG(
    dag_id="fraud_detection_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule=timedelta(days=1),
    catchup=False,
    default_args={"retries": 2, "retry_delay": timedelta(minutes=1)}
) as dag:

    extract_task = PythonOperator(task_id="extract", python_callable=task_extract)
    t1 = PythonOperator(task_id="transform_1", python_callable=task_transform1)
    t2 = PythonOperator(task_id="transform_2", python_callable=task_transform2)
    t3 = PythonOperator(task_id="transform_3", python_callable=task_transform3)
    mart = PythonOperator(task_id="create_mart", python_callable=task_create_mart)

    extract_task >> t1 >> t2 >> t3 >> mart
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

def get_spark():
    return SparkSession.builder \
        .appName("FraudDetection") \
        .getOrCreate()

def extract(filepath: str):
    spark = get_spark()
    df = spark.read.option("header", "true") \
               .option("inferSchema", "true") \
               .csv(filepath)
    print(f"✅ Extracted {df.count()} rows")
    df.show(5)
    return df

def transform_day_of_week(df):
    """Transform 1: Add day of week column"""
    df = df.withColumn("SaleDate", F.to_date("SaleDate", "yyyy-MM-dd"))
    df = df.withColumn("DayOfWeek", F.dayofweek("SaleDate"))
    df = df.withColumn("DayName", F.date_format("SaleDate", "EEEE"))
    print("✅ Transform 1 — day of week added")
    return df

def transform_total_revenue(df):
    """Transform 2: Compute total revenue per transaction"""
    df = df.withColumn(
        "TotalRevenue",
        F.round(
            F.col("Price") * F.col("Quantity") * (1 - F.col("Discount")),
            2
        )
    )
    print("✅ Transform 2 — total revenue computed")
    return df

def transform_flag_fraud(df):
    """Transform 3: Flag potentially fraudulent tablet transactions"""
    
    # Step 1: Filter to tablets only
    df = df.filter(F.col("Product") == "Tablet")
    
    # Step 2: Flag high revenue transactions (potential fraud signal)
    df = df.withColumn(
        "HighValue",
        F.when(F.col("TotalRevenue") > 3000, True).otherwise(False)
    )
    
    # Step 3: Flag weekend transactions (odd timing signal)
    df = df.withColumn(
        "IsWeekend",
        F.col("DayOfWeek").isin([1, 7])  # 1=Sunday, 7=Saturday in Spark
    )
    
    # Step 4: Mark as potential fraud if BOTH signals are true
    df = df.withColumn(
        "PotentialFraud",
        F.col("HighValue") & F.col("IsWeekend")
    )
    
    fraud_count = df.filter(F.col("PotentialFraud") == True).count()
    print(f"✅ Transform 3 — {df.count()} tablet rows, {fraud_count} flagged as fraud")
    return df

def create_data_mart(df):
    """Keep only fraud-flagged rows for the data science team"""
    mart = df.filter(F.col("PotentialFraud") == True)
    mart = mart.select(
        "SaleID", "CustomerName", "City",
        "SaleDate", "DayName", "TotalRevenue",
        "HighValue", "IsWeekend", "PotentialFraud"
    )
    print(f"✅ Data mart created — {mart.count()} rows")
    mart.show()
    return mart
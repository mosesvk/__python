from helper import (extract, transform_day_of_week, 
                    transform_total_revenue, transform_flag_fraud,
                    create_data_mart)

df = extract("transactions.csv")
df = transform_day_of_week(df)
df = transform_total_revenue(df)
df = transform_flag_fraud(df)
mart = create_data_mart(df)
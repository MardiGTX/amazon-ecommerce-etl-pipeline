from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp

spark = SparkSession.builder.getOrCreate()

# read dataset from saved data extract result in container 
df = spark.read.csv("/opt/airflow/data/extract_result", header=True, inferSchema=True)

# change column purchase_date to datetime
df = df.withColumn("purchase_date",to_timestamp(col("purchase_date")))

# save the transformed dataset into container
df.write.mode("overwrite").csv("/opt/airflow/data/transform_result", header=True)

print("transform success")
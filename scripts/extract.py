import kagglehub
import os
from pyspark.sql import SparkSession

#define location dataset to be extract to
DATASET_ROOT_DIR = "/opt/airflow/data/"

# download dataset from kaggle 
path = kagglehub.dataset_download("sharmajicoder/amazon-e-commerce")


os.makedirs(DATASET_ROOT_DIR, exist_ok=True)

# copy file dataset into folder opt airflow data
os.system(f"cp -r {path}/* {DATASET_ROOT_DIR}")

# read dataset with spark inside dataset_root_dir
spark = SparkSession.builder.getOrCreate()
df = spark.read.csv("/opt/airflow/data/amazon_ecommerce_1M.csv", header=True, inferSchema=True)

# save the dataset into dataset_root_dir
df.write.mode("overwrite").csv("/opt/airflow/data/extract_result",header=True)

print("extract success")
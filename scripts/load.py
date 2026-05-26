from pymongo import MongoClient
from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("Load_to_Mongo").getOrCreate()

#Read Dataset from transform result inside container
df = spark.read.csv("/opt/airflow/data/transform_result", header=True, inferSchema=True)
# Limit Dataset show 1000 row
df = df.limit(1000)

# convert Spark row to json
document_list = [row.asDict() for row in df.collect()]

# connection to mongodb
client = MongoClient("mongodb_URL_TOKEN")

# determines where row data will be inserted into the database and which collections.
db = client["amazon"]
collection = db["ecommerce"]

# insert row into Mongodb
collection.insert_many(document_list)

print("load succes")





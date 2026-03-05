import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, sum as spark_sum

# 1. Initialize Glue Context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

# --- USER CONFIGURATION ---

database_name = "sales_project_db"
table_name = "raw_data" # Check your Glue Table name if it's different!
# Output path: Where the cleaned data will go. CHANGE THIS BUCKET NAME!
target_path = "s3://de-project-sales-datalake-alex/processed_data/" 
# --------------------------

print("Job Started...")

# 2. Read Data from Glue Catalog (DynamicFrame)
# This connects to the metadata we created with the Crawler
datasource0 = glueContext.create_dynamic_frame.from_catalog(
    database=database_name, 
    table_name=table_name
)

# Convert to standard Spark DataFrame for easier manipulation
df = datasource0.toDF()

# 3. Data Cleaning & Transformation
# A. Cast columns to correct types (Crawler often sees prices as strings)
df_clean = df.withColumn("price", col("price").cast("double")) \
             .withColumn("quantity", col("quantity").cast("integer"))

# B. Remove rows where 'region' is null (The dirty data we generated)
df_clean = df_clean.filter(col("region").isNotNull())

# C. Business Logic: Calculate Total Revenue (Price * Quantity)
df_clean = df_clean.withColumn("total_revenue", col("price") * col("quantity"))

# D. Aggregation: Sum revenue by Product
df_aggregated = df_clean.groupBy("product") \
    .agg(spark_sum("total_revenue").alias("revenue"))

df_aggregated.show() # This logs the result to the console for debugging

# 4. Write Data back to S3 in Parquet format
df_aggregated.write.mode("overwrite").parquet(target_path)

print(f"Job Finished. Data written to {target_path}")
job.commit()
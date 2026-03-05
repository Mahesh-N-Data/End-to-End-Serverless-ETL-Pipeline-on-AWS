# End-to-End-Serverless-ETL-Pipeline-on-AWS
This project demonstrates a full-lifecycle Data Engineering pipeline built on AWS. It simulates a real-world scenario where raw sales data is ingested, processed, and transformed using serverless technologies, and finally loaded into a Data Warehouse for analytics.
The goal was to build a scalable, cost-effective architecture without managing underlying servers (Serverless), moving data from a **Raw Data Lake** to a **Refined Data Warehouse**.

## Architecture
Flow:Local Python Script(DataGenerator.py) -> AWS S3 (Raw) -> AWS Glue (PySpark) -> AWS S3 (Processed) -> AWS Redshift
<img width="1024" height="1536" alt="Data pipeline archit" src="https://github.com/user-attachments/assets/5da5f6bd-7e37-43eb-8080-e2c0d441d9ea" />


###Technologies Used
Language: Python, SQL, PySpark
Storage: AWS S3 (Simple Storage Service)
ETL Engine: AWS Glue (Serverless Spark)
Data Warehouse: AWS Redshift
IAM: Role-based security and permission management

---

## 📂 Project Structure

├── scripts/
│   ├── data_generator.py      # Python script to generate synthetic sales data
│   ├── glue_etl_job.py        # PySpark script for AWS Glue transformation
│   └── redshift_loader.sql    # SQL commands for table creation and data loading
├── data/
│   └── sales_data_sample.csv  # Sample of the raw data generated
└── README.md

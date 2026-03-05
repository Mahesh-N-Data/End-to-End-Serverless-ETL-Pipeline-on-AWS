COPY public.product_revenue
FROM 's3://de-project-sales-datalake-alex/processed_data/' 
IAM_ROLE 'arn:aws:iam::123456789012:role/AWSGlueServiceRole-Project1'


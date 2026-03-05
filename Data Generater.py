import pandas as pd
import random
from datetime import datetime, timedelta

# 1. Setup Data Generators
def generate_data(num_records):
    data = []
    products = ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Headphones']
    regions = ['North', 'South', 'East', 'West']
    
    for _ in range(num_records):
        date = datetime.now() - timedelta(days=random.randint(0, 365))
        product = random.choice(products)
        region = random.choice(regions)
        quantity = random.randint(1, 5)
        price = round(random.uniform(20.0, 500.0), 2)
        
        # We will introduce some "dirty data" on purpose for Glue to clean later!
        # 5% chance of a null region
        if random.random() < 0.05:
            region = None
            
        data.append([date.strftime('%Y-%m-%d'), product, region, quantity, price])
        
    return data

# 2. Generate 1000 records
records = generate_data(1000)

# 3. Create DataFrame and Save to CSV
df = pd.DataFrame(records, columns=['order_date', 'product', 'region', 'quantity', 'price'])
file_name = 'sales_data_raw.csv'
df.to_csv(file_name, index=False)

print(f"Successfully created {file_name} with {len(df)} rows.")
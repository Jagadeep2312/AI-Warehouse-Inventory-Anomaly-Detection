import pandas as pd
import random
from datetime import datetime, timedelta

# Product information
products = [
    ("Laptop", "Electronics"),
    ("Mouse", "Accessories"),
    ("Keyboard", "Accessories"),
    ("Monitor", "Electronics"),
    ("Printer", "Electronics"),
    ("Scanner", "Electronics"),
    ("Router", "Networking"),
    ("Speaker", "Electronics"),
    ("Webcam", "Accessories"),
    ("Projector", "Electronics"),
    ("Hard Disk", "Storage"),
    ("SSD", "Storage"),
    ("RAM", "Components"),
    ("CPU", "Components"),
    ("GPU", "Components")
]

locations = [
    "A1", "A2", "A3",
    "B1", "B2", "B3",
    "C1", "C2", "C3"
]

records = []

for i in range(1, 10001):

    product, category = random.choice(products)

    stock_in = random.randint(50, 500)

    stock_out = random.randint(0, stock_in)

    expected_stock = stock_in - stock_out

    current_stock = expected_stock + random.randint(-20, 20)

    supplier = random.choice([
        "Dell",
        "HP",
        "Lenovo",
        "Samsung",
        "Logitech"
    ])

    warehouse = random.choice(locations)

    date = datetime.now() - timedelta(
        days=random.randint(0, 365)
    )

    records.append({

        "Product_ID": i,

        "Product_Name": product,

        "Category": category,

        "Supplier": supplier,

        "Warehouse_Location": warehouse,

        "Stock_In": stock_in,

        "Stock_Out": stock_out,

        "Expected_Stock": expected_stock,

        "Current_Stock": current_stock,

        "Date": date.strftime("%Y-%m-%d")

    })

df = pd.DataFrame(records)

df.to_csv(
    "data/inventory.csv",
    index=False
)

print("Dataset Created Successfully")
print("Rows:", len(df))
print("Columns:", len(df.columns))
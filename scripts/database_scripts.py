import sqlite3
import pandas as pd

# Load AI prediction dataset
df = pd.read_csv(
    "data/inventory_predictions.csv"
)

# Create Database
connection = sqlite3.connect(
    "database/warehouse.db"
)

cursor = connection.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Inventory (

Product_ID INTEGER,

Product_Name TEXT,

Category TEXT,

Supplier TEXT,

Warehouse_Location TEXT,

Stock_In INTEGER,

Stock_Out INTEGER,

Expected_Stock INTEGER,

Current_Stock INTEGER,

Difference INTEGER,

Movement_Rate REAL,

Inventory_Status TEXT,

Movement_Status TEXT,

AI_Prediction TEXT,

Date TEXT

)
""")

# Insert Data
df.to_sql(
    "Inventory",
    connection,
    if_exists="replace",
    index=False
)

connection.commit()

cursor.execute(
"SELECT COUNT(*) FROM Inventory"
)

print(
"Total Records:",
cursor.fetchone()[0]
)

connection.close()

print("\nDatabase Created Successfully")
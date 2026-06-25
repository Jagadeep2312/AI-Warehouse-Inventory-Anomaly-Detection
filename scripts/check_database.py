import sqlite3
import pandas as pd

connection = sqlite3.connect(
    "database/warehouse.db"
)

df = pd.read_sql(
    "SELECT * FROM Inventory LIMIT 10",
    connection
)

print(df)

connection.close()
import sqlite3
import pickle
import random
import time
from datetime import datetime

# ----------------------------
# DATABASE CONNECTION
# ----------------------------
conn = sqlite3.connect("database/warehouse.db")
cursor = conn.cursor()

# ----------------------------
# LOAD TRAINED MODEL
# ----------------------------
with open("models/anomaly_model.pkl", "rb") as file:
    model = pickle.load(file)

# ----------------------------
# PRODUCTS
# ----------------------------
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
    ("SSD", "Storage"),
    ("Hard Disk", "Storage")
]

suppliers = [
    "Dell",
    "HP",
    "Lenovo",
    "Samsung",
    "Logitech"
]

locations = [
    "A1","A2","A3",
    "B1","B2","B3",
    "C1","C2","C3"
]

print("="*60)
print("LIVE INVENTORY SIMULATOR STARTED")
print("="*60)

while True:

    product, category = random.choice(products)

    supplier = random.choice(suppliers)

    location = random.choice(locations)

    stock_in = random.randint(100,500)

    stock_out = random.randint(0,stock_in)

    expected_stock = stock_in - stock_out

    current_stock = expected_stock + random.randint(-20,20)

    difference = current_stock - expected_stock

    movement_rate = round(stock_out/stock_in,2)

    # ----------------------------
    # RULE BASED STATUS
    # ----------------------------

    if difference < -15:
        inventory_status = "Missing Inventory"

    elif difference > 15:
        inventory_status = "Overstock"

    else:
        inventory_status = "Normal"

    if movement_rate >= 0.80:
        movement_status = "Fast Moving"

    elif movement_rate <= 0.20:
        movement_status = "Slow Moving"

    else:
        movement_status = "Normal"

    # ----------------------------
    # AI PREDICTION
    # ----------------------------

    features = [[
        stock_in,
        stock_out,
        expected_stock,
        current_stock,
        difference,
        movement_rate
    ]]

    prediction = model.predict(features)[0]

    if prediction == -1:
        ai_prediction = "Anomaly"
    else:
        ai_prediction = "Normal"

    # ----------------------------
    # INSERT INTO DATABASE
    # ----------------------------

    cursor.execute("""
        INSERT INTO Inventory
        (
        Product_ID,
        Product_Name,
        Category,
        Supplier,
        Warehouse_Location,
        Stock_In,
        Stock_Out,
        Expected_Stock,
        Current_Stock,
        Difference,
        Movement_Rate,
        Inventory_Status,
        Movement_Status,
        AI_Prediction,
        Date
        )
        VALUES
        (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """,
    (
        random.randint(10001,99999),
        product,
        category,
        supplier,
        location,
        stock_in,
        stock_out,
        expected_stock,
        current_stock,
        difference,
        movement_rate,
        inventory_status,
        movement_status,
        ai_prediction,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()

    # ----------------------------
    # LIVE OUTPUT
    # ----------------------------

    print("\n" + "="*60)

    print("Product            :", product)

    print("Category           :", category)

    print("Supplier           :", supplier)

    print("Warehouse          :", location)

    print("Stock In           :", stock_in)

    print("Stock Out          :", stock_out)

    print("Expected Stock     :", expected_stock)

    print("Current Stock      :", current_stock)

    print("Difference         :", difference)

    print("Movement Rate      :", movement_rate)

    print("Inventory Status   :", inventory_status)

    print("Movement Status    :", movement_status)

    print("AI Prediction      :", ai_prediction)

    print("Time               :", datetime.now())

    print("="*60)

    time.sleep(5)
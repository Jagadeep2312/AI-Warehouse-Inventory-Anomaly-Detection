import pandas as pd

df = pd.read_csv("data/inventory.csv")

print(df.head())

print(df.shape)

print(df.columns)

print(df.isnull().sum())

df.drop_duplicates(inplace=True)

df["Difference"] = df["Current_Stock"] - df["Expected_Stock"]

def detect_status(diff):

    if diff < -15:
        return "Missing Inventory"

    elif diff > 15:
        return "Overstock"

    else:
        return "Normal"

df["Inventory_Status"] = df["Difference"].apply(detect_status)

df["Movement_Rate"] = df["Stock_Out"] / df["Stock_In"]

def movement(speed):

    if speed >= 0.80:
        return "Fast Moving"

    elif speed <= 0.20:
        return "Slow Moving"

    else:
        return "Normal"

df["Movement_Status"] = df["Movement_Rate"].apply(movement)

print(df["Inventory_Status"].value_counts())

print(df["Movement_Status"].value_counts())

df.to_csv(

    "data/inventory_clean.csv",

    index=False

)

print("\nDataset Saved Successfully")
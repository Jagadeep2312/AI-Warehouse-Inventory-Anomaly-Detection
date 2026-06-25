import pandas as pd
import pickle
from sklearn.ensemble import IsolationForest

# Load cleaned dataset
df = pd.read_csv("data/inventory_clean.csv")

# Select numerical features
features = df[
    [
        "Stock_In",
        "Stock_Out",
        "Expected_Stock",
        "Current_Stock",
        "Difference",
        "Movement_Rate"
    ]
]

# Create AI Model
model = IsolationForest(
    contamination=0.10,
    random_state=42
)

# Train Model
model.fit(features)

# Predict
prediction = model.predict(features)

# Convert predictions
df["AI_Prediction"] = prediction

df["AI_Prediction"] = df["AI_Prediction"].replace({
    1: "Normal",
    -1: "Anomaly"
})

# Save model
with open("models/anomaly_model.pkl", "wb") as file:
    pickle.dump(model, file)

# Save prediction dataset
df.to_csv(
    "data/inventory_predictions.csv",
    index=False
)

print("\nAI Prediction Summary")
print(df["AI_Prediction"].value_counts())

print("\nModel Saved Successfully")
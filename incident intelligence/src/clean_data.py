import pandas as pd
import numpy as np

df = pd.read_csv("data/incidents.csv")

<<<<<<< HEAD
# Deduplication & Clean categorical strings
=======
# 1. Deduplication & Clean categorical strings
>>>>>>> 16aebcb19ea0102e36f3c98eba7448ac63a6948f
df = df.drop_duplicates()
df["location"] = df["location"].str.strip().str.title()
df["source"] = df["source"].fillna("UNKNOWN").str.strip().str.upper()
df["asset"] = df["asset"].fillna("UNKNOWN").str.strip().str.title()

<<<<<<< HEAD
# Out-of-bounds confidence handling
invalid_confidence = (df["confidence"] < 0) | (df["confidence"] > 1)
df.loc[invalid_confidence, "confidence"] = np.nan

# Datetime conversions (CRITICAL FIX: converted BEFORE deriving features)
=======
# 2. Out-of-bounds confidence handling
invalid_confidence = (df["confidence"] < 0) | (df["confidence"] > 1)
df.loc[invalid_confidence, "confidence"] = np.nan

# 3. Datetime conversions (CRITICAL FIX: converted BEFORE deriving features)
>>>>>>> 16aebcb19ea0102e36f3c98eba7448ac63a6948f
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["date"] = df["timestamp"].dt.date
df["hour"] = df["timestamp"].dt.hour
df["day"] = df["timestamp"].dt.day_name()
df["month"] = df["timestamp"].dt.month_name()

# Export clean file
df.to_csv("data/incidents_clean.csv", index=False)
print("Cleaned dataset saved successfully.")
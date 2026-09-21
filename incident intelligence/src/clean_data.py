import pandas as pd
import numpy as np

df = pd.read_csv("data/incidents.csv")

# Deduplication & Clean categorical strings
df = df.drop_duplicates()
df["location"] = df["location"].str.strip().str.title()
df["source"] = df["source"].fillna("UNKNOWN").str.strip().str.upper()
df["asset"] = df["asset"].fillna("UNKNOWN").str.strip().str.title()

# Out-of-bounds confidence handling
invalid_confidence = (df["confidence"] < 0) | (df["confidence"] > 1)
df.loc[invalid_confidence, "confidence"] = np.nan

# Datetime conversions (CRITICAL FIX: converted BEFORE deriving features)
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["date"] = df["timestamp"].dt.date
df["hour"] = df["timestamp"].dt.hour
df["day"] = df["timestamp"].dt.day_name()
df["month"] = df["timestamp"].dt.month_name()

# Export clean file
df.to_csv("data/incidents_clean.csv", index=False)
print("Cleaned dataset saved successfully.")
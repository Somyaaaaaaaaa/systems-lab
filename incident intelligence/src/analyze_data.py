import pandas as pd

df = pd.read_csv("data/incidents_clean.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

print("\n--- INCIDENT TYPES ---")
print(df["incident_type"].value_counts())

print("\n--- INCIDENTS BY SEVERITY ---")
print(df["severity"].value_counts())

print("\n--- CASUALTIES BY INCIDENT TYPE ---")
print(df.groupby("incident_type")["casualties"].sum().sort_values(ascending=False))

print("\n--- INCIDENTS BY LOCATION ---")
print(df["location"].value_counts())

print("\n--- INCIDENT TYPE BY LOCATION ---")
print(pd.crosstab(df["location"], df["incident_type"]))

print("\n--- INCIDENTS BY HOUR ---")
print(df["hour"].value_counts().sort_index())

print("\n--- INCIDENTS BY DAY ---")
print(df["day"].value_counts())

print("\n--- INCIDENTS BY MONTH ---")
print(df["month"].value_counts())

print("\n--- DAILY INCIDENTS ---")
daily_incidents = df.groupby("date").size().reset_index(name="incident_count")
print(daily_incidents.head())

print("\n--- WEEKLY INCIDENTS ---")
df["week"] = df["timestamp"].dt.to_period("W")
weekly_incidents = df.groupby("week").size().reset_index(name="incident_count")
print(weekly_incidents)

print("\n--- CONFIDENCE BY SOURCE ---")
print(df.groupby("source")["confidence"].agg(["count", "mean", "min", "max"]).sort_values("mean", ascending=False))
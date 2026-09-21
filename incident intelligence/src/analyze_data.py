import pandas as pd

df= pd.read_csv("data/incidents_clean.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

print("\nINCIDENT TYPES:")
<<<<<<< HEAD
print(df["incident_type"].value_counts())

print("\nINCIDENTS BY SEVERITY:")
print(df["severity"].value_counts())

print("\nCASUALTIES BY INCIDENT TYPE:")
print(df.groupby("incident_type")["casualties"].sum().sort_values(ascending=False))

print("\nINCIDENTS BY LOCATION:")
print(df["location"].value_counts())

print("\nINCIDENT TYPE BY LOCATION:")
print(pd.crosstab(df["location"], df["incident_type"]))

print("\nINCIDENTS BY HOUR:")
print(df["hour"].value_counts().sort_index())

print("\nINCIDENTS BY DAY:")
print(df["day"].value_counts())

print("\nINCIDENTS BY MONTH:")
print(df["month"].value_counts())

daily_incidents = (df.groupby("date").size().reset_index(name="incident_count"))
=======
print(
    df["incident_type"]
    .value_counts()
)

print("\nINCIDENTS BY SEVERITY:")
print(
    df["severity"]
    .value_counts()
)

print("\nCASUALTIES BY INCIDENT TYPE:")
print(
    df.groupby("incident_type")["casualties"]
    .sum()
    .sort_values(ascending=False)
)

print("\nINCIDENTS BY LOCATION:")
print(
    df["location"]
    .value_counts()
)

print("\nINCIDENT TYPE BY LOCATION:")
print(
    pd.crosstab(
        df["location"],
        df["incident_type"]
    )
)

print("\nINCIDENTS BY HOUR:")
print(
    df["hour"]
    .value_counts()
    .sort_index()
)

print("\nINCIDENTS BY DAY:")
print(
    df["day"]
    .value_counts()
)

print("\nINCIDENTS BY MONTH:")
print(
    df["month"]
    .value_counts()
)

daily_incidents = (
    df.groupby("date")
      .size()
      .reset_index(name="incident_count")
)
>>>>>>> 16aebcb19ea0102e36f3c98eba7448ac63a6948f

print("\nDAILY INCIDENTS:")
print(daily_incidents.head())

df["week"] = df["timestamp"].dt.to_period("W")

<<<<<<< HEAD
weekly_incidents = (df.groupby("week").size().reset_index(name="incident_count"))
=======
weekly_incidents = (
    df.groupby("week")
      .size()
      .reset_index(name="incident_count")
)
>>>>>>> 16aebcb19ea0102e36f3c98eba7448ac63a6948f

print("\nWEEKLY INCIDENTS:")
print(weekly_incidents)

print("\nCONFIDENCE BY SOURCE:")

<<<<<<< HEAD
print(df.groupby("source")["confidence"].agg(["count", "mean", "min", "max"]).sort_values("mean", ascending=False))
=======
print(
    df.groupby("source")["confidence"]
      .agg(["count", "mean", "min", "max"])
      .sort_values("mean", ascending=False)
)
>>>>>>> 16aebcb19ea0102e36f3c98eba7448ac63a6948f

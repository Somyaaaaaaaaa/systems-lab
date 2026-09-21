import pandas as pd
import plotly.express as px

df = pd.read_csv("data/incidents_clean.csv")

df["timestamp"] = pd.to_datetime(df["timestamp"])

<<<<<<< HEAD
incident_counts = (df["incident_type"].value_counts().reset_index())
=======
incident_counts = (
    df["incident_type"]
    .value_counts()
    .reset_index()
)
>>>>>>> 16aebcb19ea0102e36f3c98eba7448ac63a6948f

incident_counts.columns = ["incident_type", "count"]

fig = px.bar(
    incident_counts,
    x="incident_type",
    y="count",
    title="Incidents by Type"
)

fig.show()

location_counts = (
    df["location"]
    .value_counts()
    .reset_index()
)

location_counts.columns = ["location", "count"]

fig = px.bar(
    location_counts,
    x="location",
    y="count",
    title="Incidents by Location"
)

fig.show()

daily = (
<<<<<<< HEAD
    df.groupby(df["timestamp"].dt.date).size().reset_index(name="incident_count"))

=======
    df.groupby(df["timestamp"].dt.date)
      .size()
      .reset_index(name="incident_count")
)

# FIXED: Column name updated to "timestamp" so px.line finds x="timestamp"
>>>>>>> 16aebcb19ea0102e36f3c98eba7448ac63a6948f
daily.columns = ["timestamp", "incident_count"]

fig = px.line(
    daily,
    x="timestamp",
    y="incident_count",
    title="Incidents Over Time"
)

fig.show()

<<<<<<< HEAD
hourly = (df["timestamp"].dt.hour.value_counts().sort_index().reset_index())
=======
hourly = (
    df["timestamp"]
    .dt.hour
    .value_counts()
    .sort_index()
    .reset_index()
)
>>>>>>> 16aebcb19ea0102e36f3c98eba7448ac63a6948f

hourly.columns = ["hour", "count"]

fig = px.bar(
    hourly,
    x="hour",
    y="count",
    title="Incidents by Hour"
)

fig.show()
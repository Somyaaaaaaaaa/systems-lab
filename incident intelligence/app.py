import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/incidents_clean.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

st.sidebar.header("Filters")

selected_locations = st.sidebar.multiselect(
    "Location",
    options=sorted(df["location"].unique()),
    default=sorted(df["location"].unique())
)

selected_severity = st.sidebar.multiselect(
    "Severity",
    options=sorted(df["severity"].unique()),
    default=sorted(df["severity"].unique())
)

selected_types = st.sidebar.multiselect(
    "Incident Type",
    options=sorted(df["incident_type"].unique()),
    default=sorted(df["incident_type"].unique())
)

filtered_df = df[
    df["location"].isin(selected_locations)
    & df["severity"].isin(selected_severity)
    & df["incident_type"].isin(selected_types)
]

total_incidents = len(filtered_df)
total_casualties = filtered_df["casualties"].sum()
locations = filtered_df["location"].nunique()
avg_confidence = filtered_df["confidence"].mean()

st.set_page_config(
    page_title="Incident Intelligence Dashboard",
    layout="wide"
)

st.title("Incident Intelligence Dashboard")

st.write(
    "Synthetic incident monitoring and analysis dashboard."
)

total_incidents = len(df)

total_casualties = filtered_df["casualties"].sum()
locations = filtered_df["location"].nunique()
avg_confidence = filtered_df["confidence"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Incidents", total_incidents)
col2.metric("Total Casualties", total_casualties)
col3.metric("Locations", locations)
col4.metric("Avg Confidence", f"{avg_confidence:.2f}")
incident_counts = (
    filtered_df["incident_type"]
    .value_counts()
    .reset_index()
)

incident_counts.columns = ["incident_type", "count"]

fig = px.bar(
    incident_counts,
    x="incident_type",
    y="count",
    title="Incidents by Type"
)

st.plotly_chart(fig, use_container_width=True)

location_counts = (
    filtered_df["location"]
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

st.plotly_chart(fig, use_container_width=True)

daily = (
    filtered_df.groupby(filtered_df["timestamp"].dt.date)
      .size()
      .reset_index(name="incident_count")
)

daily.columns = ["date", "incident_count"]

fig = px.line(
    daily,
    x="date",
    y="incident_count",
    title="Incident Activity Over Time"
)

st.plotly_chart(fig, use_container_width=True)

source_confidence = (
    filtered_df.groupby("source")["confidence"]
      .mean()
      .reset_index()
)

fig = px.bar(
    source_confidence,
    x="source",
    y="confidence",
    title="Average Confidence by Source"
)

fig.update_yaxes(range=[0, 1])

st.plotly_chart(fig, use_container_width=True)

location_type = pd.crosstab(
    filtered_df["location"],
    filtered_df["incident_type"]
)

fig = px.imshow(
    location_type,
    title="Incident Type by Location",
    labels={
        "x": "Incident Type",
        "y": "Location",
        "color": "Incident Count"
    },
    aspect="auto"
)

st.plotly_chart(fig, use_container_width=True)

hourly = (
    filtered_df["timestamp"]
    .dt.hour
    .value_counts()
    .sort_index()
    .reset_index()
)

hourly.columns = ["hour", "incident_count"]

fig = px.line(
    hourly,
    x="hour",
    y="incident_count",
    markers=True,
    title="Incident Activity by Hour"
)

st.plotly_chart(fig, use_container_width=True)

st.header("Key Findings")

if len(filtered_df) > 0:

    top_location = (
        filtered_df["location"]
        .value_counts()
        .idxmax()
    )

    top_incident = (
        filtered_df["incident_type"]
        .value_counts()
        .idxmax()
    )

    top_severity = (
        filtered_df["severity"]
        .value_counts()
        .idxmax()
    )

    peak_hour = (
        filtered_df["timestamp"]
        .dt.hour
        .value_counts()
        .idxmax()
    )

    st.write(
        f"- Most incidents occurred in **{top_location}**."
    )

    st.write(
        f"- **{top_incident}** was the most frequently observed incident type."
    )

    st.write(
        f"- **{top_severity}** was the most common severity level."
    )

    st.write(
        f"- Peak incident activity occurred around **{peak_hour:02d}:00**."
    )

else:
    st.warning("No incidents match the selected filters.")

top_location_count = (
    filtered_df["location"]
    .value_counts()
    .iloc[0]
)

location_percentage = (
    top_location_count / len(filtered_df) * 100
)

st.write(
    f"- **{top_location}** accounts for "
    f"**{location_percentage:.1f}%** of filtered incidents."
)
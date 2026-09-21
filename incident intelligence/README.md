# Incident Intelligence Dashboard

A synthetic incident intelligence dashboard built with Python, Pandas, Plotly, and Streamlit.

The project simulates an incident reporting pipeline and demonstrates how raw, inconsistent incident data can be cleaned, analyzed, visualized, and transformed into an interactive intelligence dashboard.

> **Note:** All data in this project is synthetic and created for educational and demonstration purposes.

## Objective

The dashboard is designed to answer four core intelligence questions:

* **What** happened?
* **Where** did it happen?
* **When** did it happen?
* **How frequently** did it occur?

It also examines incident severity, casualties, reporting sources, and source confidence.

## Features

* Synthetic incident data generation
* Missing-value detection and handling
* Duplicate detection and removal
* Categorical value normalization
* Invalid confidence-value detection
* Timestamp parsing and temporal feature engineering
* Incident frequency analysis
* Location-based analysis
* Severity analysis
* Casualty analysis
* Source-confidence analysis
* Interactive Plotly visualizations
* Interactive Streamlit filters
* Location × incident-type heatmap
* Automated key findings

## Dataset

The synthetic dataset contains incident records with the following fields:

| Field           | Description                      |
| --------------- | -------------------------------- |
| `incident_id`   | Unique incident identifier       |
| `incident_type` | Type of incident                 |
| `location`      | Reported location                |
| `timestamp`     | Date and time of incident        |
| `severity`      | Incident severity                |
| `asset`         | Associated asset                 |
| `casualties`    | Number of casualties             |
| `source`        | Reporting or intelligence source |
| `confidence`    | Confidence score between 0 and 1 |

The raw dataset intentionally contains:

* Duplicate records
* Missing values
* Inconsistent capitalization
* Invalid confidence values
* Unknown sources/assets

This allows the project to demonstrate a realistic data-cleaning workflow rather than beginning with suspiciously perfect data, as tutorials tend to do.

## Project Structure

```text
D1/
│
├── data/
│   ├── incidents.csv
│   └── incidents_clean.csv
│
├── src/
│   ├── generate_data.py
│   ├── clean_data.py
│   ├── analyze_data.py
│   └── visualize.py
│
├── app.py
├── README.md
└── requirements.txt
```

## Pipeline

```text
Synthetic Data
      ↓
Data Inspection
      ↓
Data Cleaning
      ↓
Feature Engineering
      ↓
Exploratory Analysis
      ↓
Visualization
      ↓
Interactive Dashboard
      ↓
Automated Findings
```

## Analysis

The analysis examines:

### Incident Frequency

Identifies the most frequently observed incident types and locations.

### Temporal Patterns

Examines incident activity by:

* Hour
* Day of week
* Month
* Day
* Week

### Severity

Examines the distribution of Low, Medium, High, and Critical incidents.

### Casualties

Calculates total casualties and casualty totals by incident type.

### Source Confidence

Compares confidence distributions across reporting sources.

The confidence values are generated synthetically using source-specific ranges. Therefore, differences between source categories reflect the assumptions used to generate the dataset and should not be interpreted as real-world evidence about intelligence-source reliability.

## Dashboard

The Streamlit dashboard provides:

* Total incident count
* Total casualties
* Number of locations
* Average confidence
* Incident-type distribution
* Location distribution
* Incident activity over time
* Hourly activity
* Source-confidence analysis
* Location × incident-type heatmap
* Interactive filtering by location, severity, and incident type
* Automatically generated key findings

## Technologies

* Python
* Pandas
* NumPy
* Plotly
* Streamlit

## Running the Project

Create and activate a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install pandas numpy plotly streamlit
```

Generate the dataset:

```bash
python src/generate_data.py
```

Clean the dataset:

```bash
python src/clean_data.py
```

Run the analysis:

```bash
python src/analyze_data.py
```

Run the visualization script:

```bash
python src/visualize.py
```

Launch the dashboard:

```bash
streamlit run app.py
```

## Key Learning Outcomes

This project demonstrates a complete small-scale data intelligence workflow:

1. Generating structured synthetic data
2. Introducing realistic data-quality problems
3. Detecting and correcting those problems
4. Engineering temporal features
5. Performing exploratory analysis
6. Identifying patterns without confusing correlation with causation
7. Building interactive visualizations
8. Creating an analytical dashboard
9. Converting numerical analysis into concise findings

## Limitations

This project uses synthetic data and therefore does not represent real-world incident patterns.

The dataset is intentionally generated with predefined distributions and relationships. Findings are therefore demonstrations of analytical techniques rather than real intelligence assessments.

Future versions could incorporate:

* Real open-source datasets
* Geospatial mapping
* Anomaly detection
* Time-series forecasting
* Entity extraction
* Event clustering
* Network analysis
* OSINT source ingestion
* Automated incident summarization
* Alert generation

## License

This project is intended for educational and portfolio use.

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

random.seed(7)  
np.random.seed(7)

incident_types = ["Cyber Intrusion", "Drone Sighting", "Communication Outage", "Unauthorized Access", "Data Breach", "Physical Security Breach", "Vehicle Incident", "Infrastructure Failure", "Supply Disruption", "Fire", "Personnel Incident", "GPS Interference", "Suspicious Activity"]
locations = ["Kolkata", "Siliguri", "Darjeeling", "Durgapur", "Asansol", "Bardhaman", "Haldia", "Kharagpur", "Jalpaiguri", "Malda", "Raiganj", "Cooch Behar"]
severity_levels = ["Low", "Medium", "High", "Critical"]
assets= ["Server", "Vehicle", "Communication Tower", "Database", "Drone", "Warehouse", "Power Grid", "Personnel", "Satellite", "Network Infrastructure"]
sources = ["OSINT", "HUMINT", "SIGINT", "IMINT", "ELINT", "Sensor", "CCTV", "Social Media", "Internal Report", "Unknown"]

rows = []
start_date = datetime(2023, 1, 1)

for i in range (300):
    timestamp = start_date + timedelta(minutes=random.randint(0, 60*24*180))

    source = random.choice(sources)

    confidence_ranges= {
        "OSINT": (0.5, 0.9),
        "HUMINT": (0.6, 0.95),
        "SIGINT": (0.7, 0.99),
        "IMINT": (0.4, 0.85),
        "ELINT": (0.5, 0.9),
        "Sensor": (0.6, 0.95),
        "CCTV": (0.7, 0.99),
        "Social Media": (0.3, 0.8),
        "Internal Report": (0.8, 1.0),
        "Unknown": (0.2, 0.7)
    }

    low, high = confidence_ranges[source]

    row = {
        "incident_id": f"INC-{i+1:04d}",
        "incident_type": random.choice(incident_types),
        "location": random.choice(locations),
        "timestamp": timestamp,
        "severity": random.choice(severity_levels),
        "asset": random.choice(assets),
        "casualties": np.random.poisson(0.3),
        "source": source,
        "confidence": round(random.uniform(low, high), 2)
    }

    rows.append(row)

df = pd.DataFrame(rows)

# missing data simulation
for column in ["source", "confidence", "asset"]:
    indices = df.sample(frac=0.03).index
    df.loc[indices, column] = np.nan

# duplicate data simulation
duplicates = df.sample(n=8, random_state=42)
df = pd.concat(
    [df, duplicates],
    ignore_index=True
)

# inconsistent categorical values
location_indices = df.sample(frac=0.03, random_state=10).index
df.loc[location_indices, "location"] = "kolkata"
source_indices = df.sample(frac=0.02, random_state=20).index
df.loc[source_indices, "source"] = "cctv"

# invalid confidence values
bad_indices = df.sample(n=5, random_state=30).index
df.loc[bad_indices, "confidence"] = [
    1.2,
    -0.1,
    1.5,
    -0.3,
    2.0
]

df.to_csv("data/incidents.csv", index=False)
print(f"Generated {len(df)} records.")
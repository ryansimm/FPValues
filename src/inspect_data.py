import json
from pathlib import Path

import pandas as pd

latest = sorted(Path("data/raw").glob("bootstrap_*.json"))[-1]
data = json.loads(latest.read_text())
df = pd.DataFrame(data["elements"])

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)

wanted = ["web_name", "element_type", "minutes", "goals_scored",
          "assists", "saves", "defensive_contribution"]

present = [col for col in wanted if col in df.columns]
missing = [col for col in wanted if col not in df.columns]

print("File:", latest)
print("Shape:", df.shape)
print("All columns:", df.columns.tolist())
print("Missing expected columns:", missing)
print(df[present].head(10))

nulls = df.isnull().sum()
print("Columns with missing values:")
print(nulls[nulls > 0])
print("Players with more than 500 minutes played:", (df["minutes"] > 500).sum())

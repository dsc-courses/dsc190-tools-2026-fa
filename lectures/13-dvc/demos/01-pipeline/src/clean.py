"""Drop incomplete rows and strip whitespace from name."""
import sys
import pandas as pd
import time

print("Cleaning data...")
time.sleep(5)  # Simulate a long-running process

raw_path, out_path = sys.argv[1], sys.argv[2]

df = pd.read_csv(raw_path)
df = df.dropna(subset=["name", "score", "submitted_at"])
df["name"] = df["name"].str.strip()
df["submitted_at"] = pd.to_datetime(df["submitted_at"])

df.to_csv(out_path, index=False)

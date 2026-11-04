"""Compute derived features and one-hot encode course."""
import sys
import pandas as pd
import time

print("Extracting features...")
time.sleep(5)  # Simulate a long-running process

in_path, out_path = sys.argv[1], sys.argv[2]

df = pd.read_csv(in_path)
df["score_per_hour"] = df["score"] / df["study_hours"]
df["passed"] = (df["score"] >= 70).astype(int)

features = pd.get_dummies(df, columns=["course"], prefix="course")
features = features.drop(columns=["name", "submitted_at"])

features.to_csv(out_path, index=False)

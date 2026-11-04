"""Normalize capitalization of names and course titles."""
import sys
import pandas as pd
import time

print("Transforming data...")
time.sleep(5)  # Simulate a long-running process

in_path, out_path = sys.argv[1], sys.argv[2]

df = pd.read_csv(in_path)
df["name"] = df["name"].str.title()
df["course"] = df["course"].str.capitalize()

df.to_csv(out_path, index=False)

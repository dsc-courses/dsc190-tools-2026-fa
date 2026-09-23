import pandas as pd

df = pd.read_csv("data_FINAL_v2.csv")
df.columns = df.columns.str.strip().str.lower()
df = df.dropna()
df.to_csv("data_clean.csv", index=False)

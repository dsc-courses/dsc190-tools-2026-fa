import pandas as pd

df = pd.read_csv("data_clean.csv")
print(df.groupby("region")["score"].mean())

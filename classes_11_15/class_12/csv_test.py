import pandas as pd

CSV_PATH = "classes_11_15/example.csv"

df = pd.read_csv(CSV_PATH)

df_filter = df[df["state"] == "CA"]

print(df_filter)

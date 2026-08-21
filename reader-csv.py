import pandas as pd

df = pd.read_csv("./dados.csv", encoding="cp1252")

df["CPU"] = pd.to_numeric(df["CPU"], errors="coerce")

ram_agrupado = df.groupby("Empresa")["CPU"].mean().reset_index()
print(ram_agrupado["CPU"].iloc[1:])
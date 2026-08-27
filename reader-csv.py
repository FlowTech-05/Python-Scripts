import pandas as pd

df = pd.read_csv("dados.csv", encoding="cp1252")

df["CPU"] = pd.to_numeric(df["CPU"], errors="coerce")
df["RAM"] = pd.to_numeric(df["RAM"], errors="coerce")
df["Disco"] = pd.to_numeric(df["Disco"], errors="coerce")

medias = df.groupby("Empresa")[["CPU", "RAM", "Disco"]].mean()

print(medias)
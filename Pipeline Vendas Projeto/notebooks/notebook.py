import pandas as pd

df = pd.read_csv("data/processed/superstore_clean.csv", encoding="latin-1")
df.head()
df.info()

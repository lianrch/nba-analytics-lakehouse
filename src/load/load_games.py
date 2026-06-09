import pandas as pd
from src.database.connection import engine

print('Lendo arquivo...')

df = pd.read_csv("data/raw/nba_games.csv")

print(f"Registros encontrados: {len(df)}")

df.colums = df.columns.str.lower()

df.to_sql(
    "bronze_games",
    engine,
    if_exists="replace",
    index=False
)

print("Tabela bronze_games criada com sucesso!")
import pandas as pd 
from src.database.connection import engine

df = pd.read_csv("data/raw/nba_teams.csv")

df.to_sql(
    "bronze_teams",
    engine,
    if_exists="replace",
    index=False
)

print(f"{len(df)} registros carregados!")
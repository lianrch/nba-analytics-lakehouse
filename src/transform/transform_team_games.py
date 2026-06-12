import pandas as pd
from src.database.connection import engine

print("Lendo bronze_games...")

df = pd.read_sql("SELECT * FROM bronze_games", engine)

print(f"Registros encontrados: {len(df)}]")

df.columns = df.columns.str.lower()

silver_df = df[["game_id", "game_date", "season_id", "team_id", "team_abbreviation", "team_name", "wl", "pts", "reb", "ast", "fg_pct", "fg3_pct"]].copy()

silver_df.rename(
    columns={
        'wl': 'result',
        'pts': 'points',
        'reb': 'rebounds',
        'ast': 'assists'
    },
    inplace=True
)

silver_df["is_win"] = (
    silver_df["result"] == "W"
).astype(int)

print(silver_df.head())

silver_df.to_sql('silver_team_games', engine, if_exists='replace', index=False)

print('Tabela silver_team_games criada!')
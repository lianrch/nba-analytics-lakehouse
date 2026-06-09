from nba_api.stats.endpoints import leaguegamefinder
import pandas as pd

print("Buscando jogos da NBA...")

games = leaguegamefinder.LeagueGameFinder()

df = games.get_data_frames()[0]

print(f"Total de registros: {len(df)}")

print(df.head())

df.to_csv("data/raw/nba_games.csv",
          index=False
)

print("Arquivo salvo em data/raw/nba_games.csv")
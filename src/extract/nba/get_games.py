from nba_api.stats.endpoints import leaguegamefinder
import pandas as pd

games = leaguegamefinder.LeagueGameFinder()

print(df.head())

df.to_csv("data/raw/nba_games.csv",
          index=False
)
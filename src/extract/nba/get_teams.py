from nba_api.stats.static import teams
import pandas as pd

nba_teams = teams.get_teams()

df = pd.DataFrame(nba_teams)

print(df.head())

df.to_csv("data/raw/nba_teams.csv", 
          index=False
)
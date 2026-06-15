import pandas as pd
from Load import engine


read_data = pd.read_sql("SELECT * FROM ucl_players", engine)

# Top scorer

player_goals = read_data.groupby("PLAYER")["GOALS"].sum()
top_scorers = player_goals.sort_values(ascending=False)
# print(top_scorers.head(10))


# Top assiter


Player_assists = read_data.groupby("PLAYER")["ASSISTS"].sum()

most_assists =Player_assists.sort_values(ascending=False)
# print(most_assists.head(10))


# Most distance Covered

Player_distance = read_data.groupby("PLAYER")["DISTANCE(KM)"].sum()

distance_covered = Player_distance.sort_values(ascending=False)
#
# print(distance_covered.head(10))
# print(distance_covered.mean().__round__(2))

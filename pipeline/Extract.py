import pandas as pd

# data files

attack = "../data/raw/attacking.csv"
defence = "../data/raw/defending.csv"
key_data = "../data/raw/key_stats.csv"

# loading data into pandas
attacking_data = pd.read_csv(attack)
defence_data = pd.read_csv(defence)
key_stats = pd.read_csv(key_data)


# printing data for verification

# print(attacking_data.info() )

# print(defence_data.info() )
# #
# print(key_stats.info() )



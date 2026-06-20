import pandas as pd

import os
# data files

attack = "../data/raw/attacking.csv"
defence = "../data/raw/defending.csv"
key_data = "../data/raw/key_stats.csv"





# loading data into pandas
attacking_data = pd.read_csv(attack)
defence_data = pd.read_csv(defence)
key_stats = pd.read_csv(key_data)



if not os.path.exists(attack):
    raise FileNotFoundError(f"File not found: {attack}")

if not os.path.exists(defence):
    raise FileNotFoundError(f"File not found: {defence}")

if not os.path.exists(key_data):
    raise FileNotFoundError(f"File not found: {key_data}")

if not os.path.exists(attack):
    raise FileNotFoundError(f"File not found: {attack}")

# printing data for verification



# print(defence_data.columns )
# #
# print(key_stats.info() )



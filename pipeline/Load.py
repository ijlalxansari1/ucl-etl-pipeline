from sqlalchemy import create_engine
import pandas as pd

from pipeline.Transform import main_data ,attack , defence



# Database engine)
engine = create_engine("postgresql://postgres:postgres@localhost:5432/ucl_pipeline?client_encoding=utf8")


# KEY DATA ADDED IN DB

main_data.to_sql('ucl_players', con=engine, if_exists='replace', index=False)

# print("The ucl data has been added to database")

df = pd.read_sql("SELECT * FROM ucl_players LIMIT 5", engine)
# print(df)

# ATTACKING  DATA ADDED IN DB

attack.to_sql('attack_ucl_players', con=engine, if_exists='replace', index=False)

attacking_df = pd.read_sql("SELECT * FROM attack_ucl_players LIMIT 5", engine)
# print(attacking_df)

# Defence  DATA ADDED IN DB

defence.to_sql('defence_ucl_players', con=engine, if_exists='replace', index=False)
defence_df = pd.read_sql("SELECT * FROM defence_ucl_players LIMIT 5", engine)
# print(defence_df)



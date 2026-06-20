
from sqlalchemy import create_engine, try_cast
import pandas as pd
import os
from pipeline.Transform import main_data ,attack , defence
from dotenv import load_dotenv

load_dotenv()
# Database engine)
engine = create_engine(os.getenv("DATABASE_URL"))


# KEY DATA ADDED IN DB
try:
    main_data.to_sql('ucl_players', con=engine, if_exists='replace', index=False)
finally:
    engine.dispose()


# print("The ucl data has been added to database")


df = pd.read_sql("SELECT * FROM ucl_players LIMIT 5", engine)
# print(df)

# ATTACKING  DATA ADDED IN DB
try:

 attack.to_sql('attack_ucl_players', con=engine, if_exists='replace', index=False)
finally:
    engine.dispose()

attacking_df = pd.read_sql("SELECT * FROM attack_ucl_players LIMIT 5", engine)
# print(attacking_df)

# Defence  DATA ADDED IN DB


try:
     defence.to_sql('defence_ucl_players', con=engine, if_exists='replace', index=False)
finally:
    engine.dispose()


defence_df = pd.read_sql("SELECT * FROM defence_ucl_players LIMIT 5", engine)
# print(defence_df)


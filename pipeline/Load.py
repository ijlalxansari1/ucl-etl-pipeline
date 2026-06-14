from sqlalchemy import create_engine
import pandas as pd

from pipeline.Transform import main_data



# Database engine)
engine = create_engine("postgresql://postgres:postgres@localhost:5432/ucl_pipeline?client_encoding=utf8")


main_data.to_sql('ucl_players', con=engine, if_exists='replace', index=False)

print("The ucl data has been added to database")


df = pd.read_sql("SELECT * FROM ucl_players LIMIT 5", engine)
print(df)
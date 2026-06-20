from Extract import key_stats as main_data
from Extract import defence_data as defence
from Extract import attacking_data as attack

import pandas as pd
# transform phase




# ----------- DEFENCE DATA ------#

# dropping serial column.
defence =defence.drop(columns=["serial"])



# renaming columns.

defence = defence.rename(columns={"player_name": "player" ,"balls_recoverd":"Recovery(Ball)" ,"t_won":"Tackles(Won)",
                                  "t_lost":"Tackles(Lost)", "clearance_attempted":"Clearance(Attempt)","match_played":
                                  "Matches"})

# converting to upper case (columns)

defence.columns = defence.columns.str.upper()


defence.to_csv("../data/processed/defence_Processed.csv", index=False)
print("Defence data saved.")

#####---- Key stats data for the main data ---------#####



# renaming columns
attack = attack.drop(columns=["serial"])
attack = attack.rename(columns={"player_name":"player","corner_taken":"corner(taken)","match_played":"Matches" })

# converting to upper case (columns)
attack.columns = attack.columns.str.upper()

attack.to_csv("../data/processed/attack_Processed.csv",index=False)
print("Attack data saved.")


# print(type(defence))

#####---- Key stats data for the main data ---------#####


# converting column - distance_covered to float from string and sorting extra spaces



main_data["distance_covered"] =main_data["distance_covered"].replace('-',None)


main_data["distance_covered"] =main_data["distance_covered"].astype(float)
main_data["distance_covered"] = pd.to_numeric(
    main_data["distance_covered"], errors='coerce'
)
# 'coerce' turns anything it can't parse into NaN automatically
main_data["distance_covered"] = main_data["distance_covered"].fillna(
    main_data["distance_covered"].mean()
)


# Renaming and fixing column names

main_data =main_data.rename(columns={"distance_covered":"Distance(Km)" , "player_name" :  "Player" ,"minutes_played": "Minutes" , "match_played":"Matches" })
main_data.columns =  main_data.columns.str.upper()
# print(main_data.info() )


# saving files
main_data.to_csv("../data/processed/UCL_Processed.csv",index=False)
print("Main data saved.")


# print(f"The processed file has been saved in data/processed directory and file named 'UCL_Processed.csv'")




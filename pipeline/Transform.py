from Extract import key_stats as main_data
from Extract import defence_data as defence
from Extract import attacking_data as attack

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


processed_defence_csv = defence.to_csv("../data/processed/defence_Processed.csv",index=False)


#####---- Key stats data for the main data ---------#####



# renaming columns
attack = attack.drop(columns=["serial"])
attack = attack.rename(columns={"player_name":"player","corner_taken":"corner(taken)","match_played":"Matches" })

# converting to upper case (columns)
attack.columns = attack.columns.str.upper()

attacking_processed = attack.to_csv("../data/processed/attack_Processed.csv",index=False)
print(attack.head("CLUB"))

# print(type(defence))

#####---- Key stats data for the main data ---------#####


# converting column - distance_covered to float from string and sorting extra spaces

main_data["distance_covered"] =main_data["distance_covered"].replace('-',None)


main_data["distance_covered"] =main_data["distance_covered"].astype(float)
main_data["distance_covered"] = main_data["distance_covered"].fillna(main_data["distance_covered"].mean())


# Renaming and fixing column names

main_data =main_data.rename(columns={"distance_covered":"Distance(Km)" , "player_name" :  "Player" ,"minutes_played": "Minutes" , "match_played":"Matches" })
main_data.columns =  main_data.columns.str.upper()
# print(main_data.info() )


# saving files


processed_csv = main_data.to_csv("../data/processed/UCL_Processed.csv",index=False)


# print(f"The processed file has been saved in data/processed directory and file named 'UCL_Processed.csv'")







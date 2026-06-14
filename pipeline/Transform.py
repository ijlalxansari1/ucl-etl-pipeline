from Extract import key_stats as main_data

# transform phase


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











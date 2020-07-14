from sportsreference.mlb.schedule import Schedule

# from sportsreference.mlb.teams import Teams as MLB_Teams
# teams = MLB_Teams()
# print(dir(teams))
houston_schedule = Schedule('HOU')
print(houston_schedule.dataframe)
print(houston_schedule.dataframe.columns)

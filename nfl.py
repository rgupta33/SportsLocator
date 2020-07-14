
import sportsreference.nfl.teams as nfl
import sportsreference.nba as nba
from sportsreference.nfl.schedule import Schedule as NFL_Schedule
from sportsreference.nfl.boxscore import Boxscore as NFL_Boxscore

from sportsreference.nba.schedule import Schedule as NBA_Schedule
from sportsreference.nba.boxscore import Boxscore as NBA_Boxscore

# from sportsreference.nhl.schedule import Schedule as NhlSchedule
# from sportsreference.nfl.schedule import Schedule as NflSchedule
# from sportsreference.mlb.schedule import Schedule as MlbSchedule
# from sportsreference.nba.schedule import Schedule as NbaSchedule
# from sportsreference.nfl.teams import Teams
print(dir(nfl))
teams = nfl.Teams(2019)
chosen = None
for team in teams:
    print(team.abbreviation)
    df = NFL_Schedule(team.abbreviation).dataframe
    print(df)
    print(df.columns)
    break

print(dir(NFL_Boxscore('201909150rai')))
print(NFL_Boxscore('201909150rai').dataframe['date'])
games = {}


    # Prints the team's name
    # Prints the team's average margin of victory
# print(NflSchedule('PHI').dataframe)
# print(MlbSchedule('HOU').dataframe)
# teams = Teams()
# for team in teams:
#     print(team.name)

# print(NbaSchedule('HOU').dataframe)
# print(NhlSchedule('LAL').dataframe)

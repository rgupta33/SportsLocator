from flask import Flask,render_template,request
from sportsreference.nba.schedule import Schedule as NBA_Schedule
from sportsreference.nba.teams import Teams as NBA_Teams
from sportsreference.nfl.teams import Teams as NFL_Teams
from sportsreference.mlb.teams import Teams as MLB_Teams
import json


from datetime import date
import pandas as pd

app = Flask(__name__)

@app.route('/')
def homepage():
    leagues = {'nba': NBA_Teams(),'nfl': NFL_Teams(),'mlb': MLB_Teams()}
    return render_template('homepage.html',leagues = leagues)

@app.route('/games', methods=['GET','POST'])
def find_games():
    sport = request.form['sport']
    visiting_teams_abbrevs = request.form.getlist('visiting[]')
    home_teams_abbrevs = request.form.getlist('home[]')
    if sport == 'nba':
        toReturn = json.dumps(nba(home_teams_abbrevs,visiting_teams_abbrevs))
        print(toReturn)
        return toReturn
    elif sport =='nfl':
        print('nfl')
        return ''
    elif sport == 'mlb':
        print('mlb')
        return ''
    elif sport == 'nhl':
        print('nhl')
        return ''
    else:
        return 'Error: Invalid League'



def nba(home_teams_abbrevs,visiting_teams_abbrevs):
    games = {}
    for home_team_abbrev in home_teams_abbrevs:
        schedule = NBA_Schedule(home_team_abbrev).dataframe
        schedule = schedule[(schedule['opponent_abbr'].isin(visiting_teams_abbrevs)) & (schedule['datetime'] >= pd.Timestamp('today'))]
        schedule = schedule[['datetime','opponent_abbr','time']]
        schedule['datetime'] = schedule['datetime'].dt.strftime('%Y-%m-%d')
        schedule['home_team'] = home_team_abbrev
        games[home_team_abbrev] = schedule.values.tolist()
        print(schedule.values.tolist())
    return games

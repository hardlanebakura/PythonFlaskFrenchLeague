#from api_keys import API_FOOTBALL_KEY
import http.client
import json
import pandas as pd
from clubs import *
from log_config import logging
from player import Player
from goalkeeper import Goalkeeper
#from mongo_collections import DatabaseAtlas
from m import DatabaseAtlas
import difflib
from teams_info import teams_info
import os
from operator import itemgetter

connection = http.client.HTTPConnection('api.football-data.org')
API_FOOTBALL_KEY = os.getenv('API_FOOTBALL_KEY')
headers = { 'X-Auth-Token': str(API_FOOTBALL_KEY) }


#get detailed info for teams
connection.request('GET', '/v2/competitions/2015/teams', None, headers )
#response_teams = json.loads(connection.getresponse().read().decode())

#logging.debug(response_teams)


#get detailed info for scorers
#commented out in order to prevent API calls limit and use DatabaseAtlas
#connection.request('GET', '/v2/competitions/2015/scorers?limit=22', None, headers )
#response_top_scorers = json.loads(connection.getresponse().read().decode())

response_top_scorers = {}
response_top_scorers["scorers"] = DatabaseAtlas.findAll("french_league_1_top_scorers", {})

logging.debug(response_top_scorers)


#get detailed info for one player
#connection.request('GET', '/v2/players/8517', None, headers )
#response = json.loads(connection.getresponse().read().decode())

#logging.debug(response)

df = pd.read_csv("fifa-20-complete-dataset/players_22.csv")

player_categories = ['pace', 'shooting', 'passing', 'dribbling', 'physic', 'attacking_crossing', 'attacking_heading_accuracy', 'skill_dribbling',
                     'skill_fk_accuracy', 'movement_acceleration', 'movement_sprint_speed', 'movement_agility', 'power_shot_power', 'power_jumping', 'power_stamina', 'power_strength',
                     'power_long_shots', 'defending_sliding_tackle', 'value_eur', 'wage_eur']

def get_updated_categories(categories):
    for category in categories:
        df[category] = df[category].fillna(0)
        df[category] = df[category].astype(int)

get_updated_categories(player_categories)

d = df.to_dict("index")
players = [item[1] for item in d.items()]
players_for_ligue_1_teams = []
for club in clubs:
    players_for_ligue_1_teams.append({"{}".format(club["name"]):[]})

all_players = []
all_goalkeepers = []

#get all players in French Ligue 1
def get_all_players():
    counter = 0
    for player in players:
        for item in fifa_names:
            if player["club_name"] == item:
                counter = counter + 1
                #player is a goalkeeper
                if player["player_positions"] == "GK":
                    Goalkeeper1 = Goalkeeper(player)
                    Goalkeeper1.link_id = counter
                    all_goalkeepers.append(Goalkeeper1)
                    all_players.append(Goalkeeper1)
                else:
                    Player1 = Player(player)
                    Player1.link_id = counter
                    all_players.append(Player1)
                d = clubs[fifa_names.index(player["club_name"])]["name"]
                for team in players_for_ligue_1_teams:
                    for key in team:
                        if key == d:
                            team[key].append(player)
    return all_players
        #players_for_ligue_1_teams.index(fifa_names.index(item))

all_players = get_all_players()

def player_positions():

    counter = 1
    for player in all_players:
        player.player_id = counter
        counter = counter + 1
        if isinstance(player, Player):
            player.player_positions = player.player_positions.split(",")
            player.player_traits = str(player.player_traits).split(",")
        else:
            player.player_positions = ["GK"]
        for i in range(1, len(player.player_positions)):
            player.player_positions[i] = player.player_positions[i][1:]
    return

player_positions()

positions = [player.player_positions for player in all_players]

def get_players_for_team(team):

    # selected_index = fifa_names.index(team)
    # players_for_one_team = players_for_ligue_1_teams[selected_index][clubs[selected_index]["name"]]
    # return players_for_one_team
    players_for_one_team = []
    for player in all_players:
        if player.club_name == team:
            players_for_one_team.append(player)
    return players_for_one_team

#logging.debug(response_top_scorers)
def get_top_scorers():
    top_scorers = []
    for scorer in response_top_scorers["scorers"]:
        for player in all_players:

            #scorer playerdateOfBirth playerCountryOfBirth playernationality playershirtNumber
            # swap Reunion nationality in top_scorers with "France"
            #dob nationality_name club_jersey_number
            if scorer["player"]["dateOfBirth"] == player.dob and (scorer["player"]["nationality"] == player.nationality_name or (scorer["player"]["nationality"] == "Reunion" and player.nationality_name == "France")):
                top_scorers.append(player)
                top_scorers[-1].goals_for_top_scorers(scorer["numberOfGoals"])
    return top_scorers

top_scorers = get_top_scorers()

teams_all_info_df = pd.read_csv("fifa-20-complete-dataset/ligue_1_teams_info.csv", encoding = "ISO-8859-1")
teams_all_info_d = teams_all_info_df.to_dict("index")
response_teams = {}
response_teams["teams"] = [item for item in teams_all_info_d.values()]

def get_info_for_team(team):
    for item in response_teams["teams"]:
        team_name = difflib.get_close_matches(item["name"], fifa_names)
        if item["shortName"] == "Lille":
            team_name = ["LOSC Lille"]
        d = item.copy()
        d["name"] = team_name[0]
        return d
    # for item in DatabaseAtlas.findAll("french_league_1_team_info", {}):
    #     if item["name"] == team:
    #         return item

#get_players_for_team("Nice")
logging.debug(get_info_for_team("Olympique de Marseille"))

def get_player_diagrams(player):
    Player1 = player
    Player1.power = player.power_shot_power + player.power_jumping + player.power_long_shots + player.power_strength

def get_all_scorers():
    connection.request('GET', '/v2/competitions/2015/scorers?limit=240', None, headers)
    response_all_scorers = json.loads(connection.getresponse().read().decode())
    all_scorers = []
    for scorer in response_all_scorers["scorers"]:
            for player in all_players:
                if scorer["player"]["dateOfBirth"] == player.dob and (
                        scorer["player"]["nationality"] == player.nationality_name or (
                        scorer["player"]["nationality"] == "Reunion" and player.nationality_name == "France")):
                    all_scorers.append(player)
                    all_scorers[-1].goals_for_top_scorers(scorer["numberOfGoals"])
                    DatabaseAtlas.insertOne("scorers", player.__dict__)

def get_top_scorers_for_team(team):
    top_scorers_for = DatabaseAtlas.findAll("scorers", {})
    top_scorers_for_team = [i for i in top_scorers_for if i["club_name"] == team]
    return top_scorers_for_team

#commented out in order to prevent multiple unnecessary adds to the database
#get_all_scorers()
all_scorers = DatabaseAtlas.findAll("scorers", {})
ts = all_scorers[:22]
logging.debug(ts)
get_top_scorers_for_team("AS Monaco")

def get_detailed_stats_for_team(team):
    for fifa_name in fifa_names:
        if fifa_name == team:
            return clubs[fifa_names.index(team)]

#DatabaseAtlas.dropCol("scorers")

def get_roles_for_team(team):
    goalkeepers = []
    defenders = []
    midfielders = []
    forwards = []
    for player in team:
        logging.debug(player.new_id)
        position = player.player_positions[0]
        if position == "GK":
            goalkeepers.append(player)
        elif position[-1] == "B":
            defenders.append(player)
        elif position[-1] == "M":
            midfielders.append(player)
        else:
            forwards.append(player)
    squad = {"goalkeepers":goalkeepers, "defenders":defenders, "midfielders":midfielders, "forwards":forwards}
    return squad

logging.debug(fifa_names)
for team in fifa_names:
    logging.debug(get_info_for_team(team))

#connection.request('GET', '/v2/competitions/2015/matches?matchday=20', None, headers )
#response_matches = json.loads(connection.getresponse().read().decode())

#DatabaseAtlas.dropCol("french_ligue_1_upcoming_matches")

def get_trophies(team):
    return teams_info[team]["trophies"]

get_trophies("AS Monaco")

def get_best_position(selected_player):

    all_positions_for_one_player = []
    all_positions_values = []
    for position in selected_player.player_positions:
        # logging.debug(position.lower())
        if isinstance(selected_player, Player):
            all_positions_for_one_player.append(position)
            all_positions_values.append(selected_player.__getattribute__(position.lower()))
        else:
            all_positions_for_one_player.append("GK")
            all_positions_values.append(selected_player.overall)
    main_value = max(all_positions_values)
    main_player_position = all_positions_for_one_player[all_positions_values.index(main_value)]
    return main_player_position

def get_similar_players(selected_player):

    similar_players = []
    for player in all_players:
        if player.short_name != selected_player.short_name:
            player_best_position = get_best_position(player)
            if player_best_position in selected_player.player_positions:
                chosen_index = selected_player.player_positions.index(player_best_position)
                player_best_position_value = player.__getattribute__(player_best_position.lower())
                if type(player_best_position_value) == str:
                    player_best_position_value_1 = player_best_position_value.split("+")
                    if len(player_best_position_value_1) > 1:
                        player_best_position_value_total = int(player_best_position_value_1[0]) + int(player_best_position_value_1[1])
                        logging.debug(player_best_position_value_total)
                    else:
                        if "-" not in player_best_position_value_1[0]:
                            player_best_position_value_total = int(player_best_position_value_1[0])
                        else:
                            logging.debug(player_best_position_value_1[0])
                            player_best_position_value_m = player_best_position_value_1[0].split("-")
                            player_best_position_value_total = int(player_best_position_value_m[0]) - int(player_best_position_value_m[1])
                selected_player_position = selected_player.player_positions[chosen_index].lower()
                selected_player_value = selected_player.__getattribute__(selected_player_position)
                if type(selected_player_value) == str:
                    selected_player_value_1 = selected_player_value.split("+")
                    if len(selected_player_value_1) > 1:
                        selected_player_value_total = int(selected_player_value_1[0]) + int(selected_player_value_1[1])
                        logging.debug(selected_player_value_total)
                    else:
                        selected_player_value_total = int(selected_player_value_1[0])
                dict = player.__dict__
                dict["abs"] = selected_player_value_total - player_best_position_value_total
                similar_players.append(dict)
    similar_players = sorted(similar_players, key=lambda d: d['abs'])
    return similar_players[:10]

def get_similar_goalkeepers(goalkeeper):
    similar_goalkeepers = []
    for player in all_goalkeepers:
        if player.long_name != goalkeeper.long_name:
            d = player.__dict__
            d["abs"] = abs(goalkeeper.overall - player.overall)
            logging.info(d)
            similar_goalkeepers.append(d)
    similar_goalkeepers = sorted(similar_goalkeepers, key=itemgetter('abs'))

    return similar_goalkeepers[:10]

get_similar_goalkeepers(all_players[100])

logging.debug(get_players_for_team("AS Monaco"))
get_roles_for_team(get_players_for_team("AS Monaco"))

#DatabaseAtlas.dropCol("french_league_1_top_scorers")

def get_teams_colors():
    all_team_colors = []
    for team in fifa_names:
        team_colors = get_info_for_team(team)["clubColors"].split(" / ")
        if len(team_colors) > 2:
            team_colors.pop(1)
        for color in team_colors:
            team_colors[team_colors.index(color)] = color.lower()
        d = {"name":team, "team_colors":team_colors}
        all_team_colors.append(d)
        logging.debug(all_team_colors)
    return all_team_colors

def get_team_calendar(team):
    fixture_id = 1
    team_calendar = {}
    for match in DatabaseAtlas.findAll("french_league_1", {}):
        if match["home_team"] == fifa_to_clubs[team] or match["away_team"] == fifa_to_clubs[team]:
            match["home_team"] = clubs_to_fifa[match["home_team"]]
            match["away_team"] = clubs_to_fifa[match["away_team"]]
            team_calendar["Fixture {}".format(fixture_id)] = match
            fixture_id = fixture_id + 1
    return team_calendar

teams_colors = get_teams_colors()
top_assists = DatabaseAtlas.findAll("french_league_1_top_assists", {})
#logging.debug(teams_all_info)
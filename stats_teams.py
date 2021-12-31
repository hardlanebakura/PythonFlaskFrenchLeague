import matplotlib.pyplot as plt
import numpy as np
from teams import all_players, get_players_for_team
from matches import *
from logging.config import logging
from operator import itemgetter
from clubs import *
from player import Player

plt.rcdefaults()

def get_team_salaries():
    all_salaries_and_overall_skills = {}
    for team in fifa_names:
        team_rank = clubs[fifa_names.index(team)]["rank"]
        #logging.info(team_rank)
        team_salaries_and_overall_skills = [[player.overall, player.value_eur, player.wage_eur] for player in get_players_for_team(team)]
        #logging.info(team_salaries_and_overall_skills)
        team_overall = int(sum([item[0] for item in team_salaries_and_overall_skills])/len([item[0] for item in team_salaries_and_overall_skills]))
        team_value = int(sum([item[1] for item in team_salaries_and_overall_skills])/len([item[1] for item in team_salaries_and_overall_skills]))
        team_wage = int(sum([item[2] for item in team_salaries_and_overall_skills])/len([item[2] for item in team_salaries_and_overall_skills]))
        all_salaries_and_overall_skills[team] = [team_rank, team_overall, team_value, team_wage]
    team_value = all_salaries_and_overall_skills.copy()
    for team in team_value:
        team_value[team] = all_salaries_and_overall_skills[team][2]
    team_value = {k: v for k, v in sorted(team_value.items(), key=itemgetter(1), reverse=True)}
    all_values = list(team_value.items())
    team_with_the_highest_budget = all_values [0]
    team_with_the_lowest_budget = all_values [-1]
    underachieving_teams = []
    overachieving_teams = []
    for team in fifa_names:
        #logging.info(team_value[team])
        for club in clubs_sorted:
            if club["name"] == club_names[fifa_names.index(team)]:
                #logging.info(team)
                #logging.info(club["rank"])
                #logging.info((team, team_value[team]))
                team_budget_rank = all_values.index((team, team_value[team]))
                #logging.info(team_budget_rank)
                if (team_budget_rank < club["rank"]):
                #team is underachieving
                    budget_and_rank_diff = club["rank"] - team_budget_rank - 1
                    #logging.info(budget_and_rank_diff)
                    underachieving_teams.append({"name":team, "ranks_below_expectations":budget_and_rank_diff})
                else:
                #team is overachieving
                    budget_and_rank_diff = team_budget_rank - club["rank"] - 1
                    #logging.info(budget_and_rank_diff)
                    overachieving_teams.append({"name": team, "ranks_above_expectations": budget_and_rank_diff})
    #logging.debug(team_value)
    underachieving_teams = sorted(underachieving_teams, key=itemgetter("ranks_below_expectations"), reverse=True)[:3]
    overachieving_teams = sorted(overachieving_teams, key=itemgetter("ranks_above_expectations"), reverse=True)[:3]
    logging.info(all_salaries_and_overall_skills)
    #logging.info(overachieving_teams)
    #logging.info(team_value)
    d = {"all_salaries":all_values, "lowest_budgets":all_values[-3:], "highest_budgets":all_values[:3], "underachieving_teams":underachieving_teams, "overachieving_teams":overachieving_teams}
    #logging.info(d)
    return [d, all_salaries_and_overall_skills]

team_salaries = get_team_salaries()[0]
team_budgets = get_team_salaries()[1]

def lower_ranked_beat_higher(team, match):
    #checks if the team beat the higher ranked team
    #team was home
    if team["name"] == match["home_team"]:
        home_team = team["name"]
        home_team_rank = team["rank"]
        home_team_goals = match["home_team_goals"]
        for club in clubs_sorted:
            if club["name"] == match["away_team"]:
                away_team = club["name"]
                away_team_rank = club["rank"]
                away_team_goals = match["away_team_goals"]
                if home_team_goals > away_team_goals and home_team_rank > away_team_rank:
                    logging.info(match)
                    return 1
                else:
                    return 0
    else:
    #team was away
        away_team = team["name"]
        away_team_rank = team["rank"]
        away_team_goals = match["away_team_goals"]
        for club in clubs_sorted:
            if club["name"] == match["home_team"]:
                home_team = club["name"]
                home_team_rank = club["rank"]
                home_team_goals = match["home_team_goals"]
                if home_team_goals < away_team_goals and home_team_rank < away_team_rank:
                    logging.info(match)
                    return 1
                else:
                    return 0
        return 0

def get_goals_teams():
    d = clubs_sorted
    goals_teams_scored = sorted(d, key=itemgetter('gs'), reverse=True)
    goals_teams_conceeded = sorted(d, key=itemgetter('gc'), reverse=True)
    for item in goals_teams_scored:
        item["fifa_name"] = clubs_to_fifa[item["name"]]
    for item in goals_teams_conceeded:
        item["fifa_name"] = clubs_to_fifa[item["name"]]
    return [goals_teams_scored, goals_teams_conceeded]

def team_with_best_counterattack():
    #measures how many matches team was able to repel attacks of better ranked teams and counter attack for win
    d = {}
    for club in clubs_sorted:
        number_of_upsets_club_made = 0
        for match in matches:
            if match["home_team"] == club["name"] or match["away_team"] == club["name"]:
                number_of_upsets_club_made = number_of_upsets_club_made + lower_ranked_beat_higher(club, match)
        logging.info(number_of_upsets_club_made)
        d[clubs_to_fifa[club["name"]]] = number_of_upsets_club_made
    d = sorted(d.items(), key=itemgetter(1), reverse=True)[:10]
    return d

goals_teams = get_goals_teams()
teams_with_best_counterattack = team_with_best_counterattack()

logging.info(get_team_salaries())

def get_best_managers():
    best_managers = []
    overachieving_teams = [team["name"] for team in team_salaries["overachieving_teams"]]
    for team in overachieving_teams:
        best_managers.append({"team":team, "coach": teams_info[team]["coach"], "coach_url": teams_info[team]["coach_url"]})
    for club in clubs_sorted:
        for i in range(1,10):
            if clubs_to_fifa[club["name"]] not in overachieving_teams:
                if club["rank"] == i:
                    logging.debug(teams_info[clubs_to_fifa[club["name"]]]["coach"])
                    best_managers.append({"team":clubs_to_fifa[club["name"]], "coach":teams_info[clubs_to_fifa[club["name"]]]["coach"], "coach_url":teams_info[clubs_to_fifa[club["name"]]]["coach_url"]})
    logging.info(best_managers)
    return best_managers

def get_accuracy_of_teams():
    teams_accuracy = []
    for team in fifa_names:
        accuracy_for_team = [player.skill_fk_accuracy for player in get_players_for_team(team) if isinstance(player, Player)]
        accuracy_for_team = sum(accuracy_for_team) / len(accuracy_for_team)
        teams_accuracy.append({"name":team, "accuracy":int(round(accuracy_for_team))})
    teams_accuracy = sorted(teams_accuracy, key=itemgetter('accuracy'), reverse=True)
    logging.info(teams_accuracy)
    return teams_accuracy

best_managers = get_best_managers()
get_goals_teams()
teams_accuracy = get_accuracy_of_teams()
logging.debug(best_managers)
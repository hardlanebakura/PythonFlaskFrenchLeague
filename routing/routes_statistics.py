from flask import Flask, render_template, request, url_for, session, jsonify, Blueprint, abort
from jinja2 import TemplateNotFound
from log_config import logging
from m import matches, clubs_sorted
from clubs import *
from teams import *
from stats import *
from stats_teams import *

match_least_goals = matches_goals_number_records()[0]
match_most_goals = matches_goals_number_records()[1]

statistics_page = Blueprint('statistics', __name__,
                      template_folder='templates', static_folder='static', url_prefix='/statistics')

@statistics_page.route("/")
def statistics():
    return render_template("statistics/index.html", latest_matches = matches[-5:], clubs = clubs_sorted, teams = fifa_names, team = fifa_names[10], top_scorers = top_scorers,
                           highest_match_capacity = highest_match_capacity(), match_most_goals = match_most_goals, match_least_goals = match_least_goals, top_assists = top_assists,
                           fifa_to_clubs = fifa_to_clubs, best_managers = best_managers, biggest_upset = find_biggest_upset())

@statistics_page.route("/player_stats")
def player_stats():
    return render_template("statistics/player_stats.html", latest_matches = matches[-5:], clubs = clubs_sorted, teams = fifa_names, team = fifa_names[10], top_scorers = top_scorers)

@statistics_page.route("/team_stats")
def team_stats():
    return render_template("statistics/team_stats.html", latest_matches = matches[-5:], clubs = clubs_sorted, teams = fifa_names, team = fifa_names[10], top_scorers = top_scorers,
                           team_salaries = get_team_salaries(), fifa_to_clubs = fifa_to_clubs, teams_with_best_counterattack = teams_with_best_counterattack, goals_teams = goals_teams,
                           team_with_most_foreigners = team_with_most_foreigners, clubs_to_fifa = clubs_to_fifa)

@statistics_page.route("/fun_facts")
def fun_facts():
    interesting_players = find_number_one_players_in_various_categories()
    return render_template("statistics/fun_facts.html", latest_matches = matches[-5:], clubs = clubs_sorted, teams = fifa_names, team = fifa_names[10], top_scorers = top_scorers,
                           interesting_players = interesting_players, left_team = get_preferred_foot_teams(), teams_accuracy = teams_accuracy, fifa_to_clubs = fifa_to_clubs, clubs_to_fifa = clubs_to_fifa)
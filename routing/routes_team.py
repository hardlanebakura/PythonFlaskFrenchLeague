from flask import Flask, render_template, request, url_for, session, jsonify, Blueprint, abort
from jinja2 import TemplateNotFound
from log_config import logging
from m import *
from clubs import *
from teams import *
from teams_info import teams_info

team_page = Blueprint('team', __name__,
                        template_folder='templates', static_folder='static')

@team_page.route('/teams/<int:id>')
def team(id):
    try:
        team = fifa_names[id - 1]
        team_info = get_info_for_team(team)
        team_detailed_stats = get_detailed_stats_for_team(team)
        logging.info(team_info)
        latest_match = get_latest_team_match(team)
        upcoming_match = get_next_match_for_team(team)
        logging.debug(upcoming_match)
        return render_template("/teams/team.html", latest_matches = matches[-5:], id = id, team = team, top_scorers = get_top_scorers_for_team(team), team_info = team_info, team_detailed_stats = team_detailed_stats,
                               clubs = clubs_sorted, latest_match = latest_match, upcoming_match = upcoming_match, fifa_to_clubs = fifa_to_clubs, teams_colors = teams_colors)
    except TemplateNotFound:
        abort(404)

@team_page.route('/teams/<int:id>/calendar')
def team_calendar(id):
    try:
        team = fifa_names[id - 1]
        return render_template("/teams/team_calendar.html", latest_matches=matches[-5:], id=id, team=team, team_calendar = get_team_calendar(team), fifa_to_clubs = fifa_to_clubs)
    except TemplateNotFound:
        abort(404)

@team_page.route('/teams/<int:id>/stadium')
def team_stadium(id):
    try:
        team = team=fifa_names[id - 1]
        return render_template("/teams/team_stadium.html", latest_matches=matches[-5:], id=id, team = team, d = teams_info, team_info = get_info_for_team(team))
    except TemplateNotFound:
        abort(404)

@team_page.route('/teams/<int:id>/squad')
def team_squad(id):
    try:
        team = fifa_names[id - 1]
        squad = get_roles_for_team(get_players_for_team(team))
        return render_template("/teams/team_squad.html", latest_matches=matches[-5:], id=id, team = team, squad = squad)
    except TemplateNotFound:
        abort(404)

@team_page.route('/teams/<int:id>/staff')
def team_staff(id):
    try:
        team = fifa_names[id - 1]
        return render_template("/teams/team_staff.html", latest_matches=matches[-5:], id=id, team = team, d = teams_info, clubs = clubs_sorted)
    except TemplateNotFound:
        abort(404)


@team_page.route('/teams/<int:id>/stats')
def team_stats(id):
    try:
        return render_template("/teams/team_stats.html", latest_matches=matches[-5:], id=id, team=fifa_names[id - 1])
    except TemplateNotFound:
        abort(404)


@team_page.route('/teams/<int:id>/honours')
def team_honours(id):
    try:
        team = fifa_names[id - 1]
        trophies = get_trophies(team)
        logging.debug(trophies)
        return render_template("/teams/team_honours.html", latest_matches=matches[-5:], id=id, team=fifa_names[id - 1], trophies = trophies)
    except TemplateNotFound:
        abort(404)


@team_page.route('/teams/<int:id>/history')
def team_history(id):
    try:
        return render_template("/teams/team_history.html", latest_matches=matches[-5:], id=id, team=fifa_names[id - 1])
    except TemplateNotFound:
        abort(404)
        
    

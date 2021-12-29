from flask import Flask, render_template, request, url_for, session, jsonify, Blueprint, abort
#from flask_paginate import Pagination, get_page_parameter, get_page_args
from jinja2 import TemplateNotFound
from log_config import logging
from matches import matches, clubs_sorted
from teams import *
from player import Player
from goalkeeper import Goalkeeper
from skill_diagram import get_skill_diagram_for_player

PLAYER_ROWS_PER_PAGE = 40

players_pages = Blueprint('players', __name__,
                        template_folder='templates', static_folder='static', url_prefix="/players")

@players_pages.route("/")
def players():
    search = False
    q = request.args.get('q')
    if q:
        search = True

    page = request.args.get('page', default = 1, type = int)
    #pagination = Pagination(page = page, per_page = 5, search = search, total = 100, css_framework="bootstrap3")
    #return render_template("/players/players.html", all_players=all_players[:100], latest_matches=matches[-5:],
                           #pagination=pagination)

    return render_template("/players/players.html", all_players = all_players[:100], latest_matches = matches[-5:])

@players_pages.route("/<int:id>")
def player(id):
    for player in all_players:
        if player.player_id == id:
            selected_player = player
    if isinstance(selected_player, Player):
        get_skill_diagram_for_player(selected_player)
        return render_template("/players/player.html", all_players = all_players[:100], latest_matches = matches[-5:], positions = positions, similar_players = get_similar_players(selected_player),  player = selected_player)
    elif isinstance(selected_player, Goalkeeper):
        return render_template("/players/gk.html", all_players=all_players[:100], latest_matches=matches[-5:], positions=positions, m = 1, similar_players = get_similar_players(selected_player), player=selected_player)
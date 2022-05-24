from flask import Flask, render_template, request, url_for, session, jsonify, Blueprint, abort
from flask_paginate import Pagination, get_page_args
from jinja2 import TemplateNotFound
from log_config import logging
from matches import matches, clubs_sorted
from teams import *
from player import Player
from goalkeeper import Goalkeeper
from skill_diagram import get_skill_diagram_for_player
import math

PLAYER_ROWS_PER_PAGE = 40

players_pages = Blueprint('players', __name__,
                        template_folder='Templates', static_folder='static', url_prefix="/players")

def get_players(offset=0, per_page=10):
    return all_players[offset: offset + per_page]

@players_pages.route("/")
def players():
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    players = get_players(offset=offset, per_page=per_page)
    total = math.ceil(len(all_players) / 10) * 10
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')

    return render_template("/players/players.html",  all_players = players, page = page, per_page = 50, pagination = pagination, total = total, fifa_names = fifa_names, latest_matches=matches[-5:])

@players_pages.route("/<int:id>")
def player(id):
    for player in all_players:
        if player.player_id == id:
            selected_player = player
    if isinstance(selected_player, Player):
        get_skill_diagram_for_player(selected_player)
        return render_template("/players/player.html", all_players = all_players[:100], latest_matches = matches[-5:], positions = positions, similar_players = get_similar_players(selected_player),  player = selected_player)
    elif isinstance(selected_player, Goalkeeper):
        return render_template("/players/gk.html", all_players=all_players[:100], latest_matches=matches[-5:], positions=positions, m = 1, similar_players = get_similar_goalkeepers(selected_player), player=selected_player)
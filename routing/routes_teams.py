from flask import Flask, render_template, request, url_for, session, jsonify, Blueprint, abort
from jinja2 import TemplateNotFound
from log_config import logging
from matches import matches, clubs_sorted
from clubs import fifa_names
from teams import *

teams_page = Blueprint('teams', __name__,
                        template_folder='templates', static_folder='static')

@teams_page.route('/teams/')
def teams():
    try:
        return render_template("/teams/teams.html", latest_matches = matches[-5:], clubs = clubs_sorted, teams = fifa_names)
    except TemplateNotFound:
        abort(404)





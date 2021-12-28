from flask import Flask, request, redirect, render_template, url_for, jsonify, Blueprint
from config import config1
from routing.routes import *
from routing.routes_teams import *
from routing.routes_players import *
from routing.routes_team import *
from routing.routes_news import *
from routing.routes_statistics import *

app = Flask(__name__)

#Configuring application
config1(app.config, app.jinja_env)

app.register_blueprint(index_page)
app.register_blueprint(teams_page)
app.register_blueprint(players_pages)
app.register_blueprint(team_page)
app.register_blueprint(news_page)
app.register_blueprint(statistics_page)

if (__name__ == "__main__"):
    app.run(debug=True)
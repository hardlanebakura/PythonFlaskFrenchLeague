from flask import Flask, render_template, request, url_for, session, jsonify, Blueprint, abort
from jinja2 import TemplateNotFound
from log_config import logging
from matches import matches, clubs_sorted
from clubs import fifa_names
from teams import *

news_page = Blueprint('news', __name__,
                        template_folder='templates', static_folder='static')

news_page_ids = {
    1: "Ben Yedder",
    2: "David Guion",
    3: "Official Podcast",
    4: "Contract Extensions"
}

@news_page.route("/news")
def news_index():
    return render_template("/news/news_index_page.html", latest_matches = matches[-5:])

@news_page.route("/news/<int:id>")
def news(id):
    return render_template("/news/{}.html".format(news_page_ids[id].replace(" ", "_")), latest_matches = matches[-5:])
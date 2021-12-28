from flask import Flask, render_template, request, redirect, url_for, session, jsonify, Blueprint, abort
from jinja2 import TemplateNotFound
from log_config import logging
from matches import matches, clubs_sorted
from routing.routes_statistics import statistics_page

index_page = Blueprint('index', __name__,
                        template_folder='templates', static_folder='static')

@index_page.route('/', defaults={'page': 'index'})
def show(page):
    try:
        return redirect("/statistics/")
    except TemplateNotFound:
        abort(404)
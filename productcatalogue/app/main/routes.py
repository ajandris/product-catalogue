from productcatalogue.app.main import bp
from flask import render_template, request, redirect

@bp.route('/')
def index():
    return 'Hello World! Main Blueprint'

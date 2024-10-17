from flask import Blueprint

bp = Blueprint('main', __name__)

from productcatalogue.app.main import routes

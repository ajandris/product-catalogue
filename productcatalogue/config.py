"""
Configuration file for the project Product Catalogue

@author: Andris Jancevskis

"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))

if os.path.exists(os.path.abspath('env.py')):
    import env


class Config(object):

    # Application params
    FLASK_APP = os.environ.get('FLASK_APP', 'Product Catalogue')
    FLASK_ENV = os.environ.get('FLASK_ENV', 'development')


    # web server start params
    HOST = os.environ.get('HOST', 'localhost')
    PORT = int(os.environ.get('PORT', 5000))
    DEBUG = os.environ.get('DEBUG', 'True')

    # security
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Directory setup
    STATIC_FOLDER = os.path.join(basedir, os.environ.get('STATIC_FOLDER', 'static'))
    TEMPLATE_FOLDER = os.path.join(basedir, os.environ.get('TEMPLATE_FOLDER', 'templates'))
    STATIC_URL = os.environ.get('STATIC_URL', '/static/')

    # database
    SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}:{}/{}".format(
        os.environ.get('POSTGRES_USER', ''),
        os.environ.get('POSTGRES_PASSWORD', ''),
        os.environ.get('POSTGRES_HOST', 'localhost'),
        os.environ.get('POSTGRES_PORT', '5432'),
        os.environ.get('POSTGRES_DATABASE_NAME', '')
        )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

#SQLALCHEMY_DATABASE_URI = "postgresql://username:password@host:port/database_name"

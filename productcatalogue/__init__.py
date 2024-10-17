from flask import Flask
from .config import Config as config
from productcatalogue.app.extensions import db


def create_app():

    app = Flask(
        __name__,
        static_folder=config.STATIC_FOLDER,
        template_folder=config.TEMPLATE_FOLDER,
        static_url_path=config.STATIC_URL,
        instance_relative_config=True,
    )

    app.config["SECRET_KEY"] = config.SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI

    # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    from productcatalogue.app.main import bp as main_bp
    app.register_blueprint(main_bp)

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
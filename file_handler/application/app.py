from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import FLASK_APP_NAME

db_conn = SQLAlchemy() # TODO - initialize the DB class here - db_obj



def create_app():
    """Construct the core application."""
    app = Flask(FLASK_APP_NAME, instance_relative_config=False)
    app.config.from_object('config.FlaskConfig')
    db_conn.init_app(app) # TODO - db_obj.db_conn.init_app

    with app.app_context():
        import application.routes  # import routes
        return app

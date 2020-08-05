from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import FLASK_APP_NAME

db = SQLAlchemy() # TODO - WHERE SHOULD I PUT THIS


def create_app():
    """Construct the core application."""
    app = Flask(FLASK_APP_NAME, instance_relative_config=False)
    app.config.from_object('config.FlaskConfig')

    db.init_app(app)

    with app.app_context(): # TODO - read about it! :)
        import application.routes  # Import routes
        return app

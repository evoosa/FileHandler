from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from file_handler.config import FLASK_APP_NAME

db_conn = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(FLASK_APP_NAME, instance_relative_config=False)
    app.config.from_object('config.FlaskConfig')
    db_conn.init_app(app)

    with app.app_context():
        import file_handler.application.routes  # import routes
        return app

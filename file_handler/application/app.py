from flask import Flask

from application.models.sqldb import SQLDB
from config import FLASK_APP_NAME

db_obj = SQLDB()


def create_app():
    """Construct the core application."""
    app = Flask(FLASK_APP_NAME, instance_relative_config=False)
    with app.app_context():
        # import ipdb # TODO - remove!
        # ipdb.set_trace()
        return app

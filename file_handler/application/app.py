from flask import Flask

from application.db_handler import DBHandler

db_obj = DBHandler()


def create_app():
    """Construct the core application."""
    app = Flask('file_handler', instance_relative_config=False)
    with app.app_context():
        from application import routes
        return app

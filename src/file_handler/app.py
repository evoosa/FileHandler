from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import FLASK_APP_HOST, FLASK_APP_PORT, FLASK_APP_NAME

db = SQLAlchemy() # TODO - WHERE SHOULD I PUT THIS


def create_app() -> Flask:
    """
    initialize the flask app and the database connection
    :return: flask app
    """
    app = Flask(FLASK_APP_NAME, instance_relative_config=True)
    app.config.from_object('config.FlaskConfig')
    db.init_app(app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host=FLASK_APP_HOST, port=FLASK_APP_PORT)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import FLASK_APP_NAME, FLASK_APP_HOST, FLASK_APP_PORT

db_conn = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(FLASK_APP_NAME, instance_relative_config=False)
    app.config.from_object('config.FlaskConfig')
    db_conn.init_app(app)

    with app.app_context():
        import routes  # import routes
        return app


application = create_app()

if __name__ == '__main__':
    application.run(host=FLASK_APP_HOST, port=FLASK_APP_PORT)

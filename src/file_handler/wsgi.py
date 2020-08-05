from application.app import create_app
from config import FLASK_APP_HOST, FLASK_APP_PORT # TODO - fix imports

if __name__ == '__main__':
    app = create_app()
    app.run(host=FLASK_APP_HOST, port=FLASK_APP_PORT)

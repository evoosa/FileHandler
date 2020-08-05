from file_handler.config import FLASK_APP_HOST, FLASK_APP_PORT
from file_handler.application.app import create_app

application = create_app()

if __name__ == '__main__':
    application.run(host=FLASK_APP_HOST, port=FLASK_APP_PORT)

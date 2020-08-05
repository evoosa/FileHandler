FILES_DATABASE_NAME = 'files_db'
FILES_TABLE_NAME = 'files_table'
POSTGRES_URI = f'postgres+psycopg2://postgres:postgres@localhost:5432/{FILES_DATABASE_NAME}'
FLASK_APP_HOST = 'localhost'
FLASK_APP_PORT = 80
FLASK_APP_NAME = 'file_handler'


class FlaskConfig:
    """Set Flask configuration"""  # TODO - is it best practice
    SQLALCHEMY_DATABASE_URI = POSTGRES_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True  # TODO - REMOVE
    SQLALCHEMY_ECHO = False

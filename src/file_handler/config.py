from os import environ

DATABASE_URL = 'localhost'
FILES_DATABASE_NAME = 'files_db'
FILES_TABLE_NAME = 'files_table'
FLASK_APP_HOST = 'localhost'
FLASK_APP_PORT = 80
FLASK_APP_NAME = 'file_handler'


class FlaskConfig:
    """Set Flask configuration""" # TODO - is it best practice
    SQLALCHEMY_DATABASE_URI = environ.get('postgresql://{db_url}/{db_name}'.format(db_url=DATABASE_URL, db_name=FILES_DATABASE_NAME)) # TODO - f formating
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True # TODO - REMOVE
    # SQLALCHEMY_ECHO = False

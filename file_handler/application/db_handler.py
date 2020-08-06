import threading

from sqlalchemy import create_engine, exc
from sqlalchemy.orm import Session

from application.models.newfile import NewFile
from application.models.db_heartbeat import DBHeartbeat
from application.utils import is_file_corrupted

FILES_DATABASE_NAME = 'files_db'
POSTGRES_URI = f'postgres+psycopg2://postgres:postgres@localhost:5432/{FILES_DATABASE_NAME}'


class DBHandler:
    """ Handles the DB connection, and DB operations """

    def __init__(self):
        self.db_session = self.get_db_session()
        self.send_heartbeats()

    @staticmethod
    def get_db_session():
        """ connect to the SQL Database """
        db_engine = create_engine(POSTGRES_URI)
        return Session(bind=db_engine)

    def send_heartbeats(self):
        """
        runs a thread, that will validate the db connection every minute
        """
        threading.Timer(60, self.send_heartbeats).start()
        self.validate_conn()

    def send_heartbeat(self):
        """ update the heartbeat table with the current timestamp """
        new_heartbeat = DBHeartbeat()
        self.db_session.add(new_heartbeat)
        self.db_session.commit()

    def validate_conn(self):
        """
        check if the DB connection is alive.
        if it's invalidated - try to reconnect. else, raise
        """
        try:
            self.send_heartbeat()
        except exc.DBAPIError as e:
            if e.connection_invalidated:
                self.db_session = self.get_db_session()
            else:
                raise

    def add_files_to_db(self, filenames: list):
        """
        Go over a list of filenames, and add the non corrupted files to the database
        :arg filenames: file names the function will go over and add to the database
        """
        for filename in filenames:
            if not is_file_corrupted(filename):
                self.add_file_to_db(filename)

    def add_file_to_db(self, filename: str):
        """
        adds a single file to the database
        :param filename: name of the file to add
        """
        new_file = NewFile(
            filename=filename
        )
        self.db_session.add(new_file)
        self.db_session.commit()

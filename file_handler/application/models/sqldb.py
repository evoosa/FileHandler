from sqlalchemy import create_engine, exc
from sqlalchemy.orm import Session
from application.models.newfile import NewFile
from application.utils import is_file_corrupted

FILES_DATABASE_NAME = 'files_db'
POSTGRES_URI = f'postgres+psycopg2://postgres:postgres@localhost:5432/{FILES_DATABASE_NAME}'


# TODO - get this out of models?
# TODO - move stuff from config here

class SQLDB():  # TODO - refractore name, same for newfile?
    """Data model for the DB connection."""

    def __init__(self):
        self.db_session = self.get_db_session()
        self.send_heartbeats()

    def get_db_session(self):
        """ connect to the SQL Database """
        db_engine = create_engine(POSTGRES_URI)
        return Session(bind=db_engine)

    def send_heartbeats(self):  # TODO - one of them is unnecessary?
        """
        will run a thread, that will validate the db connection every minute
        """
        pass

        # def validate_conn(self):
        #     """
        #     check if the DB connection is alive.
        #     if it isn't, try to reconnect. if it fails, raise an exception
        #     """
        #     try:
        #         self.db_conn.engine.exec('SELECT 1') #FIXME - DATEEEEEEE
        #     except exc.DBAPIError as e:
        #         # self.db_conn =
        #
        #     except exc.OperationalError:
        # try
        # execute update date in db
        # except the disconnect error
        # try to reconnect - recreate the db_conn obj

        # except something else
        # raise

        # TODO - send timestamp to DB?
        # exception which is raised on diconnect from DB
        # execute an update
        # sqlalchemy.exc.OperationalError: (psycopg2.OperationalError)
        # check if conn is invalidated?
        # db_obj.db_conn.engine.execute('SELECT 1')
        # update DB with date in date table
        pass

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

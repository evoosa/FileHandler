from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from application.utils import is_file_corrupted
from application.models.newfile import NewFile


# TODO - get this out of models?
# TODO - move stuff form config here

class SQLDB():
    """Data model for the DB connection."""

    def __init__(self):
        self.db_conn = self.get_db_conn()
        self.send_heartbeats()

        # TODO - remove init func?

    def get_db_conn(self):
        """ connect to the SQL Database """
        return SQLAlchemy()

    def send_heartbeats(self):
        pass

    def check_conn_valid(self):
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
        self.db_conn.session.add(new_file)
        self.db_conn.session.commit()

    # __tablename__ =
    # id = Column(
    #     Integer,
    #     primary_key=True
    # )
    # filename = Column(
    #     String(),
    #     index=False,
    #     unique=False,
    #     nullable=False
    # )
    #
    # def __repr__(self):
    #     return '<File {}>'.format(self.filename)
    # def

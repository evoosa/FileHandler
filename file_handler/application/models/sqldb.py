from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy

from config import FILES_TABLE_NAME

Base = declarative_base()
# TODO - get this out of models?
# TODO - move stuff form config here


class SQLDB(Base):
    """Data model for the DB connection."""
    def __init__(self):
        db_conn = self.get_db_conn()
        self.send_heartbeats()

        # TODO - remove init func?

    def get_db_conn(self):
        return SQLAlchemy()

    def send_heartbeats(self):
        pass

    def check_conn_valid(self):
        pass

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
    def
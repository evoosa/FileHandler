from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class NewFile(Base):
    """Data model for files. each file has a unique ID, and a filename"""

    __tablename__ = 'files_table'
    id = Column(
        Integer,
        primary_key=True
    )
    filename = Column(
        String(),
        unique=False,
        nullable=False
    )

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from config import FILES_TABLE_NAME

Base = declarative_base()


class NewFile(Base):
    """Data model for files. each file has a unique ID, and a filename"""

    __tablename__ = FILES_TABLE_NAME
    id = Column(
        Integer,
        primary_key=True
    )
    filename = Column(
        String(),
        unique=False,
        nullable=False
    )

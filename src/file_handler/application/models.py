from application.app import db

from config import FILES_TABLE_NAME


class File(db.Model):
    """Data model for files. each file has a unique ID, and a filename"""

    __tablename__ = FILES_TABLE_NAME
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    filename = db.Column(
        db.String(),
        index=False,
        unique=False,
        nullable=False
    )

    def __repr__(self):
        return '<File {}>'.format(self.filename)

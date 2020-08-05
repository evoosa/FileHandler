from application.app import db_conn
from application.models import File


def is_file_corrupted(filename: str) -> bool:
    """
    a corrupted file is a file that ends with '_corrupted'
    :param filename: name of the file to check
    :return: True if file is corrupted, else False
    """
    if filename.endswith("_corrupted"):
        return True
    return False


def add_files_to_db(filenames: list):
    """
    Go over a list of filenames, and add the non corrupted files to the database
    :arg filenames: file names the function will go over and add to the database
    """
    for filename in filenames:
        if not is_file_corrupted(filename):
            add_file_to_db(filename)


def add_file_to_db(filename: str):
    """
    adds a single file to the database
    :param filename: name of the file to add
    """
    new_file = File(
        filename=filename
    )
    db_conn.session.add(new_file)
    db_conn.session.commit()
    print(f"{new_file} successfully created!")  # TODO - remove print!

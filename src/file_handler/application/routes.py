from flask import current_app as app
from flask import request

from application.utils import add_files_to_db


# TODO - HANDLE EXCEPTIONS PLEASE

@app.route('/', methods=['POST'])
def add_new_files():
    """
    Get the file names from the HTTP request, add the non-corrupted files to the database
    """
    filenames = request.get_json()['filenames']
    add_files_to_db(filenames)
    return 'OK'

    # TODO - return response according to success? else?
    # TODO - check if the request actually got a json and nothing else

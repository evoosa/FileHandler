from flask import current_app as app
from flask import request, Response
from flask_api import status

from application.utils import add_files_to_db


@app.route('/', methods=['POST'])
def add_new_files():
    """
    Get the file names from the HTTP request, add the non-corrupted files to the database
    """
    if request.is_json:
        request_json = request.get_json()
        try:
            filenames = request_json['filenames']
            add_files_to_db(filenames)
        except KeyError:
            return Response("missing 'filenames' field in JSON: {}", status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("missing JSON with filenames in the request", status=status.HTTP_400_BAD_REQUEST)
    return Response(f"processed {len(filenames)} new files", status=status.HTTP_200_OK)

from flask import current_app as app
from flask import request, Response
from flask_api import status

from application.app import db_obj


@app.route('/', methods=['POST'])
def add_new_files():
    """
    Get the file names from the HTTP request, add the non-corrupted files to the database
    """
    if request.is_json:
        request_json = request.get_json()
        try:
            filenames = request_json['filenames']
            db_obj.add_files_to_db(filenames)
            return Response(f"processed {len(filenames)} new files", status=status.HTTP_200_OK)
        except KeyError:
            return Response(f"missing 'filenames' field in JSON: {request_json}", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(f"The server encountered an internal error: {e}", status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(f"missing JSON with filenames in the request: {request.data}", status=status.HTTP_400_BAD_REQUEST)

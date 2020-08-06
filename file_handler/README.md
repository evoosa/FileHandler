# FileHandler
- a client sends HTTP requests containing a JSON with a list of filenames.
- a gunicorn WSGI server receives the requests.
    - it handles a max of 4 requests at once, with a timeout of 40 seconds per request.
- a Flask server will then handle the request, and add the files to a PostgreSQL database.
- only non-corrupted files are are added to the DB.
- The flask server sends heartbeats to the DB
    - It updates the the current timestamp in a heartbeats table.
  
# Requirements
 * linux OS
 * Python 3.8.5
 * the Python packages specified in requirements.txt
 * PostgreSQL 9.2.4
    * postgresql-server, postgresql-contrib, postgresql-devel
    
# Usage
in order to test the application: 
 * cd into the file_handler directory
 * run the application: `gunicorn -c gunicorn_conf.py wsgi`
 * OR, run the flask application only: `python wsgi.py`
 * in order to test the application: `python client.py`
 
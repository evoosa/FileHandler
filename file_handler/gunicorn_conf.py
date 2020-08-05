# usage: gunicorn -c gunicorn.py
bind = '127.0.0.1:8081'
workers = 4
timeout = 40
workers_class = 'sync'
proc_name = 'file_handler'
use = 'wsgi:create_app'


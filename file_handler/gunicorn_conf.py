# usage: gunicorn -c gunicorn.py wsgi
# gunicorn handles the 40 seconds timeout, and limits the concurrent requests to 4

bind = '127.0.0.1:8081'
workers = 4
timeout = 40
workers_class = 'sync'
proc_name = 'file_handler'


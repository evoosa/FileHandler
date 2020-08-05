import requests

filenames1 = {"filenames": ['10.25.196.3_traffic.19-10-23-21-00.cdr',
                            '10.25.196.3_traffic.19-10-23-21-01.cdr',
                            '10.25.196.3_traffic.19-10-23-21-02.cdr',
                            '10.25.196.3_traffic.19-10-23-21-03.cdr',
                            '10.25.196.3_traffic.19-10-23-21-04.cdr',
                            '10.25.196.3_traffic.19-10-23-21-05.cdr']}

filenames2 = {"filenames": ['malauncher.log.1',
                            'malauncher.log.10',
                            'malauncher.log.11',
                            'malauncher.log.2']}

res = requests.post('http://localhost:80', json=filenames2)

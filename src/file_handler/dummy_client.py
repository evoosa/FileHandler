import requests

res = requests.post('http://localhost:80', json={"filenames": ["file1", "file2"]})

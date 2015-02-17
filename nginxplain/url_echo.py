import os
from flask import request, Flask

app = Flask('nginxplain')
app.debug = True

url_echo = lambda: request.url + os.linesep

@app.route('/')
def root():
    return url_echo()

@app.route('/<path:path>')
def subpath(path):
    return url_echo()

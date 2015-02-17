import os

from flask import render_template

from nginxplain.url_echo import app

def root(*rel):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', *rel))

def template(path, **expansions):
    with app.test_request_context():
        return render_template(path,
                               **dict(os.environ, **expansions))+os.linesep

import fabric
from fabric.api import *

@task
def run():
    "Run the URL echo server"
    from werkzeug.serving import run_simple
    from nginxplain.url_echo import app

    run_simple('localhost', 12345, app, use_reloader=True)

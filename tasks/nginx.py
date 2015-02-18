import os

import fabric
from fabric.api import *

from tasks import root, template

def configure():
    "Write the NGINX configuration file"
    local('touch {}'.format(root('nginx.err')))
    with open(root('nginx.conf'), 'w') as fp:
        fp.write(template('nginx_t.conf', root=root()))

@task
def start():
    "Start the NGINX server"
    configure()
    local('nginx -c {}'.format(root('nginx.conf')))

@task
def stop():
    "Stop the NGINX server"
    local('nginx -s quit')

@task
def reload():
    "Reload NGINX configuration"
    configure()
    local('nginx -s reload')


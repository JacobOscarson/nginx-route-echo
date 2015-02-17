# NGINX routing echoer

## Purpose

When integrating several web apps together, it's a very good idea to
put an [nginx](http://nginx.org/) server in front of them and use it's
routing and it's `location` / `proxy_pass` combinations make them work
together like one web app. That also lets you handle all HTTPS via the
nginx instance.

Unfortunately, it's a bit difficult to configure nginx, especially if
you are new to it. This Python WSGI app exists to make it easier to
experiment with an nginx server by having an extremely simple URL
echoing app that simply echoes the
[request](http://flask.pocoo.org/docs/0.10/reqcontext/) full URL to
the calling client (I'd recommend [curl](http://curl.haxx.se/) for
this).

Using this you can experiment with your nginx configuration, send
requests to the nginx instance and see directly on your command line
what the requesting URL was interpreted as by the application server.

E.g as configured from the start, your URL echo server runs on port
12345, and your nginx server on port 5000. A request to the nginx
instance with an experimental URI will return:

     $ curl "http://localhost:5000/foo/bar?foo=bar"
     http://localhost/foo/bar?foo=bar

Here you can see that the URL echo server think's it's name is simply
`'localhost'`, and that the entire URI have been transmitted
correctly.

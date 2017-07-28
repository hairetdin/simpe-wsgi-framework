#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server
import re
from urls import urls
from views import *


class Server:

    def __init__(self):
        self.host = 'localhost'
        self.port = 8050

    def __call__(self, environ, start_response):
        path = environ.get('PATH_INFO', '').lstrip('/')
        for url, callback in urls:
            match = re.search(url, path)
            if match is not None:
                environ['myapp.url_args'] = match.groupdict()
                if type(callback) is str:
                    callback = eval(callback)
                response = callback(environ)
                if response[0] == 'response_ok':
                    status = '200 OK'
                    headers = [('Content-type', 'text/html')]
                    start_response(status, headers)
                    return response[1]
                if response[0] == 'redirect':
                    #redirect to anouther page
                    status = '302 Found'
                    start_response(status ,[('Location',response[1])])
                    return []
        status = '400 NOT FOUND'
        headers = [('Content-type', 'text/html')]
        start_response(status, headers)
        return not_found()

    def run(self):
        wsgi_server = make_server(self.host, self.port, self)
        print('WSGI serving on {host}:{port}'.format(host=self.host, port=self.port))
        wsgi_server.serve_forever()


if __name__ == '__main__':
    server = Server()
    server.run()

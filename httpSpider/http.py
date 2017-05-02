# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server
from hello import *

httpd = make_server('',1234,application)
print('Server HTTP on port 1234...')
httpd.serve_forever()
#!/usr/local/bin/python3

import ssl

import hyper
from hyper import HTTPConnection

hyper.tls._context = hyper.tls.init_context()
hyper.tls._context.check_hostname = False
hyper.tls._context.verify_mode = ssl.CERT_NONE

conn = HTTPConnection('localhost:4443', secure=True)
conn.request('GET', '/')
resp = conn.get_response()

print(resp.read())

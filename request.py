#!/usr/local/bin/python3


import ssl

import hyper
from hyper import HTTPConnection

hyper.tls._context = hyper.tls.init_context()
hyper.tls._context.check_hostname = False
hyper.tls._context.verify_mode = ssl.CERT_NONE

headers = {":method": "GET", "accept-encoding": "gzip, deflate, br", ":scheme": "https", "upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:52.0) Gecko/20100101 Firefox/52.0", "accept-language": "en-US,en;q=0.5", ":authority": "localhost:4443", ":path": "/", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
conn = HTTPConnection('localhost:4443', secure=True)
conn.request('GET', '/',  headers=headers)
resp = conn.get_response()

print(resp.read())

#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: authenticate

:Synopsis:

:Author:
    servilla
  
:Created:
    8/7/16
"""

import base64
import requests
import sys


def main(argv):

    base_url = argv[0]
    creds = argv[1].encode('utf-8')
    service = '/package'
    path = base_url + service

    b64_creds = base64.b64encode(creds)
    authn_header = {'Authorization': 'Basic ' + b64_creds.decode('utf-8')}

    r = requests.get(path, headers=authn_header)

    print('Response: {0}'.format(r.status_code))
    headers = r.headers
    for header in headers:
        print('{0}: {1}'.format(header, headers[header]))

    b64_auth_token = headers['Set-Cookie'].lstrip('auth-token=')
    print(b64_auth_token)
    auth_token = base64.b64decode(b64_auth_token.encode('utf-8')).decode('utf-8')
    print(auth_token)

    auth_token_cookie = dict(auth_token=b64_auth_token)

    r = requests.get(path, cookies=auth_token_cookie)

    print('Response: {0}'.format(r.status_code))
    headers = r.headers
    for header in headers:
        print('{0}: {1}'.format(header, headers[header]))

    return 0


if __name__ == "__main__":
    main(sys.argv[1:])
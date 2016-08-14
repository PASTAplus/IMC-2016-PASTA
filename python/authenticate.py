#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: authenticate

:Synopsis:

:Author:
    servilla
  
:Created:
    8/7/16
"""

import requests
import sys
from base64 import b64decode, b64encode


def main(argv):

    base_url = argv[0]
    creds = argv[1]
    service = '/package'
    path = base_url + service

    b64_creds = b64encode(creds.encode('utf-8')).decode('utf-8')
    authn_header = {'Authorization': 'Basic ' + b64_creds}

    r = requests.get(path, headers=authn_header)

    print('Response: {0}'.format(r.status_code))
    headers = r.headers
    for header in headers:
        print('{0}: {1}'.format(header, headers[header]))

    if 'Set-Cookie' in headers:

        auth_token_cookie = headers['Set-Cookie']
        print('\nCookie: {0}'.format(auth_token_cookie))
        cookie_parts = auth_token_cookie.lstrip('auth-token=').split(';')
        b64_auth_token = cookie_parts[0].split('-')
        auth_token = b64decode(b64_auth_token[0].encode('utf-8')).decode('utf-8')
        print('Auth-token: {0}\n'.format(auth_token))

        cookie = dict(auth_token=auth_token_cookie)

        r = requests.get(path, cookies=cookie)

        print('Response: {0}'.format(r.status_code))
        headers = r.headers
        for header in headers:
            print('{0}: {1}'.format(header, headers[header]))
    else:
        print('No Cookies in response!')

    return 0


if __name__ == "__main__":
    main(sys.argv[1:])
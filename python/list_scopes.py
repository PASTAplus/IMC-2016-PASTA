#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: list_scopes

:Synopsis:

:Author:
    servilla
  
:Created:
    8/4/16
"""

import requests
import sys


def main(argv):

    base_url = argv[0]
    service = '/package/eml'
    path = base_url + service

    r = requests.get(path)

    headers = r.headers
    for header in headers:
        print('{0}: {1}'.format(header, headers[header]))

    scopes = r.text.split('\n')
    for scope in scopes:
        print('{0}'.format(scope))

    return 0


if __name__ == "__main__":
    main(sys.argv[1:])
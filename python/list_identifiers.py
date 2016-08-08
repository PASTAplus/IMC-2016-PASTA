#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: list_identifiers

:Synopsis:

:Author:
    servilla
  
:Created:
    8/6/16
"""

import requests
import sys


def main(argv):

    base_url = argv[0]
    scope = argv[1]
    service = '/package/eml/'
    path = base_url + service + scope

    r = requests.get(path)

    headers = r.headers
    for header in headers:
        print('{0}: {1}'.format(header, headers[header]))

    identifiers = r.text.split('\n')
    for identifier in identifiers:
        print('{0}.{1}'.format(scope, identifier))

    return 0


if __name__ == "__main__":
    main(sys.argv[1:])
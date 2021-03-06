#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: list_revisions

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
    scope_identifier = argv[1]
    service = '/package/eml/'
    path = base_url + service + scope_identifier.replace('.', '/')

    r = requests.get(path)

    print('Response: {0}'.format(r.status_code))
    headers = r.headers
    for header in headers:
        print('{0}: {1}'.format(header, headers[header]))

    revisions = r.text.split('\n')
    for revision in revisions:
        print('{0}.{1}'.format(scope_identifier, revision))

    return 0


if __name__ == "__main__":
    main(sys.argv[1:])

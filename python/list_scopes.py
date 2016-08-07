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

    r = requests.get(base_url + service)

    scopes = r.text.split('\n')
    for scope in scopes:
        print('{0}'.format(scope))

    return 0


if __name__ == "__main__":
    main(sys.argv[1:])
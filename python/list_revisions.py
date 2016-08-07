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

    r = requests.get(base_url + service + scope_identifier.replace('.', '/'))

    revisions = r.text.split('\n')
    for revision in revisions:
        print('{0}.{1}'.format(scope_identifier, revision))

    return 0


if __name__ == "__main__":
    main(sys.argv[1:])

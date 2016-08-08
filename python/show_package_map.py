#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: show_package_map

:Synopsis:

:Author:
    servilla
  
:Created:
    8/7/16
"""

import requests
import sys
import getopt


def main(argv):

    base_url = argv[0]
    package_id = argv[1]
    service = '/package/eml/'
    path = base_url + service + package_id.replace('.', '/')

    r = requests.get(path)

    headers = r.headers
    for header in headers:
        print('{0}: {1}'.format(header, headers[header]))

    resources = r.text.split('\n')
    for resource in resources:
        print('{0}'.format(resource))

    return 0


if __name__ == "__main__":
    main(sys.argv[1:])

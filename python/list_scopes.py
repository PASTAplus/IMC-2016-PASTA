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
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
    datefmt='%Y-%m-%d% H:%M:%S%z')
logging.getLogger('').setLevel(logging.WARN)
logger = logging.getLogger('list_scopes')



def main():
    base_url = 'https://pasta.lternet.edu'
    service = '/package/eml'


    r = requests.get(base_url + service)

    scopes = r.text.split('/n')
    for scope in scopes:
        print('{0}'.format(scope))

    return 0


if __name__ == "__main__":
    main()
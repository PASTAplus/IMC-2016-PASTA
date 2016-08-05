#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: scopes

:Synopsis:

:Author:
    servilla
  
:Created:
    7/24/16
"""

import requests
# import logging
#
# logging.basicConfig(format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
#                     datefmt='%Y-%m-%d% H:%M:%S%z')
# logging.getLogger('').setLevel(logging.WARN)
# logger = logging.getLogger('scopes')


class Scopes(object):

    def __init__(self):
        scopes_url = 'https://pasta.lternet.edu/package/eml'
        self.r = requests.get(scopes_url)


    def get_headers(self):
        return self.r.headers

    def get_scopes(self):
        scopes = self.r.text.split('\n')
        return scopes


def main():
    return 0


if __name__ == "__main__":
    main()
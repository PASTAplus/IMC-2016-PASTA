#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: identifiers

:Synopsis:

:Author:
    servilla
  
:Created:
    7/24/16
"""

# import logging
#
# logging.basicConfig(format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
#                     datefmt='%Y-%m-%d% H:%M:%S%z')
# logging.getLogger('').setLevel(logging.WARN)
# logger = logging.getLogger('identifiers')

import requests

class Identifiers(object):

    def __init__(self, scope=None):
        identifiers_url = 'https://pasta.lternet.edu/package/eml/' + scope
        self.r = requests.get(identifiers_url)

    def get_headers(self):
        return self.r.headers

    def get_identifiers(self):
        identifiers = self.r.text.split('\n')
        return identifiers



def main():
    return 0


if __name__ == "__main__":
    main()
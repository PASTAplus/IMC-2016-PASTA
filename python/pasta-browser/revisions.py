#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: revisions

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
# logger = logging.getLogger('revisions')

import requests

class Revisions(object):

    def __init__(self, base_url= None, scope=None, identifier=None):
        service = '/package/eml/'
        revisions_url = base_url + service + scope + '/' + identifier
        self.r = requests.get(revisions_url)

    def get_headers(self):
        return self.r.headers

    def get_revisions(self):
        revisions = self.r.text.split('\n')
        return revisions


def main():
    return 0


if __name__ == "__main__":
    main()
#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: data_package

:Synopsis:

:Author:
    servilla
  
:Created:
    8/8/16
"""


import requests

# import logging
#
# logging.basicConfig(format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
#                     datefmt='%Y-%m-%d% H:%M:%S%z')
# logging.getLogger('').setLevel(logging.WARN)
# logger = logging.getLogger('data_package')


class Package(object):

    def __init__(self,  base_url=None, scope=None, identifier=None, revision=None):
        service = '/package/eml/'
        package_url = base_url + service + scope + '/' + identifier + '/' + revision
        self.r = requests.get(package_url)


    def get_headers(self):
        return self.r.headers


    def get_resources(self):
        resources = self.r.text.strip().split('\n')
        return resources


def main():
    return 0


if __name__ == "__main__":
    main()
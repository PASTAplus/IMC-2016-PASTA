#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: evaluate

:Synopsis:

:Author:
    servilla
  
:Created:
    8/14/16
"""

import requests
import sys
import time

def main(argv):


    base_url = argv[0]
    eml_path = argv[1]
    service = '/package'
    path = base_url + service

    eml = open(eml_path, 'r').read().encode('utf-8')

    r = requests.post(path + '/evaluate/eml', data=eml)
    if r.status_code == 202: # ACCEPTED
        transaction_id = r.text.strip()
    else:
        return 1

    done = False
    snooze = 1
    total_time = 0
    max_time = 5

    while not done:
        time.sleep(snooze)
        total_time += snooze
        print('Total time: {0}'.format(total_time))

        quality_report = requests.get(path + '/evaluate/report/eml/' + transaction_id)
        if quality_report.status_code == 200: # OK
            done = True
            print('{0}'.format(quality_report.text))

        error = requests.get(path + '/error/eml/' + transaction_id)
        if error.status_code == 200: # OK
            done = True
            print('{0}'.format(error.text))

        if total_time >= max_time:
            done = True
            print("Fiddle stix...")

    return 0


if __name__ == "__main__":
    main(sys.argv[1:])
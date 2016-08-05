#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: browser

:Synopsis:

:Author:
    servilla

:Created:
    7/24/16
"""

# import logging

from flask import Flask
from flask import render_template
from flask import url_for
from flask_bootstrap import Bootstrap

from identifiers import Identifiers
from revisions import Revisions
from scopes import Scopes

# logging.basicConfig(format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
#                     datefmt='%Y-%m-%d% H:%M:%S%z')
# logging.getLogger('').setLevel(logging.WARN)
# logger = logging.getLogger('browser')

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    scopes_url = url_for('scopes')
    return render_template('index.html', scopes_url=scopes_url)


@app.route('/eml')
def scopes():
    scopes = Scopes().get_scopes()
    return render_template('scopes.html', scopes=scopes)


@app.route('/eml/<scope>')
def identifiers(scope):
    identifiers = Identifiers(scope=scope).get_identifiers()
    return render_template('identifiers.html', scope=scope,
                           identifiers=identifiers)


@app.route('/eml/<scope>/<identifier>')
def revisions(scope, identifier):
    revisions = Revisions(scope=scope, identifier=identifier).get_revisions()
    return render_template('revisions.html', scope=scope, identifier=identifier,
                           revisions=revisions)


if __name__ == '__main__':
    app.run(debug=True)
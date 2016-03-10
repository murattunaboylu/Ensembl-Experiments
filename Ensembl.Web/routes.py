"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime
import requests, sys
import random
 

@route('/')
@route('/home')
@view('index')
def home():
    v = version()

    """Renders the home page."""
    return dict(
        year=datetime.now().year,
        version = v
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Contact details',
        year=datetime.now().year
    )


@route('/ping')
@view('ping')
def ping():
    """Renders the ping page."""
    if is_live() == "{'ping': 1}":
        m = 'LIVE'
    else:
        m = 'OFFLINE'

    return dict(
        title='Ping',
        message='Ensembl is ' + m,
        year=datetime.now().year
    )

@route('/gene')
@view('gene')
def gene():
    gene = get_gene()

    return dict(
        title='ENSG00000157764',
        message=gene,
        year=datetime.now().year
    )


def get_gene():
    """Returns a random gene information from Ensembl"""
    server = "http://rest.ensembl.org"
    ext = "/lookup/id/ENSG00000157764?"
 
    r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
 
    if not r.ok:
      r.raise_for_status()
      sys.exit()
 
    decoded = r.json()
    print(repr(decoded))
    return repr(decoded)


def is_live():
    """Returns true if Ensembl is live"""
    server = "http://rest.ensembl.org"
    ext = "/info/ping?"
 
    r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
 
    if not r.ok:
        r.raise_for_status()
        sys.exit()
 
    decoded = r.json()
    print(repr(decoded))
    return repr(decoded)


def version():
    """Returns Ensembl REST version"""
    server = "http://rest.ensembl.org"
    ext = "/info/software?"
 
    r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
 
    if not r.ok:
      r.raise_for_status()
      sys.exit()
 
    decoded = r.json()
    print(repr(decoded))
    return repr(decoded)


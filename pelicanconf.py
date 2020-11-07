#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import sys 
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from jinja_filters import sidebar

AUTHOR = 'Maria Popova'
SITENAME = 'Pelican Experiment'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'twenty-pelican-html5up'

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

JINJA_FILTERS = {'sidebar': sidebar}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
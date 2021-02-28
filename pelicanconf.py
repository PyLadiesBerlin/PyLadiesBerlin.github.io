#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'PyLadies Berlin'
SITENAME = 'PyLadies Berlin'
SITEDESCRIPTION = 'PyLadies Berlin is a local chapter of PyLadies, an international mentorship group with a focus on helping more women become active participants and leaders in the Python open-source community.'
SITEURL = 'http://localhost:8000'

# plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['i18n_subsites', 'tipue_search']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# theme and theme localization
THEME = 'pelican-fh5co-marble'
I18N_GETTEXT_LOCALEDIR = 'pelican-fh5co-marble/locale/'
I18N_GETTEXT_DOMAIN = 'messages'
I18N_GETTEXT_NEWSTYLE = True
TIMEZONE = 'Europe/Zurich'
DEFAULT_DATE_FORMAT = '%a, %d %b %Y'
I18N_TEMPLATES_LANG = 'en_US'
DEFAULT_LANG = 'en'
LOCALE = 'en_US'

# content paths
PATH = 'content'
PAGE_PATHS = ['pages/en']
ARTICLE_PATHS = ['blog/en']

# i18n
I18N_SUBSITES = {
  'de': {
    'PAGE_PATHS': ['pages/de'],
    'ARTICLE_PATHS': ['blog/de'],
    'LOCALE': 'de_DE'
  }
}

# logo path, needs to be stored in PATH Setting
LOGO = '/images/logo.png'

# special content
HERO = [
  {
    'image': '/images/hero/background-1.jpg',
    # for multilanguage support, create a simple dict
    'title': {
      'en':'Some special content',
      'de': 'Spezieller Inhalt'
    },
    'text': {
      'en': 'Any special content you want to tease here',
      'de': 'Jeglicher spezieller Inhalt den Sie hier bewerben möchten'
    },
    'links': [
      {
        'icon': 'icon-code',
        'url': 'https://github.com/claudio-walser/pelican-fh5co-marble',
        'text': 'Github'
      }
    ]
  }, {
    'image': '/images/hero/background-2.jpg',
    # keep it a string if you dont need multiple languages
    'title': 'Uh, special too',
    # keep it a string if you dont need multiple languages
    'text': 'Keep hero.text and hero.title a string if you dont need multilanguage.',
    'links': []
  }, {
    'image': '/images/hero/background-3.jpg',
    'title': 'No Blogroll yet',
    'text': 'Because of space issues in the man-nav, i didnt implemented Blogroll links yet.',
    'links': []
  }, {
    'image': '/images/hero/background-4.jpg',
    'title': 'Ads missing as well',
    'text': 'And since i hate any ads, this is not implemented as well',
    'links': []
  }
]

# Social widget
SOCIAL = (
  ('Github', 'https://github.com/PyLadiesBerlin'),
  ('Facebook', 'https://www.facebook.com/PyLadiesBerlin'),
  ('Twitter', 'https://twitter.com/PyLadiesBer')
)

ABOUT = {
  'image': '/images/about/about.jpeg',
  'mail': 'berlin@pyladies.com',
  # keep it a string if you dont need multiple languages
  'text': {
    'en': 'Learn more about PyLadies Berlin or just drop a message.',
    'de': 'Ihr wollt mehr erfahren über PyLadies Berlin, dann hinterlasst uns eine Nachricht'
  },
  'link': 'contact.html',
  # the address is also taken for google maps
  'address': 'Berlin, Germany',
  #'email': 'berlin@pyladies.com'
}

# navigation and homepage options
DISPLAY_PAGES_ON_MENU = True
DISPLAY_PAGES_ON_HOME = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True
PAGE_ORDER_BY = 'order'

MENUITEMS = [
  ('Archive', 'archives.html'),
  ('Contact', 'contact.html')
]

DIRECT_TEMPLATES = [
  'index',
  'tags',
  'categories',
  'authors',
  'archives',
  'search', # needed for tipue_search plugin
  'contact' # needed for the contact form
]

# setup disqus
DISQUS_SHORTNAME = 'gitcd-dev'
DISQUS_ON_PAGES = False # if true its just displayed on every static page, like this you can still enable it per page

# setup google maps
GOOGLE_MAPS_KEY = 'AIzaSyCefOgb1ZWqYtj7raVSmN4PL2WkTrc-KyA'

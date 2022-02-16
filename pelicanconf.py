#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'PyLadies Berlin'
SITENAME = 'PyLadies Berlin'
SITEDESCRIPTION = 'PyLadies Berlin is a local chapter of PyLadies, an international mentorship group with a focus on helping more women become active participants and leaders in the Python open-source community.'
SITEURL = ''

# plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['i18n_subsites']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# theme and theme localization
THEME = 'pelican-fh5co-marble'
I18N_GETTEXT_LOCALEDIR = 'pelican-fh5co-marble/locale/'
I18N_GETTEXT_DOMAIN = 'messages'
I18N_GETTEXT_NEWSTYLE = True
TIMEZONE = 'Europe/Berlin'
DEFAULT_DATE_FORMAT = '%a, %d %b %Y'
I18N_TEMPLATES_LANG = 'en_US'
DEFAULT_LANG = 'en'
LOCALE = 'en_US'

# content paths
PATH = 'content'
PAGE_PATHS = ['pages/en']
ARTICLE_PATHS = ['blog/en']

# extra static
RELATIVE_URLS = False
STATIC_PATHS = ['static', 'images']
EXTRA_PATH_METADATA = {
    'static/favicon.ico': {'path': 'favicon.ico'},
    }

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

# home page rotating image 
HERO = [
  {
    'image': '/images/hero/background-1.jpg',
    # for multilanguage support, create a simple dict
    'title': {
      'en':'PyLadies Berlin on YouTube',
      'de': 'PyLadies Berlin in YouTube'
    },
    'text': {
      'en': 'Find recent recodings of workshops and meetups on our YouTube Channel.',
      'de': 'Aktuelle Videos unserer Workshops und Meetups findest du auf unserem YouTube Channel.'
    },
    'links': [
      {
        'icon': 'icon-code',
        'url': 'https://www.youtube.com/user/PyLadiesBerlin',
        'text': 'YouTube'
      }
    ]
  }, {
    'image': '/images/hero/background-2.jpg',
    # keep it a string if you dont need multiple languages
    'title': 'This is PyLadies Berlin',
    'text': {
      'en': 'Get up to date about PyLadies menthorship, the organizer team and our commitment to the Python community.',
      'de': 'Infos über das PyLadies Mentorship Program, das Organizer-Team und unseren Einsatz für die Python Community.',
    },
    'links': [
      {
        'url': '/pages/about.html',
        'text': 'About'
        }
      ]
    }, 
    
    {
    'image': '/images/hero/background-3.jpg',
    'title': 'Meetups',
    'text': {
      'en': 'Meet the PyLadies community, learn something new about Python and become an active member.',
      'de': 'Lerne die PyLadies Community kennen, lerne etwas neues über Python und werde ein aktives Mitglied.'
    },
    'links': [
      {
        'url': '/pages/meetups.html',
        'text': 'Meetups'
      }
    ]
  }, {
    'image': '/images/hero/background-4.jpg',
    'title': 'Python learning resources',
    'text': {
      'eng': 'Find a list of amazing resources for your Python learning journey.',
      'de': 'Hier findest du eine Liste von Lernmaterial um mehr übers Programmiernen mit Python zu lernen.'
    },
    'links': [
      {
        'url': '/pages/resources.html',
        'text': 'Learning resources'
      }
    ]
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
  'slack': {
    'image': '/images/about/slack-logo-small.png',
    'link': 'https://slackin.pyladies.com/',
    'text': 'Join us on slack in #city-berlin channel!'
  }
}

# navigation and homepage options
DISPLAY_PAGES_ON_MENU = True
DISPLAY_PAGES_ON_HOME = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True
PAGE_ORDER_BY = 'order'

MENUITEMS = [
  # ('Archive', 'archives.html'),
  ('Contact', 'contact.html')
]

DIRECT_TEMPLATES = [
  'index',
  'tags',
  # 'categories',
  # 'authors',
  'archives',
  'contact' # needed for the contact form
]


# # setup disqus
# DISQUS_SHORTNAME = 'gitcd-dev'
# DISQUS_ON_PAGES = False # if true its just displayed on every static page, like this you can still enable it per page

# # setup google maps
# GOOGLE_MAPS_KEY = 'AIzaSyCefOgb1ZWqYtj7raVSmN4PL2WkTrc-KyA'

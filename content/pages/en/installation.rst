Installation
############

:order: 2
:date: 2018-01-25 08:46
:icon: icon-code-outline
:summary: How to install this theme.
:lang: en
:slug: installation
:use_disqus: true

Install and use this theme
~~~~~~~~~~~~~~~~~~~~~~~~~~


Installation
------------
The installation is as easy as a git clone. Give it a try.

.. code-block:: bash

    git clone https://github.com/claudio-walser/pelican-fh5co-marble.git



Usage
-----

I am pretty sure you already know how to use a pelican theme, still, here are the instructions.

By path in your pelicanconf.py

.. code-block:: python
    
    THEME = '/path/to/theme/pelican-fh5co-marble'


Install it using pelican-theme
------------------------------

Of course you can install it using the pelican-themes cli tool, which is maybe more convinient for you.

.. code-block:: bash
    
    pelican-themes -i /path/to/theme/pelican-fh5co-marble

Afterwards you can use it by just configuring its name in pelicanconf.py

.. code-block:: python
    
    THEME = 'pelican-fh5co-marble'

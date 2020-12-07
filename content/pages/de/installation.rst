Installation
#################

:order: 2
:date: 2018-01-25 08:46
:icon: icon-code-outline
:summary: Wie Sie diese Theme installieren.
:lang: de
:slug: installation
:use_disqus: true

Installation und Anwendung dieser Theme
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Installation
------------
Die Installation ist so einfach wie ein git clone. Versuchen Sie es.

.. code-block:: bash

    git clone https://github.com/claudio-walser/pelican-fh5co-marble.git



Anwendung
---------

Ich bin mir ziemlich sicher Sie wissen wie man eine Pelican Theme verwendet, trotzdem sind hier die Instruktionen.


Mittels dem Pfad in Ihrer pelicanconf.py

.. code-block:: python
    
    THEME = '/path/to/theme/pelican-fh5co-marble'


Installieren mithilfe von pelican-theme
---------------------------------------

Natürlich können Sie die Theme auch mit dem pelican-themes Kommandozeilen Programm installieren, vielleicht ist das für Sie angenehmer.

.. code-block:: bash
    
    pelican-themes -i /path/to/theme/pelican-fh5co-marble

Anschliessend können Sie die Theme ganz einfach mit dem Namen in Ihrer pelicanconf.py verwenden.

.. code-block:: python
    
    THEME = 'pelican-fh5co-marble'

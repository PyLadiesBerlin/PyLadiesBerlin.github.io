Title: My super title
Date: 2010-12-03 10:20
Modified: 2010-12-05 19:30
Category: Python
Tags: pelican, publishing
Slug: my-super-post
Authors: Alexis Metaireau, Conan Doyle
Summary: Short version for index and feeds

Build a pelican website:

* Follow pelican docu quickstart - https://docs.getpelican.com/en/stable/quickstart.html
* Add an md
* Check preview with reload
* pelican --autoreload --listen
* 127.0.0.1:8000
* Add an rst file
* Add a photo add static content in the docu (do NOT expect resizing)
* Add code in the rst
* Publish website, just check the output folder
* Clone and install a theme [FIND an easy theme] (ours was complex - https://github.com/frankV/twenty-pelican-html5up/tree/53cc173993b358690e8ea00de02154547d5dfdca)
    # pelican-themes --install ~/Dev/Python/pelican-themes/notmyidea-cms --verbose
    - add theme in settings
    - do jinja filter
    - hardcode theme folder 
    - copy over collect static ???
    # pelican content -s pelicanconf.py -t twenty-pelican-html5up
    # invoke collectstatic
    # pelican --listen
* pip install invoke # try the tasks


![Alt Text]({static}/images/sea.jpg)

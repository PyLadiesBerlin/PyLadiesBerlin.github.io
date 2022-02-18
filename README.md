# Pyladies Berlin website

Pyladies Berlin website is using [Pelican](https://docs.getpelican.com/en/latest/index.html) to generate HTML from articles in markdown. 

It is deployed in github pages under https://berlin.pyladies.com domain. 

## Inspiration
This website is inspired by https://elections.pyladies.com/ and is using the same base pelican theme. The code of that website can be found https://github.com/pyladies/pyladies-elections-website

## Structure

    |__ content
     __ pelican-plugins
     __ pelican-fh5co-marble # theme
     __ pelicanconf.py # settings
     __ publishconf.py # deployment settings

### Content
Website content in restrucured text articles and images that are getting rendered to the main HTML website pages. 

### Pelican-plugins
Submodule pointing to pelican plugins repo. 

> **_NOTE:_** Plugins are gradually moved to pip dependencies. If `i18n_subsites` moves over this dependency will not be necessary any more.

### Pelican-fh5co-marble
Pelican theme. It points to a [fork]|(https://github.com/PyLadiesBerlin/)pelican-fh5co-marble of Pyladies Berlin of the base theme. 

### pelicanconf.py
Here are all the necessary settings for Pelican. The upper case variables
are passed when rendering to all templates of the theme.

### publishconf.py

Settings used by Github Action  to build the website (see .[.github/workflows/deploy-dh-pages.yml](.github/workflows/deploy-dh-pages.yml))
# Install

> :warning: Follow the command below to get the repo with the submodules otherwise it will not render correctly!


## Clone repo and submodules

    git clone --recurse-submodules git@github.com:PyLadiesBerlin/website.git

For git < 2.11 use:

    git clone --recursive git@github.com:PyLadiesBerlin/website.git

## Update submodules

Use this command if the theme repository or the plugin in used has been updated. 

    git submodule update

## Setup a python environment

    python3 -m venv .env  # use python if it is a python > 3
    source .env/bin/activate

## Install requirements

    pip install -r requirements.txt

## Build and preview content

    pelican content
    pelican --listen

or for faster changes use:

    pelican --autoreload --listen

Open http://localhost:8000 in your browser.

# Contribute

## Add content

### Pages
New pages will show up automatically in the left menu.
* Page content in [reStructuredText](https://docutils.sourceforge.io/rst.html) format under content/pages in both languages.
* Images like in meetups.rst, with `float-left` and `float-right` possibilities.
* Title icons can be found in https://icomoon.io/#preview-free and then checked in the pelican-fh5co-marble/static/css/icomoon.css to find the exact icon name.

### Home page
This page is produced by the theme, the top part is controlled by pelicanconf `HERO` variable.

## Change looks

Consider reading about [Pelican themes](https://docs.getpelican.com/en/latest/themes.html). The used theme is under `pelican-fh5co-marble` submodule. Locally this appears as a directory and development can be done directly from here. Kind of, follow the steps below:
* Make changes in the theme folder locally to see the result
* Commit the changes to the upstream submodule repo
* Update this repository to point to the latest theme commit

# Troubleshooting

In case your plugin directories is empty, check with:

```
ls pelican-plugin
```

Try to download the git repository again with the following command:

```
git submodule update --init --recursive
```

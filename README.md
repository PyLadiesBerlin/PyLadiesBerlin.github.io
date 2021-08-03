# Installation

To reproduce the website in your local machine follow these steps.

## Clone repo and submodules

    git clone --recurse-submodules git@github.com:PyLadiesBerlin/website.git

For git < 2.11 use:

    git clone --recursive git@github.com:PyLadiesBerlin/website.git

## Update submodules

    git submodule update

## Setup an environment

### Using python

    python3 -m venv .env  # use python if it is a python > 3
    source .env/bin/activate

#### Install requirements

    pip install -r requirements.txt

### Using conda or mamba

With conda:

    conda create -n pyladies
    conda install -c conda-forge pelican markdown beautifulsoup4

Or mamba:

    conda create -n pyladies
    mamba install -c conda-forge pelican markdown beautifulsoup4

## Build and preview content

Access the `content` directory

    cd content

Build the website and listen to changes:

    pelican
    pelican --listen

or for faster changes use:

    pelican --autoreload --listen

Open http://localhost:8000 in your browser.

# How this repository is structured

The main website structure, its menus and pictures are controlled by `pelicanconf.py`.

All static files mentioned there have to be under `content` directory.

## Icons

Check https://icomoon.io/#preview-free and then in the pelican-fh5co-marble/static/css/icomoon.css to find the exact icon name.

## Content

Contains the content of the pages, its images under the `images` directory and the text sources under `pages`.

# Asking for help

If you're stuck, don't hesitate to ask for help in the [PyLadies Berlin channel](https://slackin.pyladies.com)!

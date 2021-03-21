# Install

## Clone repo and submodules

    git clone --recurse-submodules git@github.com:PyLadiesBerlin/website.git

For git < 2.11 use:

    git clone --recursive git@github.com:PyLadiesBerlin/website.git

## Update submodules

    git submodule update

## Setup a python environment

    python3 -m venv .evn  # use python if it is a python > 3
    source .env/bin/activate

## Install requirements

    pip install -r requirements.txt

## Build and preview content

    pelican content
    pelican --listen

or for faster changes use:

    pelican --autoreload --listen

Open http://localhost:8000 in your browser.


# Develop

Main website structure and menus and pictures are controlled by `pelicanconf.py`. All static files mentioned there have to be under `content` directory.

## Content

Are the articles under each 

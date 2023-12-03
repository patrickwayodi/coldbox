Commands for Installing Django
==============================

Below are some commands for installing Django.


## If you don't have Python, install it.
sudo apt-get update

sudo apt-get install python3


## Create a virtual environment 
python3 -m venv ~/virtualenvs/coldbox


## Activate the virtualenv
source ~/virtualenvs/coldbox/bin/activate


## Install Coldbox's dependencies.
mkdir ~/pyrepo/

cd coldbox/src

pip download --dest=/home/treetop/pyrepo pip wheel

pip install --upgrade --no-index --find-links=/home/treetop/pyrepo pip wheel

pip download --dest=/home/treetop/pyrepo Django==4.2.7

pip install --upgrade --no-index --find-links=/home/treetop/pyrepo Django==4.2.7


## Create the Django project 
django-admin startproject core .


## Run the project.
python manage.py runserver

Open http://127.0.0.1:8000 on your browser.

Commands for Installing Django
==============================

Below are some commands for installing Django.


## If you don't have Python, install it.
sudo apt-get update

sudo apt-get install python


## Create a virtual environment 
python3 -m venv ~/virtualenvs/grokmixdev


## Activate the virtualenv
source ~/virtualenvs/grokmixdev/bin/activate


## Install Coldbox's dependencies.
mkdir ~/pyrepo/

cd coldbox/src

pip download --dest=/home/treetop/pyrepo pip wheel

pip install --upgrade --no-index --find-links=/home/treetop/pyrepo pip wheel

pip download --dest=/home/treetop/pyrepo -r requirements/dev.txt

pip install --upgrade --no-index --find-links=/home/treetop/pyrepo -r requirements/dev.txt


## Create the Django project 
django-admin startproject core .


## Run the project.
python manage.py runserver

Open http://127.0.0.1:8000 on your browser.
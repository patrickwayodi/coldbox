Commands for Installing Coldbox
===============================


Below are some commands for installing Coldbox.


## Prepare a directory to use for the installation

* mkdir ~/apps/coldbox/exp

* cd ~/apps/coldbox/exp


## Clone the repository

* git clone https://github.com/patrickwayodi/coldbox.git


## If you don't have Python, install it.

* sudo apt-get update

* sudo apt-get install python3


## Create a PYthon virtual environment and install Coldbox's dependencies

* python3 -m venv ~/virtualenvs/coldbox

* source ~/virtualenvs/coldbox/bin/activate

* pip install --upgrade pip wheel

* cd coldbox/src

* pip install --upgrade -r requirements.txt


## Propagate the changes made to the database models into your database schema

* python manage.py makemigrations

* python manage.py migrate


## Create the admin account

* python manage.py createsuperuser


## Load data from the Django Fixtures

* python manage.py loaddata accounts.json

* python manage.py loaddata assets.json

* python manage.py loaddata gatepasses.json


## Run the tests

* python manage.py test apps.accounts.tests

* python manage.py test apps.assets.tests

* python manage.py test apps.gatepasses.tests


## Run the project

* python manage.py runserver

* Open http://127.0.0.1:8000 on your browser.


## References

* django/docs/howto/initial-data.html#provide-data-with-fixtures

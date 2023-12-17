How to Install Coldbox
======================


Below are some commands for installing Coldbox.


## References

* https://docs.djangoproject.com/en/4.2/howto/initial-data/#provide-data-with-fixtures


## Prepare a working directory

* Prepare a directory to use for the installation
      mkdir ~/workspace
      cd ~/workspace


## Clone the repository

* Create a clone of the repository using Git.
      git clone https://github.com/patrickwayodi/coldbox.git
      cd coldbox


## Install Python

* Install Python if you do not already have it.
      sudo apt-get update
      sudo apt-get install python3


## Create a Python virtual environment and install Coldbox's dependencies

* It's usually advisable to install all dependencies inside a virtual environment.
      python3 -m venv ~/virtualenvs/coldbox
      source ~/virtualenvs/coldbox/bin/activate
      pip install --upgrade pip wheel
      pip install --upgrade -r src/requirements.txt


## Initialize the Database

* Propagate the changes made to the database models into your database schema
      cd src
      python manage.py makemigrations
      python manage.py migrate


## Create the admin account

* Create the main administrator account.
      python manage.py createsuperuser


## Load data from the Django Fixtures

* Load the default data from the django fixtures.
      python manage.py loaddata accounts.json
      python manage.py loaddata assets.json
      python manage.py loaddata gatepasses.json


## Run the tests

* Run all the tests.
      python manage.py test apps.accounts.tests
      python manage.py test apps.assets.tests
      python manage.py test apps.gatepasses.tests


## Run the project

* Run the project and access it using your browser.
      python manage.py runserver
* Open http://127.0.0.1:8000 on your browser.
* The default users are "janedoe", "johndoe", and "demo". Their password is "django123".

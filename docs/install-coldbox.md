Commands for Installing Coldbox
===============================


Below are some commands for installing Coldbox.

It's assumed that the user is running the Debian GNU/Linux operating system and that
their username is "treetop". Make the necessary alterations if you're using a different
operating system.


## Prepare a directory to use for the installation

mkdir ~/apps/coldbox/exp

cd ~/apps/coldbox/exp


## Clone the repository

git clone https://github.com/patrickwayodi/coldbox.git


## If you don't have Python, install it.

sudo apt-get update

sudo apt-get install python3


## Create a PYthon virtual environment and install Coldbox's dependencies

python3 -m venv ~/virtualenvs/coldbox

source ~/virtualenvs/coldbox/bin/activate

cd coldbox/src

pip install --upgrade pip wheel

pip install --upgrade -r requirements.txt


## Propagate the changes made to the database models into your database schema

python manage.py migrate


## Create the admin account

python manage.py createsuperuser


## Run the tests

python manage.py test accounts.tests

python manage.py test assets.tests

python manage.py test gatepasses.tests


## Run the project

python manage.py runserver

Open http://127.0.0.1:8000 on your browser.

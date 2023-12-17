deploy-Coldbox with-apache
==========================


Below are some commands for installing and configuring Apache for use with Coldbox.

It's assumed that the user is running the Debian GNU/Linux operating system and that
their username is "treetop". Make the necessary alterations if you're using a different
operating system.


## Install Apache and other related software packages.

sudo apt-get update

sudo apt-get install apache2


## Configure Apache for use with Coldbox.

sudo a2dissite coldbox

sudo systemctl restart apache2

sudo nano /etc/apache2/sites-available/coldbox.conf


## Prepare a directory to use for the installation.

mkdir ~/apps/coldbox/prod

cd ~/apps/coldbox/prod


## Clone the repository.

git clone https://github.com/patrickwayodi/coldbox.git


## If you don't have Python, install it.

sudo apt-get update

sudo apt-get install python3


## Create a virtual environment and activate it.

python3 -m venv ~/virtualenvs/coldbox

source ~/virtualenvs/coldbox/bin/activate


## Install Coldbox's dependencies.

mkdir ~/pyrepo/

cd coldbox/src

pip download --dest=/home/treetop/pyrepo pip wheel

pip install --upgrade --no-index --find-links=/home/treetop/pyrepo pip wheel

pip download --dest=/home/treetop/pyrepo -r requirements/dev.txt

pip install --upgrade --no-index --find-links=/home/treetop/pyrepo -r requirements/dev.txt


## Create a directory for storing the files that users will upload.

mkdir /home/treetop/appmedia/coldbox/media/


## Propagate the changes made to the database models into your database schema.

python manage.py makemigrations accounts

python manage.py migrate

python manage.py makemigrations assets

python manage.py migrate

python manage.py makemigrations gatepasses

python manage.py migrate


## Create the admin account.

python manage.py createsuperuser


## Test the project.

sudo a2ensite coldbox

sudo systemctl restart apache2

ls -alh /etc/apache2/sites-enabled

Open http://127.0.0.1:9004 on your browser.

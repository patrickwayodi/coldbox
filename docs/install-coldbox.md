## Clone the repository.
git clone https://github.com/patrickwayodi/coldbox.git


## If you don't have Python, install it.
sudo apt-get update

sudo apt-get install python


## Install Coldbox's dependencies.
cd coldbox/src

python -m pip install --upgrade pip

pip install -r requirements/dev.txt


## Propagate the changes made to the database models into your database schema.
python manage.py makemigrations

python manage.py migrate


## Run the project.
python manage.py runserver

Open http://127.0.0.1:8000 on your browser.

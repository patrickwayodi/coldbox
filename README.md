Coldbox
=======


Coldbox is an asset management system that allocates different permissions to the 
respective users. 

The user selects an Asset and then creates a request for a Gatepass. The request is then
approved by an admin or a staff member.

Coldbox is wriiten in Python using [Django](https://www.djangoproject.com) and
[Bootstrap](https://www.getbootstrap.com).

The project is still in a pre-alpha state so use it with care.


## TODO

* Change the hardcoded URLs that appear on the main page (use template tags instead).
* Configure django-debug-toolbar
* Configure django-widget-tweaks
* Write code that will list the assets at the URL http://127.0.0.1:8000/assets
* Configure Bootstrap properly so that the pages look better.
* Extend (or override) the Django ModelForm so that the forms look better.
*     https://getbootstrap.com/docs/5.2/examples/cheatsheet
*     https://www.pypi.org/project/django-widget-tweaks
*     https://www.prettyprinted.com/tutorials/django-widget-tweaks
* Finish writing the documentation for installing and configuring Apache.
* Simplify the project so that each source code file has less than 100 lines of code.
* Create an About page for each of the Django apps.
* Use HTMX instead of JavaScript for most dynamic scripting.
* Files to be modified should first be copied to a file with a ".backup" extension.
* Files to be deleted should instead be renamed with a ".delete" extension.


## Download and Installation

To begin using this software:
* Install Python.

Clone the repo: 
* git clone https://github.com/patrickwayodi/coldbox.git

Create a PYthon virtual environment and install Coldbox's dependencies
* python3 -m venv ~/virtualenvs/coldbox
* source ~/virtualenvs/coldbox/bin/activate
* cd coldbox/src
* pip install --upgrade pip wheel
* pip install --upgrade -r requirements.txt

Propagate the changes made to the database models into your database schema:
* python manage.py migrate

Create the admin account:
* python manage.py createsuperuser

For more detailed instructions, see docs/install-coldbox.md


## Usage

To run the project, execute:
* python manage.py runserver
* Open http://127.0.0.1:8000/ on your browser


## To get more help:
* View the documentation in the "docs" directory.
* Contact me on Twitter: **[@patrickwayodi](https://www.twitter.com/patrickwayodi)**


## Copyright and License

Coldbox is free software: you can redistribute it and/or modify it under the terms
of the GNU General Public License license as published by the Free Software Foundation, 
either version 3 of the License, or (at your option) any later version.

Coldbox is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

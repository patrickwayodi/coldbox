Coldbox
=======

Coldbox is a document management system that can allocate different permissions to the 
respective users.

Coldbox is wriiten in Python using the Django framework.


## Download and Installation

To begin using this software:
* Install Python.

Clone the repo: 
* git clone https://github.com/patrickwayodi/coldbox.git

To install dependencies, run:
* cd coldbox/src
* python -m pip install --upgrade pip (Upgrading pip)
* pip install -r requirements/dev.txt


## Usage

Propagate the changes made to the database models into your database schema:
* python manage.py makemigrations
* python manage.py migrate

To run the project, execute:
* python manage.py runserver
* Open http://127.0.0.1:8000/ on your browser


## To get more help:

* Contact me on Twitter: **[@patrickwayodi](https://www.twitter.com/patrickwayodi)**


## Copyright and License

Coldbox is free software: you can redistribute it and/or modify it under the terms
of the [GNU General Public License](https://www.github.com/patrickwayodi/coldbox/blob/gh-pages/LICENSE)
license as published by the Free Software Foundation, either version 3 of the License,
or (at your option) any later version.

Coldbox is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

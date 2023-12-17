TODO
====


## Test the Project Locally

* Run the project and access it using your browser.
    - cd ~/apps/coldbox/dev/coldbox/src
    - source ~/virtualenvs/coldbox/bin/activate
    - python manage.py runserver
* Open http://127.0.0.1:8000 on your browser.
* The default users are "janedoe", "johndoe", and "demo". Their password is "django123".


## Update the GitHub Repository

* Push the latest changes to GitHub.
    - cd ~/apps/coldbox/dev/coldbox
    - git add .
    - git commit -m "new updates"
    - git push --set-upstream origin main


## Configure Bootstrap

* Configure Bootstrap so that the pages look better.
* Check if it's safe to delete this snippet in the CSS file "static/{app-name}.css":
    - :root { --bs-body-bg: var(--bs-gray-100); }
* Include the missing CSS and JS files in all the "head.html" files.


## Listing of Users

* Enable the accounts app to list users.
    - http://www.example.com/users
    - http://www.example.com/user/3456789012


## Searching of Assets

* Create a search app for searching for assets.
    - http://www.example.com/search
    - http://www.example.com/search?query=samsung+phone


## Modify the Navbars

* Check if it's safe to delete "data-bs-target" and "data-bs-toggle" in "navbar.html".


## Modify the Footers

* Remove the irrelevant links from the file "templates/footer.html".


## Increase Security

* Remove all keys and passwords from the file "settings.py".
* Configure rate-limitting (e.g. by using django-rate-limitter).
* Limit how much resources (RAM, CPU, storage, etc) the running Django project can use.


## Write More Tests

* logging in
* logging out
* uploading files


## Configure Apache

* Finish writing the documentation for installing and configuring Apache.
* For more details, see docs/deploy-with-apache.md


## Configure django-debug-toolbar

* For more details, see docs/using-django-debug-toolbar.md


## Minor Improvements

* Configure django-widget-tweaks.
* Simplify the project so that each source code file has less than 100 lines of code.
* Files to be modified should first be copied to a file with a ".backup" extension.
* Files to be deleted should instead be renamed with a ".delete" extension.


## Creating a Gatepass

* The user selects an Asset and then creates a request for a Gatepass.
* The request is then approved by an admin or a staff member.


## Use HTMX

* Use HTMX instead of JavaScript for asynchronous scripting.

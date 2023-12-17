TODO
====


## Update the GitHub Repository

* cd ~/apps/coldbox/dev/coldbox
* git add .
* git commit -m "new updates"
* git push --set-upstream origin main


## Configure Bootstrap

* Configure Bootstrap so that the pages look better.
* Check if it's safe to delete this snippet in the CSS file "static/{app-name}.css":
      :root {
        --bs-body-bg: var(--bs-gray-100);
      }
* Modify all the "head.html" files.


## Modify the Navbars

* Check if it's safe to delete "data-bs-target" and "data-bs-toggle" in "navbar.html".


## Modify the Footers

* Modify the file "templates/footer.html".


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
* Create a search app for searching for gatepasses, assets, and users.


## Creating a Gatepass

* The user selects an Asset and then creates a request for a Gatepass.
* The request is then approved by an admin or a staff member.


## Use HTMX

* Use HTMX instead of JavaScript for scripting.

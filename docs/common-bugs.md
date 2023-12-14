Common Bugs
===========


Below are some common bugs you might encounter and some suggestions on how to deal with
them.


## incorrect content types for sta�c assets

If you find improper content types for certain files, it is most likely that the
pla�orm’s map files are incorrect or need to be updated. This can be achieved, for 
example, by installing or upda�ng the mailcap package on a Red Hat distribu�on, 
mime-support on a Debian distribu�on, or by edi�ng the keys under HKEY_CLASSES_ROOT in
the Windows registry.

* sudo apt-get install mime-support


## Using HTMX to boost a page

If you’re using HTMX to boost a page you will need to add the following event handler to
your code:

{% if debug %}
    if (typeof window.htmx !== "undefined") {
        htmx.on("htmx:afterSettle", function(detail) {
            if (
                typeof window.djdt !== "undefined"
                && detail.target instanceof HTMLBodyElement
            ) {
                djdt.show_toolbar();
            }
        });
    }
{% endif %}

The use of {% if debug %} requires django.template.context_processors.debug be included
in the 'context_processors' op�on of the TEMPLATES se�ng. Django’s default
configura�on includes this context processor.


## Cross-Origin Request Blocked

To resolve, configure your sta�c files server to add the Access-Control-Allow-Origin 
header with the origin of the applica�on server. For example, if your applica�on server 
is at http://example.com , and your sta�c files are served by NGINX, add:

* add_header Access-Control-Allow-Origin http://example.com;

And for Apache:

* Header add Access-Control-Allow-Origin http://example.com


## References

* https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS/Errors/CORSMissingAllowOrigin
* https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#render-panels
* https://htmx.org/docs/#boosting
* https://django-debug-toolbar.readthedocs.io/en/latest/index.html

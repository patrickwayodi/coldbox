Using HTMX
==========


Below are some common bugs you might encounter and some suggestions on how to deal with
them.


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


## References

* https://htmx.org/docs/#boosting
* https://django-debug-toolbar.readthedocs.io/en/latest/index.html

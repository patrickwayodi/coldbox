"""
Extend (or override) the Django ModelForm so that the forms look better.

https://getbootstrap.com/docs/5.2/examples/cheatsheet
https://www.pypi.org/project/django-widget-tweaks
https://www.prettyprinted.com/tutorials/django-widget-tweaks
"""


from django import forms
from .models import Gatepass


class GatepassForm(forms.ModelForm):

    """
    https://stackoverflow.com/questions/9878475/django-modelform-override-widget
    """

    description = forms.CharField

    class Meta:

        model = Gatepass

        fields = ["description",]

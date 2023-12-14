"""
Extend (or override) the Django ModelForm so that the forms look better.

https://getbootstrap.com/docs/5.2/examples/cheatsheet
https://www.pypi.org/project/django-widget-tweaks
https://www.prettyprinted.com/tutorials/django-widget-tweaks
"""


from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Account


class AccountCreationForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ('username', 'email')

class AccountChangeForm(UserChangeForm):

    class Meta:
        model = Account
        fields = ('username', 'email')

from django import forms
from .models import Gatepass


class GatepassForm(forms.ModelForm):

    """
    https://stackoverflow.com/questions/9878475/django-modelform-override-widget
    """

    # gatepass_file = forms.FileField(label = "")
    description = forms.CharField

    class Meta:

        model = Gatepass

        fields = ["description",]

from django import forms
from .models import Asset


class AssetForm(forms.ModelForm):

    """
    https://stackoverflow.com/questions/9878475/django-modelform-override-widget
    """

    asset_file = forms.FileField(label = "")


    class Meta:

        model = Asset

        fields = ["asset_file",]

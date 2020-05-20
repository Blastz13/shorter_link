from django import forms
from django.core.validators import URLValidator


class UrlCreateForm(forms.Form):
    url = forms.CharField(widget=forms.TextInput(), validators=[URLValidator()])

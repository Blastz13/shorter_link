from django import forms
from django.core.validators import URLValidator


class UrlCreateForm(forms.Form):
    url = forms.CharField(widget=forms.TextInput(attrs={'class': 'field', 'placeholder': 'Paste your URL'}), validators=[URLValidator()])


from django import forms


class FormName(forms.Form):
    """Class for forms."""
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField()
    botcathcer = forms.CharField(required=False, widget=forms.HiddenInput())

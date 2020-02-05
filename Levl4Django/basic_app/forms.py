from django import forms
from django.core import validators

# Кастомный валидатор, проверяющий начинается ли слово с N
# def check_for_n(value):
#     if value[0].lower() != 'n':
#         raise forms.ValidationError("Name needs to start with N")


class FormName(forms.Form):
    """Class for forms."""
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea())
    # botcathcer = forms.CharField(required=False,
    #                             widget=forms.HiddenInput(),
    #                             validators=
    #                                 [validators.MaxLengthValidator(limit_value=0, message='FUCK')]) это встроенный валидатор от джанги

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError('Email is not the same')

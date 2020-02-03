from django.shortcuts import render
from .import forms

# Create your views here.


def index(request):
    """Index."""
    return render(request, 'basic_app/index.html')


def register(request):
    """Registr form."""
    form = forms.FormName()
    return render(request, 'basic_app/forms_page.html', {'form': form})

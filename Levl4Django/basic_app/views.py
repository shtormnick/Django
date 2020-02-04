from django.shortcuts import render
from .import forms
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    """Index."""
    return render(request, 'basic_app/index.html')


@csrf_exempt
def register(request):
    """Registr form."""
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("validation success")
            print("Nme " + form.cleaned_data['name'])
            print("Email " + form.cleaned_data['email'])
            print("Text " + form.cleaned_data['text'])

    return render(request, 'basic_app/forms_page.html', {'form': form})

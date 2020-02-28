from django.shortcuts import render
from appTwo.forms import NewUserForm
# Create your views here.


def index(request):
    context_dict = {'text': 'hello world', 'number': 110}
    return render(request, 'appTwo/index.html', context_dict)


def users(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FROM INVALID FORM')
    return render(request, 'appTwo/users.html', {'form': form})

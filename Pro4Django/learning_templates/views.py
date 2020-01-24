from django.shortcuts import render

# Create your views here.


def index(reqest):
    return render(reqest, 'learning_templates/index.html')


def other(reqest):
    return render(reqest, 'learning_templates/other.html')


def relative(reqest):
    return render(reqest, 'learning_templates/relative_url_templates.html')

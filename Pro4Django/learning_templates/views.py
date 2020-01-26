from django.shortcuts import render

# Create your views here.


def index(reqest):
    context_dict = {'text': 'hello world', 'number': 1000}
    return render(reqest, 'learning_templates/index.html', context_dict)


def other(reqest):
    return render(reqest, 'learning_templates/other.html')


def relative(reqest):
    return render(reqest, 'learning_templates/relative_url_templates.html')

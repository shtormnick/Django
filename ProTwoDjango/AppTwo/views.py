from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import Topic,Webpage,AccessRecord
# Create your views here.


def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpage_list}
    my_dict = {'insert_me': "Now I am coming from first_app/index.html!"}
    return render(request, 'first_app/index.html', context=date_dict)


def help(request):
    my_dict1 = {"help_page": "Welcome at help page!"}
    return render(request, 'second_app/help.html', context=my_dict1)

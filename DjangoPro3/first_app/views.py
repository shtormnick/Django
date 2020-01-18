from django.shortcuts import render
from first_app.models import User
# Create your views here.


def index(request):

    return render(request, 'appFirst/index.html')


def users(request):

    user_list = User.objects.order_by('firs_name')
    user_dict = {'users': user_list}
    return render(request, 'appFirst/index.html', context=user_dict)

from django.urls import path
from AppTwo import views
urlpatterns = [
    # path('', views.index, name='idex'),
    path('/help', views.help, name='help')
]

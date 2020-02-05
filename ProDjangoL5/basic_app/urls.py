from django.urls import path
from basic_app import views


app_name = 'basic_app'


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('sentry-debug/', trigger_error),
    path('register/', views.register, name='register'),
    
]

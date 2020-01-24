from django.urls import path
from learning_templates import views


# TEMPLATE TAGGIN
app_name = 'learning_templates'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
    ]

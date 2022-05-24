from django.urls import path

from . import views

app_name = 'controller'
urlpatterns = [
    path('', views.index, name='index'),
]


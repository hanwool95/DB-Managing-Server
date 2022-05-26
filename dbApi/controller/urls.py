from django.urls import path

from . import views

app_name = 'controller'
urlpatterns = [
    path('', views.index, name='index'),
    path('insert/<str:file_name>', views.insert_file, name='insert'),
    path('upload', views.upload_file, name='upload')
]


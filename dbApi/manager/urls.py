from django.urls import path

from . import views

app_name = 'manager'
urlpatterns = [
    path('', views.index, name='index'),
    path('concate_db/<int:number>', views.concate_db, name='concate_db'),
    path('dx/', views.DxAPI.as_view())
]
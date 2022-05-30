from django.urls import path

from . import views

app_name = 'manager'
urlpatterns = [
    path('', views.index, name='index'),
    path('concate_db/<int:number>', views.concate_db, name='concate_db'),
    path('dx/', views.DxAPI.as_view()),
    path('dx/<int:pk>', views.DxDetailAPI.as_view()),
    path('lab/', views.LabAPI.as_view()),
    path('lab/<int:pk>', views.LabDetailAPI.as_view()),
    path('med/', views.MedAPI.as_view()),
    path('med/<int:pk>', views.MedDetailAPI.as_view()),
    path('px/', views.PxAPI.as_view()),
    path('px/<int:pk>', views.PxDetailAPI.as_view()),
    path('fx/', views.FxAPI.as_view()),
    path('fx/<int:pk>', views.FxDetailAPI.as_view()),
]
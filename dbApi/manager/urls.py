from django.urls import path

from . import views

app_name = 'manager'
urlpatterns = [
    path('', views.index, name='index'),
    path('concate_db/<int:number>', views.concate_db, name='concate_db'),
    path('dx/', views.DxAPI.as_view()),
    path('dx/<int:number>', views.DxCaseAPI.as_view()),
    path('dx/id/<int:pk>', views.DxDetailAPI.as_view()),
    path('lab/', views.LabAPI.as_view()),
    path('lab/<int:number>', views.LabCaseAPI.as_view()),
    path('lab/id/<int:pk>', views.LabDetailAPI.as_view()),
    path('med/', views.MedAPI.as_view()),
    path('med/<int:number>', views.MedCaseAPI.as_view()),
    path('med/id/<int:pk>', views.MedDetailAPI.as_view()),
    path('px/', views.PxAPI.as_view()),
    path('px/<int:number>', views.PxCaseAPI.as_view()),
    path('px/id/<int:pk>', views.PxDetailAPI.as_view()),
    path('fx/', views.FxAPI.as_view()),
    path('fx/<int:number>', views.FxCaseAPI.as_view()),
    path('fx/id/<int:pk>', views.FxDetailAPI.as_view()),
    path('event/', views.EventAPI.as_view()),
    path('event/<int:number>', views.EventCaseAPI.as_view()),
]
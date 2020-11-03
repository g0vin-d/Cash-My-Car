from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="store-home"),
    path('sellcar/', views.sellacar, name="store-sellcar"),
    path('newcar/', views.newcar, name="store-newcar"),
    path('oldcar/', views.oldcar, name="store-oldcar"),
]

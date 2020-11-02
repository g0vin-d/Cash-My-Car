from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="store-home"),
    path('sellcar/', views.sellacar, name="store-sellcar"),
]
